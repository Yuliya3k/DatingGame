label sceneimg:
    call girl
    scene blankbg
    # hide kira
    # hide kris
    # hide alexa
    if position == "home":
        scene bg


    #Kira
    if position == "kiraworking" or position == "kiraworking2" or position == "kiraquestion" or position == "kiraflirting" or position == "kiraexplain" or position == "kiraenterance" or position == "kiraquestion2" or position == "kirahayoonenter"  or position == "kiraleaningtohayoon" or position == "kiraleaningwhispering":        
        scene bg
        show kira

    #Alexa
    if position == "alexaexplaining" or position == "alexaworking" or position == "alexahappy" or position == "alexasurprised" or position == "alexaskingtable" or position == "cafeenteranceavaalexafar" or position == "cafeenteranceavaalexacloser":
        scene bg
        show alexa


    #Ava
    if position == "cafeenteranceavaalexafar" or position == "cafeenteranceavaalexacloser" or position == "avawalkingout" or position == "beachavaclosehey" or position == "beachavacloselisten" or position == "beachavaclosemynameis" or position == "beachavacloseplease" or position == "beachavaclosestop" or position == "beachavaclosetalk" or position == "beachavaclose" or position == "beachava" or position == "cafeavaorderingside" or position == "cafeavasitting" or position == "beachavacloseexplaining":
        scene bg
        show ava


    #hayoon
    if position == "barhayoonlecturing" or position == "barhayoonchatting" or position == "barhayoonclarifiying" or position == "barhayoonexplaining" or position == "barhayoonhey" or position == "barhayoonstop" or position == "barhayoonwhat" or position == "kirahayoonenter":
        scene bg
        show hayoon

    if position == "krisexplaining" or position == "krishi" or position == "krisshy" or position == "kriswalking" or position == "kriswalkingbalcony" or position == "krisbackyardeating" or position == "krisbackyardhello" or position == "krisbackyardsmiling" or position == "krisbackyardsmilingslightly" or position == "krisbackyardtalking":
        scene bg
        show kris

    if position == "auroragardening" or position == "aurorahello" or position == "aurorahey" or position == "auroraiwish" or position == "auroragardeningbalcony" or position == "auroraexplain":
        scene bg
        show aurora

    if position == "linhi" or position == "linhmm" or position == "linletsdoit" or position == "linlistening" or position == "linexplaining":
        scene bg
        show lin

    if position == "margohismile" or position == "margormexplaining" or position == "margormgoodluck" or position == "margormlistening" or position == "margormpointing" or position == "margormserious" or position == "margormtalking" or position == "margormstandingwhilecooking" or position == "margoeatingleftovers":
        scene bg
        show margo


    if position == "rmjuliasit":
        scene bg
        show julia

    if position == "backyard" or position == "gardeningbalconynoaurora" or position == "kriswalkingbalconynokris" or position == "foodburger" or position == "foodburgerfrappe" or position == "foodfrappe" or position == "foodnofood" or position == "cafeenterance" or position == "barenterance" or position == "hayoonintro" or position == "linintro" or position == "avaintro" or position == "sallyintro" or position == "parkocean" or position == "parkwalk" or position == "parkbench" or position == "kitchen"  or position == "beachempty" or position == "beachlifeguardempty":
        scene bg
        
    
return