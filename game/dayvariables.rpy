label dayvariables:
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

    # if calendar.WeekDay == 'Tue' and calendar.TotalDays > 6:
    #         $ payrent = 0
    # else:
    #
    #     if calendar.WeekDay == 'Mon' and calendar.TotalDays > 6 and payrent < 1:
    #         "It is time to pay rent. You must pay $250"
    #         if money >= 250:
    #             "You've successfuly paid the rent"
    #             $ money -= 250
    #             $ payrent += 1
    #         else:
    #             "You do not have enough money to pay the rent. Game is over for you, sorry!"
    #             show text "{size=90} Game over {/size}" at truecenter
    #             with slowdissolve
    #             pause
    #             hide text
    #             with dissolve
    #             $ renpy.quit()
    #     else:
    #         pass
#label capacity:
    $ calendar.AddDay(1)
    $ calendar.hours = 9
    
    
    if g1_fullness >= g1_fullmax and g1_fullmax <= 4000:
        $ g1_fullmax += 50
        $ g1_fullmax += g1_capacitygain
        #$ g1_fullmax == int(g1_fullmax)
    else:
        if g1_fullness <= g1_fullmax*0.5 and g1_fullmax > 800:
            $ g1_fullmax -= 50
            $ g1_fullmax += g1_capacitygain
            #$ g1_fullmax == int(g1_fullmax)
        else:
            pass
#     if g2_fullness >= g2_fullmax*0.5 and g2_fullmax <=4000:
#         $ g2_fullmax += 50
#         $ g2_fullmax += g2_capacitygain
#     else:
#         if g2_fullness <= g2_fullmax*0.5 and g2_fullmax > 800:
#             $ g2_fullmax -= 50
#             $ g2_fullmax += g2_capacitygain
#         else:
#             pass
#     if g3_fullness > 0 and g3_fullmax <=7800:

#         $ g3_fullmax += 100

#     else:
#         pass

#     if g4_fullmax <= 4000 and g4_fullness > 0:
#         # $ g4_capacitygain += g4_fullness*0.1
#         $ g4_fullmax += 100
#         # $ g4_fullmax += g4_capacitygain
#     else:
#         pass
#     $ g4_fullness = 0

#     if g5_fullmax <= 8000 and g5_fullness > 0:
#         # $ g5_capacitygain += g5_fullness*0.1
#         $ g5_fullmax += 100
#         # $ g5_fullmax += g5_capacitygain
#     else:
#         pass
#     $ g5_fullness = 0


#     if g6_fullmax <= 8000 and g6_fullness > 0:
#         # $ g6_capacitygain += g6_fullness*0.1
#         $ g6_fullmax += 100 + g6_attitude/100
#         # $ g6_fullmax += g6_capacitygain
#     else:
#         pass
#     if g6_cravings == 0:
#         $ g6_fullness = 0
#     else:
#         $ g6_fullness = renpy.random.randint(3000,6000)
#         call g6girl

#     if g12_fullmax <= 8000 and g12_fullness > 0:
#         # $ g12_capacitygain += g12_fullness*0.1
#         $ g12_fullmax += 100 + g12_attitude/100
#         # $ g12_fullmax += g12_capacitygain
#     else:
#         pass
#     if g12_cravings == 0:
#         $ g12_fullness = 0
#     else:
#         $ g12_fullness = renpy.random.randint(3000,6000)
#         call g12girl

#     if g13_fullmax <= 8000 and g13_fullness > 0:
#         # $ g13_capacitygain += g13_fullness*0.1
#         $ g13_fullmax += 100 + g13_attitude/100
#         # $ g13_fullmax += g13_capacitygain
#     else:
#         pass
#     if g13_cravings == 0:
#         $ g13_fullness = 0
#     else:
#         $ g13_fullness = renpy.random.randint(3000,6000)
#         call g13girl
#     $ g14_fullness = 0
#     if g7_fullmax <= 8000 and g7_fullness > 0:
#         # $ g7_capacitygain += g7_fullness*0.1
#         $ g7_fullmax += 100
#         # $ g7_fullmax += g7_capacitygain
#     else:
#         pass
#     $ g7_fullness = 0


# #label g1_weight:
#     if g4_swamp == 1:
#         if money >= 10:
#             $ money -= 10
#         else:
#             $ money = 0





# $ firsttimeatworktoday = 1
# hide g1 with slowdissolve
# if g1_calories >= 1200:
#     $ g1_calories -= 1200
# else:
#     if g1_calories < 0:
#         $ g1_calories = 0
#     else:
#         pass

# # if daytime > 0 and daytime < 7:
# #     $ daytime = 7
# # else:
# #     if daytime >= 7 and daytime < 24:
# #         $ day += 1
# #         $ daytime = 7
# #         call weekday
# #     else:
# #         pass
# # $ day += 1


# call weight
# # call capacity
# $ stamina = 16
# $ g1_fullness = 0
# $ g1_breakfast = 0
# $ g1_lunch = 0
# $ g1_dinner = 0
# $ g1_position = 1
# $ companycheckcount = 3
# $ daycompliment = 1

# $ stretch8 = 0
# $ stretch9 = 0
# $ stretch10 = 0
# $ explode10 = 0

# $ g1_fullness = 0





# $ g1_fullmax = g1_fullmax + g1_capacity_plan

# $ g1_fullmaxoz = g1_fullmax*0.034

# $ stamina = 16

# $ g1_maxattitude = 400

# $ g1_confidence = 1

# $ d_liquid = 0

# $ g1_breakfast = 0

# $ g1_lunch = 0

# $ g1_dinner = 0

# $ g1_eatdecision = 0

# $ g2_fullness = 0



# $ g3_button_pop = 1

# $ g2_weightlbs = int(g2_weight*2.2)

# $ g3_noclubtoday = 0

# $ g2_fullmaxoz = int(g2_fullmax*0.034)

# $ g2_maxattitude = 400

# $ g2_confidence = 1

# $ g1_stamina = 15
# $ g2_stamina = 15
# $ g3_stamina = 15

# $ g2_breakfast = 0

# $ g3_alcattitude = 0

# $ g2_lunch = 0

# $ g2_dinner = 0

# $ g2_eatdecision = 0

# $ g3_fullness = 0

# $ g3_secretroomopen = 0

# $ g1_fullnessoz = int(g1_fullness*0.034)

# $ g1_weightlbs = int(g1_weight*2.2)

# $ g1_fullmaxoz = int(g1_fullmax*0.034)

# $ g2_fullnessoz = int(g2_fullness*0.034)

# $ g2_weightlbs = int(g2_weight*2.2)

# $ g2_fullmaxoz = int(g2_fullmax*0.034)

# $ g3_fullnessoz = int(g3_fullness*0.034)

# $ g3_weightlbs = int(g3_weight*2.2)

# $ g3_fullmaxoz = int(g3_fullmax*0.034)

# $ g4_fullnessoz = int(g4_fullness*0.034)

# $ g4_weightlbs = int(g4_weight*2.2)

# $ g4_fullmaxoz = int(g4_fullmax*0.034)

# $ g5_fullnessoz = int(g5_fullness*0.034)

# $ g5_weightlbs = int(g5_weight*2.2)

# $ g5_fullmaxoz = int(g5_fullmax*0.034)

# $ g6_fullnessoz = int(g6_fullness*0.034)

# $ g6_weightlbs = int(g6_weight*2.2)

# $ g6_fullmaxoz = int(g6_fullmax*0.034)

# $ g3_breakfast = 0

# $ g3_lunch = 0

# $ g3_dinner = 0

# $ g3_capacitygain = 0

# $ fired = 0

# $ daycompliment = 1

# # $ payrent = 1

# $ firstcall = 1

# $ explode10 = 0

# $ results = 0

# # $ welldone = 0

# $ stretch8 = 0

# $ stretch9 = 0

# $ stretch10 = 0

# $ allclothes = 0

# $ endgame = 0

# $ goodwork = 0

# $ beercapacity = 1200

# $ clubcounter = 6

# $ g3_drunk = 0

# $ g2_camehome = 0

# # $ weekdaynumber = 1



# # $ companycheckcount = 1

# # $ companycheck = 0

# # $ samples = 0

# # $ delivery = 0

# # $ delivered = 0

# # $ partner = 0

# $ tasteresults = 0

# $ outofbreath = 0

# $ sportcalories = 0

# # $ water = 0

# # $ contracts = 0

# $ g11_stretch8 = 0

# $ g11_stretch9 = 0

# $ g11_stretch10 = 0
# $ g11_stretch11 = 0
# $ g11_stretch12 = 0
# $ g11_stretch13 = 0
# $ g11_stretch14 = 0
# $ g11_stretch15 = 0
# $ g11_stretch16 = 0

# $ g11_stretch17 = 0
# $ g11_stretch18 = 0
# $ g11_stretch19 = 0
# $ g11_stretch20 = 0
# $ g11_stretch21 = 0

# $ g8_calories += g8_gain
# $ g8_calories -= 1200
# if g8_calories < 0:
#     $ g8_calories = 0
# else:
#     pass


# $ g8_musclestage = g8_musclepoints/200
# if g8_musclestage <= 10:
#     $ g8_musclestage = int(g8_musclestage) + 1
# else:
#     if g8_musclestage > 10:
#         $ g8_musclestage = 10

# if g8_fullmax <= 4000:
#     # $ g4_capacitygain += g4_fullness*0.1
#     $ g8_fullmax += 100
#     # $ g4_fullmax += g4_capacitygain
# else:
#     pass

# $ g8_fullness = 0 + g8_waterbelly



# $ g9_fullmax += 200
# $ g9_fullness = 0
# $ g9_stamina = 15

# if g9_bellystage == 1 and g9_fullmax >= 4000:
#     $ g9_bellystage = 2
# else:
#     if g9_bellystage == 2 and g9_fullmax >= 6000:
#         $ g9_bellystage = 3
#     else:
#         if g9_bellystage == 3 and g9_fullmax >= 8000:
#             $ g9_bellystage = 4
#         else:
#             pass





# $ g8_stamina = 15 + g8_staminabonus

# $ g10_fullmax += 200
# $ g10_fullness = 0
# $ g10_stamina = 15



# if g11_attitude < 50:
#     $ g11_breakfast = 1

#     $ g11_lunch = 1

#     $ g11_dinner = 1

# else:
#     if g11_attitude >= 50 and g11_attitude < 100:
#         $ g11_breakfast = 2

#         $ g11_lunch = 2

#         $ g11_dinner = 2
#     else:
#         if g11_attitude >= 100 and g11_attitude < 150:
#             $ g11_breakfast = 3

#             $ g11_lunch = 3

#             $ g11_dinner = 3
#         else:
#             if g11_attitude >= 150 and g11_attitude < 200:
#                 $ g11_breakfast = 4

#                 $ g11_lunch = 4

#                 $ g11_dinner = 4
#             else:
#                 if g11_attitude >= 200 and g11_attitude < 250:
#                     $ g11_breakfast = 5

#                     $ g11_lunch = 5

#                     $ g11_dinner = 5
#                 else:
#                     if g11_attitude >= 250 and g11_attitude < 300:
#                         $ g11_breakfast = 6

#                         $ g11_lunch = 6

#                         $ g11_dinner = 6

#                         $ g11_night = 1
#                     else:
#                         if g11_attitude >= 300:
#                             $ g11_breakfast = 7

#                             $ g11_lunch = 7

#                             $ g11_dinner = 7

#                             $ g11_night = 2




# if g11_attitude > 10:
#     $ g11_eattimes = 2
# else:
#     if g11_attitude > 50:
#         $ g11_eattimes = 3
#     else:
#         if g11_attitude > 75:
#             $ g11_eattimes = 4
#         else:
#             if g11_attitude > 100:
#                 $ g11_eattimes = 5
#             else:
#                 if g11_attitude > 125:
#                     $ g11_eattimes = 6
#                 else:
#                     if g11_attitude > 150:
#                         $ g11_eattimes = 7
#                     else:
#                         if g11_attitude > 175:
#                             $ g11_eattimes = 8
#                         else:
#                             if g11_attitude > 200:
#                                 $ g11_eattimes = 9
#                             else:
#                                 if g11_attitude > 225:
#                                     $ g11_eattimes = 10
#                                 else:
#                                     if g11_attitude > 250:
#                                         $ g11_eattimes = 11
#                                     else:
#                                         if g11_attitude > 275:
#                                             $ g11_eattimes = 12
#                                         else:
#                                             if g11_attitude > 300:
#                                                 $ g11_eattimes = 13
#                                             else:
#                                                 if g11_attitude > 325:
#                                                     $ g11_eattimes = 14
#                                                 else:
#                                                     if g11_attitude > 350:
#                                                         $ g11_eattimes = 15

# if g11_fullness < 8000 and g11_fullness >= g11_fullmax*0.7:
#     $ g11_fullmax += 100
# else:
#     $ g11_fullmax += 20

# $ g11_fullness = 0
# $ g11_portion = 250 + g11_fullmax*0.1
# $ g11_break = 0
# $ g11_clothes = renpy.random.randint(1,3)
# $ g11_near = 0
# $ g11_afterclub = 0
# $ g11_drunk = 0





# $ client1_fullness = 0
# $ client2_fullness = 0
# $ client3_fullness = 0
# $ client4_fullness = 0
# $ g11_morning = 1
# $ g11_dressinge = 1
# $ g11_dressingm = 1
# $ g11_intim = 1
# $ g11_orgasm = 0

# $ g11_stage1 = 0
# $ g11_stage2 = 0
# $ g11_stage3 = 0
# $ g11_stage4 = 0
# $ g11_stage5 = 0
# $ g11_stage6 = 0
# $ g11_stage7 = 0

# $ g11_club = 0

# $ daystart = 1

# $ drunkmax = 800

# if g11_attitude < 50:
#     $ g11_sms = 0
# else:
#     if g11_attitude >= 50 and g11_attitude < 100:
#         $ g11_sms = 1
#     else:
#         if g11_attitude >= 100 and g11_attitude < 150:
#             $ g11_sms = 2
#         else:
#             if g11_attitude >= 150 and g11_attitude < 200:
#                 $ g11_sms = 3

# if cover > 0:
#     $ cover -= 1
# else:
#     $ cover = 0

# call g1girl
# call g2girl
# call g3girl
# call g4girl
# call g5girl
# call g6girl

# $ g4_breakfast = 0
# $ g4_lunch = 0
# $ g4_dinner = 0

# $ g5_breakfast = 0
# $ g5_lunch = 0
# $ g5_dinner = 0


# $ g6_breakfast = 0
# $ g6_lunch = 0
# $ g6_dinner = 0


# $ g7_breakfast = 0
# $ g7_lunch = 0
# $ g7_dinner = 0

# if g5_social2 == 3:
#     $ g5_social2 = 2
# else:
#     pass

# call g7girl
# call g8girl
# call g9girl
# call g10girl
# call g11girl
# call g12girl

return
