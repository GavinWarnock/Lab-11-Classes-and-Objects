class AlarmClock:
    def __init__(self):
        self.current_time = "12:00"
        self.alarm_on = False
        self.alarm_set_to = "6:00"
    
    def change_time(self, new_time):
        self.current_time = new_time
    
    def alarm_toggle(self):
        if self.current_time == "6:00":
            self.alarm_on = True
        else:
            self.alarm_on = False

    def set_alarm(self, new_alarm_time):
        self.alarm_set_to = new_alarm_time
        print(new_alarm_time)


my_alarm_clock = AlarmClock
my_alarm_clock.change_time(new_time)
print(self.current_time)
