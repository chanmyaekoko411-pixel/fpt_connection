import ftplib
from unittest.mock import Mock

import pytest


def connect_ftp():
    """Connect to the FTP server and return the connection."""
    ftp = ftplib.FTP("127.0.0.1")
    ftp.login("chan", "rina411")
    return ftp


def close_ftp(ftp):
    """Close the FTP connection."""
    ftp.quit()


if __name__ == "__main__":
    ftp = connect_ftp()
    try:
        print("FTP connection successful!")
    finally:
        close_ftp(ftp)

    print("FTP connection closed.")


def test_connect_and_close_ftp(monkeypatch):
    ftp = Mock()
    monkeypatch.setattr(ftplib, "FTP", Mock(return_value=ftp))

    connection = connect_ftp()
    close_ftp(connection)

    ftplib.FTP.assert_called_once_with("127.0.0.1")
    ftp.login.assert_called_once_with("chan", "rina411")
    ftp.quit.assert_called_once_with()