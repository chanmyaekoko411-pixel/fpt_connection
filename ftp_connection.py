from ftplib import FTP

class FTPConnection:
    def connect(self):
        ftp = FTP()
        return ftp

    def disconnect(self, ftp):
        ftp.close()

if __name__ == "__main__":
    ftp_manager = FTPConnection()
 
    ftp = ftp_manager.connect()
    print("Connected to FTP server")
 
    ftp_manager.disconnect(ftp)
    print("FTP connection closed")