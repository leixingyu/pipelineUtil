"""
https://www.perforce.com/manuals/p4python/Content/P4Python/python.programming.html
"""


import P4
from datetime import datetime


def connect_p4(user, port, workspace):
    """
    Connect to Perforce

    :param user: str. username
    :param port: str. port number
    :param workspace: str. workspace name
    :return: P4.P4. perforce connection instance
    """
    p4 = P4.P4()
    p4.user = user
    p4.port = port
    p4.client = workspace
    p4.connect()

    return p4


def disconnect_p4(p4):
    """
    Disconnect the Perforce connection

    :param p4: P4.P4. perforce connection instance
    :return:
    """
    p4.disconnect()


def get_latest_commit_info(p4, path):
    """
    Get the latest commit information of a Perforce file

    :param p4: P4.P4. perforce connection instance
    :param path: str. unique path of the perforce file
    :return: int, str, str.
             the latest version,
             the latest commit message,
             the latest commit time
    """
    file_stat = p4.run("fstat", path)[0]
    head_version = file_stat['headRev']
    desc = p4.run("describe", "-s", file_stat['headChange'])[0]['desc']
    head_time_sec = datetime.fromtimestamp(int(file_stat['headTime']))
    head_time = head_time_sec.strftime("%m/%d/%Y, %H:%M:%S")

    return head_version, desc, head_time
