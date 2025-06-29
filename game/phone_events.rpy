label phone_motel_call:
    "Your phone rings unexpectedly."
    player "Hello?"
    "Voice" "Hey, meet me at the Sunset Motel. Room 7. I've got plenty of food waiting."
    jump motel_feeding_scene

label motel_feeding_scene:
    scene black
    "You arrive at the small motel room to find a feeder and a willing feedee surrounded by piles of takeout."
    "The aroma of food fills the cramped space as they invite you to join them."
    return

label phone_goal_check(person=None, goal=None):
    if person is None:
        $ person = last_call_person
    if goal is None:
        $ goal = last_call_goal
    "[person] calls to talk about progress on [goal]."
    return


