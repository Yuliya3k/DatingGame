label kiraweight:

    if wg == 1:
        $ kira_weight = int(kira_defaultweight + (kira_calories/7000))
        $ kira_weightlbs = int(kira_weight*2.2)
        if kira_weight <= kira_defaultweight + 3:
            $ kira_weightstage = 1
        else:
            if kira_weight <= kira_defaultweight + 6 and kira_weight > kira_defaultweight + 3:
                $ kira_weightstage = 2
            else:
                if kira_weight <= kira_defaultweight + 9 and kira_weight > kira_defaultweight + 6:
                    $ kira_weightstage = 3
                else:
                    if kira_weight <= kira_defaultweight + 12 and kira_weight > kira_defaultweight + 9:
                        $ kira_weightstage = 4
                    else:
                        if kira_weight <= kira_defaultweight + 15 and kira_weight > kira_defaultweight + 12:
                            $ kira_weightstage = 5
                        else:
                            if kira_weight <= kira_defaultweight + 18 and kira_weight > kira_defaultweight + 15:
                                $ kira_weightstage = 6
                            else:
                                if kira_weight > kira_defaultweight + 18:
                                    $ kira_weightstage = 6
    else:
        $ kira_weight = kira_defaultweight 

return