"""
This module mimics the effect of running varies Windows command

either running cmd commands or powershell commands
it also supports admin launch with UAC control
everything is still experimental at the moment
"""


import subprocess


def cmd_call(command):
    """
    Use execute command with subprocess

    :param command: str. command to execute
    :return: tuple. result, error
    """
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    return proc.communicate()


def power_call(command):
    """
    Use Window's powershell to execute powershell command

    :param command: str. command to execute
    :return: tuple. result, error
    """
    call_args = "powershell -command {command}"
    return cmd_call(call_args.format(command=command))


def cmd_call_elevated(command):
    """
    Use Window's command prompt to execute command in admin mode.
    Equivalent to running command prompt as administrator

    :param command: str. command to execute
    :return: tuple. result, error
    """
    call_args = (
        "& {{Start-Process cmd.exe"
        " -argumentlist '/k \"{command}\"'"
        " -Verb Runas}}"
    )
    return power_call(call_args.format(command=command))


def power_call_elevated(command):
    """
    Use powershell to execute powershell command in admin mode.
    Equivalent to running powershell as administrator

    :param command: str. command to execute
    :return: tuple. result, error
    """
    call_args = (
        "& {{Start-Process powershell.exe"
        " -argumentlist '-Command \"{command}\"'"
        " -Verb Runas}}"
    )
    return power_call(call_args.format(command=command))


def power_run_elevated(path):
    """
    Use powershell to shell script in admin mode.
    Equivalent to launching shell script with 'run as administrator'

    :param path: str. path to .ps1 script
    :return: tuple. result, error
    """
    call_args = (
        "& {{Start-Process powershell.exe"
        " -argumentlist '-ExecutionPolicy Bypass -File \"{path}\"'"
        " -Verb Runas}}"
    )
    return power_call(call_args.format(path=path))
