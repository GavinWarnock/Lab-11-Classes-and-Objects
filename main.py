from alarm_clock import AlarmClock

my_alarm_clock = AlarmClock()

my_alarm_clock.change_time("6")
print(my_alarm_clock.current_time)

my_alarm_clock.alarm_toggle
print(my_alarm_clock.alarm_on)

my_alarm_clock.set_alarm("6")
print(my_alarm_clock.alarm_set_to)