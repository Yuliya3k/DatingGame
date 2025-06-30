label start:

    


    call variables
    
    # First, define default or define for your variables
   

    # Define the transform in normal Ren'Py code
    transform notify_anim(start_y=0.1, end_y=0.1, fade_in=0.5, wait=1, fade_out=0.5):
        ypos start_y
        alpha 0.0
        ease fade_in ypos end_y alpha 1.0
        pause wait
        ease fade_out alpha 0.2

    # Define the screen in normal Ren'Py code
    

    init python:
        import os, store
        import random
        import math

        # ------------------------------------------------------------------
        # 1) discover thumbnails in game/videos/*.png
        # ------------------------------------------------------------------
        thumbs = [f for f in renpy.list_files(common=False)
                if f.startswith("videos/") and f.lower().endswith(".png")]

        # map file‑prefix → girl
        def guess_girl(vid_id):
            for g in GIRL_PREFIXES:
                if vid_id.lower().startswith(g):
                    return g
            return "other"

        store.VIDEO_DATA = [
            {
                "id":    (vid_id := os.path.splitext(os.path.basename(full))[0]),
                "girl":  guess_girl(vid_id),
                "thumb": full,                       # videos/xxx.png
                "video": f"videos/{vid_id}.webm",
            }
            for full in thumbs
        ]
        store.GIRLS = GIRL_PREFIXES      # keeps your chosen order

        # ------------------------------------------------------------------
        # 2) hook movie_cutscene → mark video as seen (per‑game variable)
        # ------------------------------------------------------------------
        _real_cut = renpy.movie_cutscene

        def _hook(fn, *a, **kw):
            vid = os.path.splitext(os.path.basename(fn))[0]
            seen_videos.add(vid)
            return _real_cut(fn, *a, **kw)

        renpy.movie_cutscene = _hook

        # ------------------------------------------------------------------
        # 3) helper to play from gallery without nested‑UI error
        # ------------------------------------------------------------------
        def play_from_gallery(entry):
            renpy.hide_screen("gallery")
            renpy.invoke_in_new_context(renpy.movie_cutscene, entry["video"])
            renpy.show_screen("gallery")
            

            _music_paused = False

        def pause_music():
            """
            Pause whatever is on the standard 'music' channel and remember
            that we did so, but only if a track is really playing.
            """
            global _music_paused
            if renpy.music.get_playing("music"):
                renpy.music.set_pause(True, channel="music")
                _music_paused = True
            else:
                _music_paused = False           # nothing to resume later

        def resume_music():
            """
            Resume the channel only if we actually paused it on entry.
            """
            global _music_paused
            if _music_paused:
                renpy.music.set_pause(False, channel="music")
                _music_paused = False

        
        def check_scheduled_calls():
            _jump_event = None
            _event_day = None
            for ev in scheduled_calls:
                if ev[0] == calendar.TotalDays:
                    _jump_event = ev[1]
                    _event_day = ev[0]
                    scheduled_calls.remove(ev)
                    break

            if _jump_event:
                if _jump_event == "phone_goal_check":
                    global last_call_person, last_call_goal
                    last_call_person, last_call_goal = phone_goal_details.pop(
                        _event_day, (None, None)
                    )
                renpy.call_in_new_context(_jump_event)
                return True
            return False
        
        # this does not work at all, it does not hide the dialogue menu for example, that makes all game look like buggy shit
        def show_map_unless_event():
            """Display the map unless an event is scheduled."""
            if not check_scheduled_calls():
                renpy.show_screen("map", _layer="transient")


        # === WAVE CATCH PARAMETERS ===
        wave_zone_min = 0.4
        wave_zone_max = 0.6
        wave_speed    = 1.2    # cycles per second for the marker

        # State variables (reset in the label)
        wave_time    = 0.0
        wave_marker  = 0.0
        wave_streak  = 0
        wave_fail    = False

        def _wave_update(dt):
            """
            Called by the 'wave' screen timer. Oscillates wave_marker
            between 0 and 1 using a sine wave.
            """
            global wave_time, wave_marker
            wave_time += dt
            wave_marker = 0.5 + 0.5 * math.sin(2 * math.pi * wave_speed * wave_time)

        def wave_catch():
            """
            Called on each click. Checks if the marker is inside the
            catch window. Advances streak or fails outright, and shows
            a lower‐screen success notification.
            """
            global wave_streak, wave_fail

            # if we’ve already failed or finished, do nothing
            if wave_fail or wave_streak >= 3:
                return

            # choose new y‐positions
            # default start_y=0.6, end_y=0.45 → +0.07 shifts down about 50px on 720px screen
            low_start = 0.67
            low_end   = 0.52


            if wave_zone_min <= wave_marker <= wave_zone_max:
                wave_streak += 1
                notify_success(
                    "Good catch! {}/3".format(wave_streak),
                    start_y=low_start,
                    end_y=low_end,
                )
            else:
                wave_fail = True
                notify_success(
                    "Missed the wave!",
                    start_y=low_start,
                    end_y=low_end,
                )



        # size of your scale image in pixels
        surfscaleimage_width  = 714
        surfscaleimage_height = 58

        # fraction of the bar that is the green zone
        surfscalesweetspotmin = 0.4
        surfscalesweetspotmax = 0.6

        # color of the boundary lines
        surfscaleline_color   = "#00a000"

        def clamp(x, lo, hi):
            return min(hi, max(lo, x))

        def _balance_update(dt):
            global balance_pos, balance_timer

            # board drifts randomly
            drift = random.uniform(-0.9, 0.9) * dt
            balance_pos = clamp(balance_pos + drift, 0.0, 1.0)

            # if in green zone, count up
            if 0.4 < balance_pos < 0.6:
                balance_timer += dt

        def play_fullscreen_video(video_path):
            renpy.scene()
            renpy.show_screen("_video_player", video_path)
            renpy.pause()
        
        from renpy.text import text as rtext  # import the Text class

        def barometer_angle(value):
            """
            Returns an angle (in degrees) for the arrow,
            given a pressure or 'value' in range [0..500].
            0 => -90°, 500 => +90°
            """
            # Clamp value so it never exceeds 0..500
            value = max(0, min(value, 500))

            # Convert the [0..500] range to [-90..+90] degrees
            # slope = (endAngle - startAngle) / 500 = 180 / 500 = 0.36
            angle = -90 + (value * 180.0 / 500.0)
            return angle

        def get_fill_crop(value, max_value, full_width, full_height):
            """
            Given a 'value' (0 <= value <= max_value),
            returns a LiveCrop rectangle (x, y, width, height).
            If value=0 -> width=0 (fully cropped),
            If value=max_value -> width=full_width (fully uncropped).
            """
            # Avoid division-by-zero if max_value is 0.
            if max_value == 0:
                ratio = 0
            else:
                ratio = float(value) / float(max_value)
            
            # Clamp ratio to [0, 1] just in case.
            ratio = max(0.0, min(1.0, ratio))

            # Crop width is ratio of the total width.
            crop_width = int(full_width * ratio)

            # Crop from the left edge to crop_width, full height.
            return (0, 0, crop_width, full_height)



        # Compute cropping rectangle based on stat (–100 to 100)
        def get_stat_crop(stat, full_width, full_height):
            
            normalized = stat / 100.0  # Convert to range -1 to 1.
            center = full_width / 2.0
            if normalized >= 0:
                crop_x = center
                crop_width = center * normalized
            else:
                crop_width = center * abs(normalized)
                crop_x = center - crop_width
            return (int(crop_x), 0, int(crop_width), full_height)

        
        def get_x_for_stat(stat, min_val, max_val, width):
            """
            Convert 'stat' in [min_val..max_val] into an x-position in [0..width].
            For example, if min_val=-100, max_val=100, width=260:
            -100 => x=0
            0   => x=130
            100 => x=260
            """
            # Avoid division by zero:
            if max_val == min_val:
                return 0
            # Clamp the stat so we don't go off the bar:
            if stat < min_val:
                stat = min_val
            if stat > max_val:
                stat = max_val

            # Fraction from 0.0 to 1.0:
            fraction = float(stat - min_val) / float(max_val - min_val)
            return int(width * fraction)


        def auto_text_size(text, max_width, max_height, max_size=120, min_size=6):
            text = str(text)  # ensure we have a string
            test_size = max_size
            while test_size > min_size:
                # Create a Text displayable with the given font size.
                txt = rtext.Text(text, size=test_size)
                # Render the text with both width and height constraints.
                r = txt.render(max_width, max_height, 0, 0)
                # Check if both width and height are within bounds.
                if r.width <= max_width and r.height <= max_height:
                    return test_size
                test_size -= 1
            return min_size


        def notify_success(
                message,
                start_y=0.5,
                end_y=0.15,
                fade_in=0.5,
                wait=0,
                fade_out=0.5,
                text_size=28,
                text_bold=True
            ):

            renpy.show_screen(
                "success_notification_screen",
                message=message,
                start_y=start_y,
                end_y=end_y,
                fade_in=fade_in,
                wait=wait,
                fade_out=fade_out,
                text_size=text_size,
                text_bold=text_bold
            )
            # No invoke_in needed now!
            # renpy.call_in_new_context("hide_notification_label", "success_notification_screen", duration)


        def notify_warning(
                message,
                start_y=0.6,
                end_y=0.4,
                fade_in=0.5,
                wait=1.5,
                fade_out=0.5,
                text_size=28,
                text_bold=True
            ):
            renpy.show_screen(
                "warning_notification_screen",
                message=message,
                start_y=start_y,
                end_y=end_y,
                fade_in=fade_in,
                wait=wait,
                fade_out=fade_out,
                text_size=text_size,
                text_bold=text_bold
            )
            # Hide automatically after total duration
            duration = fade_in + wait + fade_out
            renpy.invoke_in(duration, renpy.hide_screen, "warning_notification_screen")

        def notify_error(
                message,
                start_y=0.6,
                end_y=0.4,
                fade_in=0.5,
                wait=1.5,
                fade_out=0.5,
                text_size=28,
                text_bold=True
            ):
            renpy.show_screen(
                "error_notification_screen",
                message=message,
                start_y=start_y,
                end_y=end_y,
                fade_in=fade_in,
                wait=wait,
                fade_out=fade_out,
                text_size=text_size,
                text_bold=text_bold
            )
            # Hide automatically after total duration
            duration = fade_in + wait + fade_out
            renpy.invoke_in(duration, renpy.hide_screen, "error_notification_screen")


        def notify(
                message,
                xpos=0.5,
                start_y=0.6,
                end_y=0.4,
                fade_in=0.5,
                wait=1.5,
                fade_out=0.5,
                text_size=28,
                text_color="#FFFFFF",
                text_bold=True
            ):

            # Show the notification screen with all parameters
            renpy.show_screen(
                "notification_screen",
                message=message,
                xpos=xpos,
                start_y=start_y,
                end_y=end_y,
                fade_in=fade_in,
                wait=wait,
                fade_out=fade_out,
                text_size=text_size,
                text_color=text_color,
                text_bold=text_bold
            )

            # Automatically hide the screen after total animation duration
            duration = fade_in + wait + fade_out
            renpy.invoke_in(duration, renpy.hide_screen, "notification_screen")

        def update_pointer():
            if renpy.store.scaleactive == 1:
                if renpy.store.x >= 1190:
                    renpy.store.poiterforward = 0
                if renpy.store.x <= 562:
                    renpy.store.poiterforward = 1
                
                if renpy.store.x < 1190 and renpy.store.poiterforward == 1:
                    renpy.store.x += 10
                if renpy.store.x > 562 and renpy.store.poiterforward == 0:
                    renpy.store.x -= 10

        def update_pointer():
            if renpy.store.scaleactive == 1:
                if renpy.store.x >= 1190:
                    renpy.store.poiterforward = 0
                if renpy.store.x <= 562:
                    renpy.store.poiterforward = 1
                if renpy.store.x < 1190 and renpy.store.poiterforward == 1:
                    renpy.store.x += 10
                if renpy.store.x > 562 and renpy.store.poiterforward == 0:
                    renpy.store.x -= 10

        # image dynamic_ellipse = DynamicDisplayable(dynamic_ellipse)

        # screen example_ellipse():
        #     # Position it in the center, for example.
        #     add "dynamic_ellipse" xalign 0.5 yalign 0.5
        #     text "Dynamic Ellipse Example" xalign 0.5 yalign 0.7
        
        # gamerunning = 1
        # position = "home"

        # labelvariable = "sceneimg"
        
        # while gamerunning == 1:
        #     renpy.call(labelvariable)

        # renpy.call("sceneimg")

        # function to hide all girls stats screens
        def close_all_stats():
            global mapishidden
            mapishidden = 0
            renpy.hide_screen("avastats")
            renpy.hide_screen("hayoonstats")
            renpy.hide_screen("sallystats")
            renpy.hide_screen("linstats")
            renpy.hide_screen("statsgirls")

        class Calendar(object):
            def __init__(self, totaldays, hours, day, days, month, minutes, months, monthdays, weekday):
                self.totaldays = totaldays
                self.hours = hours
                self.day = day
                self.days = days
                self.month = month
                self.minutes = minutes
                self.months = months

                self.monthdays = monthdays
                self.weekday = weekday

            @property
            def Month(self):
                return self.months[self.month]

            @property
            def Time(self):
                return str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2) #+ " " + self.monthdays[self.month]

            @property
            def WeekDay(self):
                return self.weekday[self.day]

            @property
            def TotalDays(self):
                return self.totaldays

            @property
            def Days(self):
                return self.days

            @property
            def MonthDays(self):
                return self.monthdays

            @property
            def Hours(self):
                return self.hours



            def AddMinutes(self, minutes):
                self.minutes += minutes
                if self.minutes > 59:
                    self.minutes = self.minutes - 60
                    self.hours += 1


                if self.hours > 23:
                    self.hours = self.hours - 24
                    self.day += 1
                    self.days += 1
                    self.totaldays += 1

                if self.day > 6:
                    self.day = 1

                if self.days > self.monthdays[self.month]:
                    self.month += 1
                    self.days = 0
                if self.month > 11:
                    self.month = 0
                # return
            def AddHours(self, hours):
                self.hours += hours

                if self.minutes > 59:
                    self.minutes = self.minutes - 60
                    self.hours += 1


                if self.hours > 23:

                    self.hours = self.hours - 24
                    self.day += 1
                    self.days += 1
                    self.totaldays += 1

                if self.day > 6:
                    self.day = 1

                if self.days > self.monthdays[self.month]:
                    self.month += 1
                    self.days = 1
                if self.month > 11:
                    self.month = 1
                # return
            def AddDays(self, days):
                self.days += days
                self.totaldays += days
                self.day += days

                if self.minutes > 59:
                    self.minutes = self.minutes - 60
                    self.hours += 1


                if self.hours > 23:
                    self.hours = self.hours - 24
                    self.day += 1
                    self.days += 1
                    self.totaldays += 1

                if self.day > 6:
                    self.day = 0

                if self.days > self.monthdays[self.month]:
                    self.month += 1
                    self.days = 1

                if self.month > 11:
                    self.month = 1
                # return

            # def AddDay(self, days):
            #     self.days += days
            #     self.totaldays += days
            #     self.hours = 18
            #     self.minutes = 0
            #     if self.minutes > 59:
            #         self.minutes = self.minutes - 60
            #         self.hours += 1


            #     if self.hours > 23:
            #         self.hours = self.hours - 24
            #         self.day += 1
            #         self.days += 1
            #         self.totaldays += 1

            #     if self.day > 6:
            #         self.day = 1

            #     if self.days > self.monthdays[self.month]:
            #         self.month += 1
            #         self.days = 1
            #     if self.month > 11:
            #         self.month = 1



        ###############################

    show screen day_icon
    # show screen gallery_bg
    


label startloop:
    # $ play_fullscreen_video("images/walkingtest.mp4")
    # # $ renpy.pause(10)  # Duration or until skipped
    # # hide screen video_player
    
    # $ renpy.movie_cutscene("videos/home.webm")
    

    $ position = "home"
    scene bg
    "This is a belly stuffing game"
    menu:

        "I'm in and 18+":
            "Great, continue!"

            python:
                name = renpy.input("What's your name?")

                name = name.strip() or "The Feeder"

        "No I'm not into this or I'm under 18 years old":
            "Sorry, the game is over for you!"
            $ renpy.quit()
    window hide
    show text "{color=#ffffff}{size=200} Choose your way {/size}{/color}" at truecenter
    with slowdissolve
    pause 3
    hide text
    with slowdissolve
    pause 1  



    label choosetheway:
        menu:
        
            "[name]'s Culinary journey":
                
                jump culinarystart

            "[name]'s Adventurous Spirit":
                "Not yet"

            "[name]'s Professional journey (IT digital nomad)":
                "Not yet"

            "[name]'s Philanthropic Endeavors":
                "Not yet"
        jump choosetheway  

        
    

    jump startloop

    return
