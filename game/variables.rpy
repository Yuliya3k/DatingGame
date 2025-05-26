label variables:    

   

    call kira

    call kris  

    call alexa

    call lin

    call margo
    
    call girl

    call imgindex

    define player = Character("[name]")

    default calendar = Calendar(1, 7, 0, 1, 0, 0, ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

    define slowdissolve = Dissolve(.5)

    
    
    default position = "home"     

    default wg = 1

    default metric = 1

    default endgame = 0

    default goodwork = 0   

    default sevent = 0 

    default daytime = 18

    default gamerunning = 1

    default money = 1000 
    
    default invpos = 1  

    default myrandom = renpy.random.randint(0,1)

    default alexafirsttime = 0

    default krisfirsttime = 0
    
    

    default hayoonfirsttime = 0

    default training = 0

    default alexa_bloatask = 0

    default overallpeople = 0

    default hayoonintro = 0

    default avaintro = 0

    default linintro = 0

    default sallyintro = 0

    default usual = 0

    default towninfo = 0

    default mapishere = 0

    default pointerpose = 0

    default scaleactive = 0

    default x = 562

    default y = 321

    default poiterforward = 1

    default rmclients = 0

    # default monthworkresulthours = 0

    default dayworkresult = 0

    default workresult = 0

    default workreputation = 0

    default cooksalaryperhour = 7
    
    default dayworksuccessfulhours = 0    

    default cookingskill = float(10.1)

    default salarystatus = float(0.1)

    default cookingstatus = "none"
    
    default daysalary = float(cooksalaryperhour*dayworksuccessfulhours)

    default monthsalary = 0

    default rightpan = 1

    default leftpan = 1

    default rmclienttalk = "mrsanderson"

    default marshmallowraw = 0

    default marshmallowslight = 0

    default marshmallowmedium = 0

    default marshmallowmuch = 0

    default marshmallowpos = 1

    default marshmallowstate = 1

    default stop = 0

    default cooking = 0

    default promcafe = 0

    default parknothing = 0

    default promcafetoday = 0


    default hospitalhi = 0

    default hayoonfasteater = 1

    default hayoonrandome = 0


    default iced_tea = 0
    default water_bottle = 0
    default smoothie_drink = 0


    default mapbuttonisactive = True
    default youarehome = False

    

    
    

    # $ my_idle = button_idle(250, 60, 15, "#003300", "#222222", "End shift", "#FFFFFF")
    # $ my_hover = button_hover(250, 60, 15, "#005500", "#222222", "End shift", "#FFFFFF")
    # default scalecrop_x = 0
    # default scalecrop_y = 0
    # default scalecrop_width = 250
    # default scalecrop_height = 100
    default scalecrop_right = 0  # Starts fully visible (0 = no crop)
    default scalecrop_speed = 10 # Pixels to crop/reveal per click
    default scaleimage_width = 658
    default scaleimage_height = 59
    default scaleline_color = "#053f00"
    default scaleline_x1 = int(scaleimage_width * 0.75 - cookingskill)
    default scaleline_y1 = 0
    default scaleline_x2 = int(scaleimage_width * 0.75 + cookingskill)
    default scaleline_y2 = 0
    default scalepos_x = 568
    default scalepos_y = 400
    default scalesweetspotmin = 0
    default scalesweetspotmax = 0
    default button_alpha = 0.65
    default button_alpha2 = 0.65
    default button_alpha3 = 0.65
    default button_wide_alpha = 0.65
    default scalepositioncoefficient = 0.75

    default fill_w = 0
    default surfscaleimage_width = 714
    default surfscaleimage_height = 58
    default balance_pos = 0
    default surfbalancecenter_x = 0
    default surfscaleline_color = "#016d0e"
    default surfscalesweetspotmin = 0.4
    default surfscalesweetspotmax = 0.6
    default surfcrop_x = 0
    default surfminbalancex = surfscaleimage_width * surfscalesweetspotmin
    default surfmaxbalancex = surfscaleimage_width * surfscalesweetspotmax

    default wavesuccess = False
    default wavefail = False
    default wavesoso = False

    default speech = 0


    default screennotification = ""
    default notify_active = False

    default negativemessage = "Problem"
    default positivemessage = "Success"
    default neutralmessage = "Neutral"
    default message = "Message"


    default balancesuccess = False
    default balancesoso = False
    default balancefail = False
    default balacesuccessfirsttime = False

    transform flicker_effect(min_alpha=0.8, cycle_time=1.0):
        alpha 1.0
        ease cycle_time alpha min_alpha
        ease cycle_time alpha 1.0
        repeat

    default niimage = "nihayoon"
    default nigirlimage = "nihayoon"

    default reputationchange = 0
    default fullnesschange = 0
    default calorieschange = 0

    image arrow_image:
        "gui/arrow.png"
        # We assume the pivot is visually at the bottom center in the arrow image
        anchor (0.5, 1)



    
    default lin_belly_accept  = False
    default lin_belly_visible = False
    default notenoughmoney = False
    default moneytoadd = 0

    default _seen_health = False
    default _seen_history = False
    default _seen_bodyintro = False
    default _seen_fit_healthy = False
    default _seen_fit_goodlooking = False
    default _seen_fit_highenergy = False
    default _seen_fat_intro = False
    default _seen_belly_intro = False
    default _preg_right_answer = False
    default _fbarebaspreg = False
    default _dynamicbellies = False
    default _fitpeople = False
    
    default seen_videos = set()

    default joggingmotivationchange = 0
    default fitnessstate = 0
    default fitnessstatechange = 0
    default numberofsips = 0


    default hayoonmettoday = False

    # define THUMB_W      = 260          # width  of each thumb (px)
    # define THUMB_H      = 146          # height of each thumb (px)
    # define THUMB_COLS   = 4            # columns per row
    # define GALLERY_X    = 60           # top‑left corner
    # define GALLERY_Y    = 120
    # define GALLERY_W    = 1160         # viewport size
    # define GALLERY_H    = 820



    # define GIRL_PREFIXES = [
    #     "alexa", "ava", "aurora", "hayoon", "kira", "kris",
    #     "lin", "margo", "mindy", "sally", "julia",
    # ]


    # define GIRL_PRETTY = {
    #     "alexa": "Alexa",
    #     "ava":   "Ava",
    #     "aurora":"Aurora",
    #     "hayoon":"Hayoon",
    #     "kira":  "Kira",
    #     "kris":  "Kris",
    #     "lin":   "Lin",
    #     "margo": "Margo",
    #     "mindy": "Mindy",
    #     "sally": "Sally",
    #     "julia": "Julia",
    #     "other": "Misc.",
    # }
    return




    # $ position = "sallyparkmorningrunninginitisltalk"
    # call sceneimg
    # $ position = "sallyparkmorningafterrunningbreathinghard"
    # call sceneimg
    # $ position = "sallyparkmorningafterrunningsatisfied"
    # call sceneimg
    # $ position = "sallyparkmorningafterrunningsurprised"
    # call sceneimg
    # $ position = "sallyparkmorningrunningbackward"
    # call sceneimg
    # $ position = "sallyparkmorningrunningbreathinghard"
    # call sceneimg
    # $ position = "sallyparkmorningrunningbreathingsoft"
    # call sceneimg
    # $ position = "sallyparkmorningrunningforward"
    # call sceneimg
    # $ position = "sallyparkmorningrunninglisteningtalk"
    # call sceneimg
    # $ position = "sallyparkmorningrunningtalkingtalk"
    # call sceneimg
    
    # $ position = "parksallyseaviewmorninglistening"
    # call sceneimg 
    # $ position = "parksallyseaviewmorningtalking"
    # call sceneimg