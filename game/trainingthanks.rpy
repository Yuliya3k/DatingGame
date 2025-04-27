label trainingthanks:
    $ reputationchange = 1
    $ nigirlimage = "nilin"
    call reputationchange
    $ calendar.AddMinutes(60)
    $ myrandom = renpy.random.randint(1,3)
    if myrandom == 1:

        player "Thanks for the workout today, Lin. It was tough, but I feel great. I'll see you next time."

        Lin "You're welcome, [name]. Rest up, and remember, consistency is key. Have a good one!"
    jump culinarychoices
    if myrandom == 2:

        player "I appreciate your help today, Lin. You really know how to push me. I'll be back for more."

        Lin "You're doing great, [name]. Keep up the hard work, and I'll be here whenever you're ready for the next session."
    jump culinarychoices
    if myrandom == 3:

        player "Lin, thanks for being patient with me during training. It means a lot. I'll head home and recover now."

        Lin "You're welcome, [name]. Remember, progress takes time. Take care, and I'll see you for the next session."  
        jump culinarychoices

"something went wrong"
jump culinarychoices