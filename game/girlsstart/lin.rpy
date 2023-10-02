label lin:

    define Lin = Character("Lin", colour="#000984")

    image lin = "/images/linpos[position]weight[lin_weightstage] ([lin_fullstage]).png"

    default lin_fullness = int(0)

    default lin_abolutemaxfullness = 8000

    default lin_minfullness = 400

    default lin_fullnessoz = int(lin_fullness*0.034)

    default lin_weight = 48

    default lin_weightlbs = int(lin_weight*2.2)

    default lin_fullmax = 800

    default lin_fullmaxoz = int(lin_fullmax*0.034)

    default lin_weightmax = 120

    default lin_defaultweight = 48

    default lin_stamina = 15    

    # default lin_fullstage = 1

    default lin_weightstage = 1    

    default lin_eatdecision = 0    

    default lin_calories = 0

    default lin_attitude = 10

    default lin_maxattitude = 400      

    default lin_breakfast = 0

    default lin_lunch = 0

    default lin_dinner = 0

    default lin_fullstage = int(lin_fullness/lin_minfullness)
    
    default linfirsttime = 0

    

return