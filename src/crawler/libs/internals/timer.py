import time


class XTimer(object):
    """ Custom Timer Class """

    def __init__(self, name="XTimer"):
        self.name = name

    def __enter__(self):
        self.tstart = time.time()

    def __exit__(self, type, value, traceback):
        if self.name:
            print(str(self.name))
        print('Elapsed: ' + str(round(time.time() - self.tstart, 3)))
