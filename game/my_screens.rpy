label hide_notification_label(screen_name, delay):
    # Wait that many seconds (pauses this new context).
    $ renpy.pause(delay, hard=True)
    # Then hide the screen.
    $ renpy.hide_screen(screen_name)
    return

screen success_notification_screen(
        message="[positivemessage]",
        start_y=0.6,
        end_y=0.45,
        fade_in=0.5,
        wait=1.5,
        fade_out=0.5,
        text_size=28,
        text_bold=True
    ):

    zorder 100

    # 1) A timer that automatically hides this screen
    timer (fade_in + wait + fade_out) action Hide("success_notification_screen")

    # 2) The text that animates in/out using ATL
    hbox:
        ysize 500
        xalign 0.1
        yalign 0.15
        if nigirlimage != "":
            image "gui/[nigirlimage].png" at notify_anim(start_y, end_y, fade_in, wait, fade_out) xoffset 0 ysize 50 xsize 50 yalign 0.5
        
        image "gui/[niimage].png" at notify_anim(start_y, end_y, fade_in, wait, fade_out) xoffset 0 ysize 50 xsize 50 yalign 0.5
        
        text message:
            xoffset 5
            yalign 0.5
            at notify_anim(start_y, end_y, fade_in, wait, fade_out)
            bold text_bold
            size text_size
            color "#ffffff"
        
    # text message:
    #     xalign 0.15
    #     at notify_anim(start_y, end_y, fade_in, wait, fade_out)
    #     bold text_bold
    #     size text_size
    #     color "#ffffff"

screen warning_notification_screen(
        message="[negativemessage]",
        start_y=0.6,
        end_y=0.4,
        fade_in=0.5,
        wait=1.5,
        fade_out=0.5,
        text_size=28,
        text_bold=True
    ):
    zorder 100
    text message:
        xalign 0.5
        at notify_anim(start_y, end_y, fade_in, wait, fade_out)
        bold text_bold
        size text_size
        color "#FFA500"   # <-- Orange for warning

screen neutral_notification_screen(
        message="[neutralmessage]",
        start_y=0.6,
        end_y=0.4,
        fade_in=0.5,
        wait=1.5,
        fade_out=0.5,
        text_size=28,
        text_bold=True
    ):
    zorder 100
    text message:
        xalign 0.5
        at notify_anim(start_y, end_y, fade_in, wait, fade_out)
        bold text_bold
        size text_size
        color "#FFA500"   # <-- Orange for warning

screen error_notification_screen(
        message="Error!",
        start_y=0.6,
        end_y=0.4,
        fade_in=0.5,
        wait=1.5,
        fade_out=0.5,
        text_size=28,
        text_bold=True
    ):
    zorder 100
    text message:
        xalign 0.5
        at notify_anim(start_y, end_y, fade_in, wait, fade_out)
        bold text_bold
        size text_size
        color "#FF0000"   # <-- Red for error

screen kitchenscale:
    image "gui/bgposkitchencooking.png"
    


    if scaleactive == 0:
        # image "gui/dg_kitchen_arrow_idle.png" xpos x ypos y
        # imagebutton:
        #     auto "gui/dg_kitchen_scale_%s.png" xpos 568 ypos 500 action [ Play("sound", "audio/click2.mp3"), Call("scale") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

        button:
            xpos 780
            ypos 500
            xysize (250, 60)

            background Transform("gui/button_wide.png", alpha=button_wide_alpha)

            action [Play("sound", "audio/click2.mp3"), Call("scale")]
            hovered [SetVariable('button_wide_alpha', 0.85), Play("sound", "audio/button_hover4.mp3")]
            unhovered SetVariable('button_wide_alpha', 0.65)

            add Transform(
                Text("Cook", bold=True, color="#ffffff", size=22),
                alpha=button_wide_alpha,
                xalign=0.5,
                yalign=0.5,
                yoffset=-5
            )


    if scaleactive == 1:
        image "rightpan" xpos 965 ypos 306
        image "leftpan" xpos 166 ypos 290
        # Display the moving arrow independently.
        # add "gui/dg_kitchen_arrow_hover.png" xpos x ypos y
        

        # button:
        #     xpos 568
        #     ypos 500
        #     action [ Play("sound", "audio/click2.mp3"), SetVariable("scaleactive", 0)]
        #     hovered [SetVariable('button_wide_alpha', 0.85), Play("sound", "audio/button_hover4.mp3")],
        #     unhovered SetVariable('button_wide_alpha', 0.65)

        #     background Transform("gui/button_wide.png", alpha=button_wide_alpha)

        #     add Transform(Text("Cook", bold=True, color="#ffffff", size=22), alpha=button_wide_alpha):
        #         xalign 0.5
        #         yalign 0.5
        #         yoffset 5
        #         xoffset 0
        

        button:
            xpos 780
            ypos 500
            xysize (250, 60)

            background Transform("gui/button_wide2.png", alpha=button_wide_alpha)

            action [ Play("sound", "audio/click2.mp3"), SetVariable("scaleactive", 0)]
            hovered [SetVariable('button_wide_alpha', 0.85), Play("sound", "audio/button_hover4.mp3")]
            unhovered SetVariable('button_wide_alpha', 0.65)

            add Transform(
                Text("Cook", bold=True, color="#ffffff", size=22),
                alpha=button_wide_alpha,
                xalign=0.5,
                yalign=0.5,
                yoffset=-5
            )
    
    fixed:
        pos (scalepos_x, scalepos_y)  # Position on screen where image stays anchored
        # xysize (scaleimage_width, scaleimage_height)
        image "gui/cookingscale_bg.png" xpos -10 ypos -10
        # The dynamically cropped image (right side gets cut off)
        add LiveCrop(
            (0, 0, scaleimage_width - scalecrop_right, scaleimage_height),  # (x, y, width, height)
            "gui/scale_inner.png"
        )

        # text "scalecrop_right - [scalecrop_right], scaleline_x1 - [scaleline_x1], scaleline_x2 - [scaleline_x2], scalesweetspotmin [scalesweetspotmin], scalesweetspotmax [scalesweetspotmax]" xpos 0 ypos 0 color ("#080606") size 19
    
    add Solid(scaleline_color, xsize=4, ysize=59):
        pos (scalepos_x + scaleline_x1, scalepos_y + scaleline_y1)  # (x, y) position
        anchor (0, 0)  # Anchor at top-left corner

    # Line 2 (Right)
    add Solid(scaleline_color, xsize=4, ysize=59):
        pos (scalepos_x + scaleline_x2, scalepos_y + scaleline_y2)
        anchor (0, 0)


    # if scaleactive == 0:
    # imagebutton:
    #     idle Transform("gui/button_std.png", alpha=0.65)        
    #     hover Transform("gui/button_std.png", alpha=0.85) 
    #     xpos 30 
    #     ypos 650 
    #     action [ Play("sound", "audio/click2.mp3"), Call("endshift") ]
    #     hovered [Play("sound", "audio/button_hover4.mp3")]
    #     text "End shift" bold 1 xpos 33 ypos 660 color ("#ffffffff") size 23
    #     text "End shift" bold 1 xpos 33 ypos 660 color ("#ffffffff") size 23

    text "[cookingstatus]":
        bold True
        xalign 0.5
        xpos 905
        ypos 469
        color "#ffffff"
        size 22
        at flicker_effect(min_alpha=0.3, cycle_time=1.75)

        
    
   
    fixed:
        xpos 30
        ypos 413
        image "gui/info_field1.png" ysize 40 xsize 333 
        text "Cook reputation [workreputation]" bold 1 xoffset 10 yoffset 5 color ("#ffffffff") size 25

        image "gui/info_field1.png" ysize 40 xsize 333 yoffset 45 
        text "Day earnings [daysalary:.2f]" bold 1 xoffset 10 yoffset 50 color ("#ffffffff") size 25

        image "gui/info_field1.png" ysize 40 xsize 333 yoffset 90
        text "Cooking skill [cookingskill:.1f]" bold 1 xoffset 10 yoffset 95 color ("#ffffffff") size 25

        button:
            xoffset 100
            yoffset 140
            # xpos 30
            # ypos 650
            action [Play("sound", "audio/click2.mp3"), Call("endshift")]
            hovered [SetVariable('button_alpha', 0.85), Play("sound", "audio/button_hover4.mp3")]
            unhovered SetVariable('button_alpha', 0.65)

            background Transform("gui/button_std2.png", alpha=button_alpha)

            add Transform(Text("End shift", bold=True, color="#ffffff", size=21), alpha=button_alpha):
                xalign 0.5
                yalign 0.5
                yoffset 7
                xoffset 3
 
screen callmap():
    

    if mapbuttonisactive == True:
        imagebutton:
            auto "gui/dg_map_callmap_%s.png" xpos 1834 ypos 0 action [ Play("sound", "audio/click2.mp3"), ShowTransient("map") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    
    if youarehome == False:
        imagebutton:
            auto "gui/dg_home_%s.png" xpos 20 ypos 540 action [ Play("sound", "audio/click2.mp3"), Jump("culinarychoices") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    
    if youarehome == True and (avafirstmeet > 0 or hayoonfirstmeet > 0 or sallyhello > 0 or linfirsttime > 0):
        imagebutton:
            auto "gui/statsallgirls_%s.png" xpos 320 ypos 18 action [ Play("sound", "audio/click2.mp3"), ToggleScreen("girlsstats")] hovered [ Play("sound", "audio/button hover4.mp3") ]
    
    if mapishere == 0:
        imagebutton:
            auto "gui/dg_map_pointer_%s.png" xpos 1622 ypos 42 action [ Play("sound", "audio/click2.mp3"), Call("mapishere") ] hovered [ Play("sound", "audio/button hover4.mp3") ] 
    
    if youarehome == True:
        fixed:
            xpos 5 ypos 120 xsize 300 ysize 24
            imagebutton:
                    auto "gui/vgallerybutton_bg_%s.png" xpos 0 ypos 0 action [ Play("sound", "audio/click2.mp3"), ToggleScreen("gallery"), ToggleScreen("callmap") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
            text "Unlocked videos" bold True color "#ffffff" size 15 xalign 0.5 yalign 0.5
    
screen attitude_stat_bar(
        attitude,           # current value in [-100..100]
        width=260, 
        height=40,
        min_val=-100,
        max_val=100
    ):

    # Draw the background bar.
    add "gui/girlstatsscalebg.png"

    # Draw the cropped fill image (center-based).
    $ crop_rect = get_stat_crop(attitude, width, height)
    add LiveCrop(crop_rect, "gui/girlstatsscaleattitude.png") xpos crop_rect[0]

    # Place lines & labels in a fixed container that matches the bar size.
    fixed:
        xsize width
        ysize height

        # Compute x positions for min_val, 0, current, max_val
        $ min_x = get_x_for_stat(min_val, min_val, max_val, width)  # should be 0
        $ zero_x = get_x_for_stat(0,       min_val, max_val, width)  # should be 130 if width=260
        $ curr_x = get_x_for_stat(attitude, min_val, max_val, width)
        $ max_x = get_x_for_stat(max_val, min_val, max_val, width)  # should be 260

        # -- VERTICAL LINES (black) --
        # If you want them exactly inside the bar’s 40px, do ysize=40
        # If you want them bigger/longer, adjust as needed.

        # # Min line (left edge)
        # add Solid("#000000", xsize=1, ysize=70) xpos min_x ypos 5 anchor (0.5, 0.0)

        # Zero line (center)
        add Solid("#000000", xsize=1, ysize=80) xpos zero_x ypos 0 anchor (0.5, 0.0)

        # Current attitude line
        add Solid("#000000", xsize=1, ysize=80) xpos curr_x ypos 0 anchor (0.5, 0.5)

        # # Max line (right edge)
        # add Solid("#000000", xsize=1, ysize=70) xpos max_x ypos 5 anchor (0.5, 0.0)

        # -- LABELS --
        # If you want text to the *left* of the line, use anchor (1.0, 0.5)
        # If you want text to the *right* of the line, use anchor (0.0, 0.5)
        # If you want it above or below, adjust ypos accordingly.

        # Min value label (left)
        # text "[min_val]":
        #     xpos min_x
        #     ypos height + 2
        #     anchor (-0.1, -0.3)  # left-edge alignment to the line

        # Zero value label (middle)
        text "0":
            xpos zero_x
            ypos height + 2
            anchor (-0.1, -0.3)  # center on the line, below the bar

        # Current attitude label (top)
        text "[attitude]":
            xpos curr_x
            ypos -2
            anchor (0.0, 1.3)  # left-edge alignment, above the bar

        # Max value label (right)
        # text "[max_val]":
        #     xpos max_x
        #     ypos height + 2
        #     anchor (-0.1, -0.3)  # right-edge alignment, below the bar

screen fullness_bar(
        value, 
        max_value, 
        width=261, 
        height=41
    ):
    

    # We'll use a container bigger than the bar so we can draw lines above/below.
    fixed:
        xsize width
        ysize 80  # 40px for the bar, plus 40px of space. Adjust as you like.

        # 1) Draw the bar background at the top (y=0).
        add "gui/girlstatsscalebg.png" xpos 0 ypos 0

        # 2) Cropped fill from the left edge to the ratio.
        $ crop_rect = get_fill_crop(value, max_value, width, height)
        add LiveCrop(crop_rect, "gui/girlstatsscalefullness.png") xpos 0 ypos 0

        # 3) Compute x positions for 0, current, max_value.
        #    clamp so it never goes beyond 0..width
        $ ratio = 0.0
        if max_value > 0:
            $ ratio = min(max(value / float(max_value), 0.0), 1.0)
        $ curr_x = int(width * ratio)
        $ zero_x = 0
        $ max_x = width

        # 4) Lines
        #
        #  - The bar is 41px tall, so we place lines for 0 & max below it
        #    by anchoring them at the bar's bottom (ypos=height).
        #  - The current line extends above the bar by anchoring at y=0
        #    with anchor (0.5,1.0).

        # # 4A) 0 line (left edge), below the bar
        # add Solid("#000000", xsize=1, ysize=30) xpos zero_x ypos height anchor (0.5, 0.0)

        # # 4B) max_value line (right edge), below the bar
        # add Solid("#000000", xsize=1, ysize=30) xpos max_x ypos height anchor (0.5, 0.0)

        # 4C) current value line, above the bar
        # add Solid("#000000", xsize=1, ysize=30) xpos curr_x ypos 0 anchor (0.5, 1.0)

        # 5) Labels
        #
        #  - "0" and "[max_value]" below the bar near their lines
        #  - "[value]" above the bar near its line

        # text "0":
        #     xpos zero_x
        #     ypos height + 2
        #     anchor (0.5, 0.0)

        # text "[max_value]":
        #     xpos max_x
        #     ypos height + 2
        #     anchor (0.5, 0.0)

        # text "[value]":
        #     xpos curr_x
        #     ypos -2
        #     anchor (0, 1.0)

screen girlsstats():
    on "show" action SetVariable("mapbuttonisactive", False)
    on "hide" action SetVariable("mapbuttonisactive", True)
    
    vpgrid:
        xpos 420
        ypos 18
        # xsize 243
        # ysize 735
        rows 1
        spacing 5
        if avafirstmeet > 0:
            imagebutton:
                auto "gui/statsava_%s.png" action [ Play("sound", "audio/click2.mp3"), ToggleScreen("avastats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        if hayoonfirstmeet > 0:
            imagebutton:
                auto "gui/statshayoon_%s.png" action [ Play("sound", "audio/click2.mp3"), ToggleScreen("hayoonstats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        if sallyhello > 0:
            imagebutton:
                auto "gui/statssally_%s.png" action [ Play("sound", "audio/click2.mp3"), ToggleScreen("sallystats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        if linfirsttime > 0:
            imagebutton:
                auto "gui/statslin_%s.png" action [ Play("sound", "audio/click2.mp3"), ToggleScreen("linstats") ] hovered [ Play("sound", "audio/button hover4.mp3") ]

screen map():
    on "show" action SetVariable("youarehome", False)
    on "show" action Function(pause_music)
    on "hide" action Function(resume_music)

    image "gui/dg_map.png"
    imagebutton:
        auto "gui/dg_map_home_%s.png" xpos 863 ypos 102 action [ Play("sound", "audio/click2.mp3"), Jump("culinarychoices") ] hovered [ Play("sound", "audio/button hover4.mp3") ] 
    
    imagebutton:
        auto "gui/dg_map_bar_%s.png" xpos 1027 ypos 315 action [ Play("sound", "audio/click2.mp3"), Jump("bar") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    imagebutton:
        auto "gui/dg_map_burgers_%s.png" xpos 1034 ypos 160 action [ Play("sound", "audio/click2.mp3"), Jump("bcafe") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    if hayoonrandome > 0:
        imagebutton:
            auto "gui/dg_map_hospital_%s.png" xpos 818 ypos 511 action [ Play("sound", "audio/click2.mp3"), Jump("hayoonhospital") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
    
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

    fixed:
        xpos 5
        ypos 5
        image "gui/statsbgbox.png"


        fixed:
            xsize 90
            ysize 90
            xpos 10
            ypos 10
            image "gui/tdaybox.png"
            
            $ text_size = auto_text_size("[calendar.TotalDays]", 75, 37)  # 160 - 20 padding
            text "Day" xalign 0.5 yalign 0.16 bold True color "#ffffff" size text_size 
            text "[calendar.TotalDays]":
                xoffset 0
                yoffset 0
                xalign 0.5
                yalign 0.86
                color "#ffffff"
                size text_size 
                bold True
        
        fixed:
            xsize 90
            ysize 40
            xpos 105
            ypos 10
            image "gui/stdbox.png"
            
            $ text_size = auto_text_size("[calendar.Days]/ [calendar.Month]", 80, 40)  # 160 - 20 padding
            
            text "[calendar.Days] [calendar.Month]":
                xoffset 0
                yoffset 2
                xalign 0.5
                yalign 0.5
                color "#ffffff"
                size text_size 
                bold True
            
        fixed:
            xsize 90
            ysize 40
            xpos 200
            ypos 10
            image "gui/stdbox.png"
            
            $ text_size = auto_text_size("[calendar.WeekDay]", 75, 35)  # 160 - 20 padding
            
            text "[calendar.WeekDay]":
                xoffset 0
                yoffset 1
                xalign 0.5
                yalign 0.5
                color "#ffffff"
                size text_size 
                bold True

        fixed:
            xsize 90
            ysize 40
            xpos 105
            ypos 60
            image "gui/stdbox.png"
            
            $ text_size = auto_text_size("[calendar.Time]", 75, 40)  # 160 - 20 padding
            
            text "[calendar.Time]":
                xoffset 0
                yoffset 1
                xalign 0.5
                yalign 0.5
                color "#ffffff"
                size text_size 
                bold True

        fixed:
            xsize 90
            ysize 40
            xpos 200
            ypos 60
            image "gui/stdbox.png"
            
            $ text_size = auto_text_size("$ [money:.2f]", 75, 35)  # 160 - 20 padding
            
            text "$ [money:.0f]":
                xoffset 0
                yoffset 2
                xalign 0.5
                yalign 0.5
                color "#ffffff"
                size text_size 
                bold True
    
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

screen avastats():
    modal True

    
    fixed:
        # Outer border (full screen)
        add Solid("#5b0098") xysize (1920, 1080)
        # Inner background inset by 3 pixels, with 80% opacity (0xcc = ~80% opacity)
        add Solid("#575757cc") xpos 5 ypos 5 xsize 1910 ysize 1070

    if ava_attitude < 10 and ava_attitude > -10:
        image "gui/girlsstatsgirlbgwhite.png" xpos 678 ypos 85
    if ava_attitude >= 10:
        image "gui/girlsstatsgirlbggreen.png" xpos 678 ypos 85
    if ava_attitude <= -10:
        image "gui/girlsstatsgirlbgred.png" xpos 678 ypos 85
        
    image "avastats" align (0.5, 0.0)
    
    fixed:
            xsize 271
            ysize 72
            xpos 836
            ypos 19
            image "gui/girlsstatsname.png"
            
            $ text_size = auto_text_size("Ava", 271, 50)  # 160 - 20 padding
            
            text "Ava":
                xoffset 0
                yoffset 0
                xalign 0.5
                yalign 0.5
                color "#000000"
                size text_size 
                bold True
    
    

    fixed:
        xpos 1845 ypos 13
        
        imagebutton:
                auto "gui/roundbutton_%s.png" action [ Play("sound", "audio/click2.mp3"), Function(close_all_stats) ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "X" xpos 17 ypos 10 color ("#000000") size 40 bold True
    
    if ava_weightstage <= 4:
        if metric == 1:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[ava_weight] kg", 50, 75)  # 160 - 20 padding
                    
                    text "[ava_weight] kg":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#ffffff"
                        size text_size 
                        bold True
        
        else:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[ava_weightlbs] lbs", 50, 75)  # 160 - 20 padding
                    
                    text "[ava_weightlbs] lbs":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#ffffff"
                        size text_size 
                        bold True
    if ava_weightstage > 4 and ava_weightstage <= 7:
        if metric == 1:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[ava_weight] kg", 50, 75)  # 160 - 20 padding
                    
                    text "[ava_weight] kg":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#e5e500"
                        size text_size 
                        bold True
        
        else:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[ava_weightlbs] lbs", 50, 75)  # 160 - 20 padding
                    
                    text "[ava_weightlbs] lbs":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#e5e500"
                        size text_size 
                        bold True
    if ava_weightstage > 7 and ava_weightstage <= 10:
        if metric == 1:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[ava_weight] kg", 50, 75)  # 160 - 20 padding
                    
                    text "[ava_weight] kg":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#cb0000"
                        size text_size 
                        bold True
        
        else:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[ava_weightlbs] lbs", 50, 75)  # 160 - 20 padding
                    
                    text "[ava_weightlbs] lbs":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#cb0000"
                        size text_size 
                        bold True
    
    fixed:
        xpos 1095 
        ypos 106
        image "gui/girlsstatsbgforstats.png" xpos 0 ypos 0
        image "gui/reputationup.png" xpos 10 ypos 10 xsize 40 ysize 40
        fixed:
            xpos 58 
            ypos 10
            use attitude_stat_bar(ava_attitude, width=260, height=40, min_val=-100, max_val=100)
 

    fixed:
        xpos 321
        ypos 500
        image "gui/girlsstatsbgforstats.png" xpos 0 ypos 0
        image "gui/fullness.png" xpos 10 ypos 10 xsize 40 ysize 40
        fixed:
            xpos 58
            ypos 10
            use fullness_bar(ava_fullness, ava_fullmax, width=261, height=41) 

    $ xposimperial = 515    
    $ yposimperial = 931

    $ xpostextimperial = xposimperial + 29
    $ ypostextimperial = yposimperial + 15

    $ xposmetric = 515
    $ yposmetric = 855

    $ xpostextmetric = xposmetric + 18
    $ ypostextmetric = yposmetric + 15
    
    if metric == 1:
        
        imagebutton:
            auto "gui/roundbutton_%s.png" xpos xposimperial ypos yposimperial action [ Play("sound", "audio/click2.mp3"), Call("imperial") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "I" xpos xpostextimperial ypos ypostextimperial color ("#a1a1a1") size 32
        imagebutton:
            auto "gui/roundbutton_%s.png" xpos xposmetric ypos yposmetric action [ Play("sound", "audio/click2.mp3"), Call("metric") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "M" xpos xpostextmetric ypos ypostextmetric color ("#000000") size 32
    else:
        
        imagebutton:
            auto "gui/roundbutton_%s.png" xpos xposimperial ypos yposimperial action [ Play("sound", "audio/click2.mp3"), Call("imperial") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "I" xpos xpostextimperial ypos ypostextimperial color ("#000000") size 32
        
        imagebutton:
            auto "gui/roundbutton_%s.png" xpos xposmetric ypos yposmetric action [ Play("sound", "audio/click2.mp3"), Call("metric") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "M" xpos xpostextmetric ypos ypostextmetric color ("#a1a1a1") size 32

screen hayoonstats():
    modal True
    fixed:
        # Outer border (full screen)
        add Solid("#5b0098") xysize (1920, 1080)
        # Inner background inset by 3 pixels, with 80% opacity (0xcc = ~80% opacity)
        add Solid("#575757cc") xpos 5 ypos 5 xsize 1910 ysize 1070

    if hayoon_attitude < 10 and hayoon_attitude > -10:
        image "gui/girlsstatsgirlbgwhite.png" xpos 678 ypos 85
    if hayoon_attitude >= 10:
        image "gui/girlsstatsgirlbggreen.png" xpos 678 ypos 85
    if hayoon_attitude <= -10:
        image "gui/girlsstatsgirlbgred.png" xpos 678 ypos 85
        
    image "hayoonstats" align (0.5, 0.0)
    
    fixed:
            xsize 271
            ysize 72
            xpos 836
            ypos 19
            image "gui/girlsstatsname.png"
            
            $ text_size = auto_text_size("Ha-yoon", 271, 50)  # 160 - 20 padding
            
            text "Ha-yoon":
                xoffset 0
                yoffset 0
                xalign 0.5
                yalign 0.5
                color "#000000"
                size text_size 
                bold True
    
    

    fixed:
        xpos 1845 ypos 13
        
        imagebutton:
                auto "gui/roundbutton_%s.png" action [ Play("sound", "audio/click2.mp3"), Function(close_all_stats) ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "X" xpos 17 ypos 10 color ("#000000") size 40 bold True
    
    if hayoon_weightstage <= 4:
        if metric == 1:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[hayoon_weight] kg", 50, 75)  # 160 - 20 padding
                    
                    text "[hayoon_weight] kg":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#ffffff"
                        size text_size 
                        bold True
        
        else:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[hayoon_weightlbs] lbs", 50, 75)  # 160 - 20 padding
                    
                    text "[hayoon_weightlbs] lbs":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#ffffff"
                        size text_size 
                        bold True
    if hayoon_weightstage > 4 and hayoon_weightstage <= 7:
        if metric == 1:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[hayoon_weight] kg", 50, 75)  # 160 - 20 padding
                    
                    text "[hayoon_weight] kg":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#e5e500"
                        size text_size 
                        bold True
        
        else:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[hayoon_weightlbs] lbs", 50, 75)  # 160 - 20 padding
                    
                    text "[hayoon_weightlbs] lbs":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#e5e500"
                        size text_size 
                        bold True
    if hayoon_weightstage > 7 and hayoon_weightstage <= 10:
        if metric == 1:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[hayoon_weight] kg", 50, 75)  # 160 - 20 padding
                    
                    text "[hayoon_weight] kg":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#cb0000"
                        size text_size 
                        bold True
        
        else:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[hayoon_weightlbs] lbs", 50, 75)  # 160 - 20 padding
                    
                    text "[hayoon_weightlbs] lbs":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#cb0000"
                        size text_size 
                        bold True
    
    fixed:
        xpos 1095 
        ypos 106
        image "gui/girlsstatsbgforstats.png" xpos 0 ypos 0
        image "gui/reputationup.png" xpos 10 ypos 10 xsize 40 ysize 40
        fixed:
            xpos 58 
            ypos 10
            use attitude_stat_bar(hayoon_attitude, width=260, height=40, min_val=-100, max_val=100)
 

    fixed:
        xpos 321
        ypos 500
        image "gui/girlsstatsbgforstats.png" xpos 0 ypos 0
        image "gui/fullness.png" xpos 10 ypos 10 xsize 40 ysize 40
        fixed:
            xpos 58
            ypos 10
            use fullness_bar(hayoon_fullness, hayoon_fullmax, width=261, height=41) 

    $ xposimperial = 515    
    $ yposimperial = 931

    $ xpostextimperial = xposimperial + 29
    $ ypostextimperial = yposimperial + 15

    $ xposmetric = 515
    $ yposmetric = 855

    $ xpostextmetric = xposmetric + 18
    $ ypostextmetric = yposmetric + 15
    
    if metric == 1:
        
        imagebutton:
            auto "gui/roundbutton_%s.png" xpos xposimperial ypos yposimperial action [ Play("sound", "audio/click2.mp3"), Call("imperial") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "I" xpos xpostextimperial ypos ypostextimperial color ("#a1a1a1") size 32
        imagebutton:
            auto "gui/roundbutton_%s.png" xpos xposmetric ypos yposmetric action [ Play("sound", "audio/click2.mp3"), Call("metric") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "M" xpos xpostextmetric ypos ypostextmetric color ("#000000") size 32
    else:
        
        imagebutton:
            auto "gui/roundbutton_%s.png" xpos xposimperial ypos yposimperial action [ Play("sound", "audio/click2.mp3"), Call("imperial") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "I" xpos xpostextimperial ypos ypostextimperial color ("#000000") size 32
        
        imagebutton:
            auto "gui/roundbutton_%s.png" xpos xposmetric ypos yposmetric action [ Play("sound", "audio/click2.mp3"), Call("metric") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "M" xpos xpostextmetric ypos ypostextmetric color ("#a1a1a1") size 32

screen sallystats():
    modal True
    fixed:
        # Outer border (full screen)
        add Solid("#5b0098") xysize (1920, 1080)
        # Inner background inset by 3 pixels, with 80% opacity (0xcc = ~80% opacity)
        add Solid("#575757cc") xpos 5 ypos 5 xsize 1910 ysize 1070

    if sally_attitude < 10 and sally_attitude > -10:
        image "gui/girlsstatsgirlbgwhite.png" xpos 678 ypos 85
    if sally_attitude >= 10:
        image "gui/girlsstatsgirlbggreen.png" xpos 678 ypos 85
    if sally_attitude <= -10:
        image "gui/girlsstatsgirlbgred.png" xpos 678 ypos 85
        
    image "sallystats" align (0.5, 0.0)
    
    fixed:
            xsize 271
            ysize 72
            xpos 836
            ypos 19
            image "gui/girlsstatsname.png"
            
            $ text_size = auto_text_size("Sally", 271, 50)  # 160 - 20 padding
            
            text "Sally":
                xoffset 0
                yoffset 0
                xalign 0.5
                yalign 0.5
                color "#000000"
                size text_size 
                bold True
    
    

    fixed:
        xpos 1845 ypos 13
        
        imagebutton:
                auto "gui/roundbutton_%s.png" action [ Play("sound", "audio/click2.mp3"), Function(close_all_stats) ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "X" xpos 17 ypos 10 color ("#000000") size 40 bold True
    
    if sally_weightstage <= 4:
        if metric == 1:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[sally_weight] kg", 50, 75)  # 160 - 20 padding
                    
                    text "[sally_weight] kg":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#ffffff"
                        size text_size 
                        bold True
        
        else:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[sally_weightlbs] lbs", 50, 75)  # 160 - 20 padding
                    
                    text "[sally_weightlbs] lbs":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#ffffff"
                        size text_size 
                        bold True
    if sally_weightstage > 4 and sally_weightstage <= 7:
        if metric == 1:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[sally_weight] kg", 50, 75)  # 160 - 20 padding
                    
                    text "[sally_weight] kg":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#e5e500"
                        size text_size 
                        bold True
        
        else:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[sally_weightlbs] lbs", 50, 75)  # 160 - 20 padding
                    
                    text "[sally_weightlbs] lbs":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#e5e500"
                        size text_size 
                        bold True
    if sally_weightstage > 7 and sally_weightstage <= 10:
        if metric == 1:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[sally_weight] kg", 50, 75)  # 160 - 20 padding
                    
                    text "[sally_weight] kg":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#cb0000"
                        size text_size 
                        bold True
        
        else:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[sally_weightlbs] lbs", 50, 75)  # 160 - 20 padding
                    
                    text "[sally_weightlbs] lbs":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#cb0000"
                        size text_size 
                        bold True
    
    fixed:
        xpos 1095 
        ypos 106
        image "gui/girlsstatsbgforstats.png" xpos 0 ypos 0
        image "gui/reputationup.png" xpos 10 ypos 10 xsize 40 ysize 40
        fixed:
            xpos 58 
            ypos 10
            use attitude_stat_bar(sally_attitude, width=260, height=40, min_val=-100, max_val=100)
 

    fixed:
        xpos 321
        ypos 500
        image "gui/girlsstatsbgforstats.png" xpos 0 ypos 0
        image "gui/fullness.png" xpos 10 ypos 10 xsize 40 ysize 40
        fixed:
            xpos 58
            ypos 10
            use fullness_bar(sally_fullness, sally_fullmax, width=261, height=41) 

    $ xposimperial = 515    
    $ yposimperial = 931

    $ xpostextimperial = xposimperial + 29
    $ ypostextimperial = yposimperial + 15

    $ xposmetric = 515
    $ yposmetric = 855

    $ xpostextmetric = xposmetric + 18
    $ ypostextmetric = yposmetric + 15
    
    if metric == 1:
        
        imagebutton:
            auto "gui/roundbutton_%s.png" xpos xposimperial ypos yposimperial action [ Play("sound", "audio/click2.mp3"), Call("imperial") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "I" xpos xpostextimperial ypos ypostextimperial color ("#a1a1a1") size 32
        imagebutton:
            auto "gui/roundbutton_%s.png" xpos xposmetric ypos yposmetric action [ Play("sound", "audio/click2.mp3"), Call("metric") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "M" xpos xpostextmetric ypos ypostextmetric color ("#000000") size 32
    else:
        
        imagebutton:
            auto "gui/roundbutton_%s.png" xpos xposimperial ypos yposimperial action [ Play("sound", "audio/click2.mp3"), Call("imperial") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "I" xpos xpostextimperial ypos ypostextimperial color ("#000000") size 32
        
        imagebutton:
            auto "gui/roundbutton_%s.png" xpos xposmetric ypos yposmetric action [ Play("sound", "audio/click2.mp3"), Call("metric") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "M" xpos xpostextmetric ypos ypostextmetric color ("#a1a1a1") size 32

screen linstats():
    modal True
    # achivements

    




    fixed:
        # Outer border (full screen)
        add Solid("#5b0098") xysize (1920, 1080)
        # Inner background inset by 3 pixels, with 80% opacity (0xcc = ~80% opacity)
        add Solid("#575757cc") xpos 5 ypos 5 xsize 1910 ysize 1070

    if lin_attitude < 10 and lin_attitude > -10:
        image "gui/girlsstatsgirlbgwhite.png" xpos 678 ypos 85
    if lin_attitude >= 10:
        image "gui/girlsstatsgirlbggreen.png" xpos 678 ypos 85
    if lin_attitude <= -10:
        image "gui/girlsstatsgirlbgred.png" xpos 678 ypos 85
        
    image "linstats" align (0.5, 0.0)
    
    fixed:
            xsize 271
            ysize 72
            xpos 836
            ypos 19
            image "gui/girlsstatsname.png"
            
            $ text_size = auto_text_size("Lin", 271, 50)  # 160 - 20 padding
            
            text "Lin":
                xoffset 0
                yoffset 0
                xalign 0.5
                yalign 0.5
                color "#000000"
                size text_size 
                bold True
    
    

    fixed:
        xpos 1845 ypos 13
        
        imagebutton:
                auto "gui/roundbutton_%s.png" action [ Play("sound", "audio/click2.mp3"), Function(close_all_stats) ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "X" xpos 17 ypos 10 color ("#000000") size 40 bold True
    
    if lin_weightstage <= 4:
        if metric == 1:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[lin_weight] kg", 50, 75)  # 160 - 20 padding
                    
                    text "[lin_weight] kg":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#ffffff"
                        size text_size 
                        bold True
        
        else:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[lin_weightlbs] lbs", 50, 75)  # 160 - 20 padding
                    
                    text "[lin_weightlbs] lbs":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#ffffff"
                        size text_size 
                        bold True
    if lin_weightstage > 4 and lin_weightstage <= 7:
        if metric == 1:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[lin_weight] kg", 50, 75)  # 160 - 20 padding
                    
                    text "[lin_weight] kg":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#e5e500"
                        size text_size 
                        bold True
        
        else:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[lin_weightlbs] lbs", 50, 75)  # 160 - 20 padding
                    
                    text "[lin_weightlbs] lbs":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#e5e500"
                        size text_size 
                        bold True
    if lin_weightstage > 7 and lin_weightstage <= 10:
        if metric == 1:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[lin_weight] kg", 50, 75)  # 160 - 20 padding
                    
                    text "[lin_weight] kg":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#cb0000"
                        size text_size 
                        bold True
        
        else:
            fixed:
                    xsize 150
                    ysize 150
                    xpos 580
                    ypos 850
                    image "gui/girlsstatsweight.png"
                    
                    $ text_size = auto_text_size("[lin_weightlbs] lbs", 50, 75)  # 160 - 20 padding
                    
                    text "[lin_weightlbs] lbs":
                        xoffset 0
                        yoffset 0
                        xalign 0.5
                        yalign 0.75
                        color "#cb0000"
                        size text_size 
                        bold True
    
    fixed:
        xpos 1095 
        ypos 106
        image "gui/girlsstatsbgforstats.png" xpos 0 ypos 0
        image "gui/reputationup.png" xpos 10 ypos 10 xsize 40 ysize 40
        fixed:
            xpos 58 
            ypos 10
            use attitude_stat_bar(lin_attitude, width=260, height=40, min_val=-100, max_val=100)
 

    fixed:
        xpos 321
        ypos 500
        image "gui/girlsstatsbgforstats.png" xpos 0 ypos 0
        image "gui/fullness.png" xpos 10 ypos 10 xsize 40 ysize 40
        fixed:
            xpos 58
            ypos 10
            use fullness_bar(lin_fullness, lin_fullmax, width=261, height=41) 

    $ xposimperial = 515    
    $ yposimperial = 931

    $ xpostextimperial = xposimperial + 29
    $ ypostextimperial = yposimperial + 15

    $ xposmetric = 515
    $ yposmetric = 855

    $ xpostextmetric = xposmetric + 18
    $ ypostextmetric = yposmetric + 15
    
    if metric == 1:
        
        imagebutton:
            auto "gui/roundbutton_%s.png" xpos xposimperial ypos yposimperial action [ Play("sound", "audio/click2.mp3"), Call("imperial") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "I" xpos xpostextimperial ypos ypostextimperial color ("#a1a1a1") size 32
        imagebutton:
            auto "gui/roundbutton_%s.png" xpos xposmetric ypos yposmetric action [ Play("sound", "audio/click2.mp3"), Call("metric") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "M" xpos xpostextmetric ypos ypostextmetric color ("#000000") size 32
    else:
        
        imagebutton:
            auto "gui/roundbutton_%s.png" xpos xposimperial ypos yposimperial action [ Play("sound", "audio/click2.mp3"), Call("imperial") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "I" xpos xpostextimperial ypos ypostextimperial color ("#000000") size 32
        
        imagebutton:
            auto "gui/roundbutton_%s.png" xpos xposmetric ypos yposmetric action [ Play("sound", "audio/click2.mp3"), Call("metric") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "M" xpos xpostextmetric ypos ypostextmetric color ("#a1a1a1") size 32


    fixed:
        xpos 1275
        ypos 540
        image "gui/achievements.png" xsize 90 ysize 90
        hbox:
            xoffset 90
            fixed:
                xsize 90
                ysize 90
                if lin_hikingsuccessfeeding >= 1:
                    image "gui/achivementsbg.png" xpos -3 ypos -3
                    image "gui/cell1.png" ysize 90 xsize 90                                
                    image "gui/hiking1.png" ysize 90 xsize 90
                    image "gui/roundbutton_hover.png" ysize 30 xsize 30 xpos 60 ypos 60
                    $ text_size = auto_text_size("[lin_hikingsuccessfeeding]", 30, 30)  # 160 - 20 padding                     
                    text "[lin_hikingsuccessfeeding]":
                        xoffset 69
                        yoffset 65
                        # xalign 0.5
                        # yalign 0.86
                        color "#000000"
                        size 16 
                        bold True
                    # text "[lin_hikingsuccessfeeding]" color ("#000000") size 16 xpos 70 ypos 65


    # switching WG and sounds buttons
    # imagebutton:
    #     auto "gui/roundbutton_%s.png" xpos 622 ypos 780 action [ Play("sound", "audio/click1.mp3"), Jump("wgswitch") ] hovered [ Play("sound", "audio/button hover2.mp3") ]
    # text "WG" xpos 630 ypos 795 color ("#000000") size 28

screen back():
    imagebutton:
        auto "gui/back_%s.png" xpos 6 ypos 625 action [ Play("sound", "audio/click1.mp3"), Jump("test") ] hovered [ Play("sound", "audio/button hover2.mp3") ]

screen barometer_screen(barometer_value=0):
        # Show scoreboard in the center
        add "gui/scoreboard.png" xalign 0 yalign 0

        # Compute the arrow’s angle
        $ angle = barometer_angle(barometer_value)

        # Show the arrow in front of the scoreboard.
        # We'll place it in the same center, but you can offset with xpos/ypos if needed.
        add Transform("arrow_image", rotate=angle) xoffset 103 yoffset 57

screen linhikefeeding:    

    button:
            xpos 1475
            ypos 530
            xysize (250, 60)

            background Transform("gui/button_wide2.png", alpha=button_wide_alpha)

            action [ Play("sound", "audio/click2.mp3"), Jump("linfeedingscale")]
            hovered [SetVariable('button_alpha', 0.85), Play("sound", "audio/button_hover4.mp3")]
            unhovered SetVariable('button_alpha', 0.65)

            add Transform(
                Text("Feed", bold=True, color="#ffffff", size=22),
                alpha=button_alpha,
                xalign=0.5,
                yalign=0.5,
                yoffset=-5
            )

    button:
            xpos 1475
            ypos 590
            xysize (250, 60)

            background Transform("gui/button_wide2.png", alpha=button_wide_alpha)

            action [ Play("sound", "audio/click2.mp3"), Jump("linhiking")]
            hovered [SetVariable('button_alpha2', 0.85), Play("sound", "audio/button_hover4.mp3")]
            unhovered SetVariable('button_alpha2', 0.65)

            add Transform(
                Text("Stop", bold=True, color="#ffffff", size=22),
                alpha=button_alpha2,
                xalign=0.5,
                yalign=0.5,
                yoffset=-5
            )

    fixed:
        xpos 1500
        ypos 300
        use barometer_screen(linfeedingpressurexsize)
        image "gui/pressure1.png" xpos 65 ypos 130


    fixed:
        xpos 1410
        ypos 459
        image "gui/girlsstatsbgforstats.png" xpos 0 ypos 0
        image "gui/fullness.png" xpos 10 ypos 10 xsize 40 ysize 40
        fixed:
            xpos 58
            ypos 10
            use fullness_bar(lin_fullness, lin_fullmax, width=261, height=41) 

screen _video_player(video_path):
    zorder 1000
    modal True
    
    # This will handle all resolutions automatically
    add Movie(
        play=video_path,
        size=(1920, 1080),  # Base resolution
        xalign=0.5,
        yalign=0.5,
        xfill=True,
        yfill=True
    )
    
    # Optional skip button
    textbutton "Skip":
        xalign 0.95
        yalign 0.95
        action Return()

screen surfbalancetraining():

    # drift + input logic stays the same
    key "K_LEFT"  action SetVariable("balance_pos", clamp(balance_pos - 0.02, 0.0, 1.0))
    key "K_RIGHT" action SetVariable("balance_pos", clamp(balance_pos + 0.02, 0.0, 1.0))
    timer 0.05 repeat True action [ Function(_balance_update, 0.05), NullAction() ]

    
    
    imagebutton:
            idle  "gui/arrow_left_idle.png"
            hover "gui/arrow_left_hover.png"
            action SetVariable("balance_pos", clamp(balance_pos - 0.02, 0.0, 1.0))
            xpos  947 ypos 627
    imagebutton:
        idle  "gui/arrow_right_idle.png"
        hover "gui/arrow_right_hover.png"
        action SetVariable("balance_pos", clamp(balance_pos + 0.02, 0.0, 1.0))
        xpos  1041 ypos  627

    fixed:
        # center it
        xpos 672
        ypos 477   

        add "gui/scale_surfbg.png"
        add "gui/scale_surfbalancebg.png" xpos 10 ypos 68
        
        $ fill_w = int(surfscaleimage_width * balance_pos)        
        
        $ surfbalancecenter_x = int(surfscaleimage_width * balance_pos)
        
        $ surfcrop_x = clamp(surfbalancecenter_x - 2, 0, surfscaleimage_width - 4)
        
        add LiveCrop((surfcrop_x, 0, 4, surfscaleimage_height), "gui/scale_surfbalance.png") xpos surfcrop_x + 10 ypos 68 anchor (0, 0)      

        $ surfminbalancex = surfscaleimage_width * surfscalesweetspotmin
        $ surfmaxbalancex = surfscaleimage_width * surfscalesweetspotmax
        
        add Solid("#0b6b00", xsize=4, ysize=surfscaleimage_height) xpos 295 ypos 69 anchor (0,0)
        add Solid("#0b6b00", xsize=4, ysize=surfscaleimage_height) xpos 438 ypos 69 anchor (0,0)

        add Solid("#810000", xsize=4, ysize=surfscaleimage_height) xpos 81 ypos 69 anchor (0,0)
        add Solid("#810000", xsize=4, ysize=surfscaleimage_height) xpos 652 ypos 69 anchor (0,0)

        

    # 4) Labels above & below
    text "Balance Training" size 36:
        xalign 0.5
        yalign 0.5
        ypos -surfscaleimage_height - 40

    fixed:
        
            
        
        # $ surfscalecrop_right = 714*((balance_timer)/10)    
        pos (682, 536)  # Position on screen where image stays anchored
        $ frac      = clamp(balance_timer / 10.0, 0.0, 1.0)
        $ left_w    = int(714 * frac)

        # 3) Crop only that many pixels from the left of your full‑width image
        add LiveCrop((0, 0, left_w, 7), "gui/balanceresultscale.png")

screen surfwavephase():

    # 1) Update the marker
    timer 0.01 repeat True action Function(_wave_update, 0.01)

    # 2) Click anywhere to attempt a catch
    key "mouseup_1" action Function(wave_catch)

    # add "gui/wavecatchscalebg.png" xpos 297 ypos 272

    fixed:
        # Position this block however you like
        xpos 1500
        ypos 150
        anchor (0, 0)
        add "gui/wavecatchscalebg.png" xpos -3 ypos 120
        # A simple background for your wave bar
        

        # Draw the “catch window” as a green horizontal band
        $ bar_w =  50
        $ bar_h = 300
        $ catch_y1 = int((1 - wave_zone_max) * bar_h)
        $ catch_y2 = int((1 - wave_zone_min) * bar_h)
        add Solid("#8f8", xsize=bar_w, ysize=(catch_y2 - catch_y1)) xpos 10 ypos (150 + catch_y1) anchor (0, 0)

        # Draw the moving marker as a thin red line
        $ marker_y = int((1 - wave_marker) * bar_h)
        add Solid("#f00", xsize=bar_w, ysize=4) xpos 10 ypos (150 + marker_y - 2) anchor (0, 0)

        # Optional: show your “click to catch” hint
        add "gui/clicktocatch2.png" xpos 35 ypos 90 anchor (0.5, 0.5)
        text "Click to catch!" xpos 40 ypos 90 anchor (0.5, 0.5) color "#ffffff" size 19

screen gallery():

    modal True
    tag gallery
    add "gui/vgallery_bg.png" xpos 5 ypos 120
    fixed:
        xpos 1845 ypos 123
        
        imagebutton:
                auto "gui/roundbutton_%s.png" action [ Play("sound", "audio/click2.mp3"), ToggleScreen("gallery"), ToggleScreen("callmap") ] hovered [ Play("sound", "audio/button hover4.mp3") ]
        text "X" xpos 16 ypos 9 color ("#000000") size 40 bold True

    fixed xpos GALLERY_X ypos GALLERY_Y xsize GALLERY_W ysize GALLERY_H:
        
        vbox:
            spacing 20
            text "Unlocked Videos" xalign 0.5 size 32 bold True

            viewport draggable True mousewheel True:
                xmaximum GALLERY_W
                ymaximum GALLERY_H - 80

                vbox spacing 20:

                    # build current‑session girl list on the fly,
                    # so we never crash even if GIRLS were empty
                    $ current_girls = sorted({ v["girl"] for v in VIDEO_DATA
                                               if v["id"] in seen_videos })

                    for girl in current_girls:

                        $ vids = [ v for v in VIDEO_DATA
                                    if v["girl"] == girl and v["id"] in seen_videos ]

                        text GIRL_PRETTY.get(girl, girl.capitalize()) style "gallery_girl_label"

                        # --- NEW: work out rows so the grid never overflows ----------
                        $ rows = (len(vids) + THUMB_COLS - 1) // THUMB_COLS
                        grid THUMB_COLS rows spacing 10:
                            for v in vids:
                                imagebutton:
                                    idle  Transform(v["thumb"], size=(THUMB_W, THUMB_H))
                                    hover Transform(v["thumb"], size=(THUMB_W, THUMB_H))
                                    action Function(play_from_gallery, v)

style gallery_girl_label:
    size     24
    bold     True
    ypadding 8
