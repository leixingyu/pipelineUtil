import psutil


def get_port_of_process(pid):
    """
    Get opened port from a process

    :param pid: int. process ID
    :return: [(str, str)]. list of tuple containing ip and port
    """
    proc = psutil.Process(pid=pid)
    connections = proc.connections(kind='tcp4')

    ports = list()
    for c in [x for x in connections if x.status == psutil.CONN_LISTEN]:
        # gets the port number
        ports.append((c.laddr[-1]))
    return ports
