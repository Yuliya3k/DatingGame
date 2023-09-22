label culinarychoices:
    play music "audio/campfire.mp3" 
    $ position = "backyard"
    call sceneimg
    menu:
        "Go upstairs and look around":
            jump balcony
        "Go to the burger cafe":
            jump bcafe
        "Go to the bar":
            jump bar
    
    
    jump culiarychoices