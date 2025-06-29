init python:

    fc_listeners = [
            "nahuelfccloselisten",
            "charliefccloselisten",
            "ashfccloselisten",
            "borisfccloselisten",
            "nikkifccloselisten",
            "faridafccloselisten",
            "aurorafccloselisten",
            "fc",
        ]

label show_random_listener:
    $ position = renpy.random.choice(fc_listeners)
    call sceneimg
    return



label afmeeting:

   if fetish_club_first_meeting_done:
        "A week has passed, and everyone gathers again to discuss progress."
        jump weekly_goal_report

    $ position = "fc"
    call sceneimg

    with fade


    $ position = "fc"
    call sceneimg
    
    with fade

    # The host (player character) opens the meeting
    player "Hello, everyone. Thank you all for coming tonight."
    call show_random_listener
    player "My name is [name], and I'm the one who put this group together."
    call show_random_listener
    player "As some of you know, I'm a cook by trade... and I also have a feeder fetish."
    call show_random_listener
    player "Yeah, I guess you could say I literally love to feed people."
    call show_random_listener
    player "I started this group because I wanted a safe space for us to talk about our desires."
    call show_random_listener
    player "This isn't about trying to get rid of our fetishes or feeling ashamed."
    call show_random_listener
    player "It's not like some addiction group where the goal is abstinence."
    call show_random_listener
    player "Instead, it's about understanding ourselves, finding balance, and setting healthy boundaries."
    call show_random_listener
    player "We want to enjoy who we are without hurting ourselves or anyone else, right?"
    call show_random_listener
    "A few heads around the circle nod in agreement."
    player "So, let's get started by introducing ourselves, if that's okay."
    call show_random_listener
    player "You can share as much or as little as you're comfortable with."
    call show_random_listener
    player "Maybe tell us your name, what your fetish or interest is, and what you're hoping to get out of this group."
    call show_random_listener
    player "I'll go first to break the ice."
    call show_random_listener
    "You take a breath, meeting the eyes of each person in the small circle."
    player "Like I said, I'm [name], and I have a feeder fetish."
    call show_random_listener
    player "I love cooking and watching people enjoy my food... maybe a bit too much sometimes."
    call show_random_listener
    player "There's this thrill I get from seeing someone really indulge in something I made."
    call show_random_listener
    player "But I've realized I need to keep it within healthy limits."
    call show_random_listener
    player "I don't want to pressure anyone into overeating or cross boundaries just because it excites me."
    call show_random_listener
    player "I'm here to learn how to balance that desire with respect and care for my partners."
    call show_random_listener
    player "Honestly, I also want to make sure I don't lose myself in it, since, well, food is basically my life and my job."
    call show_random_listener
    player "So yeah, I'm looking for a healthier relationship with my fetish, and I'm really glad to meet others who understand."
    call show_random_listener
    player "Thank you for listening."
    call show_random_listener
    "You smile and give a small nod, then look around the room encouragingly."
    player "Who'd like to go next?"
    call show_random_listener
    "There's a brief, quiet moment. Then one woman raises her hand slightly, offering a polite smile."
    $ position = "aurorafcclosetalk"
    call sceneimg
    Aurora "Hi, I'm Aurora, and I'm a feeder too."
    Aurora "I’m really happy to be here with all of you."
    Aurora "For me, feeding someone is... well, it’s my way of showing love and care."
    Aurora "I adore cooking and preparing big meals for people. I always have."
    Aurora "And I'm not going to lie, I enjoy having a bit of control in that situation."
    Aurora "There's something satisfying about seeing someone take that next bite because of me."
    Aurora "I suppose I'm a bit subtly controlling by nature."
    Aurora "I like to gently nudge my partner to eat more, to savor just one more bite, one more plate."
    Aurora "It gives me a sense of comfort and, yes, power, knowing I'm taking care of them in that way."
    Aurora "But I know it can cross a line. I've worried about pushing too hard."
    Aurora "The last thing I want is to hurt someone’s health or make them uncomfortable."
    Aurora "So my goal here is to learn how to keep that caring and... controlling side of me in check."
    Aurora "I want to make sure my partner—current or future—feels loved, not pressured."
    Aurora "And I want to find more confidence that this fetish can be a positive part of a relationship, not a secret shame."
    Aurora "So, that's me. Thank you."
    $ position = "aurorafccloselisten"
    call sceneimg
    "The group echoes a gentle chorus of 'Thank you, Aurora,' as she finishes. Aurora sits back, calm and collected."
    "After a moment, another woman tentatively raises her hand. She looks a little nervous, but she smiles warmly."
    $ position = "nikkifcclosetalk"
    call sceneimg
    Nikki "Hi, I'm Nikki, and... I'm a feedee."
    Nikki "I uh... I really like being fed by someone."
    Nikki "For me it's very sensual and emotional. Like, it makes me feel adored and safe."
    Nikki "When someone feeds me, or even just encourages me to enjoy as much as I want, I feel this rush of warmth and intimacy."
    Nikki "But it also makes me feel vulnerable."
    Nikki "I’ve always been a very emotional person, and honestly this fetish can be a rollercoaster for me."
    Nikki "Part of me loves feeling so full and satisfied, like I'm the center of someone's attention..."
    Nikki "But another part of me worries about being judged for it."
    Nikki "I've had partners who didn't understand. One even told me it was 'weird' and it really hurt."
    Nikki "So I sometimes feel ashamed or afraid to bring it up."
    Nikki "Physically, I do worry about my health too. I mean, I enjoy gaining a little weight in the moment, but later on I can panic about it."
    Nikki "It's confusing, loving something that I'm also afraid of."
    Nikki "I'm here because I want to accept this part of myself without feeling guilty."
    Nikki "I want to learn how to enjoy it in a balanced way, where I can be safe and happy."
    Nikki "And I want to know it's possible to find someone who actually understands this side of me and respects me, not just fetishizes me."
    Nikki "I guess I just want to feel... normal, in a way. Or at least not alone."
    Nikki "So... yeah. That's me. Thank you for listening."
    $ position = "nikkifccloselisten"
    call sceneimg
    "Nikki tucks a strand of hair behind her ear as she finishes, and you notice her eyes glisten a bit with emotion."
    player "Thank you for sharing, Nikki."
    "A couple of people nearby give Nikki encouraging nods and smiles, and she relaxes back into her chair."
    "Next, a woman sitting forward with her arms loosely crossed speaks up without hesitation."
    $ position = "faridabeachbbq"
    call sceneimg
    $ position = "faridafcclosetalk"
    call sceneimg
    farida "Hey, I'm Farida, and I'm also a feedee."
    farida "Unlike some, I'm pretty open about it. I mean, I love to eat and I love being fed. Simple as that."
    farida "There's no point in me pretending otherwise. Food makes me happy, and being spoiled with food is even better."
    farida "I'm probably one of those people who plan my day around what's for dinner, you know?"
    farida "And when it comes to the fetish side... I really enjoy pushing my limits a bit, seeing how much I can indulge."
    farida "It makes me feel free, like I'm breaking some silly rule about how women—or anyone—'should' eat."
    farida "People might call it gluttony or whatever, but to me it's just owning my own body and desires."
    farida "That said, I'm not blind to the downsides. I know I gotta stay healthy."
    farida "I've definitely had times where I overdid it and felt sick after. Not fun, even if the feeding part was fun while it lasted."
    farida "And, uh, I've had an ex who really didn't get it at all."
    farida "He would say things like, 'This isn't normal, Farida' or he'd make me feel like a freak for wanting a third helping."
    farida "Eventually I just stopped talking to him about it. That relationship didn't last long, surprise, surprise."
    farida "I'm strong-willed, so I didn't let his words shame me completely, but it did make me hesitate to share this with new people."
    farida "I'm here because I want to find a community that gets it, like all of you."
    farida "I want to keep enjoying this part of my life without feeling I have to apologize for it."
    farida "And yeah, also keep myself in check so I don't end up on one of those reality shows about, you know, being too far gone. A little balance wouldn't hurt."
    farida "So, that's me. I'm really glad to meet you all."
    farida "Thanks."
    $ position = "faridafccloselisten"
    call sceneimg
    "Farida flashes a quick, confident smile as she finishes. A few people chuckle softly at her reality show comment, and the mood lightens."
    "Next, a man lounging comfortably in his chair gives a playful salute."
    $ position = "borisfcclosetalk"
    call sceneimg
    Boris "Hey folks, I'm Boris. I'm, well... a hedonist, I guess."
    Boris "If there's pleasure to be had, I'll probably try it at least once."
    Boris "For me, indulgence is kind of the name of the game."
    Boris "I love rich foods, long dinners, big desserts — the works. And I love sharing those with someone special."
    Boris "So I suppose in our terms, I'm both a feeder and a feedee when the mood strikes."
    Boris "I enjoy feeding my partners treats and watching them enjoy every bite."
    Boris "And I definitely enjoy being on the receiving end too."
    Boris "There's something just... blissful about eating to your heart's content with someone who encourages it."
    Boris "And if there's a little erotic fun involved with whipped cream or chocolate sauce, hey, I'm all in."
    Boris "Life's short, you know? I figure why not revel in the things that feel good."
    Boris "But... I do know it can be a slippery slope. Indulgence can turn into overindulgence real quick."
    Boris "I've had a scare or two with my health — nothing major, but enough to wake me up a bit."
    Boris "Also, not everyone in my life understands my 'live for pleasure' philosophy. I've been called irresponsible a time or two."
    Boris "So I'm here looking for that same balance everyone’s talking about."
    Boris "I want to keep things fun and pleasurable, but also make sure I'm not hurting myself or anyone else in the process."
    Boris "And maybe learn a bit of self-discipline... or at least find friends who will tell me when I've had enough cake, right?"
    Boris "Heh, anyway, it's really great to meet you all and to know I'm not the only one out there like this."
    Boris "Thanks for hearing me out."
    $ position = "borisfccloselisten"
    call sceneimg
    "Boris grins as he finishes, and a few of you exchange friendly laughter. The atmosphere feels a bit lighter after his warm, joking tone."
    "Next to speak is a man who sits up very straight, hands folded in his lap. He takes a slow breath before he begins."
    $ position = "charliefcclosetalk"
    call sceneimg
    Charlie "Hello, I'm Charlie."
    Charlie "I... um, I have a fetish that leans toward control and domination."
    Charlie "I'm probably a bit different from the rest of you in terms of specifics, but I think we're all here for similar reasons."
    Charlie "In my case, I get aroused by being the one in charge. Whether that's in the bedroom or sometimes even with things like... well, like controlling a partner's diet or routines."
    Charlie "I'm a pretty disciplined person in general. I follow a strict routine for myself, and I guess I find comfort and excitement in imposing structure on someone I’m with, too."
    Charlie "It's consensual — or at least, I intend it to be. But I know it can cross into unhealthy territory if I'm not careful."
    Charlie "I haven't really had a safe way to explore that side of me. In past relationships, I've mostly kept it under wraps at first."
    Charlie "When I have opened up about it, reactions have been... mixed. Some people get uncomfortable, or they just don't understand why anyone would want that kind of control dynamic."
    Charlie "So I've often felt like I have to hide it. That leads to frustration for me, and it's not fair to my partners either."
    Charlie "I'm here because I want to learn how to navigate this fetish responsibly."
    Charlie "I want to be able to communicate better about it, and find ways to satisfy that urge for control without violating anyone's boundaries or my own principles."
    Charlie "Also, honestly, to make sure I keep my own need for control in check. It can be kind of addictive to feel that power, and I don't want to let it run wild."
    Charlie "So... yeah. I'm trying to find that healthy balance between who I am and who I want to be in a relationship."
    Charlie "Thank you for listening."
    $ position = "charliefccloselisten"
    call sceneimg
    "Charlie offers a brief, reserved smile and bows his head slightly. Everyone gives him a moment of respectful quiet, sensing the weight of what he shared."
    "After Charlie, a confident-looking person with a smirk on his face speaks up, lounging with one arm slung over the back of his chair."
    $ position = "ashfcclosetalk"
    call sceneimg
    Ash "Guess I'm up next. Name's Ash."
    Ash "So, I'm... probably a bit of a narcissist, if I'm being honest."
    Ash "I really get off on power dynamics. I like feeling in control, and I love when a partner kinda, well, worships me."
    Ash "Sounds arrogant, I know. And it is. I'm not gonna sugarcoat it."
    Ash "I enjoy seeing myself as the center of attention. In my fantasies, I'm the king of my little world."
    Ash "But I'm not totally without a conscience, promise."
    Ash "I can laugh about it, but there's a part of me that worries I'm just using people to feed my ego."
    Ash "I've had relationships where my need to be, uh, adored, let’s say, ended up pushing people away."
    Ash "Either I came on too strong with the whole 'I'm in charge' vibe, or I attracted people who were into it at first but then it got to be too much."
    Ash "I also realized that even if I like being on top, so to speak, I do actually care about the people I'm with."
    Ash "I don't want to be a total jerk or hurt someone just because I was too caught up in my own head."
    Ash "So my goal here is to keep myself in check, learn a bit of humility maybe."
    Ash "I'm looking to find ways to still enjoy the power dynamics I love, but in a way that's safe and fun for both sides."
    Ash "And maybe learn to, you know, take turns once in a while, or at least communicate better so I don't cross lines."
    Ash "It's weird, because joking about being a narcissist is easy, but facing it is harder."
    Ash "So kudos to all of you for being so open. I'm glad I'm not the only one in the room with... let's call them 'unique' personality quirks."
    Ash "Thanks, everyone."
    $ position = "ashfccloselisten"
    call sceneimg
    "Ash gives a little two-finger salute in lieu of a wave, and you notice a few others smiling at his candor."
    "Finally, the last person in the circle, a man with a relaxed posture and a friendly face, chimes in."
    $ position = "nahuelfcclosetalk"
    call sceneimg
    Nahuel "Hi all, I'm Nahuel."
    Nahuel "I'm pretty open-minded and, I guess, exploratory by nature."
    Nahuel "To be honest, I'm here more to learn and support than because of one specific fetish."
    Nahuel "Don't get me wrong, I have my kinks and interests – a bit of bondage here, a bit of roleplay there, I'm no saint."
    Nahuel "But I never really had one 'main' fetish that defined me."
    Nahuel "What I do have is a curiosity and a willingness to try and understand new things."
    Nahuel "When I heard about this group, I thought it sounded like something important."
    Nahuel "I've seen friends struggle with feeling ashamed about what they like, and I've been a confidant for a couple of them."
    Nahuel "And even for myself, I figured it couldn't hurt to reflect on my own boundaries and how I handle the things I'm into."
    Nahuel "I like to think I'm pretty grounded. I'm the kind of person who believes in moderation and self-awareness."
    Nahuel "But nobody is perfect, and it's easy to lose perspective when you're dealing with something as intense as a fetish or even just a new sexual interest."
    Nahuel "So, I'm here to build that sense of community with you all."
    Nahuel "I want to understand what each of you is going through, and maybe share any insights I have from my experiences."
    Nahuel "And of course, learn from your insights too."
    Nahuel "My goal is to make sure that whatever our desires are, we keep them as a healthy part of our lives and not the whole of it."
    Nahuel "I'm really glad to be here and to meet everyone. Thanks."
    $ position = "nahuelfccloselisten"
    call sceneimg
    "Nahuel's easygoing tone leaves a calm hush in the air as he finishes. You look around at the group, feeling a warmth in your chest."
    "Everyone has spoken now, each person laying out their feelings with honesty. There's a palpable sense of relief and solidarity in the room."
    player "Thank you, all of you, for sharing."
    player "I know it isn't always easy to open up about these things. It means a lot that everyone here is being so honest and respectful."
    player "Hearing all of you, I feel really hopeful. It's clear none of us are alone in this."
    player "We might all have different desires and personalities, but I think our goals are very much the same."
    player "We want to understand ourselves better, take care of ourselves and the people we care about, and not feel alone or ashamed."
    player "This is exactly why I wanted to start this group."
    player "I believe we can really help each other."
    player "Maybe it's just listening, maybe it's sharing advice or just knowing someone else 'gets it'."
    player "Whatever it is, we're building a little community here."
    player "I for one am really grateful to have you all here."
    "You take a moment to meet each person's eyes in turn, sharing a sincere smile."
    player "So, since this was our first meeting, I figured we'd mostly just get to know each other."
    player "Going forward, we can talk more about whatever topics or challenges you all want to bring up."
    player "Nothing's off the table as long as we keep respecting each other."
    player "How does that sound?"
    "Around the circle, you see expressions of agreement—smiles, nods, a few murmured 'yeah' and 'absolutely'."
    player "Great."
    player "Alright, before we wrap up, does anyone have anything else they want to add or ask?"
    "The group glances around at each other, but no one seems eager to speak up just yet. It seems everyone is content with how the meeting went."
    player "Okay then. I guess we'll call it here for tonight."
    player "Thank you again, truly. This was a great start."
    player "Let's plan to meet again next week, same time, same place."
    player "In the meantime, if anyone wants to talk or hang out, we can exchange numbers or something after the meeting."
    player "No pressure, of course. Just throwing it out there."
    player "And remember, everything we share here is confidential. This is our trust circle."
    player "You're not alone, and there's no judgment here."
    player "Take care of yourselves this week."
    player "I’ll see you all next time."
    "There’s a general atmosphere of warmth and understanding as everyone slowly rises from their chairs."
    "People begin to chat softly among themselves, a few exchanging phone numbers or friendly touches on the shoulder."
    "Aurora and Farida are comparing notes about recipes, while Nikki and Boris laugh about something quietly."
    "Charlie and Ash shake hands, a mutual respect passing between them, and Nahuel gives you an encouraging nod as he helps stack a couple of chairs."
    "As everyone files out, you feel a sense of pride and hope swelling in your chest."
    "In this small room, a new community has begun — one built on acceptance, understanding, and the promise of growth."
    "You couldn't have asked for a better first meeting."
    $ fetish_club_first_meeting_done = True

    # After introductions, discuss weekly goals
    "As the chatter dies down, you clear your throat to draw everyone's attention."
    player "Before we head out, I'd like each of us to set a small goal for the week."
    player "We'll hold each other accountable and talk about how it went next time."
    player "Here are some ideas you can choose from:"

    $ goal_options = [
        "Keep a daily journal about your desires and feelings.",
        "Avoid pushing or indulging a specific trigger this week.",
        "Share your fetish with a trusted friend or partner.",
        "Track how you feel each time you act on your fetish.",
        "Set a clear limit on how often you indulge.",
        "Reach out to another member for support at least once.",
        "Plan a non-fetish activity to enjoy and stay balanced."
    ]

    jump choose_goal_member

label choose_goal_member:
    menu:
        "Aurora" if goal_aurora == "":
            jump goal_aurora
        "Nikki" if goal_nikki == "":
            jump goal_nikki
        "Farida" if goal_farida == "":
            jump goal_farida
        "Boris" if goal_boris == "":
            jump goal_boris
        "Charlie" if goal_charlie == "":
            jump goal_charlie
        "Ash" if goal_ash == "":
            jump goal_ash
        "Nahuel" if goal_nahuel == "":
            jump goal_nahuel
        "Everyone has a goal." if goal_aurora != "" and goal_nikki != "" and goal_farida != "" and goal_boris != "" and goal_charlie != "" and goal_ash != "" and goal_nahuel != "":
            jump goals_done

label goal_aurora:
    player "Aurora, let's start with you."
    $ position = "aurorafccloselisten"
    call sceneimg
    menu:
        "Keep a daily journal about your desires and feelings.":
            player "How about keeping a journal each day about your desires and feelings?"
            $ position = "aurorafcclosetalk"
            call sceneimg
            Aurora "I like that idea. Writing things down might keep me mindful."
            $ goal_aurora = goal_options[0]
        "Avoid pushing or indulging a specific trigger this week.":
            player "Maybe try not to push anyone to eat more than they want this week."
            $ position = "aurorafcclosetalk"
            call sceneimg
            Aurora "Right, focusing on boundaries sounds good."
            $ goal_aurora = goal_options[1]
        "Share your fetish with a trusted friend or partner.":
            player "What if you shared your fetish with someone you trust?"
            $ position = "aurorafcclosetalk"
            call sceneimg
            Aurora "That's a bit scary, but it could be freeing. I'll consider it."
            $ goal_aurora = goal_options[2]
        "Track how you feel each time you act on your fetish.":
            player "You could track how you feel whenever you indulge the urge to feed."
            $ position = "aurorafcclosetalk"
            call sceneimg
            Aurora "Keeping tabs on my emotions should help me see patterns."
            $ goal_aurora = goal_options[3]
        "Set a clear limit on how often you indulge.":
            player "Maybe limit how often you encourage big meals this week."
            $ position = "aurorafcclosetalk"
            call sceneimg
            Aurora "A sensible limit will keep things healthy. I'm in."
            $ goal_aurora = goal_options[4]
        "Reach out to another member for support at least once.":
            player "Reach out to someone here for support during the week."
            $ position = "aurorafcclosetalk"
            call sceneimg
            Aurora "I'd like that. It's nice knowing I can lean on you all."
            $ goal_aurora = goal_options[5]
        "Plan a non-fetish activity to enjoy and stay balanced.":
            player "Plan something unrelated to feeding, just for balance."
            $ position = "aurorafcclosetalk"
            call sceneimg
            Aurora "Good idea. I'll set up a hobby night with my partner."
            $ goal_aurora = goal_options[6]
        $ goal_aurora_outcome = renpy.random.choice(["success", "fail"])
    jump choose_goal_member

label goal_nikki:
    player "Nikki, let's pick something for you."
    $ position = "nikkifccloselisten"
    call sceneimg
    menu:
        "Keep a daily journal about your desires and feelings.":
            player "Would you try keeping a daily journal about how you feel?"
            $ position = "nikkifcclosetalk"
            call sceneimg
            Nikki "Sure, it might help me work through the guilt."
            $ goal_nikki = goal_options[0]
        "Avoid pushing or indulging a specific trigger this week.":
            player "Maybe avoid one of your eating triggers for the week."
            $ position = "nikkifcclosetalk"
            call sceneimg
            Nikki "That's tough, but I'll do my best."
            $ goal_nikki = goal_options[1]
        "Share your fetish with a trusted friend or partner.":
            player "How about sharing your fetish with someone you trust?"
            $ position = "nikkifcclosetalk"
            call sceneimg
            Nikki "I think I'm ready to open up to a close friend."
            $ goal_nikki = goal_options[2]
        "Track how you feel each time you act on your fetish.":
            player "You could note your emotions whenever you indulge."
            $ position = "nikkifcclosetalk"
            call sceneimg
            Nikki "That could show me why certain moments feel better than others."
            $ goal_nikki = goal_options[3]
        "Set a clear limit on how often you indulge.":
            player "Consider setting a limit on your indulgence this week."
            $ position = "nikkifcclosetalk"
            call sceneimg
            Nikki "A little structure might keep me calm."
            $ goal_nikki = goal_options[4]
        "Reach out to another member for support at least once.":
            player "Reach out to one of us if you feel overwhelmed."
            $ position = "nikkifcclosetalk"
            call sceneimg
            Nikki "I'd appreciate having someone to talk to."
            $ goal_nikki = goal_options[5]
        "Plan a non-fetish activity to enjoy and stay balanced.":
            player "Plan something fun that isn't about feeding."
            $ position = "nikkifcclosetalk"
            call sceneimg
            Nikki "That'll help me remember I'm more than my fetish."
            $ goal_nikki = goal_options[6]
    $ goal_nikki_outcome = renpy.random.choice(["success", "fail"])
    jump choose_goal_member

label goal_farida:
    player "Farida, your turn."
    $ position = "faridafccloselisten"
    call sceneimg
    menu:
        "Keep a daily journal about your desires and feelings.":
            player "Would a daily journal help you keep track of things?"
            $ position = "faridafcclosetalk"
            call sceneimg
            farida "Yeah, I can do that. Might be interesting to read later."
            $ goal_farida = goal_options[0]
        "Avoid pushing or indulging a specific trigger this week.":
            player "Try skipping whatever usually makes you overdo it."
            $ position = "faridafcclosetalk"
            call sceneimg
            farida "Sure, I'll give that a shot."
            $ goal_farida = goal_options[1]
        "Share your fetish with a trusted friend or partner.":
            player "Maybe tell someone you trust about your fetish."
            $ position = "faridafcclosetalk"
            call sceneimg
            farida "I know just who I could talk to."
            $ goal_farida = goal_options[2]
        "Track how you feel each time you act on your fetish.":
            player "You could track your feelings whenever you go all out."
            $ position = "faridafcclosetalk"
            call sceneimg
            farida "That might reveal if I'm really enjoying it or just chasing a rush."
            $ goal_farida = goal_options[3]
        "Set a clear limit on how often you indulge.":
            player "Set yourself a limit for indulgence this week."
            $ position = "faridafcclosetalk"
            call sceneimg
            farida "Okay, I'll keep it to reasonable portions."
            $ goal_farida = goal_options[4]
        "Reach out to another member for support at least once.":
            player "Reach out to one of us during the week for support."
            $ position = "faridafcclosetalk"
            call sceneimg
            farida "Sounds good, I'm not shy about asking for help."
            $ goal_farida = goal_options[5]
        "Plan a non-fetish activity to enjoy and stay balanced.":
            player "Plan something fun outside of food and feeding."
            $ position = "faridafcclosetalk"
            call sceneimg
            farida "Maybe a hike or something active. I like it."
            $ goal_farida = goal_options[6]
    
    $ goal_farida_outcome = renpy.random.choice(["success", "fail"])
    jump choose_goal_member

label goal_boris:
    player "Boris, let's find a goal for you."
    $ position = "borisfccloselisten"
    call sceneimg
    menu:
        "Keep a daily journal about your desires and feelings.":
            player "How about keeping a journal about your cravings and moods?"
            $ position = "borisfcclosetalk"
            call sceneimg
            Boris "Sure, that might help me see patterns."
            $ goal_boris = goal_options[0]
        "Avoid pushing or indulging a specific trigger this week.":
            player "Maybe skip that extra dessert you love so much this week."
            $ position = "borisfcclosetalk"
            call sceneimg
            Boris "Ha, that'll be a challenge, but I'll try."
            $ goal_boris = goal_options[1]
        "Share your fetish with a trusted friend or partner.":
            player "Consider sharing your interests with someone you trust."
            $ position = "borisfcclosetalk"
            call sceneimg
            Boris "I could open up to my partner about it more."
            $ goal_boris = goal_options[2]
        "Track how you feel each time you act on your fetish.":
            player "Track your feelings whenever you indulge."
            $ position = "borisfcclosetalk"
            call sceneimg
            Boris "Might be eye-opening. I'll do it."
            $ goal_boris = goal_options[3]
        "Set a clear limit on how often you indulge.":
            player "Set yourself a limit on indulgence this week."
            $ position = "borisfcclosetalk"
            call sceneimg
            Boris "Probably wise, I'll pace myself."
            $ goal_boris = goal_options[4]
        "Reach out to another member for support at least once.":
            player "Reach out to someone here if you need a nudge to slow down."
            $ position = "borisfcclosetalk"
            call sceneimg
            Boris "Deal. It's good to have accountability."
            $ goal_boris = goal_options[5]
        "Plan a non-fetish activity to enjoy and stay balanced.":
            player "Plan something fun that doesn't revolve around food."
            $ position = "borisfcclosetalk"
            call sceneimg
            Boris "Maybe I'll pick up jogging again."
            $ goal_boris = goal_options[6]
    $ goal_boris_outcome = renpy.random.choice(["success", "fail"])
    jump choose_goal_member

label goal_charlie:
    player "Charlie, what about you?"
    $ position = "charliefccloselisten"
    call sceneimg
    menu:
        "Keep a daily journal about your desires and feelings.":
            player "Keep a journal about your urges and how you handle them."
            $ position = "charliefcclosetalk"
            call sceneimg
            Charlie "That should help me stay self-aware."
            $ goal_charlie = goal_options[0]
        "Avoid pushing or indulging a specific trigger this week.":
            player "Try avoiding strict control over anyone's routine this week."
            $ position = "charliefcclosetalk"
            call sceneimg
            Charlie "A good exercise in restraint."
            $ goal_charlie = goal_options[1]
        "Share your fetish with a trusted friend or partner.":
            player "Maybe share your need for control with someone close."
            $ position = "charliefcclosetalk"
            call sceneimg
            Charlie "It would be nice not to hide it. I'll consider that."
            $ goal_charlie = goal_options[2]
        "Track how you feel each time you act on your fetish.":
            player "Track your emotions each time you feel that urge to take charge."
            $ position = "charliefcclosetalk"
            call sceneimg
            Charlie "Could reveal when I'm overdoing it."
            $ goal_charlie = goal_options[3]
        "Set a clear limit on how often you indulge.":
            player "Set a limit on how often you impose control this week."
            $ position = "charliefcclosetalk"
            call sceneimg
            Charlie "I'll keep myself in check."
            $ goal_charlie = goal_options[4]
        "Reach out to another member for support at least once.":
            player "Reach out if you feel you're slipping."
            $ position = "charliefcclosetalk"
            call sceneimg
            Charlie "I appreciate that."
            $ goal_charlie = goal_options[5]
        "Plan a non-fetish activity to enjoy and stay balanced.":
            player "Plan something relaxing that isn't about control."
            $ position = "charliefcclosetalk"
            call sceneimg
            Charlie "Maybe a casual game night with friends."
            $ goal_charlie = goal_options[6]
    $ goal_charlie_outcome = renpy.random.choice(["success", "fail"])
    jump choose_goal_member

label goal_ash:
    player "Ash, your turn."
    $ position = "ashfccloselisten"
    call sceneimg
    menu:
        "Keep a daily journal about your desires and feelings.":
            player "How about writing down your thoughts and desires each day?"
            $ position = "ashfcclosetalk"
            call sceneimg
            Ash "Could be humbling. I'll try."
            $ goal_ash = goal_options[0]
        "Avoid pushing or indulging a specific trigger this week.":
            player "Avoid situations where you might dominate just for ego's sake."
            $ position = "ashfcclosetalk"
            call sceneimg
            Ash "Yeah, reigning it in is smart."
            $ goal_ash = goal_options[1]
        "Share your fetish with a trusted friend or partner.":
            player "Maybe share your interest in power dynamics with someone close."
            $ position = "ashfcclosetalk"
            call sceneimg
            Ash "Might help me stay grounded if they know."
            $ goal_ash = goal_options[2]
        "Track how you feel each time you act on your fetish.":
            player "Track your feelings whenever you take the lead."
            $ position = "ashfcclosetalk"
            call sceneimg
            Ash "Could show me when I'm going too far."
            $ goal_ash = goal_options[3]
        "Set a clear limit on how often you indulge.":
            player "Set a limit on how often you demand that attention."
            $ position = "ashfcclosetalk"
            call sceneimg
            Ash "Fair enough, I'll pace myself."
            $ goal_ash = goal_options[4]
        "Reach out to another member for support at least once.":
            player "Reach out if you need a reality check."
            $ position = "ashfcclosetalk"
            call sceneimg
            Ash "Ha, I can do that."
            $ goal_ash = goal_options[5]
        "Plan a non-fetish activity to enjoy and stay balanced.":
            player "Plan something unrelated to dominance, just for balance."
            $ position = "ashfcclosetalk"
            call sceneimg
            Ash "Maybe I'll volunteer somewhere low key."
            $ goal_ash = goal_options[6]
    $ goal_ash_outcome = renpy.random.choice(["success", "fail"])
    jump choose_goal_member

label goal_nahuel:
    player "Finally, Nahuel, let's choose one for you."
    $ position = "nahuelfccloselisten"
    call sceneimg
    menu:
        "Keep a daily journal about your desires and feelings.":
            player "Would keeping a journal help you reflect on what you learn here?"
            $ position = "nahuelfcclosetalk"
            call sceneimg
            Nahuel "Absolutely, I like writing anyway."
            $ goal_nahuel = goal_options[0]
        "Avoid pushing or indulging a specific trigger this week.":
            player "Is there a trigger you could avoid this week?"
            $ position = "nahuelfcclosetalk"
            call sceneimg
            Nahuel "Sure, I'll stay mindful of that."
            $ goal_nahuel = goal_options[1]
        "Share your fetish with a trusted friend or partner.":
            player "Maybe share one of your kinks with a trusted friend."
            $ position = "nahuelfcclosetalk"
            call sceneimg
            Nahuel "Yeah, opening up more can't hurt."
            $ goal_nahuel = goal_options[2]
        "Track how you feel each time you act on your fetish.":
            player "Track your emotions whenever you explore a kink."
            $ position = "nahuelfcclosetalk"
            call sceneimg
            Nahuel "Good idea, that will keep me grounded."
            $ goal_nahuel = goal_options[3]
        "Set a clear limit on how often you indulge.":
            player "Set a limit on how much you experiment this week."
            $ position = "nahuelfcclosetalk"
            call sceneimg
            Nahuel "Moderation is key. I'll do that."
            $ goal_nahuel = goal_options[4]
        "Reach out to another member for support at least once.":
            player "Reach out to someone here for a chat this week."
            $ position = "nahuelfcclosetalk"
            call sceneimg
            Nahuel "I'd like that."
            $ goal_nahuel = goal_options[5]
        "Plan a non-fetish activity to enjoy and stay balanced.":
            player "Plan a hobby activity unrelated to any kink."
            $ position = "nahuelfcclosetalk"
            call sceneimg
            Nahuel "Perfect, I'll go hiking."
            $ goal_nahuel = goal_options[6]
    $ goal_nahuel_outcome = renpy.random.choice(["success", "fail"])
    jump choose_goal_member



label goals_done:
    player "Great work, everyone. We'll check in next week to see how we all did."
    jump culinarychoices





label weekly_goal_report:
    if goal_aurora != "":
        $ goal_aurora_outcome = renpy.random.choice(["success", "disaster"])
        if goal_aurora_outcome == "success":
            "[renpy.random.choice(aurora_success_lines)] Aurora successfully completed: [goal_aurora]."
        else:
            "[renpy.random.choice(aurora_fail_lines)] Aurora's attempt at [goal_aurora] ended in disaster."
        $ goal_aurora = ""
    if goal_nikki != "":
        $ goal_nikki_outcome = renpy.random.choice(["success", "disaster"])
        if goal_nikki_outcome == "success":
            "[renpy.random.choice(nikki_success_lines)] Nikki successfully completed: [goal_nikki]."
        else:
            "[renpy.random.choice(nikki_fail_lines)] Nikki's attempt at [goal_nikki] ended in disaster."
        $ goal_nikki = ""
    if goal_farida != "":
        $ goal_farida_outcome = renpy.random.choice(["success", "disaster"])
        if goal_farida_outcome == "success":
            "[renpy.random.choice(farida_success_lines)] Farida successfully completed: [goal_farida]."
        else:
            "[renpy.random.choice(farida_fail_lines)] Farida's attempt at [goal_farida] ended in disaster."
        $ goal_farida = ""
    if goal_boris != "":
        $ goal_boris_outcome = renpy.random.choice(["success", "disaster"])
        if goal_boris_outcome == "success":
            "[renpy.random.choice(boris_success_lines)] Boris successfully completed: [goal_boris]."
        else:
            "[renpy.random.choice(boris_fail_lines)] Boris's attempt at [goal_boris] ended in disaster."
        $ goal_boris = ""
    if goal_charlie != "":
        $ goal_charlie_outcome = renpy.random.choice(["success", "disaster"])
        if goal_charlie_outcome == "success":
            "[renpy.random.choice(charlie_success_lines)] Charlie successfully completed: [goal_charlie]."
        else:
            "[renpy.random.choice(charlie_fail_lines)] Charlie's attempt at [goal_charlie] ended in disaster."
        $ goal_charlie = ""
    if goal_ash != "":
        $ goal_ash_outcome = renpy.random.choice(["success", "disaster"])
        if goal_ash_outcome == "success":
            "[renpy.random.choice(ash_success_lines)] Ash successfully completed: [goal_ash]."
        else:
            "[renpy.random.choice(ash_fail_lines)] Ash's attempt at [goal_ash] ended in disaster."
        $ goal_ash = ""
    if goal_nahuel != "":
        $ goal_nahuel_outcome = renpy.random.choice(["success", "disaster"])
        if goal_nahuel_outcome == "success":
            "[renpy.random.choice(nahuel_success_lines)] Nahuel successfully completed: [goal_nahuel]."
        else:
            "[renpy.random.choice(nahuel_fail_lines)] Nahuel's attempt at [goal_nahuel] ended in disaster."
        $ goal_nahuel = ""
    return