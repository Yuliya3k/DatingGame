label wavecatching:
    
    # --- Wave Catch ---
    $ wave_time   = 0.0
    $ wave_streak = 0
    $ wave_fail   = False

    show screen surfwavephase

    if wavefail == True:
        $ wavefail == False
        $ position = "playerinthewater"
        call sceneimg
        pause 1.0
        $ position = "playertryingtostand"
        call sceneimg
    
    $ position = "playerinbalance"
    call sceneimg

    # Wait for either 3 catches or a miss
    while wave_streak < 3 and not wave_fail:
        $ renpy.pause(0.01, hard=True)

    hide screen surfwavephase

    if wave_fail:
        jump wavefail

    # --- Open‑Ocean Ride (7s target) ---
    Ava "Great catch! Now ride it out and keep your balance..."
    call surfbalancetraining_target(7.0)

    # If you hit balancesuccess above, jump to wave_complete.
    # jump wave_complete
    "Something went wrong"
    jump wavecatching