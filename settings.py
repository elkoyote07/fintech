import threading

def init():
    global stop_event
    stop_event = threading.Event()