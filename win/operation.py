import call


def make_shortcut(source, path):
    """
    Create a Windows shortcut

    :param source: str. source path to create shortcut with
    :param path: str. target shortcut path
    :return: tuple. result, error
    """
    command = (
        "$s=(New-Object -COM WScript.Shell).CreateShortcut(\"{0}\"); "
        "$s.TargetPath=\"{1}\"; "
        "$s.Save()".format(path, source)
    )
    return call.power_call(command)


def get_installed_apps():
    """
    Get a list of applications installed on the Windows machine

    :return: list of str. application names
    """
    command = ['wmic', 'product', 'get', 'name']
    result, error = call.cmd_call(command)
    if error:
        return None

    return [app.replace(" ", "") for app in result.split("\r\r\n")]


def uninstall_app(name):
    """
    Un-install an application on Windows

    :param name: str. name of the application to un-install
    :return: bool. whether the un-install is successful or not
    """
    arg = 'name=\'{}\''.format(name)
    command = ['wmic', 'product', 'where', arg, 'call', 'uninstall']
    result, error = call.cmd_call(command)
    if error:
        return False

    return True


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
