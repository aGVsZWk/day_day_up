import time


class ConcreteObserver(object):
    def update(self, observerd):
        print("Observing： {}".format(observerd))


class Observable(object):
    def __init__(self):
        self.callbacks = set()
        self.changed = False

    def register(self, callback):
        self.callbacks.add(callback)

    def unregister(self, callback):
        self.callbacks.discard(callback)

    def poll_for_change(self):
        if self.changed:
            self.update_all

    def update_all(self):
        for callback in self.callbacks:
            callback(self)


def main():
    observed = Observable()
    observer1 = ConcreteObserver()
    observed.register(lambda x: observer1.update(x))
    while True:
        time.sleep(3)
        observed.poll_for_change()


if __name__ == '__main__':
    main()
