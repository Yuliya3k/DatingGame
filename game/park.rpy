label park:
    play music "audio/sea.mp3" 
    call closescreens
    $ calendar.AddMinutes(20)


    if linrideabikesat == 1 and calendar.Hours >= 9 and calendar.Hours < 16 and calendar.WeekDay == "Sat":
        
        $ linrideabikesat = 0
        jump lincycling
    else:
        pass

    
    

    if calendar.Hours > 5 and calendar.Hours < 9:
        $ myrandom = renpy.random.randint(1,3)
        if myrandom == 1:
            $ position = "parkmorningwalk"
            call sceneimg  
            jump sallyfirsttime
        if myrandom == 2:
            if linfirsttime == 0:
                jump parknothing
            else:
                jump linpark
        if myrandom == 3:
            if linfirsttime == 0:
                jump parknothing
            jump lincycling
    if calendar.Hours > 17 and calendar.Hours < 23:        
        $ position = "parkeveningwalk"
        call sceneimg
        jump sallyfirsttime
    if calendar.Hours > 8 and calendar.Hours < 18:
        $ position = "parkwalk"
        call sceneimg
        

    label parknothing:
        $ position = "parkmorningseaview"
        call sceneimg  
        if parknothing == 0:
            $ parknothing = 1
            player "As I strolled along the ocean promenade, the salty breeze kissed my cheeks, and the rhythmic sound of waves crashing against the shore created a soothing melody. The sun dipped toward the horizon, casting a warm, golden glow across the sandy expanse. Seagulls glided effortlessly through the sky, their calls echoing in the distance."

            player "My footsteps left a faint imprint in the soft, sun-warmed sand as I walked, lost in thought. The ocean stretched out before me, its vastness seeming endless. Occasionally, a seashell or piece of driftwood would catch my eye, briefly distracting me from my contemplation."
            if calendar.Hours > 8 and calendar.Hours < 18:
                $ position = "parkocean"
            if calendar.Hours > 5 and calendar.Hours < 9:        
                $ position = "parkmorningseaview"
                call sceneimg    
            if calendar.Hours > 17 and calendar.Hours < 23:
                $ position = "parkeveningseaview"
                call sceneimg        
            "Despite the tranquil beauty of the scene, I noticed that the promenade was surprisingly empty today. It was just me and the ocean, as if the world had paused for a moment to let me savor the serenity of the sea. The absence of other people allowed me to immerse myself fully in the calming ambiance of the coastline."

            "I continued my leisurely walk, feeling a deep sense of peace wash over me. There was something magical about the ocean, its ever-changing nature mirroring the ebb and flow of life itself. As I gazed out at the vast, endless horizon, I couldn't help but feel a profound connection to the world around me.As I strolled along the ocean promenade, the salty breeze kissed my cheeks, and the rhythmic sound of waves crashing against the shore created a soothing melody. The sun dipped toward the horizon, casting a warm, golden glow across the sandy expanse. Seagulls glided effortlessly through the sky, their calls echoing in the distance."
            if calendar.Hours > 8 and calendar.Hours < 18:
                $ position = "parkbench"
                call sceneimg
            if calendar.Hours > 5 and calendar.Hours < 9:        
                $ position = "parkmorningbench"
                call sceneimg  
            if calendar.Hours > 17 and calendar.Hours < 23:        
                $ position = "parkeveningbench"
                call sceneimg
                
            "My footsteps left a faint imprint in the soft, sun-warmed sand as I walked, lost in thought. The ocean stretched out before me, its vastness seeming endless. Occasionally, a seashell or piece of driftwood would catch my eye, briefly distracting me from my contemplation."

            "Despite the tranquil beauty of the scene, I noticed that the promenade was surprisingly empty today. It was just me and the ocean, as if the world had paused for a moment to let me savor the serenity of the sea. The absence of other people allowed me to immerse myself fully in the calming ambiance of the coastline."

            "I continued my leisurely walk, feeling a deep sense of peace wash over me. There was something magical about the ocean, its ever-changing nature mirroring the ebb and flow of life itself. As I gazed out at the vast, endless horizon, I couldn't help but feel a profound connection to the world around me."
    
    label parkmenuloop:

        menu:
            "Go to the beach":
                jump avabeach
            "Take a look at a prom cafe" if calendar.Hours > 17 and calendar.Hours < 23 and promcafetoday == 0:

                call promcafe
            "Go home":
                jump culinarychoices
                $ calendar.AddMinutes(30)
        jump parkmenuloop

    jump culinarychoices

    
    return