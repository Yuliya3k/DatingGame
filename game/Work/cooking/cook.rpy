label cook:
    if margo_fullmax != 4000:
        $ margo_fullmax = 4000
        
    play music "audio/rmkitchen.mp3" volume 0.3
    if calendar.Hours > 20:
        "Time to go home!"
        call endshift
        jump culinarychoices
    scene
    show screen kitchenscale

    pause

    jump cook