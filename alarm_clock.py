class AlarmClock:
    def __init__(self):
        self.current_time = input("What time is it? ")
        self.alarm_on = False
        self.alarm_set_to = input("When would you like to set your alarm ")
    
    def change_time(self,):
        self.current_time = self.current_time

    
    def alarm_toggle(self):
        if self.current_time == "6":
            self.alarm_on = True
        else:
            self.alarm_on = False

    def set_alarm(self):
        self.alarm_set_to = self.alarm_set_to
        print(f" Your alarm is set for {self.alarm_set_to}")

my_alarm_clock = AlarmClock()

my_alarm_clock.change_time()
my_alarm_clock.alarm_toggle()
my_alarm_clock.set_alarm()
my_alarm_clock.alarm_toggle()