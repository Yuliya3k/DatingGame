label julia:

    define Julia = Character("julia", colour="#000984")

    

    default julia_fullness = int(0)

    default julia_abolutemaxfullness = 8000

    default julia_minfullness = 400

    default julia_fullnessoz = int(julia_fullness*0.034)

    default julia_weight = 48

    default julia_weightlbs = int(julia_weight*2.2)

    default julia_fullmax = 4000

    default julia_fullmaxoz = int(julia_fullmax*0.034)

    default julia_weightmax = 120

    default julia_defaultweight = 48

    default julia_stamina = 15        

    default julia_weightstage = 1    

    default julia_eatdecision = 0    

    default julia_calories = 0

    default julia_attitude = 10

    default julia_maxattitude = 400      

    default julia_breakfast = 0

    default julia_lunch = 0

    default julia_dinner = 0

    default julia_fullstage = int(julia_fullness/julia_minfullness) + 1
    
    default juliafirsttime = 0

return