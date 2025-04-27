label surfbalancetraining_target(target=10.0):
    # reset
    $ balance_pos        = 0.5
    $ balance_timer      = 0.0
    $ outofbalance_timer = 0.0

    $ position = "playertryingtostand"
    call sceneimg
    
    show screen surfbalancetraining

    while True:
        $ renpy.pause(0.05, hard=True)

        if 0.4 < balance_pos < 0.6:
            $ balance_timer      += 0.05
        else:
            $ outofbalance_timer += 0.05

        if balance_pos < 0.1 or balance_pos > 0.9:
            hide screen surfbalancetraining
            jump wavefail

        

        if balance_timer >= target:
            hide screen surfbalancetraining
            if outofbalance_timer < 20.0:
                jump wavesuccess
            else:
                jump wavesoso
