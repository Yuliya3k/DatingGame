label bardrinks:
    
    menu:
        "City Lights":
            Kira "Today, we're featuring a signature cocktail called the 'City Lights.' It's a delightful blend of citrus and a hint of spice."
            $ moneytoadd = -5
            call moneynotification
            if notenoughmoney == True:
                jump bar3
            else:
                $ fullnesschange = 200
                $ nigirlimage = "nikira"
                call fullnesschange
                pause 0.6
                $ calorieschange = 200
                $ nigirlimage = "nikira"
                call calorieschange
        "Sapphire Sunset":
            Kira "You can't go wrong with our 'Sapphire Sunset.' It's been a hit lately, and I think you'll love its smooth and refreshing taste."
            $ moneytoadd = -5
            call moneynotification
            if notenoughmoney == True:
                jump bar3
            else:
                $ fullnesschange = 200
                $ nigirlimage = "nikira"
                call fullnesschange
                pause 0.6
                $ calorieschange = 200
                $ nigirlimage = "nikira"
                call calorieschange
        "Mystic Mirage":
            Kira "Good choice! I whip up a 'Mystic Mirage' for you. It's a bit mysterious, just like the city."
            $ moneytoadd = -5
            call moneynotification
            if notenoughmoney == True:
                jump bar3
            else:
                $ fullnesschange = 200
                $ nigirlimage = "nikira"
                call fullnesschange
                pause 0.6
                $ calorieschange = 200
                $ nigirlimage = "nikira"
                call calorieschange
        "Moonlit Martini":
            Kira "Our 'Moonlit Martini' has been a long-time favorite. It's a classic, elegant choice."
            $ moneytoadd = -5
            call moneynotification
            if notenoughmoney == True:
                jump bar3
            else:
                $ fullnesschange = 200
                $ nigirlimage = "nikira"
                call fullnesschange
                pause 0.6
                $ calorieschange = 200
                $ nigirlimage = "nikira"
                call calorieschange
        "Starfall Sour":
            Kira "Today's special is a 'Starfall Sour.' It's a unique blend of sweet and sour with a hint of raspberry."
            $ moneytoadd = -5
            call moneynotification
            if notenoughmoney == True:
                jump bar3
            else:
                $ fullnesschange = 200
                $ nigirlimage = "nikira"
                call fullnesschange
                pause 0.6
                $ calorieschange = 200
                $ nigirlimage = "nikira"
                call calorieschange

    call drinkthank

return