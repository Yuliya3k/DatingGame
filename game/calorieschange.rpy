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


    return