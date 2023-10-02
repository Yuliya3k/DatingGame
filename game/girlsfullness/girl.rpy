label girl:
    
    $ kira_fullnessoz = int(kira_fullness*0.034)  
    $ kira_fullstage = 1+int(kira_fullness/kira_minfullness)
    if kira_fullstage > 10 and sevent == 0:
        $ kira_fullstage = 10
    if kira_fullstage > 20 and sevent == 1:
        $ kira_fullstage = 20


    $ kris_fullstage = 1+int(kris_fullness/kris_minfullness)

    $ alexa_fullnessoz = int(alexa_fullness*0.034)  
    $ alexa_fullstage = 1+int(alexa_fullness/alexa_minfullness)
    if alexa_fullstage > 10 and sevent == 0:
        $ alexa_fullstage = 10
    if alexa_fullstage > 20 and sevent == 1:
        $ alexa_fullstage = 20

    $ lin_fullnessoz = int(lin_fullness*0.034)  
    $ lin_fullstage = 1+int(lin_fullness/lin_minfullness)
    if lin_fullstage > 10 and sevent == 0:
        $ lin_fullstage = 10
    if lin_fullstage > 20 and sevent == 1:
        $ lin_fullstage = 20
    
    return


    