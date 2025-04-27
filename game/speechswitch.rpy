label speechswitch:
    if speech == 0:
        $ speech = 1
        $ nigirlimage = ""
        $ niimage = "speechsound"    
        $ notify_success("ON")
    else:
        $ speech = 0
        $ nigirlimage = ""
        $ niimage = "speechsound"    
        $ notify_success("OFF")

    return