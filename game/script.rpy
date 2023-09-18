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
    menu:

        "[name]'s Professional Journey":
            "You are [name], a recent transplant to the thriving city of Urbana. Armed with a degree in computer science, you've come here in search of job opportunities in the tech industry. Your goal is to make your mark on the city's booming startup scene and develop groundbreaking software that changes the world."

        "[name]'s Adventurous Spirit":
            "You are [name], an adventurer at heart who has just arrived in the bustling city of Urbana. Tired of the mundane, you seek excitement and new experiences around every corner. Whether it's exploring hidden alleys, joining local clubs, or embarking on spontaneous road trips, you're determined to make your time in Urbana unforgettable."

        "[name]'s Culinary Journey":
            "You are [name], a culinary enthusiast who has relocated to the food-loving city of Urbana. With a love for experimenting in the kitchen, you're excited to dive into the diverse culinary scene and maybe even open your own restaurant one day. From food trucks to upscale eateries, you're ready to savor every flavor the city has to offer."

        "[name]'s Social Butterfly":
            "You are [name], a people person who has recently moved to the vibrant city of Urbana. Eager to connect with others, you're excited about the endless possibilities for making new friends, attending parties, and immersing yourself in the city's social scene. Your charisma and charm are your greatest assets as you navigate your way through this exciting chapter of your life."
        "Next day":
            call dayvariables
    pause

    jump startloop

    return
