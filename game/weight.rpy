label weight:


    if wg == 1:

        

        $ g1_weight = int(g1_defaultweight + (g1_calories/7000))
        $ g2_weight = int(g2_defaultweight + (g2_calories/7000))
        $ g3_weight = int(g3_defaultweight + (g3_calories/7000))
        $ g4_weight = int(g4_defaultweight + (g4_calories/7000))
        $ g5_weight = int(g5_defaultweight + (g5_calories/7000))
        $ g6_weight = int(g6_defaultweight + (g6_calories/7000))

        $ g7_weight = int(g7_defaultweight + (g7_calories/7000))
        $ g8_weight = int(g8_defaultweight + (g8_calories/7000))
        $ g9_weight = int(g9_defaultweight + (g9_calories/7000))
        $ g10_weight = int(g10_defaultweight + (g10_calories/7000))
        $ g11_weight = int(g11_defaultweight + (g11_calories/7000))
        $ g12_weight = int(g12_defaultweight + (g12_calories/7000))
        $ g13_weight = int(g13_defaultweight + (g13_calories/7000))
        $ g14_weight = int(g14_defaultweight + (g14_calories/7000))
        # $ g1_weight = int(g1_defaultweight + (g1_calories/7000))

        if g1_weight <= 55:
            $ g1_weightstage = 1
        else:
            if g1_weight <= 58 and g1_weight > 55:
                $ g1_weightstage = 2
            else:
                if g1_weight <= 61 and g1_weight > 58:
                    $ g1_weightstage = 3
                else:
                    if g1_weight <= 65 and g1_weight > 61:
                        $ g1_weightstage = 4
                    else:
                        if g1_weight <= 68 and g1_weight > 65:
                            $ g1_weightstage = 5
                        else:
                            if g1_weight <= 71 and g1_weight > 68:
                                $ g1_weightstage = 6
                            else:
                                if g1_weight >71:
                                    $ g1_weightstage = 6



        if g2_weight <= 54:
            $ g2_weightstage = 1
        else:
            if g2_weight <= 56 and g2_weight > 54:
                $ g2_weightstage = 2
            else:
                if g2_weight <= 61 and g2_weight > 56:
                    $ g2_weightstage = 3
                else:
                    if g2_weight <= 64 and g2_weight > 61:
                        $ g2_weightstage = 4
                    else:
                        if g2_weight <= 67 and g2_weight > 64:
                            $ g2_weightstage = 5
                        else:
                            if g2_weight <= 70 and g2_weight > 67:
                                $ g2_weightstage = 6
                            else:
                                if g2_weight >70:
                                    $ g2_weightstage = 6


        if g3_weight <= 53:
            $ g3_weightstage = 1
        else:
            if g3_weight <= 59 and g3_weight > 53:
                $ g3_weightstage = 2
            else:
                if g3_weight <= 62 and g3_weight > 59:
                    $ g3_weightstage = 3
                else:
                    if g3_weight <= 65 and g3_weight > 62:
                        $ g3_weightstage = 4
                    else:
                        if g3_weight <= 68 and g3_weight > 65:
                            $ g3_weightstage = 5
                        else:
                            if g3_weight <= 71 and g3_weight > 68:
                                $ g3_weightstage = 6
                            else:
                                if g3_weight >71:
                                    $ g3_weightstage = 6



        $ g4_calories -= 1600
        if g4_calories < 0:
            $ g4_calories = 0
        else:
            pass




        if g4_weight <= 53:
            $ g4_weightstage = 1
        else:
            if g4_weight <= 59 and g4_weight > 53:
                $ g4_weightstage = 2
            else:
                if g4_weight <= 62 and g4_weight > 59:
                    $ g4_weightstage = 3
                else:
                    if g4_weight <= 65 and g4_weight > 62:
                        $ g4_weightstage = 4
                    else:
                        if g4_weight <= 68 and g4_weight > 65:
                            $ g4_weightstage = 5
                        else:
                            if g4_weight <= 71 and g4_weight > 68:
                                $ g4_weightstage = 6
                            else:
                                if g4_weight >71:
                                    $ g4_weightstage = 6

        $ g5_calories -= 1600
        if g5_calories < 0:
            $ g5_calories = 0
        else:
            pass




        if g5_weight <= 53:
            $ g5_weightstage = 1
        else:
            if g5_weight <= 59 and g5_weight > 53:
                $ g5_weightstage = 2
            else:
                if g5_weight <= 62 and g5_weight > 59:
                    $ g5_weightstage = 3
                else:
                    if g5_weight <= 65 and g5_weight > 62:
                        $ g5_weightstage = 4
                    else:
                        if g5_weight <= 68 and g5_weight > 65:
                            $ g5_weightstage = 5
                        else:
                            if g5_weight <= 71 and g5_weight > 68:
                                $ g5_weightstage = 6
                            else:
                                if g5_weight >71:
                                    $ g5_weightstage = 6






        if g6_weight <= 53:
            $ g6_weightstage = 1
        else:
            if g6_weight <= 59 and g6_weight > 53:
                $ g6_weightstage = 2
            else:
                if g6_weight <= 62 and g6_weight > 59:
                    $ g6_weightstage = 3
                else:
                    if g6_weight <= 65 and g6_weight > 62:
                        $ g6_weightstage = 4
                    else:
                        if g6_weight <= 68 and g6_weight > 65:
                            $ g6_weightstage = 5
                        else:
                            if g6_weight <= 71 and g6_weight > 68:
                                $ g6_weightstage = 6
                            else:
                                if g6_weight >71:
                                    $ g6_weightstage = 6




        if g7_weight <= 53:
            $ g7_weightstage = 1
        else:
            if g7_weight <= 59 and g7_weight > 53:
                $ g7_weightstage = 2
            else:
                if g7_weight <= 62 and g7_weight > 59:
                    $ g7_weightstage = 3
                else:
                    if g7_weight <= 65 and g7_weight > 62:
                        $ g7_weightstage = 4
                    else:
                        if g7_weight <= 68 and g7_weight > 65:
                            $ g7_weightstage = 5
                        else:
                            if g7_weight <= 71 and g7_weight > 68:
                                $ g7_weightstage = 6
                            else:
                                if g7_weight >71:
                                    $ g7_weightstage = 6







        if g8_weight <= 53:
            $ g8_weightstage = 1
        else:
            if g8_weight <= 59 and g8_weight > 53:
                $ g8_weightstage = 2
            else:
                if g8_weight <= 62 and g8_weight > 59:
                    $ g8_weightstage = 3
                else:
                    if g8_weight <= 65 and g8_weight > 62:
                        $ g8_weightstage = 4
                    else:
                        if g8_weight <= 68 and g8_weight > 65:
                            $ g8_weightstage = 5
                        else:
                            if g8_weight <= 71 and g8_weight > 68:
                                $ g8_weightstage = 6
                            else:
                                if g8_weight >71:
                                    $ g8_weightstage = 6




        if g10_weight <= 53:
            $ g10_weightstage = 1
        else:
            if g10_weight <= 59 and g10_weight > 53:
                $ g10_weightstage = 2
            else:
                if g10_weight <= 62 and g10_weight > 59:
                    $ g10_weightstage = 3
                else:
                    if g10_weight <= 65 and g10_weight > 62:
                        $ g10_weightstage = 4
                    else:
                        if g10_weight <= 68 and g10_weight > 65:
                            $ g10_weightstage = 5
                        else:
                            if g10_weight <= 71 and g10_weight > 68:
                                $ g10_weightstage = 6
                            else:
                                if g10_weight >71:
                                    $ g10_weightstage = 6



        if g11_weight <= 53:
            $ g11_weightstage = 1
        else:
            if g11_weight <= 59 and g11_weight > 53:
                $ g11_weightstage = 2
                $ g11_gainquestion = 1
            else:
                if g11_weight <= 62 and g11_weight > 59:
                    $ g11_weightstage = 3
                    $ g11_gainquestion = 1
                else:
                    if g11_weight <= 65 and g11_weight > 62:
                        $ g11_weightstage = 4
                        $ g11_gainquestion = 1
                    else:
                        if g11_weight <= 68 and g11_weight > 65:
                            $ g11_weightstage = 5
                            $ g11_gainquestion = 1
                        else:
                            if g11_weight <= 71 and g11_weight > 68:
                                $ g11_weightstage = 6
                                $ g11_gainquestion = 1
                            else:
                                if g11_weight >71:
                                    $ g11_weightstage = 6
        if g12_weight <= 53:
            $ g12_weightstage = 1
        else:
            if g12_weight <= 59 and g12_weight > 53:
                $ g12_weightstage = 2
                $ g12_gainquestion = 1
            else:
                if g12_weight <= 62 and g12_weight > 59:
                    $ g12_weightstage = 3
                    $ g12_gainquestion = 1
                else:
                    if g12_weight <= 65 and g12_weight > 62:
                        $ g12_weightstage = 4
                        $ g12_gainquestion = 1
                    else:
                        if g12_weight <= 68 and g12_weight > 65:
                            $ g12_weightstage = 5
                            $ g12_gainquestion = 1
                        else:
                            if g12_weight <= 71 and g12_weight > 68:
                                $ g12_weightstage = 6
                                $ g12_gainquestion = 1
                            else:
                                if g12_weight >71:
                                    $ g12_weightstage = 6
        if g13_weight <= 53:
            $ g13_weightstage = 1
        else:
            if g13_weight <= 59 and g13_weight > 53:
                $ g13_weightstage = 2
                $ g13_gainquestion = 1
            else:
                if g13_weight <= 62 and g13_weight > 59:
                    $ g13_weightstage = 3
                    $ g13_gainquestion = 1
                else:
                    if g13_weight <= 65 and g13_weight > 62:
                        $ g13_weightstage = 4
                        $ g13_gainquestion = 1
                    else:
                        if g13_weight <= 68 and g13_weight > 65:
                            $ g13_weightstage = 5
                            $ g13_gainquestion = 1
                        else:
                            if g13_weight <= 71 and g13_weight > 68:
                                $ g13_weightstage = 6
                                $ g13_gainquestion = 1
                            else:
                                if g13_weight >71:
                                    $ g13_weightstage = 6
        if g14_weight <= 53:
            $ g14_weightstage = 1
        else:
            if g14_weight <= 59 and g14_weight > 53:
                $ g14_weightstage = 2
                $ g14_gainquestion = 1
            else:
                if g14_weight <= 62 and g14_weight > 59:
                    $ g14_weightstage = 3
                    $ g14_gainquestion = 1
                else:
                    if g14_weight <= 65 and g14_weight > 62:
                        $ g14_weightstage = 4
                        $ g14_gainquestion = 1
                    else:
                        if g14_weight <= 68 and g14_weight > 65:
                            $ g14_weightstage = 5
                            $ g14_gainquestion = 1
                        else:
                            if g14_weight <= 71 and g14_weight > 68:
                                $ g14_weightstage = 6
                                $ g14_gainquestion = 1
                            else:
                                if g14_weight >71:
                                    $ g14_weightstage = 6
    else:
        $ g1_weight = g1_defaultweight
        $ g2_weight = g2_defaultweight
        $ g3_weight = g3_defaultweight
        $ g4_weight = g4_defaultweight
        $ g5_weight = g5_defaultweight
        $ g6_weight = g6_defaultweight
        $ g7_weight = g7_defaultweight
        $ g8_weight = g8_defaultweight
        $ g9_weight = g9_defaultweight
        $ g10_weight = g10_defaultweight
        $ g11_weight = g11_defaultweight
        $ g12_weight = g12_defaultweight
        $ g13_weight = g13_defaultweight
        $ g14_weight = g14_defaultweight


return
