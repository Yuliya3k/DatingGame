label myscreens:


# ************************************************





screen day_icon():



    frame:
        xsize 160
        ysize 37
        xpos 0
        ypos 0
        background Solid("#0000005F")
        xpadding 10
        ypadding 10
    if calendar.TotalDays <= 9:
        text "Day [calendar.TotalDays]" bold 1 xpos 30 ypos 1 color ("#999900") size 30
    if calendar.TotalDays >=10 and calendar.TotalDays <= 99:
        text "Day [calendar.TotalDays]" bold 1 xpos 25 ypos 1 color ("#999900") size 30
    if calendar.TotalDays >=100 and calendar.TotalDays <= 999:
        text "Day [calendar.TotalDays]" bold 1 xpos 12 ypos 1 color ("#999900") size 30
    if calendar.TotalDays >=1000 and calendar.TotalDays <= 9999:
        text "Day [calendar.TotalDays]" bold 1 xpos 1 ypos 1 color ("#999900") size 29
    if calendar.TotalDays >=10000 and calendar.TotalDays <= 99999:
        text "Day [calendar.TotalDays]" bold 1 xpos 1 ypos 3 color ("#999900") size 25

    if calendar.Days <= 9:
        frame:
            xsize 110
            ysize 37
            xpos 180
            ypos 0
            background Solid("#0000005F")
            xpadding 10
            ypadding 10
        text "[calendar.Days]" bold 1 xpos 185 ypos 1 color ("#999900") size 30
        text "[calendar.Month]" bold 1 xpos 220 ypos 1 color ("#999900") size 30
    if calendar.Days >= 10 and calendar.Days <= 99:
        frame:
            xsize 125
            ysize 37
            xpos 170
            ypos 0
            background Solid("#0000005F")
            xpadding 10
            ypadding 10
        text "[calendar.Days]" bold 1 xpos 175 ypos 1 color ("#999900") size 30
        text "[calendar.Month]" bold 1 xpos 220 ypos 1 color ("#999900") size 30

    frame:
        xsize 80
        ysize 37
        xpos 310
        ypos 0
        background Solid("#0000005F")
        xpadding 10
        ypadding 10
    text "[calendar.WeekDay]" bold 1 xpos 313 ypos 1 color ("#999900") size 30
    frame:
        xsize 105
        ysize 37
        xpos 410
        ypos 0
        background Solid("#0000005F")
        xpadding 10
        ypadding 10
    text "[calendar.Time]" bold 1 xpos 413 ypos 1 color ("#999900") size 30

    if money >= 10 and money <= 99:
        frame:
            xsize 80
            ysize 37
            xpos 530
            ypos 0
            background Solid("#0000005F")
            xpadding 10
            ypadding 10

        text "$ [money]" bold 1 xpos 533 ypos 1 color ("#999900") size 30

    if money >= 100 and money <= 999:
        frame:
            xsize 105
            ysize 37
            xpos 530
            ypos 0
            background Solid("#0000005F")
            xpadding 10
            ypadding 10

        text "$ [money]" bold 1 xpos 533 ypos 1 color ("#999900") size 30
    if money >= 1000 and money <= 9999:
        frame:
            xsize 125
            ysize 37
            xpos 530
            ypos 0
            background Solid("#0000005F")
            xpadding 10
            ypadding 10

        text "$ [money]" bold 1 xpos 533 ypos 1 color ("#999900") size 30
    if money >= 10000 and money <= 99999:
        frame:
            xsize 145
            ysize 37
            xpos 530
            ypos 0
            background Solid("#0000005F")
            xpadding 10
            ypadding 10

        text "$ [money]" bold 1 xpos 533 ypos 1 color ("#999900") size 30
    if money >= 100000 and money <= 999999:
        frame:
            xsize 165
            ysize 37
            xpos 530
            ypos 0
            background Solid("#0000005F")
            xpadding 10
            ypadding 10

        text "$ [money]" bold 1 xpos 533 ypos 1 color ("#999900") size 30
    if money >= 1000000 and money <= 9999999:
        frame:
            xsize 185
            ysize 37
            xpos 530
            ypos 0
            background Solid("#0000005F")
            xpadding 10
            ypadding 10

        text "$ [money]" bold 1 xpos 533 ypos 1 color ("#999900") size 30
    if money >= 10000000 and money <= 99999999:
        frame:
            xsize 205
            ysize 37
            xpos 530
            ypos 0
            background Solid("#0000005F")
            xpadding 10
            ypadding 10

        text "$ [money]" bold 1 xpos 533 ypos 1 color ("#999900") size 30
    if money >= 100000000 and money <= 999999999:
        frame:
            xsize 225
            ysize 37
            xpos 530
            ypos 0
            background Solid("#0000005F")
            xpadding 10
            ypadding 10

        text "$ [money]" bold 1 xpos 533 ypos 1 color ("#999900") size 30

    if money >= 1000000000 and money <= 9999999999:
        frame:
            xsize 245
            ysize 37
            xpos 530
            ypos 0
            background Solid("#0000005F")
            xpadding 10
            ypadding 10

        text "$ [money]" bold 1 xpos 533 ypos 1 color ("#999900") size 30
    if money >= 10000000000 and money <= 99999999999:
        frame:
            xsize 265
            ysize 37
            xpos 530
            ypos 0
            background Solid("#0000005F")
            xpadding 10
            ypadding 10

        text "$ [money]" bold 1 xpos 533 ypos 1 color ("#999900") size 30

    if money >= 100000000000 and money <= 999999999999:
        frame:
            xsize 290
            ysize 37
            xpos 530
            ypos 0
            background Solid("#0000005F")
            xpadding 10
            ypadding 10

        text "$ [money]" bold 1 xpos 533 ypos 1 color ("#999900") size 30


    # image:
    #     # auto "gui/month_%s.png" xpos 305 ypos 8
    # text "[calendar.Month]" bold 1 xpos 320 ypos 15 color ("#999900") size 30
    # if calendar.Days < 10:
    #     imagebutton:
    #         # auto "gui/monthday_%s.png" xpos 409 ypos 8
    #
    # else:
    #     imagebutton:
    #         # auto "gui/monthday_%s.png" xpos 409 ypos 8
    #     text "[calendar.Days]" bold 1 xpos 435 ypos 15 color ("#999900") size 30
    #
    # image:
    #     # auto "gui/weekday_%s.png" xpos 513 ypos 8
    # text "[calendar.WeekDay]" bold 1 xpos 523 ypos 15 color ("#999900") size 30
    #
    # image:
    #     # auto "gui/time_%s.png" xpos 619 ypos 8 action
    # text "[calendar.Time]" bold 1 xpos 633 ypos 15 color ("#999900") size 30


# *********************************************************************

screen comroom():
    image "bg"
    imagebutton:
        auto "gui/brain_%s.png" xpos 449 ypos 482 action Jump("brain")
    imagebutton:
        auto "gui/comp_%s.png" xpos 621 ypos 0 action Jump("mainmenu")
    image "chair"
    image "g1p"
    image "g2p"

screen comp():
    image "gui/menubg.png" xpos 97 ypos 59
    imagebutton:
        auto "gui/map_%s.png" xpos 324 ypos 270 action Jump("map")
    # imagebutton:
    #     auto "gui/talk_%s.png" xpos 1167 ypos 155 action Jump("talk")
    imagebutton:
        auto "gui/stats_%s.png" xpos 741  ypos 563 action Jump("stats")
    imagebutton:
        auto "gui/backhome_%s.png" xpos 135 ypos 580 action Jump("test")


screen brain():
    image "gui/brainclose.png" xpos 0 ypos 0
    imagebutton:
        auto "gui/skip_%s.png" xpos 99  ypos 53 action Call("skip")
    imagebutton:
        auto "gui/hybernate_%s.png" xpos 99  ypos 208 action Call("hybernate")
    if gameended == 1:
        imagebutton:
            auto "gui/resetgirls_%s.png" xpos 1313  ypos 672 action Call("resetgirls")
    if cover == 0:
        imagebutton:
            auto "gui/publishing_%s.png" xpos 1313  ypos 53 action Call("publishcover")
    else:
        pass
    imagebutton:
        auto "gui/bback_%s.png" xpos 99  ypos 826 action Jump("test")
    imagebutton:
        auto "gui/surveillance_%s.png" xpos 1313  ypos 208 action Jump("surveillance")
    imagebutton:
        auto "gui/simulation_%s.png" xpos 1313  ypos 362 action Jump("simulation")
    if wg == 1:
        imagebutton:
            auto "gui/wgon_%s.png" xpos 1313  ypos 826 action Call("wgoff")
    else:
        imagebutton:
            auto "gui/wgoff_%s.png" xpos 1313  ypos 826 action Jump("wgon")

screen cover():
    image "images/pubroom.png"
    image "cover" xpos 654  ypos 55 xzoom 0.8 yzoom 0.8
    imagebutton:
        auto "gui/pubroombutton_%s.png" xpos 1421  ypos 111 action Call("publishcover")
    if cover == 0:
        imagebutton:
            auto "gui/pubroompublish_%s.png" xpos 1421  ypos 191 action Call("cover1")
    else:
        pass
    # if cover == 0:
    #     imagebutton:
    #         auto "gui/cover1_%s.png" xpos 96  ypos 55 action Call("cover1")
    #     imagebutton:
    #         auto "gui/cover2_%s.png" xpos 1195  ypos 55 action Call("cover2")


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
            background Solid("#0000005F")
            xsize 160
            ysize 37
            textbutton "Kira" text_size 17 text_color ("#A3F170") action [ Play("sound", "audio/click2.mp3"), Call("g1stats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        frame:
            background Solid("#0000005F")
            xsize 160
            ysize 37
            textbutton "Kris" text_size 17 text_color ("#A3F170") action [ Play("sound", "audio/click2.mp3"), Call("g2stats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

        frame:
            background Solid("#0000005F")
            xsize 160
            ysize 37
            textbutton "Helga" text_size 17 text_color ("#A3F170") action [ Play("sound", "audio/click2.mp3"), Call("g3stats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

        frame:
            background Solid("#0000005F")
            xsize 160
            ysize 37
            textbutton "Marisa" text_size 17 text_color ("#A3F170") action [ Play("sound", "audio/click2.mp3"), Call("g4stats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        frame:
            background Solid("#0000005F")
            xsize 160
            ysize 37
            textbutton "Misty" text_size 17 text_color ("#A3F170") action [ Play("sound", "audio/click2.mp3"), Call("g5stats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        frame:
            background Solid("#0000005F")
            xsize 160
            ysize 37
            textbutton "Ha-yoon" text_size 17 text_color ("#A3F170") action [ Play("sound", "audio/click2.mp3"), Call("g6stats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        frame:
            background Solid("#0000005F")
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



screen g2stats():
    image "g2stats"
    if g2_weightstage <= 4:
        if metric == 1:
            text "Weight [g2_weight]" xpos 610 ypos 277 color ("#A3F170")
        else:
            text "Weight [g2_weightlbs]" xpos 610 ypos 277 color ("#A3F170")
    if g2_weightstage > 4 and g2_weightstage <= 7:
        if metric == 1:
            text "Weight [g2_weight]" xpos 610 ypos 277 color ("#F4F400")
        else:
            text "Weight [g2_weightlbs]" xpos 610 ypos 277 color ("#F4F400")
    if g2_weightstage > 7 and g2_weightstage <= 10:
        if metric == 1:
            text "Weight [g2_weight]" xpos 610 ypos 277 color ("#E50000")
        else:
            text "Weight [g2_weightlbs]" xpos 610 ypos 277 color ("#E50000")
    if g2_fullstage <= 8:
        if metric == 1:
            text "Fullness [g2_fullness]/[g2_fullmax]" xpos 610 ypos 345 color ("#A3F170")
        else:
            text "Fullness [g2_fullnessoz]/[g2_fullmaxoz]" xpos 610 ypos 345 color ("#A3F170")
    if g2_fullstage > 8 and g2_fullstage <= 15:
        if metric == 1:
            text "Fullness [g2_fullness]/[g2_fullmax]" xpos 610 ypos 345 color ("#F4F400")
        else:
            text "Fullness [g2_fullnessoz]/[g2_fullmaxoz]" xpos 610 ypos 345 color ("#F4F400")
    if g2_fullstage > 15 and g2_fullstage <= 20:
        if metric == 1:
            text "Fullness [g2_fullness]/[g2_fullmax]" xpos 610 ypos 345 color ("#E50000")
        else:
            text "Fullness [g2_fullnessoz]/[g2_fullmaxoz]" xpos 610 ypos 345 color ("#E50000")
    text "Kris" xpos 737 ypos 168 color ("#A3F170")
    text "Attitude [g2_attitude]" xpos 610 ypos 413 color ("#A3F170")
    text "Resistance [g2_resistance]" xpos 610 ypos 481 color ("#A3F170")
    imagebutton:
        auto "gui/plus_%s.png" xpos 503 ypos 275 action Call("g2gain")
    imagebutton:
        auto "gui/minus_%s.png" xpos 558 ypos 275 action Call("g2loose")

    imagebutton:
        auto "gui/plus_%s.png" xpos 503 ypos 345 action Call("g2eat")
    imagebutton:
        auto "gui/minus_%s.png" xpos 558 ypos 345 action Call("g2purge")

    if metric == 1:
        imagebutton:
            auto "gui/imperial_%s.png" xpos 1513 ypos 168 action [ Play("sound", "audio/click2.mp3"), Call("imperial") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    else:
        imagebutton:
            auto "gui/metric_%s.png" xpos 1513 ypos 168 action [ Play("sound", "audio/click2.mp3"), Call("metric") ] hovered [ Play("sound", "audio/button hover4.mp3") ]



screen g3stats():
    image "g3stats" xzoom 0.75 yzoom 0.75 xpos 50 ypos 150
    if g3_weightstage <= 4:
        if metric == 1:
            text "Weight [g3_weight]" xpos 610 ypos 277 color ("#A3F170")
        else:
            text "Weight [g3_weightlbs]" xpos 610 ypos 277 color ("#A3F170")
    if g3_weightstage > 4 and g3_weightstage <= 7:
        if metric == 1:
            text "Weight [g3_weight]" xpos 610 ypos 277 color ("#F4F400")
        else:
            text "Weight [g3_weightlbs]" xpos 610 ypos 277 color ("#F4F400")
    if g3_weightstage > 7 and g3_weightstage <= 10:
        if metric == 1:
            text "Weight [g3_weight]" xpos 610 ypos 277 color ("#E50000")
        else:
            text "Weight [g3_weightlbs]" xpos 610 ypos 277 color ("#E50000")
    if g3_fullstage <= 8:
        if metric == 1:
            text "Fullness [g3_fullness]/[g3_fullmax]" xpos 610 ypos 345 color ("#A3F170")
        else:
            text "Fullness [g3_fullnessoz]/[g3_fullmaxoz]" xpos 610 ypos 345 color ("#A3F170")
    if g3_fullstage > 8 and g3_fullstage <= 15:
        if metric == 1:
            text "Fullness [g3_fullness]/[g3_fullmax]" xpos 610 ypos 345 color ("#F4F400")
        else:
            text "Fullness [g3_fullnessoz]/[g3_fullmaxoz]" xpos 610 ypos 345 color ("#F4F400")
    if g3_fullstage > 15 and g3_fullstage <= 20:
        if metric == 1:
            text "Fullness [g3_fullness]/[g3_fullmax]" xpos 610 ypos 345 color ("#E50000")
        else:
            text "Fullness [g3_fullnessoz]/[g3_fullmaxoz]" xpos 610 ypos 345 color ("#E50000")
    text "Helga" xpos 737 ypos 168 color ("#A3F170")
    text "Attitude [g3_attitude]" xpos 610 ypos 413 color ("#A3F170")
    text "Resistance [g3_resistance]" xpos 610 ypos 481 color ("#A3F170")
    text "Stuffing resistance [g3_sresistance]" xpos 610 ypos 550 color ("#A3F170")
    text "Weight gain resistance [g3_fresistance]" xpos 610 ypos 620 color ("#A3F170")
    if metric == 1:
        imagebutton:
            auto "gui/imperial_%s.png" xpos 1513 ypos 168 action [ Play("sound", "audio/click2.mp3"), Call("imperial") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    else:
        imagebutton:
            auto "gui/metric_%s.png" xpos 1513 ypos 168 action [ Play("sound", "audio/click2.mp3"), Call("metric") ] hovered [ Play("sound", "audio/button hover4.mp3") ]


screen g4stats():
    image "g4stats"  xpos 0 ypos 0 #xzoom 0.75 yzoom 0.75
    if g4_weightstage <= 4:
        if metric == 1:
            text "Weight [g4_weight]" xpos 610 ypos 277 color ("#A3F170")
        else:
            text "Weight [g4_weightlbs]" xpos 610 ypos 277 color ("#A3F170")
    if g4_weightstage > 4 and g4_weightstage <= 7:
        if metric == 1:
            text "Weight [g4_weight]" xpos 610 ypos 277 color ("#F4F400")
        else:
            text "Weight [g4_weightlbs]" xpos 610 ypos 277 color ("#F4F400")
    if g4_weightstage > 7 and g4_weightstage <= 10:
        if metric == 1:
            text "Weight [g4_weight]" xpos 610 ypos 277 color ("#E50000")
        else:
            text "Weight [g4_weightlbs]" xpos 610 ypos 277 color ("#E50000")
    if g4_fullstage <= 8:
        if metric == 1:
            text "Fullness [g4_fullness]/[g4_fullmax]" xpos 610 ypos 345 color ("#A3F170")
        else:
            text "Fullness [g4_fullnessoz]/[g4_fullmaxoz]" xpos 610 ypos 345 color ("#A3F170")
    if g4_fullstage > 8 and g4_fullstage <= 15:
        if metric == 1:
            text "Fullness [g4_fullness]/[g4_fullmax]" xpos 610 ypos 345 color ("#F4F400")
        else:
            text "Fullness [g4_fullnessoz]/[g4_fullmaxoz]" xpos 610 ypos 345 color ("#F4F400")
    if g4_fullstage > 15 and g4_fullstage <= 20:
        if metric == 1:
            text "Fullness [g4_fullness]/[g4_fullmax]" xpos 610 ypos 345 color ("#E50000")
        else:
            text "Fullness [g4_fullnessoz]/[g4_fullmaxoz]" xpos 610 ypos 345 color ("#E50000")
    text "Marisa" xpos 737 ypos 168 color ("#A3F170")
    text "Attitude [g4_attitude]" xpos 610 ypos 413 color ("#A3F170")
    text "Resistance [g4_resistance]" xpos 610 ypos 481 color ("#A3F170")
    text "Stuffing resistance [g4_sresistance]" xpos 610 ypos 550 color ("#A3F170")
    text "Weight gain resistance [g4_fresistance]" xpos 610 ypos 620 color ("#A3F170")
    if metric == 1:
        imagebutton:
            auto "gui/imperial_%s.png" xpos 1513 ypos 168 action [ Play("sound", "audio/click2.mp3"), Call("imperial") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    else:
        imagebutton:
            auto "gui/metric_%s.png" xpos 1513 ypos 168 action [ Play("sound", "audio/click2.mp3"), Call("metric") ] hovered [ Play("sound", "audio/button hover4.mp3") ]


screen g5stats():
    image "g5stats"  xpos 0 ypos 0 #xzoom 0.75 yzoom 0.75
    if g5_weightstage <= 4:
        if metric == 1:
            text "Weight [g5_weight]" xpos 610 ypos 277 color ("#A3F170")
        else:
            text "Weight [g5_weightlbs]" xpos 610 ypos 277 color ("#A3F170")
    if g5_weightstage > 4 and g5_weightstage <= 7:
        if metric == 1:
            text "Weight [g5_weight]" xpos 610 ypos 277 color ("#F4F400")
        else:
            text "Weight [g5_weightlbs]" xpos 610 ypos 277 color ("#F4F400")
    if g5_weightstage > 7 and g5_weightstage <= 10:
        if metric == 1:
            text "Weight [g5_weight]" xpos 610 ypos 277 color ("#E50000")
        else:
            text "Weight [g5_weightlbs]" xpos 610 ypos 277 color ("#E50000")
    if g5_fullstage <= 8:
        if metric == 1:
            text "Fullness [g5_fullness]/[g5_fullmax]" xpos 610 ypos 345 color ("#A3F170")
        else:
            text "Fullness [g5_fullnessoz]/[g5_fullmaxoz]" xpos 610 ypos 345 color ("#A3F170")
    if g5_fullstage > 8 and g5_fullstage <= 15:
        if metric == 1:
            text "Fullness [g5_fullness]/[g5_fullmax]" xpos 610 ypos 345 color ("#F4F400")
        else:
            text "Fullness [g5_fullnessoz]/[g5_fullmaxoz]" xpos 610 ypos 345 color ("#F4F400")
    if g5_fullstage > 15 and g5_fullstage <= 20:
        if metric == 1:
            text "Fullness [g5_fullness]/[g5_fullmax]" xpos 610 ypos 345 color ("#E50000")
        else:
            text "Fullness [g5_fullnessoz]/[g5_fullmaxoz]" xpos 610 ypos 345 color ("#E50000")
    text "Misty" xpos 737 ypos 168 color ("#A3F170")
    text "Attitude [g5_attitude]" xpos 610 ypos 413 color ("#A3F170")
    text "Resistance [g5_resistance]" xpos 610 ypos 481 color ("#A3F170")
    text "Stuffing resistance [g5_sresistance]" xpos 610 ypos 550 color ("#A3F170")
    text "Weight gain resistance [g5_fresistance]" xpos 610 ypos 620 color ("#A3F170")
    if metric == 1:
        imagebutton:
            auto "gui/imperial_%s.png" xpos 1513 ypos 168 action [ Play("sound", "audio/click2.mp3"), Call("imperial") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    else:
        imagebutton:
            auto "gui/metric_%s.png" xpos 1513 ypos 168 action [ Play("sound", "audio/click2.mp3"), Call("metric") ] hovered [ Play("sound", "audio/button hover4.mp3") ]



screen g6stats():
    image "g6stats"  xpos 0 ypos 0 #xzoom 0.75 yzoom 0.75
    if g6_weightstage <= 4:
        if metric == 1:
            text "Weight [g6_weight]" xpos 610 ypos 277 color ("#A3F170")
        else:
            text "Weight [g6_weightlbs]" xpos 610 ypos 277 color ("#A3F170")
    if g6_weightstage > 4 and g6_weightstage <= 7:
        if metric == 1:
            text "Weight [g6_weight]" xpos 610 ypos 277 color ("#F4F400")
        else:
            text "Weight [g6_weightlbs]" xpos 610 ypos 277 color ("#F4F400")
    if g6_weightstage > 7 and g6_weightstage <= 10:
        if metric == 1:
            text "Weight [g6_weight]" xpos 610 ypos 277 color ("#E50000")
        else:
            text "Weight [g6_weightlbs]" xpos 610 ypos 277 color ("#E50000")
    if g6_fullstage <= 8:
        if metric == 1:
            text "Fullness [g6_fullness]/[g6_fullmax]" xpos 610 ypos 345 color ("#A3F170")
        else:
            text "Fullness [g6_fullnessoz]/[g6_fullmaxoz]" xpos 610 ypos 345 color ("#A3F170")
    if g6_fullstage > 8 and g6_fullstage <= 15:
        if metric == 1:
            text "Fullness [g6_fullness]/[g6_fullmax]" xpos 610 ypos 345 color ("#F4F400")
        else:
            text "Fullness [g6_fullnessoz]/[g6_fullmaxoz]" xpos 610 ypos 345 color ("#F4F400")
    if g6_fullstage > 15 and g6_fullstage <= 20:
        if metric == 1:
            text "Fullness [g6_fullness]/[g6_fullmax]" xpos 610 ypos 345 color ("#E50000")
        else:
            text "Fullness [g6_fullnessoz]/[g6_fullmaxoz]" xpos 610 ypos 345 color ("#E50000")
    text "Ha-yoon" xpos 737 ypos 168 color ("#A3F170")
    text "Attitude [g6_attitude]" xpos 610 ypos 413 color ("#A3F170")
    text "Resistance [g6_resistance]" xpos 610 ypos 481 color ("#A3F170")
    text "Stuffing resistance [g6_sresistance]" xpos 610 ypos 550 color ("#A3F170")
    text "Weight gain resistance [g6_fresistance]" xpos 610 ypos 620 color ("#A3F170")
    if metric == 1:
        imagebutton:
            auto "gui/imperial_%s.png" xpos 1513 ypos 168 action [ Play("sound", "audio/click2.mp3"), Call("imperial") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    else:
        imagebutton:
            auto "gui/metric_%s.png" xpos 1513 ypos 168 action [ Play("sound", "audio/click2.mp3"), Call("metric") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

    imagebutton:
        auto "gui/left_%s.png" xpos 6 ypos 462 action [ Play("sound", "audio/click2.mp3"), Call("g6statspose1") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    imagebutton:
        auto "gui/right_%s.png" xpos 1871 ypos 462 action [ Play("sound", "audio/click2.mp3"), Call("g6statspose2") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

screen g7stats():
    image "g7stats"  xpos 0 ypos 0 #xzoom 0.75 yzoom 0.75
    if g7_weightstage <= 4:
        if metric == 1:
            text "Weight [g7_weight]" xpos 610 ypos 277 color ("#A3F170")
        else:
            text "Weight [g7_weightlbs]" xpos 610 ypos 277 color ("#A3F170")
    if g7_weightstage > 4 and g7_weightstage <= 7:
        if metric == 1:
            text "Weight [g7_weight]" xpos 610 ypos 277 color ("#F4F400")
        else:
            text "Weight [g7_weightlbs]" xpos 610 ypos 277 color ("#F4F400")
    if g7_weightstage > 7 and g7_weightstage <= 10:
        if metric == 1:
            text "Weight [g7_weight]" xpos 610 ypos 277 color ("#E50000")
        else:
            text "Weight [g7_weightlbs]" xpos 610 ypos 277 color ("#E50000")
    if g7_fullstage <= 8:
        if metric == 1:
            text "Fullness [g7_fullness]/[g7_fullmax]" xpos 610 ypos 345 color ("#A3F170")
        else:
            text "Fullness [g7_fullnessoz]/[g7_fullmaxoz]" xpos 610 ypos 345 color ("#A3F170")
    if g7_fullstage > 8 and g7_fullstage <= 15:
        if metric == 1:
            text "Fullness [g7_fullness]/[g7_fullmax]" xpos 610 ypos 345 color ("#F4F400")
        else:
            text "Fullness [g7_fullnessoz]/[g7_fullmaxoz]" xpos 610 ypos 345 color ("#F4F400")
    if g7_fullstage > 15 and g7_fullstage <= 20:
        if metric == 1:
            text "Fullness [g7_fullness]/[g7_fullmax]" xpos 610 ypos 345 color ("#E50000")
        else:
            text "Fullness [g7_fullnessoz]/[g7_fullmaxoz]" xpos 610 ypos 345 color ("#E50000")
    text "Kassidy" xpos 737 ypos 168 color ("#A3F170")
    text "Attitude [g7_attitude]" xpos 610 ypos 413 color ("#A3F170")
    text "Resistance [g7_resistance]" xpos 610 ypos 481 color ("#A3F170")
    text "Stuffing resistance [g7_sresistance]" xpos 610 ypos 550 color ("#A3F170")
    text "Weight gain resistance [g7_fresistance]" xpos 610 ypos 620 color ("#A3F170")
    if metric == 1:
        imagebutton:
            auto "gui/imperial_%s.png" xpos 1513 ypos 168 action [ Play("sound", "audio/click2.mp3"), Call("imperial") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    else:
        imagebutton:
            auto "gui/metric_%s.png" xpos 1513 ypos 168 action [ Play("sound", "audio/click2.mp3"), Call("metric") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    # imagebutton:
    #     auto "gui/left_%s.png" xpos 6 ypos 462 action Call("g7statspose1")
    # imagebutton:
    #     auto "gui/right_%s.png" xpos 1871 ypos 462 action Call("g7statspose2")

screen map():
    image "gui/mapbg.png"
    imagebutton:
        auto "gui/mapglobe_%s.png" xpos 656 ypos 442 action Call("map1")
    imagebutton:
        auto "gui/back_%s.png" xpos 6 ypos 625 action Jump("test")



screen map1():
    image "gui/globe1.png"
    imagebutton:
        auto "gui/left_%s.png" xpos 6 ypos 462 action Call("map4")
    imagebutton:
        auto "gui/right_%s.png" xpos 1871 ypos 462 action Call("map2")
    imagebutton:
        auto "gui/back_%s.png" xpos 6 ypos 625 action Jump("test")
    imagebutton:
        auto "gui/beach_%s.png" xpos 1050 ypos 350 action Jump("beach")
    imagebutton:
        auto "gui/swamp_%s.png" xpos 1100 ypos 130 action Jump("swamp")


screen map2():
    image "gui/globe2.png"
    imagebutton:
        auto "gui/left_%s.png" xpos 6 ypos 462 action Call("map1")
    imagebutton:
        auto "gui/right_%s.png" xpos 1871 ypos 462 action Call("map3")
    imagebutton:
        auto "gui/back_%s.png" xpos 6 ypos 625 action Jump("test")

    imagebutton:
        auto "gui/kcafe_%s.png" xpos 617 ypos 326 action Jump("kriscafe")


screen map3():
    image "gui/globe3.png"
    imagebutton:
        auto "gui/left_%s.png" xpos 6 ypos 462 action Call("map2")
    imagebutton:
        auto "gui/right_%s.png" xpos 1871 ypos 462 action Call("map4")
    imagebutton:
        auto "gui/back_%s.png" xpos 6 ypos 625 action Jump("test")

screen map4():
    image "gui/globe4.png"
    imagebutton:
        auto "gui/left_%s.png" xpos 6 ypos 462 action Call("map3")
    imagebutton:
        auto "gui/right_%s.png" xpos 1871 ypos 462 action Call("map1")
    imagebutton:
        auto "gui/back_%s.png" xpos 6 ypos 625 action Jump("test")


screen back():
    imagebutton:
        auto "gui/back_%s.png" xpos 6 ypos 625 action [ Play("sound", "audio/click1.mp3"), Jump("test") ] hovered [ Play("sound", "audio/button hover2.mp3") ]


screen experiment:

    if stimulate == 0:
        imagebutton:
            auto "gui/stimulate_%s.png" xpos 182 ypos 432 action Call("stimulate")
        imagebutton:
            auto "gui/left_%s.png" xpos 6 ypos 462 action Call("expview")
        imagebutton:
            auto "gui/right_%s.png" xpos 1871 ypos 462 action Call("expview")
        imagebutton:
            auto "gui/back_%s.png" xpos 6 ypos 625 action Jump("continue1")


    if stimulate == 1:
        if position == 127:
            imagebutton:
                auto "gui/arrow_%s.png" xpos 960 ypos 813 action [ Play("sound", "audio/click2.mp3"), Call("p128") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        if position == 128:
            imagebutton:
                auto "gui/arrow_%s.png" xpos 960 ypos 813 action [ Play("sound", "audio/click2.mp3"), Call("p127") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        if position == 126:
            image "gui/brain.png" xpos 1405 ypos 81 #xzoom 0.2 yzoom 0.2

            imagebutton:
                auto "gui/startexp_%s.png" xpos 1367 ypos 349 action Call("implantexp")

            imagebutton:
                auto "gui/back_%s.png" xpos 6 ypos 625 action Jump("continue1")

            imagebutton:
                auto "gui/limbic_%s.png" xpos 1405 ypos 42 action [ Play("sound", "audio/click2.mp3"), Call("limbic") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

            imagebutton:
                auto "gui/prefrontal_%s.png" xpos 1317 ypos 45 action [ Play("sound", "audio/click2.mp3"), Call("prefrontal") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

            if topology == "prefrontal":

                vbox:
                    text "Prefrontal cortex" xpos 1600 ypos 300 bold 2 size 22
                    text "Frequency" xpos 1600 ypos 300
                    vbox:

                        bar value VariableValue("frequencypc", 150) xpos 1600 ypos 300 ysize 20 xsize 200 left_bar "#464CFF"  right_bar "#CACACA"

                        text "[frequencypc] Hz" xpos 1600 ypos 300

                vbox:
                    text "Intensity" xpos 1600 ypos 400

                    vbox:

                        bar value VariableValue("intensitypc", 0.100) xpos 1600 ypos 400 ysize 20 xsize 200 left_bar "#C10000"  right_bar "#CACACA"
                        text "[intensitypc] mW" xpos 1600 ypos 400
                vbox:
                    text "Width" xpos 1600 ypos 500

                    vbox:

                        bar value VariableValue("widthpc", 100) xpos 1600 ypos 500 ysize 20 xsize 200 left_bar "#007C07"  right_bar "#CACACA"
                        text "[widthpc] µs" xpos 1600 ypos 500

            if topology == "limbic":
                vbox:
                    text "Limbic system" xpos 1600 ypos 300 bold 2 size 22
                    text "Frequency" xpos 1600 ypos 300
                    vbox:

                        bar value VariableValue("frequencyls", 150) xpos 1600 ypos 300 ysize 20 xsize 200 left_bar "#464CFF"  right_bar "#CACACA"

                        text "[frequencyls] Hz" xpos 1600 ypos 300

                vbox:
                    text "Intensity" xpos 1600 ypos 400

                    vbox:

                        bar value VariableValue("intensityls", 0.100) xpos 1600 ypos 400 ysize 20 xsize 200 left_bar "#C10000"  right_bar "#CACACA"
                        text "[intensityls] mW" xpos 1600 ypos 400

                vbox:
                    text "Width" xpos 1600 ypos 500

                    vbox:

                        bar value VariableValue("widthls", 100) xpos 1600 ypos 500 ysize 20 xsize 200 left_bar "#007C07"  right_bar "#CACACA"
                        text "[widthls] µs" xpos 1600 ypos 500


        else:
            pass

screen stream:
    if position == 35 or position == 36:
        if streamaction == 0:
            imagebutton:
                auto "gui/keyboard_%s.png" xpos 980 ypos 859 action Call("streamaction")
        else:
            pass
    else:
        pass
    if randomsaction == 1 and streamaction == 1:
        image "gui/eat.png" xpos 115 ypos 74
        imagebutton:
            auto "gui/doit_%s.png" xpos 1573 ypos 495 action Call("eataction")
        imagebutton:
            auto "gui/pass_%s.png" xpos 198 ypos 495 action Jump("stream")


    if randomsaction == 2 and streamaction == 1:
        image "gui/relax.png" xpos 115 ypos 74
        imagebutton:
            auto "gui/doit_%s.png" xpos 1573 ypos 495 action Call("actionrelax")
        imagebutton:
            auto "gui/pass_%s.png" xpos 198 ypos 495 action Jump("stream")

    if randomsaction == 3 and streamaction == 1:
        image "gui/change.png" xpos 115 ypos 74
        imagebutton:
            auto "gui/doit_%s.png" xpos 1573 ypos 495 action Call("changepose")
        imagebutton:
            auto "gui/pass_%s.png" xpos 198 ypos 495 action Jump("stream")

    if publicapprove == 1:
        image "gui/approve.png" xpos -3 ypos -3
    else:
        image "gui/notapprove.png" xpos -3 ypos -3


    frame:
        xsize 750
        ysize 90
        xpos 1260
        ypos 0
        background Solid("#0000005F")
        xpadding 10
        ypadding 10
    text "Public stuffing opinion [spublicopinion]" bold 1 xpos 1280 ypos 1 color ("#999900") size 30
    text "Public weight gain opinion [fpublicopinion]" bold 1 xpos 1280 ypos 50 color ("#999900") size 30

screen hayoon:
    # text "Stimulation frequency [ffrequency:.02f]" xpos 200 ypos 370
    # textbutton "Up" text_size 17 text_color ("#A3F170") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("up") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    # textbutton "Down" text_size 17 text_color ("#A3F170") xpos 200 ypos 400 action [ Play("sound", "audio/click2.mp3"), Call("down") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    if position == 132 or position == 133 or position == 134:
        vbox:
            text "Stimulation frequency" xpos 200 ypos 670 bold 2 size 22 color ("#999900")

            vbox:

                bar value VariableValue("ffrequency", 0.50) xpos 200 ypos 690 ysize 20 xsize 200 left_bar "#464CFF"  right_bar "#CACACA"

                text "[ffrequency:.02f] sec" xpos 200 ypos 700 color ("#999900")

screen ggame:

    if sequence == 1:

        vbox:
            if myrandom == 1:
                textbutton "[g1]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 2:
                textbutton "[g2]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 3:
                textbutton "[g3]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 4:
                textbutton "[g4]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 5:
                textbutton "[g5]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 6:
                textbutton "[g6]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 7:
                textbutton "[g7]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 8:
                textbutton "[g8]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 9:
                textbutton "[g11]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 10:
                textbutton "[g12]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 11:
                textbutton "[g13]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

            if option1 == 1:
                textbutton "[g1]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 2:
                textbutton "[g2]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 3:
                textbutton "[g3]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 4:
                textbutton "[g4]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 5:
                textbutton "[g5]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 6:
                textbutton "[g6]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 7:
                textbutton "[g7]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 8:
                textbutton "[g8]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 9:
                textbutton "[g11]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 10:
                textbutton "[g12]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 11:
                textbutton "[g13]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]


            if option2 == 1:
                textbutton "[g1]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 2:
                textbutton "[g2]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 3:
                textbutton "[g3]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 4:
                textbutton "[g4]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 5:
                textbutton "[g5]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 6:
                textbutton "[g6]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 7:
                textbutton "[g7]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 8:
                textbutton "[g8]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 9:
                textbutton "[g11]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 10:
                textbutton "[g12]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 11:
                textbutton "[g13]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]


            if option3 == 1:
                textbutton "[g1]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 2:
                textbutton "[g2]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 3:
                textbutton "[g3]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 4:
                textbutton "[g4]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 5:
                textbutton "[g5]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 6:
                textbutton "[g6]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 7:
                textbutton "[g7]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 8:
                textbutton "[g8]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 9:
                textbutton "[g11]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 10:
                textbutton "[g12]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 11:
                textbutton "[g13]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

    if sequence == 2:

        vbox:

            if option1 == 1:
                textbutton "[g1]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 2:
                textbutton "[g2]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 3:
                textbutton "[g3]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 4:
                textbutton "[g4]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 5:
                textbutton "[g5]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 6:
                textbutton "[g6]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 7:
                textbutton "[g7]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 8:
                textbutton "[g8]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 9:
                textbutton "[g11]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 10:
                textbutton "[g12]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 11:
                textbutton "[g13]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

            if myrandom == 1:
                textbutton "[g1]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 2:
                textbutton "[g2]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 3:
                textbutton "[g3]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 4:
                textbutton "[g4]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 5:
                textbutton "[g5]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 6:
                textbutton "[g6]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 7:
                textbutton "[g7]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 8:
                textbutton "[g8]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 9:
                textbutton "[g11]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 10:
                textbutton "[g12]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 11:
                textbutton "[g13]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]



            if option2 == 1:
                textbutton "[g1]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 2:
                textbutton "[g2]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 3:
                textbutton "[g3]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 4:
                textbutton "[g4]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 5:
                textbutton "[g5]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 6:
                textbutton "[g6]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 7:
                textbutton "[g7]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 8:
                textbutton "[g8]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 9:
                textbutton "[g11]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 10:
                textbutton "[g12]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 11:
                textbutton "[g13]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]


            if option3 == 1:
                textbutton "[g1]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 2:
                textbutton "[g2]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 3:
                textbutton "[g3]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 4:
                textbutton "[g4]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 5:
                textbutton "[g5]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 6:
                textbutton "[g6]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 7:
                textbutton "[g7]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 8:
                textbutton "[g8]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 9:
                textbutton "[g11]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 10:
                textbutton "[g12]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 11:
                textbutton "[g13]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

    if sequence == 3:

        vbox:

            if option1 == 1:
                textbutton "[g1]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 2:
                textbutton "[g2]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 3:
                textbutton "[g3]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 4:
                textbutton "[g4]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 5:
                textbutton "[g5]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 6:
                textbutton "[g6]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 7:
                textbutton "[g7]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 8:
                textbutton "[g8]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 9:
                textbutton "[g11]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 10:
                textbutton "[g12]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 11:
                textbutton "[g13]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]



            if option2 == 1:
                textbutton "[g1]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 2:
                textbutton "[g2]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 3:
                textbutton "[g3]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 4:
                textbutton "[g4]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 5:
                textbutton "[g5]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 6:
                textbutton "[g6]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 7:
                textbutton "[g7]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 8:
                textbutton "[g8]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 9:
                textbutton "[g11]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 10:
                textbutton "[g12]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 11:
                textbutton "[g13]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

            if myrandom == 1:
                textbutton "[g1]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 2:
                textbutton "[g2]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 3:
                textbutton "[g3]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 4:
                textbutton "[g4]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 5:
                textbutton "[g5]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 6:
                textbutton "[g6]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 7:
                textbutton "[g7]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 8:
                textbutton "[g8]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 9:
                textbutton "[g11]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 10:
                textbutton "[g12]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 11:
                textbutton "[g13]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]



            if option3 == 1:
                textbutton "[g1]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 2:
                textbutton "[g2]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 3:
                textbutton "[g3]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 4:
                textbutton "[g4]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 5:
                textbutton "[g5]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 6:
                textbutton "[g6]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 7:
                textbutton "[g7]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 8:
                textbutton "[g8]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 9:
                textbutton "[g11]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 10:
                textbutton "[g12]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 11:
                textbutton "[g13]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

    if sequence == 4:

        vbox:

            if option1 == 1:
                textbutton "[g1]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 2:
                textbutton "[g2]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 3:
                textbutton "[g3]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 4:
                textbutton "[g4]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 5:
                textbutton "[g5]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 6:
                textbutton "[g6]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 7:
                textbutton "[g7]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 8:
                textbutton "[g8]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 9:
                textbutton "[g11]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 10:
                textbutton "[g12]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option1 == 11:
                textbutton "[g13]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]



            if option2 == 1:
                textbutton "[g1]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 2:
                textbutton "[g2]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 3:
                textbutton "[g3]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 4:
                textbutton "[g4]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 5:
                textbutton "[g5]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 6:
                textbutton "[g6]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 7:
                textbutton "[g7]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 8:
                textbutton "[g8]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 9:
                textbutton "[g11]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 10:
                textbutton "[g12]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option2 == 11:
                textbutton "[g13]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]




            if option3 == 1:
                textbutton "[g1]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 2:
                textbutton "[g2]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 3:
                textbutton "[g3]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 4:
                textbutton "[g4]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 5:
                textbutton "[g5]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 6:
                textbutton "[g6]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 7:
                textbutton "[g7]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 8:
                textbutton "[g8]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 9:
                textbutton "[g11]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 10:
                textbutton "[g12]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if option3 == 11:
                textbutton "[g13]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggamewrong") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

            if myrandom == 1:
                textbutton "[g1]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 2:
                textbutton "[g2]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 3:
                textbutton "[g3]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 4:
                textbutton "[g4]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 5:
                textbutton "[g5]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 6:
                textbutton "[g6]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 7:
                textbutton "[g7]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 8:
                textbutton "[g8]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 9:
                textbutton "[g11]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 10:
                textbutton "[g12]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            if myrandom == 11:
                textbutton "[g13]" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("ggameright") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

screen fgame:
    textbutton "Switch the girl" text_size 45 text_color ("#000000") xpos 200 ypos 320 action [ Play("sound", "audio/click2.mp3"), Call("fchoosinggirl") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    vbox:
        text "Recovery" xpos 200 ypos 670 bold 2 size 22 color ("#999900")
        vbox:
            bar value VariableValue("recovery", 100) xpos 200 ypos 690 ysize 20 xsize 200 left_bar "#000000"  right_bar "#00B22A"

    if send == 0:
        imagebutton:
            auto "gui/banana_%s.png" xpos 82 ypos 626 action [ Play("sound", "/audio/throw1.mp3"), Call("send") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    if fway == 1:
        image "gui/banana.png" xpos 82 ypos 626
    if fway == 2:
        image "gui/banana.png" xpos 133 ypos 565
    if fway == 3:
        image "gui/banana.png" xpos 175 ypos 509
    if fway == 4:
        image "gui/banana.png" xpos 230 ypos 454
    if fway == 5:
        image "gui/banana.png" xpos 294 ypos 401
    if fway == 6:
        image "gui/banana.png" xpos 350 ypos 360
    if fway == 7:
        image "gui/banana.png" xpos 409 ypos 323
    if fway == 8:
        image "gui/banana.png" xpos 465 ypos 287
    if fway == 9:
        image "gui/banana.png" xpos 529 ypos 245
    if fway == 10:
        image "gui/banana.png" xpos 596 ypos 214
    if fway == 11:
        image "gui/banana.png" xpos 664 ypos 184
    if fway == 12:
        image "gui/banana.png" xpos 741 ypos 153
    if fway == 13:
        image "gui/banana.png" xpos 818 ypos 123
    if fway == 14:
        image "gui/banana.png" xpos 896 ypos 83
    if fway == 15:
        image "gui/banana.png" xpos 966 ypos 73
    if fway == 16:
        image "gui/banana.png" xpos 1040 ypos 76
    if fway == 17:
        image "gui/banana.png" xpos 1098 ypos 92
    if fway == 18:
        image "gui/banana.png" xpos 1157 ypos 106
    if fway == 19:
        image "gui/banana.png" xpos 123 ypos 1208
    if fway == 20:
        image "gui/banana.png" xpos 1272 ypos 144

# screen actions():
#     image brain zoom
#     image button publishing
#
# screen publishing:
#     image publisher bg
#     buttons journal cover options
