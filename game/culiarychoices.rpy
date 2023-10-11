label culinarychoices:
    $ calendar.AddMinutes(20)
    play music "audio/campfire.mp3" 
    call closescreens
    label cchoicesloop:
        $ monthworkresulthours += dayworksuccessfulhours
        $ dayworksuccessfulhours = 0
        
        if calendar.Days == 1:
            $ money += monthsalary
            $ monthsalary = 0            
            $ monthworkresulthours = 0
            $ cooksalaryperhour = 23.5*salarystatus
        else:
            pass
        
        
        $ position = "backyard"
        call sceneimg
        menu:
            "Go upstairs and look around":
                jump balcony
            "Sleep":
                call dayvariables
        
        


        jump cchoicesloop