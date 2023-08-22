label start:


    call variables

    init python:

        class Items(object):
            def __init__ (self, name, val, volume, calories, NoOwned, ID, img):
                self.name = name
                self.val = val
                self.volume = volume
                self.calories = calories
                self.NoOwned = NoOwned
                self.ID = ID
                self.img = img

            def AddItem(self):
                MaxVolume = 50

                if self.CurrentVolume + self.volume > MaxVolume:
                    return
                else:
                    self.NoOwned += 1

            @property
            def CurrentVolume(self):
                CurrentW = 0
                for q in Inventory:
                    CurrentW += (q.volume*q.NoOwned)
                return CurrentW

            @property
            def ItemImg(self):
                return self.img

            @property
            def ItemNoOwned(self):
                return self.NoOwned


        Inventory = []
        t = 0

        while t < 50:
            # Events.append(Event(0,0,0, "", False))
            Inventory.append(Items("none", 0, 0, 0, 0, t, "none"))
            t += 1


        class Calendar(object):
            def __init__(self, totaldays, hours, day, days, month, minutes, months, monthdays, weekday):
                self.totaldays = totaldays
                self.hours = hours
                self.day = day
                self.days = days
                self.month = month
                self.minutes = minutes
                self.months = months

                self.monthdays = monthdays
                self.weekday = weekday

            @property
            def Month(self):
                return self.months[self.month]

            @property
            def Time(self):
                return str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2) #+ " " + self.monthdays[self.month]

            @property
            def WeekDay(self):
                return self.weekday[self.day]

            @property
            def TotalDays(self):
                return self.totaldays

            @property
            def Days(self):
                return self.days

            @property
            def MonthDays(self):
                return self.monthdays

            @property
            def Hours(self):
                return self.hours



            def AddMinutes(self, minutes):
                self.minutes += minutes
                if self.minutes > 59:
                    self.minutes = self.minutes - 60
                    self.hours += 1


                if self.hours > 23:
                    self.hours = self.hours - 24
                    self.day += 1
                    self.days += 1
                    self.totaldays += 1

                if self.day > 6:
                    self.day = 1

                if self.days > self.monthdays[self.month]:
                    self.month += 1
                    self.days = 0
                if self.month > 11:
                    self.month = 0
                # return
            def AddHours(self, hours):
                self.hours += hours

                if self.minutes > 59:
                    self.minutes = self.minutes - 60
                    self.hours += 1


                if self.hours > 23:

                    self.hours = self.hours - 24
                    self.day += 1
                    self.days += 1
                    self.totaldays += 1

                if self.day > 6:
                    self.day = 1

                if self.days > self.monthdays[self.month]:
                    self.month += 1
                    self.days = 1
                if self.month > 11:
                    self.month = 1
                # return
            def AddDays(self, days):
                self.days += days
                self.totaldays += days
                self.day += days
                if self.minutes > 59:
                    self.minutes = self.minutes - 60
                    self.hours += 1


                if self.hours > 23:
                    self.hours = self.hours - 24
                    self.day += 1
                    self.days += 1
                    self.totaldays += 1

                if self.day > 6:
                    self.day = 1

                if self.days > self.monthdays[self.month]:
                    self.month += 1
                    self.days = 1
                if self.month > 11:
                    self.month = 1
                # return

            def AddDay(self, days):
                self.days += days
                self.totaldays += days
                self.hours = 18
                self.minutes = 0
                if self.minutes > 59:
                    self.minutes = self.minutes - 60
                    self.hours += 1


                if self.hours > 23:
                    self.hours = self.hours - 24
                    self.day += 1
                    self.days += 1
                    self.totaldays += 1

                if self.day > 6:
                    self.day = 0

                if self.days > self.monthdays[self.month]:
                    self.month += 1
                    self.days = 1
                if self.month > 11:
                    self.month = 1



        ###############################

    show screen day_icon

    label startloop:
    scene bghome
    pause

    jump startloop

    return
