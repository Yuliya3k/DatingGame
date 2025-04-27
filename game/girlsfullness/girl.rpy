label girl:

    call imgindexruntime
    

    if kira_fullness > kira_fullmax:
        $ kira_fullness = kira_fullmax
    $ kira_fullnessoz = int(kira_fullness*0.034)  
    $ kira_fullstage = int(kira_fullness/kira_minfullness)
    if kira_fullstage <= 0:
        $ kira_fullstage = 1
    if kira_fullstage > 10 and sevent == 0:
        $ kira_fullstage = 10
    if kira_fullstage > 20 and sevent == 1:
        $ kira_fullstage = 20


    if kris_fullness > kris_fullmax:
        $ kris_fullness = kris_fullmax
    $ kris_fullnessoz = int(kris_fullness*0.034) 
    $ kris_fullstage = int(kris_fullness/kris_minfullness)
    if kris_fullstage <= 0:
        $ kris_fullstage = 1    
    if kris_fullstage > 10 and sevent == 0:
        $ kris_fullstage = 10
    if kris_fullstage > 20 and sevent == 1:
        $ kris_fullstage = 20


    if alexa_fullness > alexa_fullmax:
        $ alexa_fullness = alexa_fullmax
    $ alexa_fullnessoz = int(alexa_fullness*0.034)  
    $ alexa_fullstage = int(alexa_fullness/alexa_minfullness)
    if alexa_fullstage <= 0:
        $ alexa_fullstage = 1
    if alexa_fullstage > 10 and sevent == 0:
        $ alexa_fullstage = 10
    if alexa_fullstage > 20 and sevent == 1:
        $ alexa_fullstage = 20

    if lin_fullness > lin_fullmax:
        $ lin_fullness = lin_fullmax
    $ lin_fullnessoz = int(lin_fullness*0.034)
    $ lin_fullstage =int(lin_fullness/lin_minfullness)
    if lin_fullstage <= 0:
        $ lin_fullstage = 1
    if lin_fullstage > 10 and sevent == 0:
        $ lin_fullstage = 10
    if lin_fullstage > 20 and sevent == 1:
        $ lin_fullstage = 20

    if margo_fullness > margo_fullmax:
        $ margo_fullness = margo_fullmax
    $ margo_fullnessoz = int(margo_fullness*0.034)  
    $ margo_fullstage = int(margo_fullness/margo_minfullness)
    if margo_fullstage <= 0:
        $ margo_fullstage = 1
    if margo_fullstage > 10 and sevent == 0:
        $ margo_fullstage = 10
    if margo_fullstage > 20 and sevent == 1:
        $ margo_fullstage = 20


    if hayoon_fullness > hayoon_fullmax:
        $ hayoon_fullness = hayoon_fullmax
    $ hayoon_fullnessoz = int(hayoon_fullness*0.034)  
    $ hayoon_fullstage = int(hayoon_fullness/hayoon_minfullness)
    if hayoon_fullstage <= 0:
        $ hayoon_fullstage = 1
    if hayoon_fullstage > 10 and sevent == 0:
        $ hayoon_fullstage = 10
    if hayoon_fullstage > 20 and sevent == 1:
        $ hayoon_fullstage = 20

    if ava_fullness > ava_fullmax:
        $ ava_fullness = ava_fullmax
    $ ava_fullnessoz = int(ava_fullness*0.034)  
    $ ava_fullstage = int(ava_fullness/ava_minfullness)
    if ava_fullstage <= 0:
        $ ava_fullstage = 1
    if ava_fullstage > 10 and sevent == 0:
        $ ava_fullstage = 10
    if ava_fullstage > 20 and sevent == 1:
        $ ava_fullstage = 20
    
    if sally_fullness > sally_fullmax:
        $ sally_fullness = sally_fullmax
    $ sally_fullnessoz = int(sally_fullness*0.034)  
    $ sally_fullstage = int(sally_fullness/sally_minfullness)
    if sally_fullstage <= 0:
        $ sally_fullstage = 1
    if sally_fullstage > 10 and sevent == 0:
        $ sally_fullstage = 10
    if sally_fullstage > 20 and sevent == 1:
        $ sally_fullstage = 20

    if mindy_fullness > mindy_fullmax:
        $ mindy_fullness = mindy_fullmax
    $ mindy_fullnessoz = int(mindy_fullness*0.034)  
    $ mindy_fullstage = int(mindy_fullness/mindy_minfullness)
    if mindy_fullstage <= 0:
        $ mindy_fullstage = 1
    if mindy_fullstage > 10 and sevent == 0:
        $ mindy_fullstage = 10
    if mindy_fullstage > 20 and sevent == 1:
        $ mindy_fullstage = 20


    return


    