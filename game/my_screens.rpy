label myscreens:

screen kitchenscale:
    image "gui/bgposkitchencooking.png"
    
    if scaleactive == 0:
        imagebutton:
            auto "gui/dg_kitchen_scale_%s.png" xpos 568 ypos 400 action [ Play("sound", "audio/click2.mp3"), Call("scale") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    if scaleactive == 1:
        image "rightpan" xpos 965 ypos 306
        image "leftpan" xpos 166 ypos 290
        imagebutton:
            auto "gui/dg_kitchen_scale_%s.png" xpos 568 ypos 400 action [ Play("sound", "audio/click2.mp3"), SetVariable("scaleactive", "0") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    if scaleactive == 0:
        image "gui/dg_kitchen_arrow_idle.png" xpos x ypos y
    if scaleactive == 1:
        image "gui/dg_kitchen_arrow_hover.png" xpos x ypos y
    text "[cookingstatus]" bold 1 xpos 790 ypos 413 color ("#1ca600ff") size 40
    image "gui/dg_scale_signbg.png" xpos 30 ypos 413
    text "PROreputaion [workreputation]" bold 1 xpos 30 ypos 413 color ("#1ca600ff") size 30

    image "gui/dg_scale_signbg.png" xpos 30 ypos 453
    text "Day earnings [daysalary:.2f]" bold 1 xpos 30 ypos 453 color ("#1ca600ff") size 30

    image "gui/dg_scale_signbg.png" xpos 30 ypos 493
    text "Month salary [monthsalary:.2f]" bold 1 xpos 30 ypos 493 color ("#1ca600ff") size 30


    image "gui/dg_scale_signbg.png" xpos 30 ypos 533
    text "Cooking skill [cookingskill:.1f]" bold 1 xpos 30 ypos 533 color ("#1ca600ff") size 30



screen callmap():
    
    imagebutton:
        auto "gui/dg_map_callmap_%s.png" xpos 1834 ypos 0 action [ Play("sound", "audio/click2.mp3"), ShowTransient("map") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    imagebutton:
        auto "gui/dg_home_%s.png" xpos 20 ypos 540 action [ Play("sound", "audio/click2.mp3"), Jump("culinarychoices") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    if mapishere == 0:
        imagebutton:
            auto "gui/dg_map_pointer_%s.png" xpos 1622 ypos 42 action [ Play("sound", "audio/click2.mp3"), Call("mapishere") ] hovered [ Play("sound", "audio/button hover4.mp3") ] 

screen map():
    
    image "gui/dg_map.png"
    imagebutton:
        auto "gui/dg_map_home_%s.png" xpos 863 ypos 102 action [ Play("sound", "audio/click2.mp3"), Jump("culinarychoices") ] hovered [ Play("sound", "audio/button hover4.mp3") ] 
    
    imagebutton:
        auto "gui/dg_map_bar_%s.png" xpos 1027 ypos 315 action [ Play("sound", "audio/click2.mp3"), Jump("bar") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    imagebutton:
        auto "gui/dg_map_burgers_%s.png" xpos 1034 ypos 160 action [ Play("sound", "audio/click2.mp3"), Jump("bcafe") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    if hayoonfirsttime > 0:
        imagebutton:
            auto "gui/dg_map_hospital_%s.png" xpos 818 ypos 511 action [ Play("sound", "audio/click2.mp3"), Call("g7stats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    
    if calendar.Hours < 23 and calendar.Hours > 5:
        imagebutton:
            auto "gui/dg_map_park_%s.png" xpos 81 ypos 654 action [ Play("sound", "audio/click2.mp3"), Jump("park") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    
    if (calendar.WeekDay == 'Mon' or calendar.WeekDay == 'Tue' or calendar.WeekDay == 'Wed' or calendar.WeekDay == 'Thu' or calendar.WeekDay == 'Fri') and calendar.Hours > 8 and calendar.Hours < 21:
        imagebutton:
            auto "gui/dg_map_work_%s.png" xpos 1089 ypos 395 action [ Play("sound", "audio/click2.mp3"), Jump("rm") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    if overallpeople > 0 and ((calendar.WeekDay == 'Mon' or calendar.WeekDay == 'Tue' or calendar.WeekDay == 'Wed' or calendar.WeekDay == 'Thu' or calendar.WeekDay == 'Fri') and calendar.Hours >= 7 and calendar.Hours <= 23):
        imagebutton:
            auto "gui/dg_map_fitness_%s.png" xpos 544 ypos 407 action [ Play("sound", "audio/click2.mp3"), Jump("fitness") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

screen day_icon():
    frame:
        xsize 160
        ysize 37
        xpos 0
        ypos 0
        background Solid("#999966ca")
        xpadding 10
        ypadding 10
        
    if calendar.TotalDays <= 9:
        text "Day [calendar.TotalDays]" bold 1 xpos 30 ypos 1 color ("#ffffffff") size 30
    if calendar.TotalDays >=10 and calendar.TotalDays <= 99:
        text "Day [calendar.TotalDays]" bold 1 xpos 25 ypos 1 color ("#ffffffff") size 30
    if calendar.TotalDays >=100 and calendar.TotalDays <= 999:
        text "Day [calendar.TotalDays]" bold 1 xpos 12 ypos 1 color ("#ffffffff") size 30
    if calendar.TotalDays >=1000 and calendar.TotalDays <= 9999:
        text "Day [calendar.TotalDays]" bold 1 xpos 1 ypos 1 color ("#ffffffff") size 29
    if calendar.TotalDays >=10000 and calendar.TotalDays <= 99999:
        text "Day [calendar.TotalDays]" bold 1 xpos 1 ypos 3 color ("#ffffffff") size 25

    if calendar.Days <= 9:
        frame:
            xsize 110
            ysize 37
            xpos 180
            ypos 0
            background Solid("#999966")
            xpadding 10
            ypadding 10
        text "[calendar.Days]" bold 1 xpos 185 ypos 1 color ("#ffffffff") size 30
        text "[calendar.Month]" bold 1 xpos 220 ypos 1 color ("#ffffffff") size 30
    if calendar.Days >= 10 and calendar.Days <= 99:
        frame:
            xsize 125
            ysize 37
            xpos 170
            ypos 0
            background Solid("#999966")
            xpadding 10
            ypadding 10
        text "[calendar.Days]" bold 1 xpos 175 ypos 1 color ("#ffffffff") size 30
        text "[calendar.Month]" bold 1 xpos 220 ypos 1 color ("#ffffffff") size 30

    frame:
        xsize 80
        ysize 37
        xpos 310
        ypos 0
        background Solid("#999966")
        xpadding 10
        ypadding 10
    text "[calendar.WeekDay]" bold 1 xpos 313 ypos 1 color ("#ffffffff") size 30
    frame:
        xsize 105
        ysize 37
        xpos 410
        ypos 0
        background Solid("#999966")
        xpadding 10
        ypadding 10
    text "[calendar.Time]" bold 1 xpos 413 ypos 1 color ("#ffffffff") size 30

    if money >= 10 and money <= 99:
        frame:
            xsize 80
            ysize 37
            xpos 530
            ypos 0
            background Solid("#999966")
            xpadding 10
            ypadding 10

        text "$ [money:.0f]" bold 1 xpos 533 ypos 1 color ("#ffffffff") size 30

    if money >= 100 and money <= 999:
        frame:
            xsize 105
            ysize 37
            xpos 530
            ypos 0
            background Solid("#999966")
            xpadding 10
            ypadding 10

        text "$ [money:.0f]" bold 1 xpos 533 ypos 1 color ("#ffffffff") size 30
    if money >= 1000 and money <= 9999:
        frame:
            xsize 125
            ysize 37
            xpos 530
            ypos 0
            background Solid("#999966")
            xpadding 10
            ypadding 10

        text "$ [money:.0f]" bold 1 xpos 533 ypos 1 color ("#ffffffff") size 30
    if money >= 10000 and money <= 99999:
        frame:
            xsize 145
            ysize 37
            xpos 530
            ypos 0
            background Solid("#999966")
            xpadding 10
            ypadding 10

        text "$ [money:.0f]" bold 1 xpos 533 ypos 1 color ("#ffffffff") size 30
    if money >= 100000 and money <= 999999:
        frame:
            xsize 165
            ysize 37
            xpos 530
            ypos 0
            background Solid("#999966")
            xpadding 10
            ypadding 10

        text "$ [money:.0f]" bold 1 xpos 533 ypos 1 color ("#ffffffff") size 30
    if money >= 1000000 and money <= 9999999:
        frame:
            xsize 185
            ysize 37
            xpos 530
            ypos 0
            background Solid("#2f0aff70")
            xpadding 10
            ypadding 10

        text "$ [money:.0f]" bold 1 xpos 533 ypos 1 color ("#ffffffff") size 30
    if money >= 10000000 and money <= 99999999:
        frame:
            xsize 205
            ysize 37
            xpos 530
            ypos 0
            background Solid("#2f0aff70")
            xpadding 10
            ypadding 10

        text "$ [money:.0f]" bold 1 xpos 533 ypos 1 color ("#ffffffff") size 30
    if money >= 100000000 and money <= 999999999:
        frame:
            xsize 225
            ysize 37
            xpos 530
            ypos 0
            background Solid("#2f0aff70")
            xpadding 10
            ypadding 10

        text "$ [money:.0f]" bold 1 xpos 533 ypos 1 color ("#ffffffff") size 30

    if money >= 1000000000 and money <= 9999999999:
        frame:
            xsize 245
            ysize 37
            xpos 530
            ypos 0
            background Solid("#2f0aff70")
            xpadding 10
            ypadding 10

        text "$ [money:.0f]" bold 1 xpos 533 ypos 1 color ("#ffffffff") size 30
    if money >= 10000000000 and money <= 99999999999:
        frame:
            xsize 265
            ysize 37
            xpos 530
            ypos 0
            background Solid("#2f0aff70")
            xpadding 10
            ypadding 10

        text "$ [money:.0f]" bold 1 xpos 533 ypos 1 color ("#ffffffff") size 30

    if money >= 100000000000 and money <= 999999999999:
        frame:
            xsize 290
            ysize 37
            xpos 530
            ypos 0
            background Solid("#2f0aff70")
            xpadding 10
            ypadding 10

        text "$ [money:.0f]" bold 1 xpos 533 ypos 1 color ("#ffffffff") size 30



screen marshmallow:
    imagebutton:
        auto "gui/dg_backyard_place_%s.png" xpos 998 ypos 465 action [ Play("sound", "audio/click2.mp3"), Call("marshmallowpos") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    if cooking == 0:
        imagebutton:
            auto "gui/dg_backyard_cook_%s.png" xpos 1001 ypos 837 action [ Play("sound", "audio/click2.mp3"), Jump("marshmallowcook") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    if cooking == 1:
        imagebutton:
            auto "gui/dg_backyard_stop_%s.png" xpos 1001 ypos 837 action [ Play("sound", "audio/click2.mp3"), Call("stop") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    image "marshmallow" xpos 965 ypos 527


    



    # image:
    #     # auto "gui/month_%s.png" xpos 305 ypos 8
    # text "[calendar.Month]" bold 1 xpos 320 ypos 15 color ("#ffffffff") size 30
    # if calendar.Days < 10:
    #     imagebutton:
    #         # auto "gui/monthday_%s.png" xpos 409 ypos 8
    #
    # else:
    #     imagebutton:
    #         # auto "gui/monthday_%s.png" xpos 409 ypos 8
    #     text "[calendar.Days]" bold 1 xpos 435 ypos 15 color ("#ffffffff") size 30
    #
    # image:
    #     # auto "gui/weekday_%s.png" xpos 513 ypos 8
    # text "[calendar.WeekDay]" bold 1 xpos 523 ypos 15 color ("#ffffffff") size 30
    #
    # image:
    #     # auto "gui/time_%s.png" xpos 619 ypos 8 action
    # text "[calendar.Time]" bold 1 xpos 633 ypos 15 color ("#ffffffff") size 30

screen stats():
    image "gui/statsbg.png"
    imagebutton:
        auto "gui/showstats_%s.png" xpos 829 ypos 76 action ToggleScreen("statsgirls")
    imagebutton:
        auto "gui/back_%s.png" xpos 6 ypos 625 action Jump("test")

screen statsgirls():
    image "gui/statsshowbg3.png"
    imagebutton:
        auto "gui/hidestats_%s.png" xpos 829 ypos 76 action Call("hidestats")

    vpgrid:
        xpos 1633
        ypos 167
        xsize 243
        ysize 735
        cols 1
        spacing 5
        mousewheel True

        frame:
            background Solid("#2f0aff70")
            xsize 160
            ysize 37
            textbutton "Kira" text_size 17 text_color ("#A3F170") action [ Play("sound", "audio/click2.mp3"), Call("g1stats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        frame:
            background Solid("#2f0aff70")
            xsize 160
            ysize 37
            textbutton "Kris" text_size 17 text_color ("#A3F170") action [ Play("sound", "audio/click2.mp3"), Call("g2stats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

        frame:
            background Solid("#2f0aff70")
            xsize 160
            ysize 37
            textbutton "Helga" text_size 17 text_color ("#A3F170") action [ Play("sound", "audio/click2.mp3"), Call("g3stats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

        frame:
            background Solid("#2f0aff70")
            xsize 160
            ysize 37
            textbutton "Marisa" text_size 17 text_color ("#A3F170") action [ Play("sound", "audio/click2.mp3"), Call("g4stats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        frame:
            background Solid("#2f0aff70")
            xsize 160
            ysize 37
            textbutton "Misty" text_size 17 text_color ("#A3F170") action [ Play("sound", "audio/click2.mp3"), Call("g5stats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        frame:
            background Solid("#2f0aff70")
            xsize 160
            ysize 37
            textbutton "Ha-yoon" text_size 17 text_color ("#A3F170") action [ Play("sound", "audio/click2.mp3"), Call("g6stats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        frame:
            background Solid("#2f0aff70")
            xsize 160
            ysize 37
            textbutton "Kassidy" text_size 17 text_color ("#A3F170") action [ Play("sound", "audio/click2.mp3"), Call("g7stats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

screen g1stats():
    image "g1stats"
    if g1_weightstage <= 4:
        if metric == 1:
            text "Weight [g1_weight]" xpos 610 ypos 277 color ("#A3F170")
        else:
            text "Weight [g1_weightlbs]" xpos 610 ypos 277 color ("#A3F170")
    if g1_weightstage > 4 and g1_weightstage <= 7:
        if metric == 1:
            text "Weight [g1_weight]" xpos 610 ypos 277 color ("#F4F400")
        else:
            text "Weight [g1_weightlbs]" xpos 610 ypos 277 color ("#F4F400")
    if g1_weightstage > 7 and g1_weightstage <= 10:
        if metric == 1:
            text "Weight [g1_weight]" xpos 610 ypos 277 color ("#E50000")
        else:
            text "Weight [g1_weightlbs]" xpos 610 ypos 277 color ("#E50000")
    if g1_fullstage <= 8:
        if metric == 1:
            text "Fullness [g1_fullness]/[g1_fullmax]" xpos 610 ypos 345 color ("#A3F170")
        else:
            text "Fullness [g1_fullnessoz]/[g1_fullmaxoz]" xpos 610 ypos 345 color ("#A3F170")
    if g1_fullstage > 8 and g1_fullstage <= 15:
        if metric == 1:
            text "Fullness [g1_fullness]/[g1_fullmax]" xpos 610 ypos 345 color ("#F4F400")
        else:
            text "Fullness [g1_fullnessoz]/[g1_fullmaxoz]" xpos 610 ypos 345 color ("#F4F400")
    if g1_fullstage > 15 and g1_fullstage <= 20:
        if metric == 1:
            text "Fullness [g1_fullness]/[g1_fullmax]" xpos 610 ypos 345 color ("#E50000")
        else:
            text "Fullness [g1_fullnessoz]/[g1_fullmaxoz]" xpos 610 ypos 345 color ("#E50000")
    text "Kira" xpos 737 ypos 168 color ("#A3F170")
    text "Attitude [g1_attitude]" xpos 610 ypos 413 color ("#A3F170")
    text "Resistance [g1_resistance]" xpos 610 ypos 481 color ("#A3F170")
    imagebutton:
        auto "gui/plus_%s.png" xpos 503 ypos 275 action Call("g1gain")
    imagebutton:
        auto "gui/minus_%s.png" xpos 558 ypos 275 action Call("g1loose")

    imagebutton:
        auto "gui/plus_%s.png" xpos 503 ypos 345 action Call("g1eat")
    imagebutton:
        auto "gui/minus_%s.png" xpos 558 ypos 345 action Call("g1purge")
    if metric == 1:
        imagebutton:
            auto "gui/imperial_%s.png" xpos 1513 ypos 168 action [ Play("sound", "audio/click2.mp3"), Call("imperial") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    else:
        imagebutton:
            auto "gui/metric_%s.png" xpos 1513 ypos 168 action [ Play("sound", "audio/click2.mp3"), Call("metric") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

screen back():
    imagebutton:
        auto "gui/back_%s.png" xpos 6 ypos 625 action [ Play("sound", "audio/click1.mp3"), Jump("test") ] hovered [ Play("sound", "audio/button hover2.mp3") ]
