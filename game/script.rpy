label start:


    call variables
    call girl
    init python:

        # gamerunning = 1
        # position = "home"

        # labelvariable = "sceneimg"
        
        # while gamerunning == 1:
        #     renpy.call(labelvariable)

        # renpy.call("sceneimg")


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
    $ position = "home"
    scene bg
    "This is a belly stuffing game"
    menu:

        "I'm in and 18+":
            "Great, continue!"

            python:
                name = renpy.input("What's your name?")

                name = name.strip() or "The Feeder"

        "No I'm not into this or I'm under 18 years old":
            "Sorry, the game is over for you!"
            $ renpy.quit()
    window hide
    show text "{color=#ffffff}{size=200} Choose your way {/size}{/color}" at truecenter
    with slowdissolve
    pause 3
    hide text
    with slowdissolve
    pause 1
    label choosetheway:
        menu:
        
            "[name]'s Culinary journey":
                jump culinarystart

            "[name]'s Adventurous Spirit":
                "Not yet"

            "[name]'s Professional journey (IT digital nomad)":
                "Not yet"

            "[name]'s Philanthropic Endeavors":
                "Not yet"
        jump choosetheway  

        
    

    jump startloop

    return
