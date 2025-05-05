label bar1:
    call closescreens
    $ calendar.AddMinutes(20)
    play music "audio/barcity.mp3" volume 0.5
    $ position = "barenterance"
    call sceneimg
    # if speech == 1:
    #     play sound "audio/Waren-1946307.mp3"
    player "New city, new night—my feet led me to a buzzing downtown bar."

    
    #if speech == 1:
    #    play sound "audio/Waren-1946317.mp3"
    player "On warm evenings, the streets hum with promise. Tonight, neon spelled ‘Kira’s Haven.’ Curiosity won out."

    play music "audio/bar.mp3" volume 0.3
    $ position = "kiraenterance"
    call sceneimg
    #if speech == 1:
    #    play sound "audio/Waren-1946321.mp3"
    player "Inside, soft lights and friendly chatter wrapped around me. Kira’s Haven felt like home, not just a bar."

    $ position = "kiraworking2"
    call sceneimg
    #if speech == 1:
    #    play sound "audio/Waren-1946454.mp3"
    player "I slid onto a stool at the polished counter. Kira—35, blonde hair, sparkling blue eyes—greeted me like an old friend."

    $ position = "kiraquestion"
    call sceneimg
    #if speech == 1:
    #    play sound "audio/Zoey-1946357.mp3"
    Kira "Welcome to Kira's Haven. What can I get you tonight?"

    $ position = "kiraworking"
    call sceneimg
    #if speech == 1:
    #    play sound "audio/Waren-1946329.mp3"
    player "Menu’s full of temptations, but I trusted her."
    #if speech == 1:
    #    play sound "audio/Waren-1946397.mp3"
    player "Surprise me."

    $ position = "kiraworking2"
    call sceneimg
    #if speech == 1:
    #    play sound "audio/Waren-1946331.mp3"
    player "Shaker tin in hand, Kira crafted a jewel of a cocktail. Colors swirled; scents rose."

    $ position = "kiraworking"
    call sceneimg
    #if speech == 1:
    #    play sound "audio/Waren-1946336.mp3"
    player "That first sip—sweet, tart, with a whisper of something exotic—felt like the city in a glass."

    $ position = "kiraflirting"
    call sceneimg
    #if speech == 1:
    #    play sound "audio/Waren-1946340.mp3"
    player "Between sips, Kira leaned close, spinning tales of the bar’s origin, its regulars, and the city’s heartbeat."
    $ position = "kiraworking2"
    call sceneimg
    #if speech == 1:
    #    play sound "audio/Waren-1946342.mp3"
    player "She’d traded medicine for mixology—healing through laughter and craft over charts and charts."
    $ position = "kiraworking"
    call sceneimg
    #if speech == 1:
    #    play sound "audio/Waren-1946346.mp3"
    player "Hours flew by in shared jokes and another perfect cocktail. My first night at Kira’s Haven—and certainly not my last. I left feeling seen, with a promise of return."

    $ position = "home"
    call sceneimg
    #if speech == 1:
    #    play sound "audio/Waren-1946347.mp3"
    player "I couldn’t know then how meeting Kira would shape my journey here—full of friendship, flavor, and surprises."
    $ kirafirsttime = 1
    jump culinarychoices