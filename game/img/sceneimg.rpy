label sceneimg:
    call girl
    scene blankbg
    # hide kira
    # hide kris
    # hide alexa
    # if position == "home":
    #     scene bg


    #Kira
    if position == "kiraworking" or position == "kiraworking2" or position == "kiraquestion" or position == "kiraflirting" or position == "kiraexplain" or position == "kiraenterance" or position == "kiraquestion2" or position == "kirahayoonenter"  or position == "kiraleaningtohayoon" or position == "kiraleaningwhispering":        
        scene bg
        show kira

    #Alexa
    if position == "alexaexplaining" or position == "alexaworking" or position == "alexahappy" or position == "alexasurprised" or position == "alexaskingtable" or position == "cafeenteranceavaalexafar" or position == "cafeenteranceavaalexacloser":
        if position == "alexaworking" and alexa_fullstage == 10 and alexa_weightstage == 1:
            $ renpy.movie_cutscene("videos/alexaworking10.webm")
        if position == "alexaexplaining" and alexa_fullstage == 10 and alexa_weightstage == 1:
            $ renpy.movie_cutscene("videos/alexaexplaining10.webm")
        
        scene bg
        show alexa


    #Ava
    if position == "cafeenteranceavaalexafar" or position == "cafeenteranceavaalexacloser" or position == "avawalkingout" or position == "beachavaclosehey" or position == "beachavacloselisten" or position == "beachavacloseexplaining" or position == "beachavacloseplease" or position == "beachavaclosestop" or position == "beachavaclosetalk" or position == "beachavaclose" or position == "beachava" or position == "cafeavaorderingside" or position == "cafeavasitting" or position == "beachavacloseexplaining" or position == "avabeachsufringfar" or position == "avabeachsurflearningsmilingfullbody" or position == "avabeachaftersurfingfrontstand" or position == "avastandsthirstyside" or position == "avastandsbellylook" or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "...":
        if position == "beachavaclose"  and ava_fullstage == 1 and ava_weightstage == 1:
            $ renpy.movie_cutscene("videos/avabeachclose1.webm")

        if position == "avabeachaftersurfingfrontstand" and ava_weightstage == 1 and ava_fullstage == 10:
            $ renpy.movie_cutscene("videos/avabeachaftersurfingfrontstand10.webm")
            return
        
        
        
        scene bg
        show ava

    if position == "avabeachsurfclosetalking" or position == "avabeachsurfcloselistening" or position == "avabeachsurfclosesmiling" or position == "avabeachsurflearningthmbup" or position == "avabeachsurflearningsoso" or position == "avabeachsurflearninglistening" or position == "avabeachsurflearningtalking" or position == "avabeachsurflearningsmilingfromabove" or position == "avaaftersurfingdrinkingclose" or position == "avaaftersurfingtalkingclose" or position == "avaaftersurfinglisteningclose" or position == "avaaftersurfingsurprisedclose" or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "...":
        if position == "avabeachsurfcloselistening" and ava_weightstage == 1:
            $ renpy.movie_cutscene("videos/avabeachsurtlisten1.webm")
        scene bg
        show avadia


    #Sally
    if position == "parksallybencheveninghi" or position == "parksallybencheveninglistening" or position == "parksallybencheveningsitting" or position == "parksallybencheveningstanding" or position == "parksallybencheveningtalking" or position == "parksallyeveninglookingatthesea" or position == "parksallyeveningwalking" or position == "parksallyeveningwalkingback" or position == "parksallymorningrunning" or position == "parksallymorningrunningback" or position == "parksallyseaviewmorninglistening" or position == "parksallyseaviewmorningtalking" or position == "sallyeveningbellyholding" or position == "sallymorningseaviewbellyholding":
        scene bg
        show sally


    #hayoon
    if position == "barhayoonlecturing" or position == "barhayoonchatting" or position == "barhayoonclarifiying" or position == "barhayoonexplaining" or position == "barhayoonhey" or position == "barhayoonstop" or position == "barhayoonwhat" or position == "kirahayoonenter" or position == "randomencounterhayoon" or position == "hayoonhospitalleaning1" or position == "hayoonhospitalleaning2" or position == "hayoonhospitalstretching" or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "...":
        if position == "hayoonhospitalleaning1" and hayoon_fullstage == 1 and hayoon_weightstage == 1: 
            $ renpy.movie_cutscene("videos/hayoonhospitalleaning1.webm")
        
        scene bg
        show hayoon

    if position == "randomencounterhayoonclose" or position == "randomencounterhayooncloselisten" or position == "randomencounterhayoonclosetalk" or position == "hayoonhospitaltalklisten" or position == "hayoonhospitaltalktalk" or position == "hayoonhospitaltalkhello" or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "...":
        if position == "randomencounterhayoonclose" and hayoon_weightstage == 1:
            $ renpy.movie_cutscene("videos/hayoonrandomencounterclose1.webm")
        scene bg
        show hayoondia

    if position == "krisexplaining" or position == "krishi" or position == "krisshy" or position == "kriswalking" or position == "kriswalkingbalcony" or position == "krisbackyardeating" or position == "krisbackyardhello" or position == "krisbackyardsmiling" or position == "krisbackyardsmilingslightly" or position == "krisbackyardtalking":
        if position == "krisbackyardtalking" and kris_weightstage == 1 and kris_fullstage == 10:
            $ renpy.movie_cutscene("videos/krisstuffedbackyard110.webm")
        scene bg
        show kris

    if position == "auroragardening" or position == "aurorahello" or position == "aurorahey" or position == "auroraiwish" or position == "auroragardeningbalcony" or position == "auroraexplain":
        scene bg
        show aurora


    # Lin
    if position == "linhi" or position == "linhmm" or position == "linletsdoit" or position == "linlistening" or position == "linexplaining" or position == "parklinrunning" or position == "parklinrunningthrough" or position == "parklintalkhi" or position == "parklintalklisten" or position == "parklintalktalk" or position == "parkpromcafelincomingin" or position == "linbikeparkridingstanding" or position == "linbikeparkmeeting" or position == "linbikeparkridingsitting" or position == "..." or position == "linhikingwalking" or position == "linpromcafebellyview" or position == "linhikingcampfirebellyview" or position == "linhikingcampfireendoffeeding" or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "...":
        if position == "linhikingcampfireendoffeeding" and lin_weightstage == 1 and lin_fullstage == 10:
            $ renpy.movie_cutscene("videos/Linafterstuffing10.webm")
        
        scene bg
        show lin

    #Lin talks
    if position == "parkpromlincafesittingeating" or position == "parkpromlincafesittinglistening" or position == "parkpromlincafesittingtalking" or position == "linhikingtalklisten" or position == "linhikinghi" or position == "linhikingcampfiretalkmouthopen" or position == "linhikingcampfiretalkeatingmmm" or position == "linhikingcampfirelookingatthebellytalk" or position == "linhikingcampfiretalklisten" or position == "linhikingcampfirevomiting" or position == "linhikingno" or position == "linhikingtalk" or position == "linhikingtalksmiling" or position == "linhikingtalksurprised" or position == "linhikingcampfiretalkeating" or position == "linhikingcampfiretalktalk" or position == "linpromcafesittingtalkhappyhi" or position == "linpromcafesittingtalkangry" or position == "linhikingcampfiretalkabouttovomit" or position == "linbikeparktalkclose" or position == "linbikeparklisteningclose" or position == "linbikeparkeatinicecream1clean" or position == "linbikeparkeatinicecream2clean" or position == "linbikeparkeatinicecream1dirty" or position == "linbikeparkeatinicecream2dirty" or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "...":
        scene bg
        show lindia
    

    # Mindy
    if position == "parkmindycafeenterance":
        scene bg
        show mindy


        

    if position == "margohismile" or position == "margormexplaining" or position == "margormgoodluck" or position == "margormlistening" or position == "margormpointing" or position == "margormserious" or position == "margormtalking" or position == "margormstandingwhilecooking" or position == "margoeatingleftovers":
        scene bg
        show margo


    if position == "rmjuliasit":
        scene bg
        show julia

    if position == "backyard" or position == "gardeningbalconynoaurora" or position == "kriswalkingbalconynokris" or position == "foodburger" or position == "foodburgerfrappe" or position == "foodfrappe" or position == "foodnofood" or position == "cafeenterance" or position == "barenterance" or position == "hayoonintro" or position == "linintro" or position == "avaintro" or position == "sallyintro" or position == "parkocean" or position == "parkwalk" or position == "parkbench" or position == "kitchen"  or position == "beachempty" or position == "beachlifeguardempty" or position == "parkeveningwalk" or position == "parkeveningseaview" or position == "parkeveningbench" or position == "parkmorningseaview" or position == "parkmorningwalk" or position == "parkmorningbench" or position == "parkpromcafeempty" or position == "linbikeparklisteningclose" or position == "linbikeparktalkclose" or position == "linhikingtalklisten" or position == "linhikingno" or position == "linhikingtalk" or position == "linhikingyes" or position == "hospitalempty" or position == "playerswimming" or position == "layingonthebeach" or position == "playerinthewater" or position == "playerisfalling" or position == "playertryingtostand" or position == "playerswimming" or position == "home" or position == "playerinbalance" or position == "icecreamlisten" or position == "icecreamtalk" or position == "icecreamthumbsup" or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "..." or position == "...":
        if position == "home":
            play music "audio/countryside_birds.mp3" volume 0.3

        scene bg
        

        
        
        
    return