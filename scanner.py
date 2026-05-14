import socket
from threading import Thread
from queue import Queue

open_ports = []

def scan_target(target, start_port, end_port):

    queue = Queue()

    def scan_port(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            result = s.connect_ex((target, port))

            if result == 0:
                open_ports.append(port)

            s.close()

        except:
            pass

    def worker():
        while not queue.empty():
            port = queue.get()
            scan_port(port)
            queue.task_done()

    for port in range(start_port, end_port + 1):
        queue.put(port)

    for _ in range(100):
        thread = Thread(target=worker)
        thread.daemon = True
        thread.start()

    queue.join()

    return open_ports