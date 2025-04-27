label margo:

    define Margo = Character("Margo", colour="#000984")

    

    default margo_fullness = int(0)

    default margo_abolutemaxfullness = 8000

    default margo_minfullness = 400

    default margo_fullnessoz = int(margo_fullness*0.034)

    default margo_weight = 48

    default margo_weightlbs = int(margo_weight*2.2)

    default margo_fullmax = 800

    default margo_fullmaxoz = int(margo_fullmax*0.034)

    default margo_weightmax = 120

    default margo_defaultweight = 48

    default margo_stamina = 15        

    default margo_weightstage = 1    

    default margo_eatdecision = 0    

    default margo_calories = 0

    default margo_attitude = 10

    default margo_maxattitude = 400      

    default margo_breakfast = 0

    default margo_lunch = 0

    default margo_dinner = 0

    default margo_fullstage = int(margo_fullness/margo_minfullness) + 1
    
    default margofirsttime = 0

return