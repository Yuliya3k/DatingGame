label variables:
    # The script of the game goes in this file.

    # Declare characters used by this game. The color argument colorizes the
    # name of the character.

    define a = Character("Ann", colour="#c8ffc8")

    define b = Character("Aurora", colour="#000984")

    define c = Character("Alexa", colour="#000984")

    define p = Character("[name]")

    define g12 = Character("Margo", colour="#000984")

    define g1 = Character("Kira", colour="#000984")

    define g2 = Character("Kris", colour="#000984")

    define g3 = Character("Helga", colour="#000984")

    define g4 = Character("Marisa", colour="#000984")

    define g5 = Character("Misty", colour="#000984")

    define g6 = Character("Ha-yoon", colour="#000984")

    define g7 = Character("Kassidy", colour="#000984")

    define g8 = Character("Medina", colour="#000984")

    define g9 = Character("Vicky", colour="#000984")

    define g10 = Character("Margo", colour="#000984")

    define g11 = Character("Cassia", colour="#000984")

    define g12 = Character("Valerie", colour="#000984")

    define g13 = Character("Niobe", colour="#000984")

    define g14 = Character("Ava", colour="#000984")

    define f = Character("Emi", colour="#000984")

    define g = Character("Lucy", colour="#000984")

    define h = Character("Liz", colour="#000984")

    define i = Character("Emi", colour="#000984")

    define j = Character("Chloe", colour="#c8ffc8")

    define k = Character("Monica", colour="#c8ffc8")

    define Mika = Character("Mika", colour="#000984")

    define m = Character("Heather", colour="#000984")
    define n = Character("Jenny", colour="#000984")
    define o = Character("Liz", colour="#000984")

    define Nutritionist = Character("Nutritionist", colour="#000984")
    define Cassia = Character("Cassia", colour="#000984")
    define Mark = Character("Mark", colour="#000984")

    define Trainer = Character("Trainer", colour="#000984")

    define Scientist = Character("Scientist", colour="#000984")

    define sub = Character("Subscribers", colour="#000984")
    define Man = Character("A man", colour="#000984")

    define slowdissolve = Dissolve(.5)

    default player_stamina = 15

    default feed = 0

    default name = "player"

    default cafefirsttime = 1

    default g1_fullness = int(0)

    default g1_fullnessoz = int(g1_fullness*0.034)

    default g1_weight = 53

    default g1_weightlbs = int(g1_weight*2.2)

    default g1_fullmax = 800

    default g1_fullmaxoz = int(g1_fullmax*0.034)

    default g1_weightmax = 89
    default g2_weightmax = 85



    default g1_defaultweight = 53

    default g1_stamina = 15

    default g1_position = 1

    default g1_clothes = 1

    default g1_fullstage = 1

    default g1_weightstage = 1

    default g1_emotion = 1

    default g1_eatdecision = 0

    default weightgain = 0

    default g2_stamina = 15
    default g3_stamina = 15
    default chance = 0
    default g1_trainstamina = 3
    default g2_trainstamina = 3
    default g3_trainstamina = 3

    default g1_calories = 0

    default g1_attitude = 10

    default g1_maxattitude = 400

    default g1_confidence = 1

    default d_liquid = 0

    default g1_breakfast = 0

    default g1_lunch = 0

    default g1_dinner = 0


    default g11_fullness = 0

    default g1_intfullness = 0
    default g2_intfullness = 0
    default g3_intfullness = 0
    default g4_intfullness = 0
    default g5_intfullness = 0
    default g6_intfullness = 0
    default g7_intfullness = 0
    default g8_intfullness = 0
    default g9_intfullness = 0
    default g10_intfullness = 0
    default g11_intfullness = 0
    default g12_intfullness = 0
    default wg = 1

    default g11_intfullnesslbs = int(g11_intfullness*0.034)

    default g11_totalfullness = g11_fullness + g11_intfullness










    default mv = 0
    default cassiapose = 1


    default g2_fullness = 0

    default g2_fullnessoz = int(g2_fullness*0.034)
    default g11_fullnessoz = int(g11_fullness*0.034)



    default g2_weight = 52

    default g2_weightlbs = int(g2_weight*2.2)

    default g2_fullmax = 800

    default g2_fullmaxoz = int(g2_fullmax*0.034)



    default g2_defaultweight = 52



    default g2_calories = 0

    default g2_attitude = 10

    default g2_maxattitude = 400

    default g2_confidence = 1



    default g2_breakfast = 0

    default g2_lunch = 0

    default g2_dinner = 0

    default g2_eatdecision = 0

    default g2_position = 1
    default bg_position = 1
    default position = 1

    default g2_clothes = 1

    default g2_fullstage = 1

    default g2_weightstage = 1

    default g2_emotion = 1

    default g1_resistance = 100
    default g2_resistance = 100
    default g3_resistance = 100
    default g4_resistance = 100
    default g5_resistance = 100
    default g6_resistance = 100
    default g7_resistance = 100
    default g8_resistance = 100
    default g9_resistance = 100
    default g10_resistance = 100


    default g3_fullness = 0

    default g3_fullnessoz = int(g3_fullness*0.034)

    default g3_weight = 50

    default g3_weightlbs = int(g3_weight*2.2)

    default g3_fullmax = 800

    default g3_fullmaxoz = int(g3_fullmax*0.034)

    default g3_weightmax = 71

    default g3_defaultweight = 50



    default g3_calories = 0

    default g3_attitude = 10
    default g3_publicopinion = 0
    default g4_publicopinion = 0
    default g5_publicopinion = 0
    default g6_publicopinion = 0
    default g7_publicopinion = 0

    default g3_maxattitude = 400

    default g3_confidence = 1


    default g3_breakfast = 0

    default g3_lunch = 0

    default g3_dinner = 0

    default g3_eatdecision = 0

    default g3_position = 1

    default g3_clothes = 1

    default g3_fullstage = 1

    default g3_weightstage = 1

    default g3_emotion = 1

    default g3_drunk = 0

    default g3_alcattitude = 0

    default g1_gain = 0

    default g1_capacitygain = 0

    default g2_gain = 0

    default g2_capacitygain = 0

    default g3_gain = 0

    default g3_capacitygain = 0

    default g1_weight_plan = False
    default g1_capacity_plan = False
    default g2_weight_plan = False
    default g2_capacity_plan = False
    default g3_weight_plan = False
    default g3_capacity_plan = False


    default g4_fullness = 0
    default g4_attitude = 0
    default g5_attitude = 0
    default g6_attitude = 0
    default g7_attitude = 0
    default g8_attitude = 0
    default g9_attitude = 0

    default g4_fullnessoz = int(g4_fullness*0.034)

    default g4_weight = 53

    default g4_calories = 0
    default g5_calories = 0
    default g6_calories = 0
    default g7_calories = 0

    default g4_gain = 0

    default g4_weightlbs = int(g4_weight*2.2)

    default g4_fullmax = 800

    default g4_fullmaxoz = int(g4_fullmax*0.034)

    default g4_weightmax = 71

    default g4_defaultweight = 53

    default g4_stamina = 15

    default g4_position = 1

    default g4_clothes = 1

    default g4_fullstage = 1
    default g4_sfullstage = 1

    default g4_weightstage = 1
    default g4_sweightstage = 1

    default g4_emotion = 1

    default g4_eatdecision = 0

    default g4_firsttalk = 0

    default g4_capacitygain = 0
    default g4_beach = 1
    default g4_beachfirsttime = 0
    default g5_beach = 0
    default g5_beachfirsttime = 0
    default g4_swamp = 0

    default beach_girl = 4

    default g5_fullness = 0

    default g5_fullnessoz = int(g5_fullness*0.034)

    default g5_weight = 53

    default g5_weightlbs = int(g5_weight*2.2)

    default g5_fullmax = 800

    default g5_fullmaxoz = int(g5_fullmax*0.034)

    default g5_weightmax = 71

    default g5_defaultweight = 53

    default g5_stamina = 15

    default g5_position = 1

    default g5_clothes = 1

    default g5_fullstage = 1

    default g5_weightstage = 1

    default g5_emotion = 1

    default g5_eatdecision = 0

    default g5_firsttalk = 0


    default g6_fullness = 0

    default g6_fullnessoz = int(g6_fullness*0.034)

    default g6_weight = 53

    default g6_weightlbs = int(g6_weight*2.2)

    default g6_fullmax = 800

    default g6_fullmaxoz = int(g6_fullmax*0.034)

    default g6_weightmax = 71

    default g6_defaultweight = 53

    default g6_stamina = 15

    default g6_position = 1

    default g6_clothes = 1

    default g6_fullstage = 1

    default g6_weightstage = 1

    default g6_emotion = 1

    default g6_eatdecision = 0

    default g6_firsttalk = 0


    default g6s_fullness = 0
    default g6s_fullnessoz = int(g6s_fullness*0.034)
    default g6s_weight = 53
    default g6s_weightlbs = int(g6s_weight*2.2)
    default g6s_weightstage = 1
    default g6s_fullstage = 1
    default g6s_fullmax = 800
    default g6s_fullmaxoz = int(g6s_fullmax*0.034)
    default g6s_weightmax = 71
    default g6s_defaultweight = 53
    default g6s_musclestage = 1
    default g6s_training = 1
    default g6s_traincycle = 1
    default g6sbloat = 0

    default g7_fullness = 0

    default g7_fullnessoz = int(g7_fullness*0.034)

    default g7_weight = 53

    default g7_weightlbs = int(g7_weight*2.2)

    default g7_fullmax = 800

    default g7_fullmaxoz = int(g7_fullmax*0.034)

    default g7_weightmax = 71

    default g7_defaultweight = 53

    default g7_stamina = 15

    default g7_position = 1

    default g7_clothes = 1

    default g7_fullstage = 1

    default g7_weightstage = 1

    default g7_emotion = 1

    default g7_eatdecision = 0

    default g7_firsttalk = 0


    default g8_fullness = 0

    default g8_fullnessoz = int(g8_fullness*0.034)

    default g8_weight = 53

    default g8_weightlbs = int(g8_weight*2.2)

    default g8_fullmax = 800

    default g8_fullmaxoz = int(g8_fullmax*0.034)

    default g8_weightmax = 71

    default g8_defaultweight = 53

    default g8_stamina = 15

    default g8_position = 1

    default g8_clothes = 1

    default g8_fullstage = 1

    default g8_weightstage = 1

    default g8_emotion = 1

    default g8_eatdecision = 0

    default g8_firsttalk = 0

    default g8_musclepoints = 0

    default g8_fat = 0

    default g8_musclestage = 1

    default g8_fatgain = 0

    default g8_look = 1

    default g8_waterbelly = 0

    default g8_calories = 0

    default g8_gain = 0



    default g8_staminabonus = 0


    default g9_fullness = 0

    default g9_fullnessoz = int(g9_fullness*0.034)

    default g9_weight = 53

    default g9_weightlbs = int(g9_weight*2.2)

    default g9_fullmax = 800

    default g9_bellystage = 1

    default g9_fullmaxoz = int(g9_fullmax*0.034)

    default g9_weightmax = 71

    default g9_defaultweight = 53

    default g9_stamina = 15

    default g9_position = 1

    default g9_clothes = 1

    default g9_fullstage = 1

    default g9_weightstage = 1

    default g9_emotion = 1

    default g9_eatdecision = 0

    default g9_firsttalk = 0

    default g9_musclepoints = 0

    default g9_fat = 0

    default g9_musclestage = 1

    default g9_fatgain = 0

    default g9_look = 1

    default g9_waterbelly = 0

    default g9_calories = 0

    default g9_gain = 0


    default g9_staminabonus = 0

    default g9_firstfeeding = 1

    default g9_edgelook = 1


    default g10_fullness = 0

    default g10_fullnessoz = int(g10_fullness*0.034)

    default g10_weight = 53

    default g10_weightlbs = int(g10_weight*2.2)

    default g10_fullmax = 800

    default g10_bellystage = 1

    default g10_fullmaxoz = int(g10_fullmax*0.034)

    default g10_weightmax = 71

    default g10_defaultweight = 53

    default g10_stamina = 15

    default g10_position = 1

    default g10_clothes = 1

    default g10_fullstage = 1

    default g10_weightstage = 1

    default g10_emotion = 1

    default g10_eatdecision = 0

    default g10_firsttalk = 0

    default g10_musclepoints = 0

    default g10_fat = 0

    default g10_musclestage = 1

    default g10_fatgain = 0

    default g10_look = 1

    default g10_waterbelly = 0

    default g10_calories = 0

    default g10_gain = 0

    default g10_attitude = 0

    default g10_staminabonus = 0

    default g10_firstfeeding = 1

    default g10_firstmeet = 0

    default g10_firstdressing = 0

    default g10_edgelook = 1

    default g10_weightgain = 1


    default g11_weight = 53

    default g11_weightlbs = int(g11_weight*2.2)

    default g11_fullmax = 800

    default g11_intfullmax = 800

    default g11_intfullmaxlbs = int(g11_intfullmax*0.034)

    default g11_bellystage = 1

    default g11_fullmaxoz = int(g11_fullmax*0.034)

    default g11_weightmax = 71

    default g11_defaultweight = 53

    default g11_stamina = 15

    default g11_position = 1

    default g11_clothes = 1

    default g11_fullstage = 1

    default g11_weightstage = 1

    default g11_emotion = 1

    default g11_eatdecision = 0

    default g11_firsttalk = 0

    default g11_musclepoints = 0

    default g11_fat = 0

    default g11_musclestage = 1

    default g11_fatgain = 0

    default g11_look = 1

    default g11_waterbelly = 0

    default g11_calories = 0

    default g11_gain = 0

    default g11_attitude = 0

    default g11_staminabonus = 0

    default g11_firstfeeding = 1

    default g11_firstmeet = 0

    default g11_firstdressing = 0

    default g11_edgelook = 1

    default g11_weightgain = 1

    default g11_breakfast = 1

    default g11_lunch = 1

    default g11_dinner = 1

    default g11_night = 1

    default g11_home = 1

    default g11_totalfullmax = 8000

    default g11_clo = 1

    default g11_hair = 1

    default g11_morning = 1



    default g12_fullness = 0



    default g12_fullnessoz = int(g12_fullness*0.034)

    default g12_weight = 53

    default g12_weightlbs = int(g12_weight*2.2)

    default g12_fullmax = 800

    default g12_bellystage = 1

    default g12_fullmaxoz = int(g12_fullmax*0.034)

    default g12_weightmax = 71

    default g12_defaultweight = 53

    default g12_stamina = 15

    default g12_position = 1

    default g12_clothes = 1

    default g12_fullstage = 1

    default g12_weightstage = 1

    default g12_emotion = 1

    default g12_eatdecision = 0

    default g12_firsttalk = 0

    default g12_musclepoints = 0

    default g12_fat = 0

    default g12_musclestage = 1

    default g12_fatgain = 0

    default g12_look = 1

    default g12_waterbelly = 0

    default g12_calories = 0

    default g12_gain = 0

    default g12_attitude = 0

    default g12_staminabonus = 0

    default g12_firstfeeding = 1

    default g12_firstmeet = 0

    default g12_firstdressing = 0

    default g12_edgelook = 1

    default g12_weightgain = 1






    default g13_fullness = 0

    default g13_intfullness = 0

    default g13_fullnessoz = int(g13_fullness*0.034)

    default g13_weight = 53

    default g13_weightlbs = int(g13_weight*2.2)

    default g13_fullmax = 800

    default g13_bellystage = 1

    default g13_fullmaxoz = int(g13_fullmax*0.034)

    default g13_weightmax = 71

    default g13_defaultweight = 53

    default g13_stamina = 15

    default g13_position = 1

    default g13_clothes = 1

    default g13_fullstage = 1

    default g13_weightstage = 1

    default g13_emotion = 1

    default g13_eatdecision = 0

    default g13_firsttalk = 0

    default g13_musclepoints = 0

    default g13_fat = 0

    default g13_musclestage = 1

    default g13_fatgain = 0

    default g13_look = 1

    default g13_waterbelly = 0

    default g13_calories = 0

    default g13_gain = 0

    default g13_attitude = 0

    default g13_staminabonus = 0

    default g13_firstfeeding = 1

    default g13_firstmeet = 0

    default g13_firstdressing = 0

    default g13_edgelook = 1

    default g13_weightgain = 1



    default g14_fullness = 0

    default g14_intfullness = 0

    default g14_fullnessoz = int(g14_fullness*0.034)

    default g14_weight = 53

    default g14_weightlbs = int(g14_weight*2.2)

    default g14_fullmax = 800

    default g14_bellystage = 1

    default g14_fullmaxoz = int(g14_fullmax*0.034)

    default g14_weightmax = 71

    default g14_defaultweight = 53

    default g14_stamina = 15

    default g14_position = 1

    default g14_clothes = 1

    default g14_fullstage = 1

    default g14_weightstage = 1

    default g14_emotion = 1

    default g14_eatdecision = 0

    default g14_firsttalk = 0

    default g14_musclepoints = 0

    default g14_fat = 0

    default g14_musclestage = 1

    default g14_fatgain = 0

    default g14_look = 1

    default g14_waterbelly = 0

    default g14_calories = 0

    default g14_gain = 0

    default g14_attitude = 0

    default g14_staminabonus = 0

    default g14_firstfeeding = 1

    default g14_firstmeet = 0

    default g14_firstdressing = 0

    default g14_edgelook = 1

    default g14_weightgain = 1





    default storytell = 0

    default playerhome = 1

    default celltalk_g1 = 1

    default testfullness = 0

    default testcalories = 0

    default fired = 0

    default daycompliment = 1

    default payrent = 0

    default firstcall = 1

    default explode10 = 0

    default results = 0

    default welldone = 0

    default stretch8 = 0

    default stretch9 = 0

    default stretch10 = 0
    default stretch11 = 0
    default stretch12 = 0
    default stretch13 = 0
    default stretch14 = 0
    default stretch15 = 0
    default stretch16 = 0

    default stretch17 = 0
    default stretch18 = 0
    default stretch19 = 0
    default stretch20 = 0
    default stretch21 = 0

    default g11_stretch8 = 0
    default g11_stretch9 = 0
    default g11_stretch10 = 0
    default g11_stretch11 = 0
    default g11_stretch12 = 0
    default g11_stretch13 = 0
    default g11_stretch14 = 0
    default g11_stretch15 = 0
    default g11_stretch16 = 0
    default g11_stretch17 = 0
    default g11_stretch18 = 0
    default g11_stretch19 = 0
    default g11_stretch20 = 0
    default g11_stretch21 = 0

    default g1_stretch8 = 0
    default g1_stretch9 = 0
    default g1_stretch10 = 0
    default g1_stretch11 = 0
    default g1_stretch12 = 0
    default g1_stretch13 = 0
    default g1_stretch14 = 0
    default g1_stretch15 = 0
    default g1_stretch16 = 0
    default g1_stretch17 = 0
    default g1_stretch18 = 0
    default g1_stretch19 = 0
    default g1_stretch20 = 0
    default g1_stretch21 = 0

    default g2_stretch8 = 0
    default g2_stretch9 = 0
    default g2_stretch10 = 0
    default g2_stretch11 = 0
    default g2_stretch12 = 0
    default g2_stretch13 = 0
    default g2_stretch14 = 0
    default g2_stretch15 = 0
    default g2_stretch16 = 0
    default g2_stretch17 = 0
    default g2_stretch18 = 0
    default g2_stretch19 = 0
    default g2_stretch20 = 0
    default g2_stretch21 = 0

    default g8_stretch8 = 0
    default g8_stretch9 = 0
    default g8_stretch10 = 0
    default g8_stretch11 = 0
    default g8_stretch12 = 0
    default g8_stretch13 = 0
    default g8_stretch14 = 0
    default g8_stretch15 = 0
    default g8_stretch16 = 0
    default g8_stretch17 = 0
    default g8_stretch18 = 0
    default g8_stretch19 = 0
    default g8_stretch20 = 0
    default g8_stretch21 = 0

    default g5_stretch8 = 0
    default g5_stretch9 = 0
    default g5_stretch10 = 0
    default g5_stretch11 = 0
    default g5_stretch12 = 0
    default g5_stretch13 = 0
    default g5_stretch14 = 0
    default g5_stretch15 = 0
    default g5_stretch16 = 0
    default g5_stretch17 = 0
    default g5_stretch18 = 0
    default g5_stretch19 = 0
    default g5_stretch20 = 0
    default g5_stretch21 = 0


    default g1_near = 0
    default g2_near = 0
    default g3_near = 0
    default g4_near = 0
    default g5_near = 0
    default g6_near = 0
    default g7_near = 0
    default g8_near = 0
    default g9_near = 0
    default g10_near = 0
    default g11_near = 0
    default g12_near = 0
    default g13_near = 0
    default g14_near = 0


    default g7_state = 1


    default g11_maxfulltext = 0

    default g11_burp = 0

    default controldelivery = 0

    default controldelivered = 0

    default controlfood = 0

    default allclothes = 0

    default metric = 1

    default endgame = 0

    default goodwork = 0


    default playerroom = 0
    default g11_room = 0


    default daytime = 18

    default money = 1000

    default beercapacity = 1200

    default clubcounter = 6

    default firsttimeatwork = 1

    default firsttimeatworktoday = 0

    default weekdaynumber = 1

    default findcompany = 0

    default companycheckcount = 1

    default companycheck = 0

    default samples = 0

    default delivery = 0

    default delivered = 0

    default partner = 0

    default tasteresults = 0

    default outofbreath = 0

    default sportcalories = 0

    default water = 0

    default contracts = 0

    # default weekday = 'Mon'

    default girl = 1

    default food = "boiled_corn"

    default place = "map"

    default g1_girl = False

    default g2_girl = False

    default g3_girl = False

    default g1_cafe = False

    # default map = 0

    default g1_cafeappointment = False
    default g2_cafeappointment = False
    default g3_cafeappointment = False

    default g1_trainingappointment = False
    default g2_trainingappointment = False
    default g3_trainingappointment = False

    default g1_firstcall = 0
    default g2_firstcall = 0
    default g3_firstcall = 0

    default g1_gotopark = 0
    default gamestart = 1

    # g1_position hi 1 serious 2 happy 3 walking 4 belly close 5 home looking 6 tookphone1 7 tookphone2 8 park hi 9 park jog 10 park too much 11 park chugging 12 park bye 13
    # g1_clothes 1 dress 2 jeans
    # home work park ann home
    image bg = "/images/bgpos[position].png"
    image g1p = "/images/g1pos[position]weight[g1_weightstage] ([g1_fullstage]).png"
    image g2p = "/images/g2pos[position]weight[g2_weightstage] ([g2_fullstage]).png"
    image g3p = "/images/g3pos[position]weight[g3_weightstage] ([g3_fullstage]).png"
    image g4p = "/images/g4pos[position]weight[g4_weightstage] ([g4_fullstage]).png"
    image g4s = "/images/g4pos[position]weight[g4_sweightstage] ([g4_sfullstage]).png"
    image g5p = "/images/g5pos[position]weight[g5_weightstage] ([g5_fullstage]).png"
    image g6p = "/images/g6pos[position]weight[g6_weightstage] ([g6_fullstage]).png"
    image g6s = "/images/g6m[g6s_musclestage]weight[g6s_weightstage] ([g6s_fullstage]).png"
    image g7p = "/images/g7pos[position]state[g7_state]weight[g7_weightstage] ([g7_fullstage]).png"
    image g7s = "/images/g7pos[position]weight[g7_weightstage] ([g7_fullstage]).png"
    image g8p = "/images/g8pos[position]weight[g8_weightstage] ([g8_fullstage]).png"
    image g10p = "/images/g10pos[position]weight[g10_weightstage] ([g10_fullstage]).png"
    image g11p = "/images/g11pos[position]weight[g11_weightstage] ([g11_fullstage]).png"
    image g11f = "/images/g11pos[position] ([g11_fullstage]).png"
    image g11l = "/images/g11pos[position].png"
    image g11n = "/images/g11pos[position] ([cassiapos]).png"
    image g12p = "/images/g12pos[position]weight[g12_weightstage] ([g12_fullstage]).png"
    image g13p = "/images/g13pos[position]weight[g13_weightstage] ([g13_fullstage]).png"
    image g14p = "/images/g14pos[position]weight[g14_weightstage] ([g14_fullstage]).png"
    image mark = "/images/markpos[position].png"

    image banana = "/images/banana.png"
    image cassia = "/images/g11pos84 ([cassiapose]).png"

    image facility = "/images/facility.png"

    image chair = "/images/chairpos[position].png"
    image officeintro = "/images/office ([officeday]).png"
    image exp = "images/expose[expose] ([exstage]).png"

    image g1emo = "/images/g1pos[position]emo[g1_emo]weight[g1_weightstage] ([g1_fullstage]).png"
    image g2emo = "/images/g2pos[position]emo[g2_emo]weight[g2_weightstage] ([g2_fullstage]).png"
    image g3 = "/images/g3pos[g3_position]clo[g3_clothes]weight[g3_weightstage] ([g3_fullstage]).png"

    # image g5 = "/images/g5pos ([g5_position]).png"
    # image g6 = "/images/g6pos ([g6_position]).png"
    # image g7 = "/images/g7pos ([g7_position]).png"
    image g8 = "/images/g8look[g8_look]pos[g8_position]clo[g8_clothes]weight[g8_weightstage] ([g8_fullstage]).png"
    image g8back = "/images/g8look[g8_look]pos[g8_position].png"
    image g9 = "/images/g9pos[g9_position]clo[g9_clothes]belly[g9_bellystage] ([g9_fullstage]).png"
    image g10 = "/images/g10pos[g10_position]clo[g10_clothes]weight[g10_weightstage] ([g10_fullstage]).png"

    image g11 = "/images/g11pos[g11_position]weight[g11_weightstage] ([g11_fullstage]).png"
    image g11clo = "/images/g11pos[g11_position]clo[g11_clothes]weight[g11_weightstage] ([g11_fullstage]).png"
    image g11hair = "/images/g11hairpos[g11_position]weight[g11_weightstage] ([g11_fullstage]).png"

    image g12 = "/images/g12pos[g12_position]weight[g12_weightstage] ([g12_fullstage]).png"
    image g12emo = "/images/g12pos[g12_position]emo[g12_emo]weight[g12_weightstage] ([g12_fullstage]).png"

    image trainer = "/images/mark1.png"
    image nutritionist = "/images/cassia[cassiapose].png"

    image proto = "/images/proto1.png"
    image cover = "/images/cover[pcover]p[cposition].png"
    image marisao = "/images/marisao[marisapose].png"
    image kirao = "/images/Kirao[kirapose].png"
    default marisapose = 1
    default kirapose = 1

    image client1 = "/images/client1pos[client1pose]weight[client1_weightstage] ([client1_fullstage]).png"
    image client2 = "/images/client2pos[client2pose]weight[client2_weightstage] ([client2_fullstage]).png"
    image client3 = "/images/client3pos[client3pose]weight[client3_weightstage] ([client3_fullstage]).png"
    image client4 = "/images/client4pos[client4pose]weight[client4_weightstage] ([client4_fullstage]).png"
    # image bg = "/images/bg[bg_position][g10_position][g5_position]"
    image g1stats = "/images/g1statsweight[g1_weightstage] ([g1_fullstage]).png"
    image g2stats = "/images/g2statsweight[g2_weightstage] ([g2_fullstage]).png"
    image g3stats = "/images/g3statsweight[g3_weightstage] ([g3_fullstage]).png"
    image g4stats = "/images/g4statsweight[g4_weightstage] ([g4_fullstage]).png"
    image g5stats = "/images/g5statsweight[g5_weightstage] ([g5_fullstage]).png"
    image g6stats = "/images/g6statspos[g6_statspose]weight[g6_weightstage] ([g6_fullstage]).png"
    image g7stats = "/images/g7statsstate[g7_state]weight[g7_weightstage] ([g7_fullstage]).png"

    image g11stats = "/images/g11statsweight[g11_weightstage] ([g11_fullstage]).png"
    image runwaybg = "/images/runway[g10_position] ([g10_fullstage]).png"

    image rmbg = "/images/bgpos[g11_position].png"
    image sobg = "/images/bgpos ([g11_position]).png"
    image mvbg =  "/images/bgpos[position][girls] ([cassiapose]).png"
    image mvmbg = "/images/bgpos[position][girls].png"
    image mvebg = "/images/bgpos[position] ([cassiapose]).png"


    default girls = 61213
    image cafekrisbg = "/images/bg cafepos[g10_position]k[g4_position].png"
    default fullness = "[girl] + _fullness"
    default eatdecision = "girl + _eatdecision"


    image globe1 = "/images/globe1.png"
    image globe2 = "/images/globe2.png"
    image globe3 = "/images/globe3.png"
    image globe4 = "/images/globe4.png"
    image scientists1 = "/images/scientists1.png"

    default gamefirsttime = 1
    default g1_cafe_firsttime = 1
    default g2_cafe_firsttime = 1
    default g3_cafe_firsttime = 1
    default g3_noclubtoday = 0



    default g2_firstmeet = 0
    default g3_firstmeet = 0
    default g4_firstmeet = 0
    default g5_firstmeet = 0
    default g6_firstmeet = 0
    default g7_firstmeet = 0
    default g8_firstmeet = 0


    default g6_statspose = 1



    default g3_secretroom = 0
    default g3_secretroomopen = 0
    default g3_button_pop = 1
    default g3_roomfirsttime = 1
    default g2_plan = 0

    default g1_emo = 2
    default g2_emo = 2

    default officeday = 1
    default exstage = 1
    default expose = 1

    default g2_camehome = 0
    default g2_camehomefirst = 0

    default g2_incafe = 0

    default g1_gotospark = 0

    default client1_weightstage = 1
    default client1_fullstage = 1
    default client1_calories = 0
    default client1_fullness = 0
    default client1_fullmax = 8000
    default client1_attitude = 0
    default client1_defaultweight = 53
    default client2_weightstage = 1
    default client2_fullstage = 1
    default client2_calories = 0
    default client2_fullness = 0
    default client2_fullmax = 8000
    default client2_attitude = 0
    default client2_defaultweight = 53
    default client3_weightstage = 1
    default client3_fullstage = 1
    default client3_calories = 0
    default client3_fullness = 0
    default client3_fullmax = 8000
    default client3_attitude = 0
    default client3_defaultweight = 53
    default client4_weightstage = 1
    default client4_fullstage = 1
    default client4_calories = 0
    default client4_fullness = 0
    default client4_fullmax = 8000
    default client4_attitude = 0
    default client4_defaultweight = 53
    default client1pose = 1
    default client2pose = 1
    default client3pose = 1
    default client4pose = 1

    default invpos = 1

    image invitem = "/images/[itemname]"

    $ slotpose = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]
    default itemname = "onions.png"
    default minutes = 0
    default month = 0
    default calendar = Calendar(1, 7, 0, 1, 0, 0, ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    $ Inventory[0] = Items("apple", 1, 50, 50, 0, 0, "gui/buywater_idle.png")
    $ Inventory[1] = Items("egg", 1, 30, 30, 0, 1, "gui/buywater_hover.png")

    default slots = 42
    default invegg_volume = 1
    default egg_calories = 74
    default invegg_n = 0


    default invbutter_volume = 400
    default butter_calories = 2868
    default invbutter_n = 0

    default invsalmon_volume = 400
    default salmon_calories = 800
    default invsalmon_n = 0

    default invbasil_volume = 1
    default basil_calories = 1
    default invbasil_n = 0

    default invbroccoli_volume = 400
    default broccoli_calories = 120
    default invbroccoli_n = 0

    default invstarch_volume = 400
    default starch_calories = 1524
    default invstarch_n = 0

    default invcorn_volume = 1
    default corn_calories = 88
    default invcorn_n = 0

    default invavocado_volume = 400
    default avocado_calories = 640
    default invavocado_n = 0

    default invchickendrumsticks_volume = 400
    default chickendrumsticks_calories = 688
    default invchickendrumsticks_n = 0

    default invflour_volume = 400
    default flour_calories = 1456
    default invflour_n = 0

    default invkiwi_volume = 400
    default kiwi_calories = 224
    default invkiwi_n = 0

    default invsalad_volume = 400
    default salad_calories = 68
    default invsalad_n = 0

    default invbakingpowder_volume = 400
    default bakingpowder_calories = 212
    default invbakingpowder_n = 0

    default invribs_volume = 400
    default ribs_calories = 1404
    default invribs_n = 0

    default invblueberry_volume = 400
    default blueberry_calories = 228
    default invblueberry_n = 0

    default invbayleaf_volume = 1
    default bayleaf_calories = 1
    default invbayleaf_n = 0

    default invchicken_volume = 2000
    default chicken_calories = 4780
    default invchicken_n = 0

    default invmint_volume = 1
    default mint_calories = 1
    default invmint_n = 0

    default invlamb_volume = 400
    default lamb_calories = 1176
    default invlamb_n = 0

    default invtomato_volume = 400
    default tomato_calories = 72
    default invtomato_n = 0

    default invbulgarianpepper_volume = 400
    default bulgarianpepper_calories = 80
    default invbulgarianpepper_n = 0

    default invsugar_volume = 400
    default sugar_calories = 387
    default invsugar_n = 0

    default invraspberry_volume = 400
    default raspberry_calories = 212
    default invraspberry_n = 0

    default invsteak_volume = 400
    default steak_calories = 1084
    default invsteak_n = 0

    # default invbroccoli_volume = 30
    # default broccoli_calories = 30
    # default invbroccoli_n = 0

    default invpork_volume = 400
    default pork_calories = 968
    default invpork_n = 0

    default invonions_volume = 400
    default onions_calories = 160
    default invonions_n = 0

    default invshrimp_volume = 400
    default shrimp_calories = 396
    default invshrimp_n = 0

    default invsausages2_volume = 400
    default sausages2_calories = 1384
    default invsausages2_n = 0

    default invmushroom_volume = 400
    default mushroom_calories = 88
    default invmushroom_n = 0

    default invorange_volume = 400
    default orange_calories = 188
    default invorange_n = 0

    default invgarlic_volume = 1
    default garlic_calories = 1
    default invgarlic_n = 0

    default invchickenbreast_volume = 400
    default chickenbreast_calories = 660
    default invchickenbreast_n = 0

    default invrosemarin_volume = 1
    default rosemarin_calories = 1
    default invrosemarin_n = 0

    default invsalt_volume = 1600
    default salt_calories = 0
    default invsalt_n = 0

    default invbanana_volume = 400
    default banana_calories = 356
    default invbanana_n = 0

    default invchilipepper_volume = 1
    default chilipepper_calories = 1
    default invchilipepper_n = 0

    default invchickenthigh_volume = 400
    default chickenthigh_calories = 708
    default invchickenthigh_n = 0

    # default invchickenthigh_volume = 30
    # default chickenthigh_calories = 30
    # default invchickenthigh_n = 0

    default invpepper_volume = 1
    default pepper_calories = 1
    default invpepper_n = 0

    default invmilk_volume = 1000
    default milk_calories = 420
    default invmilk_n = 0

    default invwine_volume = 750
    default wine_calories = 647
    default invwine_n = 0

    default invsalami_volume = 400
    default salami_calories = 1344
    default invsalami_n = 0

    default invvanilla_volume = 1
    default vanilla_calories = 1
    default invvanilla_n = 0

    default invlime_volume = 400
    default lime_calories = 120
    default invlime_n = 0

    # default invflour_volume = 30
    # default flour_calories = 30
    # default invflour_n = 0

    default invwater_volume = 500
    default water_calories = 0
    default invwater_n = 0

    default invcream_volume = 1000
    default cream_calories = 1960
    default invcream_n = 0

    default invherbs_volume = 1
    default herbs_calories = 1
    default invherbs_n = 0

    default invmozzarella_volume = 400
    default mozzarella_calories = 1120
    default invmozzarella_n = 0

    default invoil_volume = 1000
    default oil_calories = 8840
    default invoil_n = 0


    default value_butter = 4
    default value_egg = 1.79
    default value_salmon = 10
    default value_basil = 1
    default value_broccoli = 4
    default value_starch = 0.05
    default value_corn = 10
    default value_avocado = 0.88
    default value_chickendrumsticks = 2.5
    default value_kiwi = 0.6
    default value_salad = 1.2
    default value_bakingpowder = 0.05
    default value_ribs = 3.5
    default value_blueberry = 4.6
    default value_bayleaf = 0.01
    default value_chicken = 8.4
    default value_mint = 1.2
    default value_lamb = 35
    default value_tomato = 0.29
    default value_bulgarianpepper = 0.1
    default value_sugar = 0.59
    default value_raspberry = 6.88
    default value_steak = 11.5
    default value_pork = 6
    default value_onions = 0.02
    default value_shrimp = 10
    default value_sausages2 = 4
    default value_mushroom = 4
    default value_orange = 0.35
    default value_garlic = 0.1
    default value_chickenbreast = 3.73
    default value_rosemarin = 0.05
    default value_salt = 1.4
    default value_banana = 0.4
    default value_chilipepper = 0.34
    default value_chickenthigh = 1.69
    default value_pepper = 0.01
    default value_milk = 3.1
    default value_wine = 15
    default value_salami = 8.4
    default value_vanilla = 1
    default value_flour = 0.39
    default value_cream = 1.5
    default value_herbs = 0.05
    default value_mozzarella = 6
    default value_water = 1.5
    default value_oil = 4
    default value_lime = 4.7

    default n_chicken = 0
    default n_chickensticks = 0
    default n_eggtoast = 0
    default n_bakedcorn = 0
    default n_mushroombreakfast = 0
    default n_mushroompizza = 0
    default n_pancakes = 0
    default n_salamipizza = 0
    default n_pannacotta = 0
    default n_guacamole = 0
    default n_caprese = 0

    default cal_chicken = 0
    default cal_chickensticks = 0
    default cal_eggtoast = 0
    default cal_bakedcorn = 0
    default cal_mushroombreakfast = 0
    default cal_mushroompizza = 0
    default cal_pancakes = 0
    default cal_salamipizza = 0
    default cal_pannacotta = 0
    default cal_guacamole = 0
    default cal_caprese = 0

    default vol_chicken = 0
    default vol_chickensticks = 0
    default vol_eggtoast = 0
    default vol_bakedcorn = 0
    default vol_mushroombreakfast = 0
    default vol_mushroompizza = 0
    default vol_pancakes = 0
    default vol_salamipizza = 0
    default vol_pannacotta = 0
    default vol_guacamole = 0
    default vol_caprese = 0

    default cookchicken = 0
    default cookchickenstick = 0
    default cookeggtoast = 0
    default cookbakedcorn = 0
    default cookmushroombreakfast = 0
    default cookmushroompizza = 0
    default cookpancakes = 0
    default cooksalamipizza = 0
    default cookpannacotta = 0
    default cookguacamole = 0
    default cookcaprese = 0


    default cookchickenresult = 0
    default cookchickenstickresult = 0
    default cookeggtoastresult = 0
    default cookbakedcornresult = 0
    default cookmushroombreakfastresult = 0
    default cookmushroompizzaresult = 0
    default cookpancakesresult = 0
    default cooksalamipizzaresult = 0
    default cookpannacottaresult = 0
    default cookguacamoleresult = 0
    default cookcapreseresult = 0

    default cookingskill = 1
    default maxcookingskill = 100



    default butter_cchicken = 0
    default butter_chicken = 20

    default salad_cchicken = 0
    default salad_chicken = 200

    default bayleaf_cchicken = 0
    default bayleaf_chicken = 1

    default chicken_cchicken = 0
    default chicken_chicken = 2000

    default tomato_cchicken = 0
    default tomato_chicken = 100

    default bulgarianpepper_cchicken = 0
    default bulgarianpepper_chicken = 100

    default garlic_cchicken = 0
    default garlic_chicken = 1

    default salt_cchicken = 0
    default salt_chicken = 1

    default pepper_cchicken = 0
    default pepper_chicken = 1

    default herbs_cchicken = 0
    default herbs_chicken = 1

    default oil_cchicken = 0
    default oil_chicken = 30

    default egg_cpancakes = 0
    default egg_pancakes = 3

    default flour_cpancakes = 0
    default flour_pancakes = 250

    default milk_cpancakes = 0
    default milk_pancakes = 500

    default oil_cpancakes = 0
    default oil_pancakes = 30

    default bakingpowder_cpancakes = 0
    default bakingpowder_pancakes = 10

    default sugar_cpancakes = 0
    default sugar_pancakes = 150

    default salt_cpancakes = 0
    default salt_pancakes = 1

    default flour_csalamipizza = 0
    default flour_salamipizza = 400

    default tomato_csalamipizza = 0
    default tomato_salamipizza = 100

    default water_csalamipizza = 0
    default water_salamipizza = 250

    default bulgarianpepper_csalamipizza = 0
    default bulgarianpepper_salamipizza = 50

    default salt_csalamipizza = 0
    default salt_salamipizza = 1

    default salami_csalamipizza = 0
    default salami_salamipizza = 100

    default herbs_csalamipizza = 0
    default herbs_salamipizza = 1

    default oil_csalamipizza = 0
    default oil_salamipizza = 10

    default flour_cmushroompizza = 0
    default flour_mushroompizza = 400

    default tomato_cmushroompizza = 0
    default tomato_mushroompizza = 100

    default bulgarianpepper_cmushroompizza = 0
    default bulgarianpepper_mushroompizza = 50

    default onions_cmushroompizza = 0
    default onions_mushroompizza = 50

    default mushroom_cmushroompizza = 0
    default mushroom_mushroompizza = 300

    default salt_cmushroompizza = 0
    default salt_mushroompizza = 1

    default herbs_cmushroompizza = 0
    default herbs_mushroompizza = 1

    default water_cmushroompizza = 0
    default water_mushroompizza = 250

    default oil_cmushroompizza = 0
    default oil_mushroompizza = 20

    default butter_ceggtoast = 0
    default butter_eggtoast = 10

    default egg_ceggtoast = 0
    default egg_eggtoast = 1


    default tomato_ceggtoast = 0
    default tomato_eggtoast = 50

    default bulgarianpepper_ceggtoast = 0
    default bulgarianpepper_eggtoast = 50

    default salt_ceggtoast = 0
    default salt_eggtoast = 1

    default pepper_ceggtoast = 0
    default pepper_eggtoast = 1

    default herbs_ceggtoast = 0
    default herbs_eggtoast = 1

    default oil_ceggtoast = 0
    default oil_eggtoast = 20

    default butter_cchickenstick = 0
    default butter_chickenstick = 10

    default chickendrumsticks_cchickenstick = 0
    default chickendrumsticks_chickenstick = 200

    default bayleaf_cchickenstick = 0
    default bayleaf_chickenstick = 1

    default bulgarianpepper_cchickenstick = 0
    default bulgarianpepper_chickenstick = 50

    default garlic_cchickenstick = 0
    default garlic_chickenstick = 1

    default salt_cchickenstick = 0
    default salt_chickenstick = 1

    default pepper_cchickenstick = 0
    default pepper_chickenstick = 1

    default wine_cchickenstick = 0
    default wine_chickenstick = 50

    default herbs_cchickenstick = 0
    default herbs_chickenstick = 1

    default oil_cchickenstick = 0
    default oil_chickenstick = 20

    default corn_cbakedcorn = 0
    default corn_bakedcorn = 1

    default butter_cbakedcorn = 0
    default butter_bakedcorn = 50

    default tomato_cbakedcorn = 0
    default tomato_bakedcorn = 50

    default bulgarianpepper_cbakedcorn = 0
    default bulgarianpepper_bakedcorn = 50

    default salt_cbakedcorn = 0
    default salt_bakedcorn = 1

    default chilipepper_cbakedcorn = 0
    default chilipepper_bakedcorn = 1

    default pepper_cbakedcorn = 0
    default pepper_bakedcorn = 1

    default butter_cmushroombreakfast = 0
    default butter_mushroombreakfast = 50

    default tomato_cmushroombreakfast = 0
    default tomato_mushroombreakfast = 50

    default bulgarianpepper_cmushroombreakfast = 0
    default bulgarianpepper_mushroombreakfast = 50

    default onions_cmushroombreakfast = 0
    default onions_mushroombreakfast = 50

    default mushroom_cmushroombreakfast = 0
    default mushroom_mushroombreakfast = 200

    default garlic_cmushroombreakfast = 0
    default garlic_mushroombreakfast = 1

    default salt_cmushroombreakfast = 0
    default salt_mushroombreakfast = 1

    default pepper_cmushroombreakfast = 0
    default pepper_mushroombreakfast = 1

    default salami_cmushroombreakfast = 0
    default salami_mushroombreakfast = 50

    default herbs_cmushroombreakfast = 0
    default herbs_mushroombreakfast = 1

    default oil_cmushroombreakfast = 0
    default oil_mushroombreakfast = 20

    default basil_ccaprese = 0
    default basil_caprese = 1

    default tomato_ccaprese = 0
    default tomato_caprese = 100

    default salt_ccaprese = 0
    default salt_caprese = 1

    default mozzarella_ccaprese = 0
    default mozzarella_caprese = 100

    default herbs_ccaprese = 0
    default herbs_caprese = 1

    default oil_ccaprese = 0
    default oil_caprese = 15

    default avocado_cguacamole = 0
    default avocado_guacamole = 200

    default tomato_cguacamole = 0
    default tomato_guacamole = 100

    default bulgarianpepper_cguacamole = 0
    default bulgarianpepper_guacamole = 100

    default onions_cguacamole = 0
    default onions_guacamole = 100

    default garlic_cguacamole = 0
    default garlic_guacamole = 1

    default salt_cguacamole = 0
    default salt_guacamole = 1

    default pepper_cguacamole = 0
    default pepper_guacamole = 1

    default herbs_cguacamole = 0
    default herbs_guacamole = 1

    default lime_cguacamole = 0
    default lime_guacamole = 1

    default blueberry_cpannacotta = 0
    default blueberry_pannacotta = 50

    default mint_cpannacotta = 0
    default mint_pannacotta = 1

    default raspberry_cpannacotta = 0
    default raspberry_pannacotta = 50

    default vanilla_cpannacotta = 0
    default vanilla_pannacotta = 1

    default cream_cpannacotta = 0
    default cream_pannacotta = 250

    default sugar_cpannacotta = 0
    default sugar_pannacotta = 100

    default girlattitude = "[girl]" + "_attitude"
    default cookdish = "cook" + "[dish]"

    default dish = "eggtoast"
    default ingredient = "egg"
    default miningforcook = "[ingredient]" + "_" + "[dish]"
    default cingredient = "[ingredient]" + "_" + "c" + "[dish]"

    default g2_toomuch = 0
    default g2_cookingcoming = 0

    default duration = 0

    default order = 0
    default cookingorder = 0

    default eat_pancakes = 1

    default g11_dressinge = 1
    default g11_dressingm = 1

    default myrandom = 1
    default g11_beach1 = 1
    default g11_beach2 = 1
    default g11_beach3 = 1
    default g11_intim = 1
    default g11_intimloop = 0
    default g11_orgasm = 0
    default g11_sms = 1


    default g11_stage1 = 0
    default g11_stage2 = 0
    default g11_stage3 = 0
    default g11_stage4 = 0
    default g11_stage5 = 0
    default g11_stage6 = 0
    default g11_stage7 = 0

    default g2_stage1 = 0
    default g2_stage2 = 0
    default g2_stage3 = 0
    default g2_stage4 = 0
    default g2_stage5 = 0
    default g2_stage6 = 0
    default g2_stage7 = 0


    default g1_stage1 = 0
    default g1_stage2 = 0
    default g1_stage3 = 0
    default g1_stage4 = 0
    default g1_stage5 = 0
    default g1_stage6 = 0
    default g1_stage7 = 0

    default g11_dieting = 0
    default g11_break = 0
    default g11_soffice = 0
    default g11_eattimes = 1
    default g11_portion = 250
    default daystart = 0
    default dream = 0
    default g11_firstclub = 0
    default g11_drunkmax = 800
    default g11_whiskey = 0
    default g11_beer = 0
    default g11_drunk = 0
    default g11_club = 0
    default g11_gainquestion = 0
    default g11_afterclub = 0

    default g3appear = renpy.random.randint(0,1)
    default g4appear = renpy.random.randint(0,1)

    default beachfirst = 1

    default g4_breakfast = 0
    default g5_breakfast = 0
    default g4_lunch = 0
    default g5_lunch = 0
    default g4_dinner = 0
    default g5_dinner = 0

    default g5_social = 0
    default g5_social2 = 0

    default daychange = 0

    default cover = 0
    default coverstage = 0
    default coverimpact = 0
    default socialimpact = 0
    default randompose = 0

    default globalresistance = 100
    default avrgopinion = 0
    default avrgattitude = 0

    default simulation = 0
    default simulationend1 = 0
    default simcounter = 0

    default spublicopinion = 0
    default fpublicopinion = 0
    default totalpublicopinion = spublicopinion + fpublicopinion

    default g3_sresistance = 100
    default g4_sresistance = 100
    default g5_sresistance = 100
    default g6_sresistance = 100
    default g7_sresistance = 100
    default g8_sresistance = 100

    default g3_fresistance = 100
    default g4_fresistance = 100
    default g5_fresistance = 100
    default g6_fresistance = 100
    default g7_fresistance = 100
    default g8_fresistance = 100

    default g4_swampfirst = 0
    default swampenumerator = 0
    default g6_sim = 0
    default loopcounter = 0
    default loop1 = 0
    default loop2 = 0
    default loop3 = 0
    default loop4 = 0
    default loop5 = 0
    default loop6 = 0
    default loop7 = 0
    default loop8 = 0
    default loop9 = 0
    default loop10 = 0
    default loop11 = 0
    default loop12 = 0
    default loop13 = 0
    default loop14 = 0
    default loop15 = 0
    default loop16 = 0

    default g5_weighttalk = 0

    default g4maxsimsize = 0

    default randomsaction = 0
    default streamaction = 0
    default publicapprove = 0
    default loopcount = 0
    default pcover = 1
    default cposition = 5
    default counter = 0
    default foodrandom = 0
    define fade = Fade(1, 0.0, 1)

    default g6_nolimits = 0
    default g12_nolimits = 0
    default g13_nolimits = 0
    default g14_nolimits = 0
    default mvfirstlunch = 0
    default mvfirstmorning = 0
    default g6_cravings = 0
    default g12_cravings = 0
    default g13_cravings = 0
    # default p_culinary_vlog = 0
    default g7_photography = 0
    default g7_beach = 0
    default g7_arthistory = 0
    default p_cooking = 0
    default p_video = 0
    default p_diving = 0
    default p_culinary_vlog = 0
    default pv = 0
    default pc = 0
    default pd = 0
    default bc = 0
    default bv = 0
    default ac = 0
    default av = 0

    default frequencypc = 50
    default intensitypc = 0.05
    default frequencyls = 50
    default intensityls = 0.05
    default topology = 0
    default stimulate = 0
    default widthpc = 20
    default widthls = 20
    default prefrontalresult = 0
    default limbicresult = 0
    default g14_ff = 0
    default g14_max = 0
    default fr1 = 0
    default fr2 = 0
    default fr3 = 0
    default fr4 = 0
    default option1 = 0
    default option2 = 0
    default option3 = 0
    default sequence = 1

    default g1_found = 0
    default g2_found = 0
    default g3_found = 0
    default g4_found = 0
    default g5_found = 0
    default g6_found = 0
    default g7_found = 0
    default g8_found = 0
    default g11_found = 0
    default g12_found = 0
    default g13_found = 0

    default g1_fed = 0
    default g2_fed = 0
    default g3_fed = 0
    default g4_fed = 0
    default g5_fed = 0
    default g6_fed = 0
    default g7_fed = 0
    default g8_fed = 0
    default g11_fed = 0
    default g12_fed = 0
    default g13_fed = 0

    default gameended = 0

    default recoveryspeed = 0
    default recovery = 0
    default first_hayoon = 0

    default send = 0

    default fway = 0


    default g7_firstdate = 0
    default ffrequency = 0.06

    return
    # The game starts here.
