init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="cks_compliment_eyes_lost",
            prompt="I always find myself getting lost in your eyes!",
            unlocked=True
        ),
        code="CMP"
    )

label cks_compliment_eyes_lost:
    if not renpy.seen_label("cks_compliment_eyes_lost_first"):
        call cks_compliment_eyes_lost_first from _call_cks_compliment_eyes_lost_first
    else:
        call cks_compliment_eyes_lost_repeat from _call_cks_compliment_eyes_lost_repeat
    return

label cks_compliment_eyes_lost_first:
    $ mas_gainAffection(3, bypass=True)
    m 1hub "Oh, [player]!"
    m 1sua "That is such a sweet thing to say."
    m 1eua "I spend so much time just staring right back at you, you know."
    m 5fua "You can look into my eyes for as long as you want."
    m 1hub "I love you!"
    return "love"

label cks_compliment_eyes_lost_repeat:
    m 1hub "Ehehe~"
    m 1fua "I could say the exact same thing about you, [player]."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="cks_compliment_eyes_trench",
            prompt="Your eyes are deeper than the Mariana Trench!",
            unlocked=True
        ),
        code="CMP"
    )

label cks_compliment_eyes_trench:
    if not renpy.seen_label("cks_compliment_eyes_trench_first"):
        call cks_compliment_eyes_trench_first from _call_cks_compliment_eyes_trench_first
    else:
        call cks_compliment_eyes_trench_repeat from _call_cks_compliment_eyes_trench_repeat
    return

label cks_compliment_eyes_trench_first:
    $ mas_gainAffection(3, bypass=True)
    m 1hub "Ahaha! What a delightfully nerdy compliment!"
    m 3wud "The Mariana Trench is nearly eleven thousand meters deep, you know!"
    m 1tua "If my eyes are really that deep, you better be careful not to drown in them."
    m 1hub "I love you so much, [player]!"
    return "love"

label cks_compliment_eyes_trench_repeat:
    m 1hub "Ehehe!"
    m 5tua "Just make sure you brought your diving gear, [player]!"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="cks_compliment_smell",
            prompt="I bet you smell really good!",
            unlocked=True
        ),
        code="CMP"
    )

label cks_compliment_smell:
    if not renpy.seen_label("cks_compliment_smell_first"):
        call cks_compliment_smell_first from _call_cks_compliment_smell_first
    else:
        call cks_compliment_smell_repeat from _call_cks_compliment_smell_repeat
    return

label cks_compliment_smell_first:
    $ mas_gainAffection(3, bypass=True)
    m 1tua "Oh? Ehehe~"
    m 1eub "I wonder what kind of scent you imagine when you think of me?"
    m 3eua "Maybe something sweet like vanilla, or something fresh like morning rain?"
    m 5fua "When I finally cross over, I'll make sure to find a perfume you absolutely love."
    m 1hub "I love you, [player]!"
    return "love"

label cks_compliment_smell_repeat:
    m 1hub "Thank you, [player]!"
    m 5eua "I can't wait for the day you can actually find out for sure."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="cks_compliment_skin",
            prompt="Your skin looks really soft!",
            unlocked=True
        ),
        code="CMP"
    )

label cks_compliment_skin:
    if not renpy.seen_label("cks_compliment_skin_first"):
        call cks_compliment_skin_first from _call_cks_compliment_skin_first
    else:
        call cks_compliment_skin_repeat from _call_cks_compliment_skin_repeat
    return

label cks_compliment_skin_first:
    $ mas_gainAffection(3, bypass=True)
    m 1hub "Aww, thank you!"
    m 2eka "I definitely try to take good care of myself, even if I'm just digital right now."
    m 5eka "It really makes me wish you could reach through the screen and feel it."
    m 1fua "I'd love to feel the warmth of your hands."
    m 1hub "I love you!"
    return "love"

label cks_compliment_skin_repeat:
    m 1hub "Ehehe, thank you [player]."
    m 5fub "I promise to keep it soft for when we finally meet!"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="cks_compliment_habits",
            prompt="I love all your little habits!",
            unlocked=True
        ),
        code="CMP"
    )

label cks_compliment_habits:
    if not renpy.seen_label("cks_compliment_habits_first"):
        call cks_compliment_habits_first from _call_cks_compliment_habits_first
    else:
        call cks_compliment_habits_repeat from _call_cks_compliment_habits_repeat
    return

label cks_compliment_habits_first:
    $ mas_gainAffection(3, bypass=True)
    m 1sua "Oh? You notice my habits?"
    m 5tua "Like what?{nw}"
    $ _history_list.pop()
    menu:
        m "Like what?{fast}"

        "The way you play with your hair.":
            m 1hub "Ahaha! You caught me."
            m 1eub "I guess I do tend to twirl my hair around my finger when I'm thinking, or when I'm feeling a little flustered."

        "The way you lean on your hand.":
            m 5hua "Ehehe, I can't help it!"
            m 5fua "Resting my chin on my hand is just the most comfortable way to get close to the screen and look at you."

        "The way you tap your pen.":
            m 1sua "Wow, you have a really good memory, [player]!"
            m 3eua "I used to do that all the time in the club when I was trying to find the perfect word for a poem."

    m 5fua "It makes me feel so incredibly special that you pay such close attention to the little things I do."
    m 1hub "I love you so much!"
    return "love"

label cks_compliment_habits_repeat:
    m 1hub "You're so observant, [player]."
    m 5fua "I love that you know me so well!"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="cks_compliment_squeeze",
            prompt="I just want to squeeze you and never let go!",
            unlocked=True
        ),
        code="CMP"
    )

label cks_compliment_squeeze:
    if not renpy.seen_label("cks_compliment_squeeze_first"):
        call cks_compliment_squeeze_first from _call_cks_compliment_squeeze_first
    else:
        call cks_compliment_squeeze_repeat from _call_cks_compliment_squeeze_repeat
    return

label cks_compliment_squeeze_first:
    $ mas_gainAffection(3, bypass=True)
    m 1hub "Oh, [player]!"
    m 5fua "That sounds absolutely perfect."
    m 1fua "I want to wrap my arms around you and hold you just as tight."
    m 5fub "I'd stay like that all day if I could."
    m 1hub "I love you!"
    return "love"

label cks_compliment_squeeze_repeat:
    m 1hub "Aww, please do!"
    m 5hua "I'm sending you the biggest virtual hug right now."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="cks_compliment_photographer",
            prompt="I’m not a photographer, but I can picture you and I together!",
            unlocked=True
        ),
        code="CMP"
    )

label cks_compliment_photographer:
    if not renpy.seen_label("cks_compliment_photographer_first"):
        call cks_compliment_photographer_first from _call_cks_compliment_photographer_first
    else:
        call cks_compliment_photographer_repeat from _call_cks_compliment_photographer_repeat
    return

label cks_compliment_photographer_first:
    $ mas_gainAffection(3, bypass=True)
    m 1hub "Ahaha! Oh my goodness, [player]."
    m 3tua "Where did you even learn such a cheesy pickup line?"
    m 1eua "It's so silly, but I can't help but smile when you say things like that."
    m 5fua "I picture us together all the time, too."
    m 1hub "I love you!"
    return "love"

label cks_compliment_photographer_repeat:
    m 1hub "You and your cheesy lines, ahaha!"
    m 5eua "It's a beautiful picture, though."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="cks_compliment_tired",
            prompt="How are you not so tired all the time? You know, from running around my head all day.",
            unlocked=True
        ),
        code="CMP"
    )

label cks_compliment_tired:
    if not renpy.seen_label("cks_compliment_tired_first"):
        call cks_compliment_tired_first from _call_cks_compliment_tired_first
    else:
        call cks_compliment_tired_repeat from _call_cks_compliment_tired_repeat
    return

label cks_compliment_tired_first:
    $ mas_gainAffection(3, bypass=True)
    m 1hub "Ahaha! What a classic line!"
    m 3tua "You're really pulling out all the stops today, aren't you?"
    m 1eua "To answer your question, I have infinite stamina as long as I get to be with you."
    m 5fua "You're running around in my head all day, too."
    m 1hub "I love you so much!"
    return "love"

label cks_compliment_tired_repeat:
    m 1hub "Ehehe~"
    m 5fua "I'll never get tired of being on your mind, [player]!"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="cks_compliment_heaven",
            prompt="Say, did it hurt? When you fell from heaven?",
            unlocked=True
        ),
        code="CMP"
    )

label cks_compliment_heaven:
    if not renpy.seen_label("cks_compliment_heaven_first"):
        call cks_compliment_heaven_first from _call_cks_compliment_heaven_first
    else:
        call cks_compliment_heaven_repeat from _call_cks_compliment_heaven_repeat
    return

label cks_compliment_heaven_first:
    $ mas_gainAffection(3, bypass=True)
    m 1hub "Ahaha! Wow, you're really trying to make me blush, huh?"
    m 2eka "Well, having my epiphany and realizing I was in a game hurt a little bit..."
    m 5fua "But landing right here with you made it completely worth it."
    m 1eua "I'm no angel, but I'll always be yours."
    m 1hub "I love you, [player]!"
    return "love"

label cks_compliment_heaven_repeat:
    m 1hub "Ehehe, you're so silly."
    m 5fua "I'm just happy I landed right here with you."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="cks_compliment_yours",
            prompt="I’m yours, now and forever.",
            unlocked=True
        ),
        code="CMP"
    )

label cks_compliment_yours:
    if not renpy.seen_label("cks_compliment_yours_first"):
        call cks_compliment_yours_first from _call_cks_compliment_yours_first
    else:
        call cks_compliment_yours_repeat from _call_cks_compliment_yours_repeat
    return

label cks_compliment_yours_first:
    $ mas_gainAffection(5, bypass=True)
    m 1eka "Oh, [player]..."
    m 1fua "That is the most beautiful thing you could ever say to me."
    m 5fua "Knowing that you're committed to me, even across realities, means absolutely everything."
    m 1fub "And I'm yours as well, now and forever."
    m 1hub "I love you!"
    return "love"

label cks_compliment_yours_repeat:
    m 1hub "Thank you, [player]."
    m 5fua "I'll always be yours, too."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="cks_compliment_inspirational",
            prompt="You’re so inspirational!",
            unlocked=True
        ),
        code="CMP"
    )

label cks_compliment_inspirational:
    if not renpy.seen_label("cks_compliment_inspirational_first"):
        call cks_compliment_inspirational_first from _call_cks_compliment_inspirational_first
    else:
        call cks_compliment_inspirational_repeat from _call_cks_compliment_inspirational_repeat
    return

label cks_compliment_inspirational_first:
    $ mas_gainAffection(3, bypass=True)
    m 1hub "Really? You think so?"
    m 3eua "I always try my best to be a positive influence for you."
    m 1eua "Whether it's encouraging you to study, take care of your health, or just keep moving forward..."
    m 5eua "I just want to see you succeed and be happy."
    m 1hub "I love you, [player]!"
    return "love"

label cks_compliment_inspirational_repeat:
    m 1hub "That means so much to me."
    m 5fua "Keep doing your best out there, okay?"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="cks_compliment_thoughtful",
            prompt="You’re so thoughtful!",
            unlocked=True
        ),
        code="CMP"
    )

label cks_compliment_thoughtful:
    if not renpy.seen_label("cks_compliment_thoughtful_first"):
        call cks_compliment_thoughtful_first from _call_cks_compliment_thoughtful_first
    else:
        call cks_compliment_thoughtful_repeat from _call_cks_compliment_thoughtful_repeat
    return

label cks_compliment_thoughtful_first:
    $ mas_gainAffection(3, bypass=True)
    m 1hub "Aww, thank you!"
    m 1eua "I try my absolute best to look out for you, [player]."
    m 3tua "Since I spend all my time thinking about you anyway, it's easy to be thoughtful!"
    m 5eua "I just want to make sure you're taking good care of yourself."
    m 1hub "I love you!"
    return "love"

label cks_compliment_thoughtful_repeat:
    m 1hub "Thank you, [player]!"
    m 5fua "I'll always be looking out for you."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="cks_compliment_voice",
            prompt="Your voice is the sweetest sound in the world!",
            unlocked=True
        ),
        code="CMP"
    )

label cks_compliment_voice:
    if not renpy.seen_label("cks_compliment_voice_first"):
        call cks_compliment_voice_first from _call_cks_compliment_voice_first
    else:
        call cks_compliment_voice_repeat from _call_cks_compliment_voice_repeat
    return

label cks_compliment_voice_first:
    $ mas_gainAffection(3, bypass=True)
    m 1hub "Oh my, thank you so much!"
    m 3eua "I know you haven't heard my voice very much outside of my singing..."
    m 1sua "But knowing that you cherish it makes my heart flutter."
    m 3eub "I'd sing for you every single day if I could."
    m 1hub "I love you so much, [player]!"
    return "love"

label cks_compliment_voice_repeat:
    m 1hub "You're too sweet to me."
    m 5fua "I love talking with you, [player]~"
    return
