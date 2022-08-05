class times:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s
    # ______________________________________________________________
    def sum(self, mehman):
        result = times(None, None, None)
        result.second = self.second + mehman.second
        result.minute = self.minute + mehman.minute
        result.hour = self.hour + mehman.hour
        if result.second >= 60:
            result.second -= 60
            result.minute += 1
        if result.minute >= 60:
            result.minute -= 60
            result.hour += 1
        return result
    # ______________________________________________________________
    def sub(self, mehman):
        result = times(None, None, None)
        result.hour = self.hour - mehman.hour
        result.minute = self.minute - mehman.minute
        result.second = self.second - mehman.second
        if result.second < 0:
            result.second += 60
            result.minute -= 1
        if result.minute < 0:
            result.minute += 60
            result.hour -= 1
        return result
    # ______________________________________________________________
    def time_second_to_hours(self):
        result = times(None, None, None)
        result.hour = self.second // 3600
        result.minute = (self.second % 3600) // 60
        result.second = (self.second % 3600) % 60
        return result
    # ______________________________________________________________
    def time_hours_to_second(self):
        result = times(None, None, None)
        result.hour = 0
        result.minute = 0
        result.second = self.hour*3600 + self.minute*60+self.second
        return result
    # ______________________________________________________________
    def show(self):
        print(self.hour, ':', self.minute, ':', self.second)
    # ______________________________________________________________
t1 = times(4, 30, 45)
t2 = times(3, 17, 40)
t1.show()
t2.show()
print('____sum____');   c = t1.sum(t2);   c.show()
print('____sub____');   d = t1.sub(t2);   d.show()
print('____time_hours_to_second____');    e = t1.time_hours_to_second();    e.show()
print('____time second to hours____');    f = e.time_second_to_hours();     f.show() 