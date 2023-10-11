label aurora:

    define Aurora = Character("Aurora", colour="#000984")

    image aurora = "/images/aurorapos[position]weight[aurora_weightstage] ([aurora_fullstage]).png"
    
    default aurora_fullness = int(0)

    default aurora_abolutemaxfullness = 8000
    
    default aurora_minfullness = 400

    default aurora_fullnessoz = int(aurora_fullness*0.034)

    default aurora_weight = 50

    default aurora_weightlbs = int(aurora_weight*2.2)

    default aurora_fullmax = 800

    default aurora_fullmaxoz = int(aurora_fullmax*0.034)

    default aurora_weightmax = 120

    default aurora_defaultweight = 50

    default aurora_stamina = 15    

    default aurora_fullstage = 1

    default aurora_weightstage = 1    

    default aurora_eatdecision = 0    

    default aurora_calories = 0

    default aurora_attitude = 10

    default aurora_maxattitude = 400      

    default aurora_breakfast = 0

    default aurora_lunch = 0

    default aurora_dinner = 0

return