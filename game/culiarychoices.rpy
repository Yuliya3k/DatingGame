label culinarychoices:
    
    $ calendar.AddMinutes(20)
    call girl
    

    
    # pause 1
    # hide screen success_notification_screen

    $ myrandom = renpy.random.randint(1,10)
    if myrandom == 5 and krisstory < 3:
        jump krisfirstmeet

    play music "audio/campfire.mp3" 
    call closescreens

    $ myrandom = renpy.random.randint(1,10)
    if krisbackyard == 1 and myrandom == 1 and krisnottoday == 0:
        jump krisbackyard

    $ youarehome = True

    label cchoicesloop: 
        
        python:
            _jump_event = None
            _event_day = None
            for ev in scheduled_calls:
                if ev[0] == calendar.TotalDays:
                    _jump_event = ev[1]
                    _event_day = ev[0]
                    scheduled_calls.remove(ev)
                    break
    if _jump_event:
        if _jump_event == "phone_goal_check":
            last_call_person, last_call_goal = phone_goal_details.pop(_event_day, (None, None))
        jump expression _jump_event    

        $ position = "backyard"
        call sceneimg
        menu:
            "Go upstairs and look around":
                jump balcony
            "Sleep":
                call dayvariables
            "Go talk to Aurora" if auroraseen == 1:
                jump aurorafirstmeet
            "Cycling" if calendar.Hours > 11 and calendar.Hours < 16 and calendar.WeekDay == "Sat" and linrideabikesat == 1:
                jump lincycling
            "Hiking" if calendar.Hours > 9 and calendar.Hours < 18 and calendar.WeekDay == "Sun" and linhikesun == 1:
                jump linhiking
            "Game adjustments":
                menu:
                    "Toggle weight gain for the girls":
                        call wgswitch
                    # "Toggle speech sounds":
                    #     call speechswitch
            
            
            
        
        


        jump cchoicesloop