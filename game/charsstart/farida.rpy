label farida:
    define farida = Character("Farida", colour="#000984")

    

    default farida_fullness = int(0)

    default farida_abolutemaxfullness = 8000

    default farida_minfullness = 400

    default farida_fullnessoz = int(farida_fullness*0.034)

    default farida_weight = 48

    default farida_weightlbs = int(farida_weight*2.2)

    default farida_fullmax = 4000

    default farida_fullmaxoz = int(farida_fullmax*0.034)

    default farida_weightmax = 120

    default farida_defaultweight = 48

    default farida_stamina = 15        

    default farida_weightstage = 1    

    default farida_eatdecision = 0    

    default farida_calories = 0

    default farida_attitude = 10

    default farida_maxattitude = 400      

    default farida_breakfast = 0

    default farida_lunch = 0

    default farida_dinner = 0

    default farida_fullstage = int(farida_fullness/farida_minfullness) + 1
    
    default faridafirsttime = 0