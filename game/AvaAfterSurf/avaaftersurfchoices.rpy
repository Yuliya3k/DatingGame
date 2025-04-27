label avaaftersurfchoices:

    call closescreens
    # play music "audio/beach_chill.mp3"

    $ avaaftersurf_done = False
    $ position = "avabeachaftersurfingfrontstand"
    call sceneimg

    # --- opening banter ----------------------------------------------------
    if ava_attitude < 50:
        player "That was some session out there.  You carved those last two waves like a pro."
        $ position = "avaaftersurfingtalkingclose"
        call sceneimg
        Ava "Flatterer.  But thanks – the swell was perfect today."
    else:
        player "You were on fire out there!  I swear the dolphins were cheering."
        $ position = "avaaftersurfingtalkingclose"
        call sceneimg
        Ava "Ha!  Well if the dolphins approve, who am I to argue?"

    $ position = "avaaftersurfinglisteningclose"
    call sceneimg
    player "Why don’t we chill for a bit?  I brought a cooler."

    while not avaaftersurf_done:

        $ position = "avaaftersurfinglisteningclose"
        call sceneimg
        menu:
            "Offer Ava an ice-cold beer":
                call ava_offer_beer

            "Chat about the sea":
                call ava_talk_sea

            "Tease her playfully":
                call ava_tease

            "Say goodbye for now":
                $ avaaftersurf_done = True
                call ava_goodbye

jump avaaftersurfchoices
# ---------------------------------------------------------------------------