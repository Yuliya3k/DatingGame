label calorieschange:

    # $ fullnesschange = 0
    # $ calorieschange = 0
    # $ calorieschange = 200
    # $ nigirlimage = "nilin"
    # call calorieschange

    if nigirlimage == "nilin":
        if lin_calories + calorieschange < 0:
            $ calorieschange = lin_calories
            $ calories = 0
        else:
            $ lin_calories += calorieschange

        if calorieschange > 0:
            $ niimage = "calories"    
            $ notify_success("+[calorieschange]")
        else:
            $ niimage = "calories"
            $ notify_success("[calorieschange]")    


    if nigirlimage == "nimargo":
        if margo_calories + calorieschange < 0:
            $ calorieschange = margo_calories
            $ calories = 0
        else:
            $ margo_calories += calorieschange

        if calorieschange > 0:
            $ niimage = "calories"    
            $ notify_success("+[calorieschange]")
        else:
            $ niimage = "calories"
            $ notify_success("[calorieschange]")  


    if nigirlimage == "nisally":
        if sally_calories + calorieschange < 0:
            $ calorieschange = sally_calories
            $ calories = 0
        else:
            $ sally_calories += calorieschange

        if calorieschange > 0:
            $ niimage = "calories"    
            $ notify_success("+[calorieschange]")
        else:
            $ niimage = "calories"
            $ notify_success("[calorieschange]")  


    if nigirlimage == "nihayoon":
        if hayoon_calories + calorieschange < 0:
            $ calorieschange = hayoon_calories
            $ calories = 0
        else:
            $ hayoon_calories += calorieschange

        if calorieschange > 0:
            $ niimage = "calories"    
            $ notify_success("+[calorieschange]")
        else:
            $ niimage = "calories"
            $ notify_success("[calorieschange]")  



    if nigirlimage == "niava":
        if ava_calories + calorieschange < 0:
            $ calorieschange = ava_calories
            $ calories = 0
        else:
            $ ava_calories += calorieschange

        if calorieschange > 0:
            $ niimage = "calories"    
            $ notify_success("+[calorieschange]")
        else:
            $ niimage = "calories"
            $ notify_success("[calorieschange]")  

    if nigirlimage == "nikira":
        if kira_calories + calorieschange < 0:
            $ calorieschange = kira_calories
            $ calories = 0
        else:
            $ kira_calories += calorieschange

        if calorieschange > 0:
            $ niimage = "calories"    
            $ notify_success("+[calorieschange]")
        else:
            $ niimage = "calories"
            $ notify_success("[calorieschange]")  



    return