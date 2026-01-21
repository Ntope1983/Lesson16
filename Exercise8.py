#The Time class encapsulates time-related data and behavior,
# ensuring valid state through setters and providing controlled
# operations such as advancing time by one second
# while hiding internal implementation details.
class Time:
    def __init__(self, hour=None, minute=None, second=None):
        if hour is None:
            self.hour = 0
        else:
            self.set_hour(hour)
        if minute is None:
            self.minute = 0
        else:
            self.set_minute(minute)
        if second is None:
            self.second = 0
        else:
            self.set_seconds(second)

    def set_hour(self, hour):
        if hour in range(0, 24):
            self.hour = hour
        else:
            self.hour=0

    def set_minute(self, minute):
        if minute in range(0, 60):
            self.minute = minute
        else:
            self.minute=0

    def set_seconds(self, seconds):
        if seconds in range(0, 60):
            self.second = seconds
        else:
            self.second=0

    def get_seconds(self):
        return self.second + self.minute * 60 + self.hour * 60 * 60

    def print(self):
        print(f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}:{str(self.second).zfill(2)}")

    def next_second(self):
        next_time = Time(self.hour, self.minute, self.second)
        if next_time.second == 59:
            next_time.second = 0
            if next_time.minute == 59:
                next_time.minute = 0
                next_time.hour = (next_time.hour + 1) % 24
            else:
                next_time.minute += 1
        else:
            next_time.second += 1
        return next_time


time2 = Time(23, 00, 30)


while time2.hour != 3:
    time2.print()
    time2 = time2.next_second()
