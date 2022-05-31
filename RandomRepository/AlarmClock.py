
class AlarmClock:
    def __init__(self):
        self.time = '4pm'
        self.isOn = True
        self.alarmtime = '7am'
    
    def change_time(self, new_time):
        self.time = new_time
        print(f'The current time is {new_time}. ')
        

    def on_off_switch(self):
        if self.isOn == True:
            self.isOn = False
            print('Alarm off')
        elif self.isOn == False:
            self.isOn = True
            print('Alarm on')

    def alarm_time(self, alarm_change):
        self.alarmtime = alarm_change
        print(f'The alarm is now set to {alarm_change}. ')

clock = AlarmClock()
clock.change_time('5pm')
clock.alarm_time('6am')
clock.on_off_switch()
clock.on_off_switch()
clock.on_off_switch()
    





