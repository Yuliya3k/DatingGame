label cook:
    play music "audio/rmkitchen.mp3" volume 0.3
    if calendar.Hours > 20:
        "Time to go home!"
        jump culinarychoices
    scene
    show screen kitchenscale

    pause

    jump cook