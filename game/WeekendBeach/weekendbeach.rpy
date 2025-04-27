label weekendbeach:
    $ calendar.AddMinutes(20)
    # show player relaxing
    $ position = "layingonthebeach"
    call sceneimg

    $ myrandom = renpy.random.randint(0, 3)
    if myrandom > 1:
        if avasurfingfirsttime == False and beachswim == True and avaignore == False:
            $ avasurfingfirsttime = True
            jump avasurfmeet

    $ myrandom = renpy.random.randint(0, 3)
    if myrandom > 1 and avasurfing == True:
        $ position = "avabeachsufringfar"
        call sceneimg 

    menu:
        "Relax on the beach":  
            $ beachswim = False
            "You relax on the beach, soaking up the sun and enjoying the sound of the waves."

        "Go for a swim":
            $ beachswim = True
            $ position = "playerswimming"
            call sceneimg
            "You are swimming in the ocean, enjoying the cool water"
            
            "You feel the sun on your skin and the waves crashing around you."

            "You take a refreshing swim in the ocean, feeling the cool water against your skin."
        "Go surfing" if avasurfing == True and position == "avabeachsufringfar":
            jump surfingoptions
        "Go home":
            $ beachswim = False
            $ avaignore = False
            jump culinarychoices

        
    

    jump weekendbeach
