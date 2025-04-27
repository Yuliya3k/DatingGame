label balancefail:
    $ reputationchange = -1
    $ nigirlimage = "niava"
    call reputationchange
    $ position = "playerisfalling"
    play sound "audio/water_splash.mp3"
    $ balancefail = True
    jump surfingoptions