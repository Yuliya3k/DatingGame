label bar1:
    call closescreens
    $ calendar.AddMinutes(20)
    play music "audio/barcity.mp3" volume 0.5
    $ position = "barenterance"
    call sceneimg
    if speech == 1:
        play sound "audio/Waren-1946307.mp3"
    player "I had just moved to the city when I stumbled upon a vibrant bar downtown."

    
    if speech == 1:
        play sound "audio/Waren-1946317.mp3"
    player "The city had begun to reveal its secrets to me, one adventure at a time. On a warm evening, the streets buzzed with activity as I decided to venture out and explore the local nightlife. A particular spot had caught my eye - 'Kira's Haven,' a neon-lit sign proudly proclaimed."

    play music "audio/bar.mp3" volume 0.3
    $ position = "kiraenterance"
    call sceneimg
    if speech == 1:
        play sound "audio/Waren-1946321.mp3"
    player "With curiosity as my guide, I entered the establishment. The atmosphere inside was cozy, with a subtle blend of dim lighting and the mellow hum of conversation. It was clear that Kira's Haven was more than just a bar; it was a place where people came to unwind and connect."

    $ position = "kiraworking2"
    call sceneimg
    if speech == 1:
        play sound "audio/Waren-1946454.mp3"
    player "I found an open spot at the bar counter, just in front of Kira. The bartender, a confident woman of around 35 years with blonde hair cascading over her shoulders, greeted me with a friendly smile. Her vibrant blue eyes sparkled as she said..."

    $ position = "kiraquestion"
    call sceneimg
    if speech == 1:
        play sound "audio/Zoey-1946357.mp3"
    Kira "Welcome to Kira's Haven. What can I get you tonight?"

    $ position = "kiraworking"
    call sceneimg
    if speech == 1:
        play sound "audio/Waren-1946329.mp3"
    player "I briefly scanned the drink menu but decided to trust Kira's expertise."
    if speech == 1:
        play sound "audio/Waren-1946397.mp3"
    player "Surprise me" 

    $ position = "kiraworking2"
    call sceneimg
    if speech == 1:
        play sound "audio/Waren-1946331.mp3"
    player "Kira's nimble hands worked their magic as she concocted a unique cocktail. The shakers clinked melodically, and the resulting drink was a dazzling mix of colors and flavors. She placed it before me, and I couldn't help but admire the artistry."

    $ position = "kiraworking"
    call sceneimg
    if speech == 1:
        play sound "audio/Waren-1946336.mp3"
    player "I took a sip, and an explosion of flavors danced on my palate. It was the perfect blend of sweet and tart, with a hint of something exotic that I couldn't quite place. The drink was as unique as the bar itself, and it felt like a taste of the city's essence."

    $ position = "kiraflirting"
    call sceneimg
    if speech == 1:
        play sound "audio/Waren-1946340.mp3"
    player "As I savored the drink, Kira leaned in slightly, striking up a conversation. She shared stories about the bar's history, its regular patrons, and the vibrant culture of the city. Her words painted a vivid picture of life in this bustling metropolis."
    $ position = "kiraworking2"
    call sceneimg
    if speech == 1:
        play sound "audio/Waren-1946342.mp3"
    player "Kira herself was a fascinating character. She had left behind a successful career as a doctor to follow her passion for mixology and bartending. The decision had been driven by a desire for a different kind of healing, one that came through laughter, camaraderie, and the magic of a well-made cocktail."
    $ position = "kiraworking"
    call sceneimg
    if speech == 1:
        play sound "audio/Waren-1946346.mp3"
    player "The evening passed in a delightful blur of laughter, shared stories, and one more expertly crafted cocktail after another. It was my first visit to Kira's Haven, but it certainly wouldn't be my last. I left the bar that night with a sense of belonging, as if I'd discovered a hidden corner of the city where I could always find good company and a delicious drink."


    $ position = "home"
    call sceneimg
    if speech == 1:
        play sound "audio/Waren-1946347.mp3"
    player "Little did I know that this encounter with Kira would be just the beginning of my journey in this city, a journey filled with new experiences, connections, and perhaps even a few unexpected twists along the way."
    $ kirafirsttime = 1
    jump culinarychoices