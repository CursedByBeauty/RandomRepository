from AlarmClock import AlarmClock

alarm_one = AlarmClock("1230", "430")

print(alarm_one.time)
alarm_one.change_time("1")
print(alarm_one.time)

alarm_one.on_off_switch("Off")
print(alarm_one.isOn)