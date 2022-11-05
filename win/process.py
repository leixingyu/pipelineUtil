"""
Process/Task related Windows operation
"""


import psutil


def get_process(name):
    """
    Find running background process

    :param name: str. name of the process (e.g. 'maya.exe')
    :return: [int]. list of process id (PID)
    """
    pids = list()

    # iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            if proc.name() == name and proc.status() == psutil.STATUS_RUNNING:
                pid = proc.pid
                pids.append(pid)
        except:
            pass

    return pids


def end_process(pid):
    """
    End a process of a ID

    :param pid: int. process id
    """
    proc = psutil.Process(pid)
    proc.terminate()  # or use .kill()
    proc.wait()
