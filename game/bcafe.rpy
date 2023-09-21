label bcafe:
    $ position = "alexaworking"
    call sceneimg
    if alexafirsttime == 0:
        player "My exploration of the city led me to a bustling fast-food cafe where I met Alexa, a vivacious waitress. She's got an infectious enthusiasm that brightens up even the busiest of days. Though I've just moved here, I can sense a shared passion for food and cooking between us. Alexa and I haven't had a proper conversation yet, but I look forward to visiting the cafe more often and maybe striking up a friendship."
        $ alexafirsttime = 1
        menu:
            "You do not seem to be hungry for now":
                jump culinarychoices
    if alexafirsttime == 1:
        player "As I settled into my new life in the city, my taste buds were eager for adventure. One sunny afternoon, I decided to step into a bustling fast-food cafe near my place. It was the kind of spot where you ordered at the counter, and within moments, your meal would appear, hot and ready."

        player "I walked in, and the aroma of sizzling burgers and crispy fries greeted me like an old friend. The menu board overhead displayed an array of options, but one in particular caught my eye - the Classic Cravings Burger. I approached the counter, and a cheerful young woman named Alexa stood ready to take my order."

        player " 'Hello, welcome to Crave Bites,' she said with a bright smile. 'What can I get for you today?'"

        
        menu:
            "You do not seem to be hungry for now":
                "Hello! Sorry, not today I cahnged my mind"
                jump culinarychoices  
            "You order some food to eat":
                player "I didn't hesitate. 'I'll have the Classic Cravings Burger, please, with a milkshake.'"

                player "Alexa's nimble fingers danced across the register keys as she processed my order. She handed me a small receipt and a friendly nod, indicating my meal would be ready shortly. I took a seat by the window, the anticipation building with each passing second."

                player "I picked up the burger, its warmth radiating through the paper wrapping. My first bite was an explosion of flavors - the juicy beef, the tangy sauce, the crunch of lettuce - it was a symphony of taste. I couldn't help but savor each bite, sipping on a cold drink that accompanied the meal."

                player "As I enjoyed my burger, Alexa came over to ensure everything was to my liking. I couldn't contain my enthusiasm and praised the burger's deliciousness. She chuckled, clearly pleased, and mentioned that their burgers were a local favorite."

                player "That first bite of the Classic Cravings Burger at Crave Bites marked the beginning of my culinary journey in the city. Little did I know that this simple meal would be the first thread in a tapestry of connections, leading me to explore more about the city, its flavors, and the people who made it all so memorable."