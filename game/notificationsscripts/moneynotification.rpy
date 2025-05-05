label moneynotification:
    # if notenoughmoney == True:
    # $ moneytoadd = -5
    # call moneynotification

    $ nigirlimage = ""

    if money + moneytoadd < 0:
        $ niimage = "money"   
        $ notify_success("Not enough money")
        $ notenoughmoney = True
        
        return

    else:
        
        $ notenoughmoney == False
        if moneytoadd < 0:
            
            $ money += moneytoadd
            $ niimage = "money"   
            $ notify_success("[moneytoadd]")
            pause 0.5
            
        else:
            
            $ money += moneytoadd
            $ niimage = "money"    
            $ notify_success("+[moneytoadd]")
            pause 0.5
            


        # $ niimage = "money"   
        # $ notify_success("Not enough money")
        # $ notenoughmoney == False
        # if calorieschange > 0:RR
        #     $ niimage = "money"    
        #     $ notify_success("+[moneytoadd]")
        # else:
        #     $ niimage = "money"
        #     $ notify_success("[moneytoadd]") 

    
    # $ moneytoadd = 0
    return