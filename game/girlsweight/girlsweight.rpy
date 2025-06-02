label girlsweight:
    
    $ caloriesperkg = 3500
    if wg == 1:
        $ sally_weight = int(sally_defaultweight + (sally_calories/caloriesperkg))
        $ sally_weightlbs = int(sally_weight*2.2)
        $ sally_weightstage = int((sally_weight - sally_defaultweight)/3)
        if sally_weightstage > 6:
            $ sally_weightstage = 6
        if sally_weightstage < 1:
            $ sally_weightstage = 1

        $ ava_weight = int(ava_defaultweight + (ava_calories/caloriesperkg))
        $ ava_weightlbs = int(ava_weight*2.2)
        $ ava_weightstage = int((ava_weight - ava_defaultweight)/3)
        if ava_weightstage > 6:
            $ ava_weightstage = 6
        if ava_weightstage < 1:
            $ ava_weightstage = 1

        $ lin_weight = int(lin_defaultweight + (lin_calories/caloriesperkg))
        $ lin_weightlbs = int(lin_weight*2.2)
        $ lin_weightstage = int((lin_weight - lin_defaultweight)/3)
        if lin_weightstage > 6:
            $ lin_weightstage = 6
        if lin_weightstage < 1:
            $ lin_weightstage = 1

        $ hayoon_weight = int(hayoon_defaultweight + (hayoon_calories/caloriesperkg))
        $ hayoon_weightlbs = int(hayoon_weight*2.2)
        $ hayoon_weightstage = int((hayoon_weight - hayoon_defaultweight)/3)
        if hayoon_weightstage > 6:
            $ hayoon_weightstage = 6
        if hayoon_weightstage < 1:
            $ hayoon_weightstage = 1

        $ margo_weight = int(margo_defaultweight + (margo_calories/caloriesperkg))
        $ margo_weightlbs = int(margo_weight*2.2)
        $ margo_weightstage = int((margo_weight - margo_defaultweight)/3)
        if margo_weightstage > 6:
            $ margo_weightstage = 6
        if margo_weightstage < 1:
            $ margo_weightstage = 1

        $ kira_weight = int(kira_defaultweight + (kira_calories/caloriesperkg))
        $ kira_weightlbs = int(kira_weight*2.2)
        $ kira_weightstage = int((kira_weight - kira_defaultweight)/3)
        if kira_weightstage > 6:
            $ kira_weightstage = 6
        if kira_weightstage < 1:
            $ kira_weightstage = 1

        $ kris_weight = int(kris_defaultweight + (kris_calories/caloriesperkg))
        $ kris_weightlbs = int(kris_weight*2.2)
        $ kris_weightstage = int((kris_weight - kris_defaultweight)/3)
        if kris_weightstage > 6:
            $ kris_weightstage = 6
        if kris_weightstage < 1:
            $ kris_weightstage = 1

        # $ farida_weight = int(farida_defaultweight + (farida_calories/caloriesperkg))
        # $ farida_weightlbs = int(farida_weight*2.2)
        # $ farida_weightstage = int((farida_weight - farida_defaultweight)/3)
        # if farida_weightstage > 6:
        #     $ farida_weightstage = 6
        # if farida_weightstage < 1:
        #     $ farida_weightstage = 1
        $ farida_weightstage = 1

    else:
        $ sally_weight = sally_defaultweight
        $ lin_weight = lin_defaultweight
        $ hayoon_weight = hayoon_defaultweight
        $ ava_weight = ava_defaultweight
        $ margo_weight = margo_defaultweight
        $ kira_weight = kira_defaultweight
        $ kris_weight = kris_defaultweight
        $ kira_weightstage = 1
        $ sally_weightstage = 1
        $ lin_weightstage = 1
        $ hayoon_weightstage = 1
        $ ava_weightstage = 1
        $ margo_weightstage = 1
        $ kris_weightstage = 1
        $ farida_weightstage = 1



    return