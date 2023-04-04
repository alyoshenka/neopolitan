import time
from threading import Thread
from queue import Queue
from demo import with_args

# doesn't this also need to listen tho??

def add_to_queue(q, e, t):
    time.sleep(t)
    q.put(e)

def runner():
    events = Queue()
    t = Thread(target=with_args, args=(events,))
    t.start()

    Thread(target=add_to_queue, args=(events, 'say abcdefg', 4,)).start()
    Thread(target=add_to_queue, args=(events, 'exit', 8,)).start()

    # todo: 'off' event

    # t.join() # no difference

runner()
