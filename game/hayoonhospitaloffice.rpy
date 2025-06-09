label hayoonhospitaloffice:
    $ position = "hayoonhospitalofficeworking"
    call sceneimg
    "Ha-Yoon is reviewing patient files in her office."
    jump hayoon_fetishists_club_menu

label hayoon_fetishists_club_menu:
    menu:
        "Tell Ha-Yoon about the Fetishists Anonymous club idea" if fetish_club_stage == 0:
            jump hayoon_fetishists_club_intro
        "Ask if the hospital could host the meetings" if fetish_club_stage == 1:
            jump hayoon_fetishists_club_host
        "Request Ha-Yoon's help with guidelines" if fetish_club_stage == 2:
            jump hayoon_fetishists_club_guidelines
        "Finish conversation":
            jump hayoonhospital

label hayoon_fetishists_club_intro:
    $ myrandom = renpy.random.randint(1,3)
    if myrandom == 1:
        $ position = "hayoonhospitalofficecloselisten"
        call sceneimg
        player "Ha-Yoon, after we talked about my fetish, I thought about starting a 'Fetishists Anonymous' group so people can share their experiences safely."
        $ position = "hayoonhospitalofficeclosetalk"
        call sceneimg
        HaYoon "A confidential space like that could really help. Just be sure everyone understands boundaries and consent."
    if myrandom == 2:
        $ position = "hayoonhospitalofficecloselisten"
        call sceneimg
        player "I’ve been considering a support club called 'Fetishists Anonymous'—somewhere folks with various fetishes can meet without judgment."
        $ position = "hayoonhospitalofficeclosetalk"
        call sceneimg
        HaYoon "That sounds like a thoughtful initiative. Focusing on education and respect will make it worthwhile."
    if myrandom == 3:
        $ position = "hayoonhospitalofficecloselisten"
        call sceneimg
        player "This may sound unusual, but I’d like to form a 'Fetishists Anonymous' group to help people feel less isolated."
        $ position = "hayoonhospitalofficeclosetalk"
        call sceneimg
        HaYoon "It could be beneficial. As long as you keep things confidential and consensual, I’m supportive."
    $ fetish_club_stage = 1
    jump hayoon_fetishists_club_menu

label hayoon_fetishists_club_host:
    $ myrandom = renpy.random.randint(1,3)
    if myrandom == 1:
        $ position = "hayoonhospitalofficecloselisten"
        call sceneimg
        player "Do you think the hospital might let us use a room after hours for the meetings?"
        $ position = "hayoonhospitalofficeclosetalk"
        call sceneimg
        HaYoon "Possibly. I'll need to check with the administration, but we might be able to reserve a quiet room."
    if myrandom == 2:
        $ position = "hayoonhospitalofficecloselisten"
        call sceneimg
        player "Could we hold the club here, or would somewhere else be better?"
        $ position = "hayoonhospitalofficeclosetalk"
        call sceneimg
        HaYoon "A small conference room could work if we keep it discreet. If not, perhaps a community center would do."
    if myrandom == 3:
        $ position = "hayoonhospitalofficecloselisten"
        call sceneimg
        player "Is there a neutral space in the hospital we could use for this group?"
        $ position = "hayoonhospitalofficeclosetalk"
        call sceneimg
        HaYoon "I’ll see about reserving one, and if that isn’t possible we can look for another venue."
    $ fetish_club_stage = 2
    jump hayoon_fetishists_club_menu

label hayoon_fetishists_club_guidelines:
    $ myrandom = renpy.random.randint(1,3)
    if myrandom == 1:
        $ position = "hayoonhospitalofficecloselisten"
        call sceneimg
        player "Would you be willing to help me draft the club guidelines?"
        $ position = "hayoonhospitalofficeclosetalk"
        call sceneimg
        HaYoon "Sure, I can help set up rules for confidentiality and consent."
    if myrandom == 2:
        $ position = "hayoonhospitalofficecloselisten"
        call sceneimg
        player "Could you assist in creating some basic rules for the meetings?"
        $ position = "hayoonhospitalofficeclosetalk"
        call sceneimg
        HaYoon "I'd be glad to. We could also invite a therapist for professional advice."
    if myrandom == 3:
        $ position = "hayoonhospitalofficecloselisten"
        call sceneimg
        player "Do you think you could help me establish proper guidelines so everything runs smoothly?"
        $ position = "hayoonhospitalofficeclosetalk"
        call sceneimg
        HaYoon "Of course. Clear boundaries and privacy policies will be essential."
    $ fetish_club_stage = 3
    jump hayoonhospital

"Something went wrong"
jump culinarychoices