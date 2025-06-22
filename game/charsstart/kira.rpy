label kira:

    define Kira = Character("Kira", colour="#000984")

    
    
    default kira_fullness = int(0)

    default kira_abolutemaxfullness = 8000

    default kira_minfullness = 400

    default kira_fullnessoz = int(kira_fullness*0.034)

    default kira_weight = 48

    default kira_weightlbs = int(kira_weight*2.2)

    default kira_fullmax = 4000

    default kira_fullmaxoz = int(kira_fullmax*0.034)

    default kira_weightmax = 120

    default kira_defaultweight = 48

    default kira_stamina = 15    

    # default kira_fullstage = 1

    default kira_weightstage = 1    

    default kira_eatdecision = 0    

    default kira_calories = 0

    default kira_attitude = 10

    default kira_maxattitude = 400      

    default kira_breakfast = 0

    default kira_lunch = 0

    default kira_dinner = 0

    default kira_fullstage = int(kira_fullness/kira_minfullness) + 1
    
    default kirafirsttime = 0

return