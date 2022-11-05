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
