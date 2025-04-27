label balancetraining:
    # reset state
    $ balance_pos        = 0.5
    $ balance_timer      = 0.0    # time spent in 0.4–0.6
    $ outofbalance_timer = 0.0    # time spent outside 0.4–0.6


    if balancefail == True:
        $ balancefail = False
        $ position = "playerinthewater"
        call sceneimg
        pause 1.0

    $ position = "playertryingtostand"
    call sceneimg
    show screen surfbalancetraining

    # main loop: step every 0.05s
    while True:
        $ renpy.pause(0.05, hard=True)
        
        # accumulate timers
        if 0.4 < balance_pos < 0.6:
            $ balance_timer      += 0.05
        else:
            $ outofbalance_timer += 0.05

        # 1) instant fall
        if balance_pos < 0.1 or balance_pos > 0.9:
            hide screen surfbalancetraining
            jump balancefail

        # 2) too much out‑of‑green → so‑so
        

        # 3) success in green
        if balance_timer >= 10.0:
            hide screen surfbalancetraining
            if outofbalance_timer < 20.0:
                jump balancesuccess
            else:
                jump balancesoso