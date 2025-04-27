label wgswitch:
    if wg == 0:
        $ wg = 1
        $ nigirlimage = ""
        $ niimage = "WG"    
        $ notify_success("ON")
        call girlsweight
        call girl
    else:
        $ wg = 0
        $ nigirlimage = "" 
        $ niimage = "WG"    
        $ notify_success("OFF")
        call girlsweight
        call girl

    