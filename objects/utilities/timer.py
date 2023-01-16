class Timer(object):
    def __init__(self, callback, initial_time, is_running=True, update_callback=None):
        self.is_running = is_running
        self.initial_time = initial_time
        self.time_left = initial_time
        self.callback = callback
        self.update_callback = update_callback

    def update(self):
        if not self.is_running:
            return
        if self.update_callback:
            self.update_callback()
        self.time_left -= 1
        if self.time_left <= 0:
            new_time = None
            if self.callback:
                new_time = self.callback()
            if new_time is not None:
                self.time_left = new_time
            else:
                self.time_left = self.initial_time
                self.stop()

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def reset(self):
        self.time_left = self.initial_time

    def running(self):
        return self.is_running
