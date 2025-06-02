label dayvariables:


    # 1) remember the month before ticking over to the next day
    $ _prev_month = calendar.month          # <-- store numeric month (0-11)

    # 2) advance one day and set the morning time
    $ calendar.AddDays(1)
    $ calendar.hours   = 7
    $ calendar.minutes = 0

    # 3) if the month rolled over, reset your monthly stat(s)
    if calendar.month != _prev_month:
        $ beachcafeevents = 4       # ← whatever you need to reset
                            
        

    
    call girlsfullness
    # call kiraweight 
    call girlsweight
    call girl
    $ auroraseen = 0
    $ aurorahi = 0
    $ krisnottoday = 0
    if sallyhello > 0:
        $ sallyhello = 1
    else:
        pass
    $ sallyhellotoday = 0
    $ sallyhowstheday = 0
    $ lin_cafetoday = 0

    $ lincompliment = 0
    $ linseen = 0
    $ linparkchat = 0
    $ linrideabike = 0
    $ asklinout = 0
    $ parknothing = 0
    $ promcafetoday = 0
    $ lindtaeeatq = 0
    $ linbloatq = 0
    $ lindatehowstheday = 0
    $ linhowstheplaceq = 0
    $ lincycling = 0
    $ lincyclingboss = 0
    $ linhikebreak = 0
    $ linhikebreakeat = 0
    $ linhikejustrest = 0
    $ linhikeexplodingeat = 0
    $ linhikefire = 0
    $ linhike = 0
    $ linhikingimpression = 0
    $ linhikingingredients = 0
    $ linhikingedible = 0
    $ linhikingecology = 0
    $ linhikingbreak = 0
    $ linfeedingpressurexsize = 10
    $ linfeedingpressureysize = 10
    $ lin_dayfullness = 0
    $ hospitalhi = 0
    $ sally_joggingtoday = False
    $ hayoonmettoday = False
    $ margo_fullnesscomplaint = False
    $ ava_fullnesscomplaint = False
    $ myrandom = renpy.random.randint(1,3)
    if myrandom == 1:
        if avabossauth == 1:
            $ avabossauth = 2

return
