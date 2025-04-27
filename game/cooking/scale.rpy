label scale:
    if speech == 1:        
        play sound "audio/rmcooking.mp3" volume 0.5

    $ rightpan = renpy.random.randint(1, 9)
    $ leftpan = renpy.random.randint(1, 9)
    $ scaleactive = 1
    $ cookingstatus = "Cooking"
    $ scalecrop_speed = renpy.random.randint(1, 9)
    $ scalepositioncoefficient = renpy.random.uniform(0.25, 0.75)
    $ scaleline_x1 = int(scaleimage_width * scalepositioncoefficient - cookingskill)
    # $ scaleline_y1 = int(scaleimage_height / 2)
    $ scaleline_x2 = int(scaleimage_width * scalepositioncoefficient + cookingskill)
    # $ scaleline_y2 = int(scaleimage_height / 2)
    $ scalesweetspotmin = scaleimage_width - scaleline_x2
    $ scalesweetspotmax = scaleimage_width - scaleline_x1

    while scaleactive == 1:
        pause 0.01
        if scalecrop_right >= scaleimage_width:
            $ poiterforward = 0

        if scalecrop_right <= 0:
            $ poiterforward = 1

        if scalecrop_right < scaleimage_width and poiterforward == 1 and scaleactive == 1:
            # $ x += 10
            $ scalecrop_right += scalecrop_speed
        if scalecrop_right > 0 and poiterforward == 0 and scaleactive == 1:
            # $ x -= 10
            $ scalecrop_right -= scalecrop_speed

        if scalecrop_right >= scalesweetspotmin and scalecrop_right <= scalesweetspotmax:
            $ scaleline_color = "#01b801"
        else:
            $ scaleline_color = "#3f0000"
            
        $ renpy.restart_interaction()  # Allow screen events (like clicks) to be processed.
    jump stoppointer
