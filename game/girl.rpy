label girl:
    label g1girl:
        $ g1_fullnessoz = int(g1_fullness*0.034)  
        if kira_fullness <= kira_minfullness:
            $ g1_fullstage = 1
        else:
            if kira_fullness <= kira_minfullness + kira_minfullness*2 and kira_fullness > kira_minfullness:
                $ g1_fullstage =2
            else:
                if kira_fullness <= kira_minfullness + kira_minfullness*3 and kira_fullness > kira_minfullness + kira_minfullness*2:
                    $ g1_fullstage =3
                else:
                    if kira_fullness <= kira_minfullness + kira_minfullness*4 and kira_fullness > kira_minfullness + kira_minfullness*3:
                        $ g1_fullstage =4
                    else:
                        if kira_fullness <= kira_minfullness + kira_minfullness*5 and kira_fullness > kira_minfullness + kira_minfullness*4:
                            $ g1_fullstage =5
                        else:
                            if kira_fullness <= kira_minfullness + kira_minfullness*6 and kira_fullness > kira_minfullness + kira_minfullness*5:
                                $ g1_fullstage =6
                            else:
                                if kira_fullness <= kira_minfullness + kira_minfullness*7 and kira_fullness > kira_minfullness + kira_minfullness*6:
                                    $ g1_fullstage =7
                                else:
                                    if kira_fullness <= kira_minfullness + kira_minfullness*8 and kira_fullness > kira_minfullness + kira_minfullness*7:
                                        $ g1_fullstage =8
                                    else:
                                        if kira_fullness <= kira_minfullness + kira_minfullness*9 and kira_fullness > kira_minfullness + kira_minfullness*8:
                                            $ g1_fullstage =9
                                        else:
                                            if kira_fullness <= kira_minfullness + kira_minfullness*10 and kira_fullness > kira_minfullness + kira_minfullness*9:
                                                $ g1_fullstage =10
                                            else:
                                                if kira_fullness <= kira_minfullness + kira_minfullness*11 and kira_fullness > kira_minfullness + kira_minfullness*10:
                                                    $ g1_fullstage =11
                                                else:
                                                    if kira_fullness <= kira_minfullness + kira_minfullness*12 and kira_fullness > kira_minfullness + kira_minfullness*11:
                                                        $ g1_fullstage =12
                                                    else:
                                                        if kira_fullness <= kira_minfullness + kira_minfullness*13 and kira_fullness > kira_minfullness + kira_minfullness*12:
                                                            $ g1_fullstage =13
                                                        else:
                                                            if kira_fullness <= kira_minfullness + kira_minfullness*14 and kira_fullness > kira_minfullness + kira_minfullness*13:
                                                                $ g1_fullstage =14
                                                            else:
                                                                if kira_fullness <= kira_minfullness + kira_minfullness*15 and kira_fullness > kira_minfullness + kira_minfullness*14:
                                                                    $ g1_fullstage =15
                                                                else:
                                                                    if kira_fullness <= kira_minfullness + kira_minfullness*16 and kira_fullness > kira_minfullness + kira_minfullness*15:
                                                                        $ g1_fullstage =16
                                                                    else:
                                                                        if kira_fullness <= kira_minfullness + kira_minfullness*17 and kira_fullness > kira_minfullness + kira_minfullness*16:
                                                                            $ g1_fullstage =17
                                                                        else:
                                                                            if kira_fullness <= kira_minfullness + kira_minfullness*18 and kira_fullness > kira_minfullness + kira_minfullness*17:
                                                                                $ g1_fullstage =18
                                                                            else:
                                                                                if kira_fullness <= kira_minfullness + kira_minfullness*19 and kira_fullness > kira_minfullness + kira_minfullness*18:
                                                                                    $ g1_fullstage =19
                                                                                else:
                                                                                    if kira_fullness <= kira_minfullness + kira_minfullness*20 and kira_fullness > kira_minfullness + kira_minfullness*19:
                                                                                        $ g1_fullstage =20
                                                                                    else:
                                                                                        if kira_fullness > kira_minfullness + kira_minfullness*20:
                                                                                            $ g1_fullstage =20
                                                                                        else:
                                                                                            pass
        return


    