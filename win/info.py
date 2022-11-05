import call


def get_cpu_name():
    """
    Get name of the CPU

    :return: str.
    """
    command = ['wmic', 'cpu', 'get', 'name']

    result, error = call.cmd_call(command)
    if error:
        return None

    return result.split("\n")[-1]


def get_cpu_core():
    """
    Get number of CPU cores

    :return: int.
    """
    command = ['wmic', 'cpu', 'get', 'numberofcores']
    result, error = call.cmd_call(command)
    if error:
        return None

    return int(result.split("\n")[-1])


def get_gpu_name():
    """
    Get name of the GPU

    :return: str.
    """
    command = ['wmic', 'path', 'Win32_videocontroller', 'get', 'description']
    result, error = call.cmd_call(command)
    if error:
        return None

    return result.split("\n")[-1]


def get_gpu_driver():
    """
    Get name of the GPU driver

    :return: str.
    """
    command = ['wmic', 'path', 'Win32_videocontroller', 'get', 'driverversion']
    result, error = call.cmd_call(command)
    if error:
        return None

    return result.split("\n")[-1]


def get_ip_mac():
    """
    Get machine IP and MAC address

    :return: tuple. str, str: IP and MAC
    """
    import re
    import socket
    import uuid

    ip = socket.gethostbyname(socket.gethostname())
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))

    return ip, mac
