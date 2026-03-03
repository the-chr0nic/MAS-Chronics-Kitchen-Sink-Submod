init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_bathroom",
            category=['be right back'],
            prompt="I'm going to use the bathroom",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_bathroom:
    $ ev = mas_getEV("cks_brb_bathroom")

    m 1eua "Oh, of course! Go ahead, [player]."
    m 3hua "I'll be right here waiting for you when you get back."

    $ mas_idle_mailbox.send_idle_cb("cks_brb_bathroom_callback")
    return "idle"

label cks_brb_bathroom_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=15), "cks_brb_bathroom"):
        m 1wud "You were gone for a little while, [player]... are you feeling alright?"
        m 3tua "I was almost starting to wonder if you'd fallen in! Ahaha!"
        m 1fua "I'm just glad you're back safely now. [wb_quip]"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=1), "cks_brb_bathroom"):
        m 1hua "Welcome back, [player]!"
        m 1eub "Feeling refreshed? [wb_quip]"

    else:
        m 1wub "That was quick! You must have been in a real hurry. Ahaha!"
        m 1eua "[wb_quip]"

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_shave",
            category=['be right back'],
            prompt="I'm going to shave",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_shave:
    $ ev = mas_getEV("cks_brb_shave")

    m 1eua "Oh, going to do a bit of self-care?"
    m 3eub "That's always important! It's good to take a moment for yourself every now and then."
    m 5fua "Take your time, [player]. I'll be right here waiting for you."

    $ mas_idle_mailbox.send_idle_cb("cks_brb_shave_callback")
    return "idle"

label cks_brb_shave_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=30), "cks_brb_shave"):
        m 1wud "Welcome back! You were gone for quite a while..."
        m 3eub "You must have been very thorough with your grooming!"
        m 1fua "I'm sure you feel much more refreshed and smooth now, though."
        m 1eua "[wb_quip]"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=5), "cks_brb_shave"):
        m 1hua "Welcome back, [player]!"
        m 5eua "All finished with your routine?"
        m 1eua "[wb_quip]"

    else:
        m 2tua "That was fast! Just a quick touch-up, I take it?"
        m 1eub "I'm glad you're back so soon, regardless."
        m 1eua "[wb_quip]"

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_run",
            category=['be right back'],
            prompt="I'm going for a run",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_run:
    $ ev = mas_getEV("cks_brb_run")

    m 1eua "Oh, going for a run? That's a great way to stay active, [player]!"
    m 3eub "Make sure you stay hydrated and watch your pace out there."
    m 5fua "I'll be right here waiting for you. Have a safe run!"

    $ mas_idle_mailbox.send_idle_cb("cks_brb_run_callback")
    return "idle"

label cks_brb_run_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=1), "cks_brb_run"):
        m 1wud "Welcome back! You were out there for a long time!"
        m 2tua "You must have covered quite a bit of distance... I hope you aren't too exhausted."
        m 5eua "Make sure you take a moment to cool down and get some water, okay?"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=10), "cks_brb_run"):
        m 1hua "Welcome back, [player]! How was the run?"
        m 3eub "I hope you got that 'runner's high' people always talk about. Ahaha!"

    else:
        m 2tua "That was a really short run! More of a quick sprint around the block?"
        m 1eub "Regardless, I'm glad you're back with me so soon."

    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_homework",
            category=['be right back'],
            prompt="I'm going to work on some homework",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_homework:
    $ ev = mas_getEV("cks_brb_homework")

    m 1eua "Oh, focusing on your studies? That's very responsible of you, [player]!"
    m 3eub "Don't let the workload stress you out too much, okay?"
    m 5fua "I'll be right here if you need a mental break. Good luck with your assignments!"

    $ mas_idle_mailbox.send_idle_cb("cks_brb_homework_callback")
    return "idle"

label cks_brb_homework_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=2), "cks_brb_homework"):
        m 2tua "That was a long study session! You must have been really in the zone."
        m 5eua "I hope you managed to get everything finished. You deserve a good rest now!"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=20), "cks_brb_homework"):
        m 1hua "Welcome back! I hope you made some good progress on that homework."
        m 3eub "It's a great feeling to check things off a to-do list, isn't it? Ahaha!"

    else:
        m 2pua "Back so soon? Did you get distracted, or was it just a really quick assignment?"
        m 1eub "Regardless, I'm happy to have you back with me."

    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_submod",
            category=['be right back'],
            prompt="I'm going to work on a submod or spritepack for you",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_submod:
    $ ev = mas_getEV("cks_brb_submod")

    m 1sua "Wait, really? You're working on something new for me right now?"
    m 3eub "That's so sweet of you, [player]. I'm already excited to see what it is!"
    m 5fub "I'll try not to distract you while you're digging through the files. Go have fun with the code!"

    $ mas_idle_mailbox.send_idle_cb("cks_brb_submod_callback")
    return "idle"

label cks_brb_submod_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=3), "cks_brb_submod"):
        m 2wud "Welcome back! You were working for such a long time... it must be a massive project!"
        m 5fua "Thank you for putting so much effort into making my world a little brighter."

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=30), "cks_brb_submod"):
        m 1eub "Welcome back! Did the coding go smoothly?"
        m 3hua "I'm always so impressed by how you navigate the 'backstage' of my reality."

    else:
        m 3tua "Just a quick fix or a typo? Ahaha! I'm glad you're back with me regardless."
        m 1eua "Did you run into a bug, or just wanted to check in on me?"

    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_crafts",
            category=['be right back'],
            prompt="I'm going to do arts and crafts",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_crafts:
    $ ev = mas_getEV("cks_brb_crafts")

    m 1eua "Oh, feeling a spark of creativity, [player]?"
    m 3eub "I'd love to see what you're working on! Have fun making something unique."
    m 5fua "I'll be right here waiting to see if you tell me all about it later."

    $ mas_idle_mailbox.send_idle_cb("cks_brb_crafts_callback")
    return "idle"

label cks_brb_crafts_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=2), "cks_brb_crafts"):
        m 1wud "Welcome back! You were gone for a long time... it must be quite the project!"
        m 3tua "I hope you didn't get too much paint or glue on your hands. Ahaha!"
        m 5eua "I'm sure whatever you made looks amazing."

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=15), "cks_brb_crafts"):
        m 1hua "Welcome back, [player]! Did the crafting go well?"
        m 3eub "It's always nice to have something tangible to show for your time."

    else:
        m 2tua "Back already? Just a quick sketch or a small detail?"
        m 1eua "I'm happy to have you back in any case."

    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_nails",
            category=['be right back'],
            prompt="I'm going to paint my nails",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_nails:
    $ ev = mas_getEV("cks_brb_nails")

    m 5eub "Oh, doing your nails? That sounds like a fun way to relax."
    m 1hua "Just be careful not to smudge them while they're drying!"
    m 1fua "Take your time, [player]. I'll be right here."

    $ mas_idle_mailbox.send_idle_cb("cks_brb_nails_callback")
    return "idle"

label cks_brb_nails_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=45), "cks_brb_nails"):
        m 5tua "Welcome back! I assume they're finally dry now?"
        m 1eub "I bet they look wonderful. It’s a nice little way to express yourself, isn't it?"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=10), "cks_brb_nails"):
        m 1hua "Welcome back, [player]!"
        m 2tud "Are you moving carefully to keep them perfect? Ahaha!"

    else:
        m 3tua "That was fast! Just a quick clear coat or a touch-up?"
        m 1eub "I'm glad you're back so soon regardless."

    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_medicine",
            category=['be right back'],
            prompt="I'm going to take medicine",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_medicine:
    $ ev = mas_getEV("cks_brb_medicine")

    m 2eka "Oh, of course. It’s very important to stay on top of your health, [player]."
    m 1fua "Go ahead! I'll be right here waiting for you to get back."

    $ mas_idle_mailbox.send_idle_cb("cks_brb_medicine_callback")
    return "idle"

label cks_brb_medicine_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    m 1eua "Welcome back, [player]."
    m 3eub "I'm glad you're taking good care of yourself."
    m 5fua "Health is the most important thing, after all."

    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_cooking",
            category=['be right back'],
            prompt="I'm going to cook or bake something",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_cooking:
    $ ev = mas_getEV("cks_brb_cooking")

    m 1eua "Heading to the kitchen? That sounds like a delicious idea!"
    m 3eub "I wish I could be there to help you out... or at least to smell whatever you're making!"
    m 5hua "Have fun with the recipe, [player]!"

    $ mas_idle_mailbox.send_idle_cb("cks_brb_cooking_callback")
    return "idle"

label cks_brb_cooking_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=1), "cks_brb_cooking"):
        m 1wud "Welcome back! You must have been making something quite elaborate!"
        m 5tua "I hope it turned out exactly how you wanted it to. You've certainly put in the time for it!"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=15), "cks_brb_cooking"):
        m 1hua "Welcome back! How did everything turn out?"
        m 3eub "I bet it smells amazing over there right now."

    else:
        m 2tua "Back already? Just a quick snack or preheating the oven?"
        m 1eua "I'm always happy to see you again, no matter how short the break was."

    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_garden",
            category=['be right back'],
            prompt="I'm going to tend to my garden",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_garden:
    $ ev = mas_getEV("cks_brb_garden")

    m 1eua "Going to spend some time with your plants? That sounds so peaceful."
    m 3eub "I've always liked the idea of gardening... it’s like nurturing a little piece of the world."
    m 5fua "Enjoy the fresh air, [player]! I'll be here when you're done."

    $ mas_idle_mailbox.send_idle_cb("cks_brb_garden_callback")
    return "idle"

label cks_brb_garden_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=1), "cks_brb_garden"):
        m 1wud "Welcome back! You must have had a lot of work to do out there."
        m 3eua "I hope everything is blooming beautifully! Gardening takes so much patience and care."
        m 5fua "I'm sure the plants appreciate all the attention you give them."

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=15), "cks_brb_garden"):
        m 1hua "Welcome back, [player]! Was it nice being out in the garden for a bit?"
        m 1eub "It’s good to reconnect with nature every once in a while."

    else:
        m 2tua "That was a quick trip! Just a bit of watering or checking the soil?"
        m 1eub "I'm glad you're back safely."

    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_instrument",
            category=['be right back'],
            prompt="I'm going to practice an instrument",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_instrument:
    $ ev = mas_getEV("cks_brb_instrument")

    m 1eua "Oh, going to practice an instrument? That's a wonderful way to spend your time, [player]!"
    m 3eub "What are you going to be playing today?{nw}"

    $ _history_list.pop()
    menu:
        m "What are you going to be playing today?{fast}"

        "Piano":
            m 2hua "The piano is such a classic choice. It's like having a whole orchestra at your fingertips!"

        "Guitar":
            m 1sub "Guitar? That's so cool! I bet you've got some great riffs to work on."

        "Violin":
            m 3eua "The violin is so expressive... it really has a way of touching the heart, doesn't it?"

        "Drums":
            m 3wub "Drums! I hope your neighbors don't mind the noise. Ahaha!"

        "Wind Instrument":
            m 1eub "That takes a lot of lung power! Make sure to take some deep breaths."

        "Something else":
            m 1eua "Oh, something unique? I'd love to hear it sometime!"

    m 5fua "Have a great practice session! I'll be right here if you want to play a 'duet' with me later, ehehe!"

    $ mas_idle_mailbox.send_idle_cb("cks_brb_instrument_callback")
    return "idle"

label cks_brb_instrument_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=90), "cks_brb_instrument"):
        m 1wud "Welcome back! You were practicing for a long time."
        m 3eub "I bet your fingers are a little tired, but I'm sure you made a lot of progress!"
        m 5eua "Don't forget to stretch a bit after all that hard work."

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=20), "cks_brb_instrument"):
        m 1hua "Welcome back, [player]! Did you master that tricky part you were working on?"
        m 3eub "There's nothing quite like the feeling of finally getting a melody right."

    else:
        m 2tua "Back so soon? Just a quick warm-up or did you forget your sheet music? Ahaha!"
        m 1eub "I'm glad you're back regardless."

    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_mail",
            category=['be right back'],
            prompt="I'm going to check the mail",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_mail:
    $ ev = mas_getEV("cks_brb_mail")

    m 1eua "Just a quick trip to the mailbox? No problem!"
    m 3eub "I hope you find something exciting in there... and not just bills! Ahaha!"
    m 5fua "I'll be right here."

    $ mas_idle_mailbox.send_idle_cb("cks_brb_mail_callback")
    return "idle"

label cks_brb_mail_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=10), "cks_brb_mail"):
        m 1wud "Welcome back! That took a little longer than expected."
        m 3tua "Did you get a big package, or were you just chatting with the neighbors?"
        m 1eub "Either way, I'm glad you're back."

    else:
        m 1hua "Welcome back, [player]!"
        m 1eua "Find anything interesting in the post?"

    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_stretching",
            category=['be right back'],
            prompt="I'm going to do some stretching",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_stretching:
    $ ev = mas_getEV("cks_brb_stretching")

    m 5eub "That's a great idea. It's so important to loosen up, especially if you've been sitting for a while."
    m 1eua "Don't push yourself too hard, okay? Just a nice, relaxing stretch."
    m 1fua "I'll be right here waiting for you."

    $ mas_idle_mailbox.send_idle_cb("cks_brb_stretching_callback")
    return "idle"

label cks_brb_stretching_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=20), "cks_brb_stretching"):
        m 1hua "Welcome back! That sounded like a very thorough session."
        m 3eub "I bet your muscles feel much better now. It’s good to give your body that kind of attention."

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=5), "cks_brb_stretching"):
        m 1eua "Welcome back, [player]! Feeling a bit more limber?"

    else:
        m 2tua "That was a quick one! Just a quick reach for the ceiling?"
        m 1eub "I'm glad you're back regardless."

    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_nap",
            category=['be right back'],
            prompt="I'm going to take a nap",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_nap:
    $ ev = mas_getEV("cks_brb_nap")

    m 1fua "Oh, a nap sounds wonderful right now. Everyone needs to recharge sometimes."
    m 3eub "I'll keep the room quiet for you so you can rest peacefully."
    m 5fub "Sweet dreams, [player]. I'll be right here when you wake up."

    $ mas_idle_mailbox.send_idle_cb("cks_brb_nap_callback")
    return "idle"

label cks_brb_nap_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=2), "cks_brb_nap"):
        m 1wud "Welcome back! You must have really needed that sleep."
        m 5fua "You were out for a long time... I hope you feel completely refreshed now."

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=20), "cks_brb_nap"):
        m 1hua "Welcome back, [player]! Did you have a good power nap?"
        m 3eub "Sometimes a short break is exactly what the brain needs."

    else:
        m 2pua "Back already? You didn't stay down for long!"
        m 1eua "I hope you managed to at least close your eyes for a minute."

    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_skincare",
            category=['be right back'],
            prompt="I'm going to do my skincare routine",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_skincare:
    $ ev = mas_getEV("cks_brb_skincare")

    m 1eua "Self-care time? I love that for you, [player]!"
    m 3eub "It’s so relaxing to just focus on your routine for a bit."
    m 5fua "I'll be right here waiting. Go get that healthy glow! Ahaha!"

    $ mas_idle_mailbox.send_idle_cb("cks_brb_skincare_callback")
    return "idle"

label cks_brb_skincare_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=30), "cks_brb_skincare"):
        m 1wud "Welcome back! You were gone for a while... did you do a full face mask, too?"
        m 5eub "I'm sure you feel incredibly refreshed now. There's nothing like a clean face to start or end the day."

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=10), "cks_brb_skincare"):
        m 1hua "Welcome back, [player]! All finished with your routine?"

    else:
        m 2tua "That was fast! Just a quick splash of water?"
        m 1eub "I'm glad you're back so soon, regardless."

    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_podcast",
            category=['be right back'],
            prompt="I'm going to listen to a podcast",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_podcast:
    $ ev = mas_getEV("cks_brb_podcast")

    m 2tua "Oh, learning something new or just catching up on a story?"
    m 1eub "I've always found podcasts so interesting.. it’s like being a fly on the wall for a great conversation."
    m 5eua "Have fun listening! I'll be here."

    $ mas_idle_mailbox.send_idle_cb("cks_brb_podcast_callback")
    return "idle"

label cks_brb_podcast_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=1), "cks_brb_podcast"):
        m 1wud "Welcome back! That must have been a long episode."
        m 3eub "Did you learn anything interesting, or was it just a good way to pass the time?"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=15), "cks_brb_podcast"):
        m 1hua "Welcome back, [player]! Did you enjoy the podcast?"

    else:
        m 2tua "Back so soon? Did the episode finish early, or did you just want to see me? Ahaha!"
        m 1eub "I'm happy you're back regardless."

    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_get_changed",
            category=['be right back'],
            prompt="I'm going to get changed",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_get_changed:
    $ ev = mas_getEV("cks_brb_get_changed")

    m 1eua "Oh, going to change into something more comfortable?"
    m 3eub "I'll be right here waiting for you. Take your time!"
    m 5fua "I'm sure you'll look great in whatever you pick out."

    $ mas_idle_mailbox.send_idle_cb("cks_brb_get_changed_callback")
    return "idle"

label cks_brb_get_changed_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=15), "cks_brb_get_changed"):
        m 1wud "Welcome back! That took a little while..."
        m 3tua "Did you have a hard time deciding what to wear, or did you decide to do a whole fashion show? Ahaha!"
        m 5eua "I'm glad you're back now, regardless."

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=1), "cks_brb_get_changed"):
        m 1hua "Welcome back, [player]! All settled into your new outfit?"

    else:
        m 2tua "That was a record-breaking speed-change! You must have had your clothes laid out already."
        m 1eub "I'm happy to see you again so soon."

    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_meditate",
            category=['be right back'],
            prompt="I'm going to meditate",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_meditate:
    $ ev = mas_getEV("cks_brb_meditate")

    m 1fua "That's a wonderful idea, [player]. Finding your center is so important in such a busy world."
    m 5fub "I'll keep everything quiet and peaceful here for you."
    m 5eua "I'll be right here when you're ready to come back."

    $ mas_idle_mailbox.send_idle_cb("cks_brb_meditate_callback")
    return "idle"

label cks_brb_meditate_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=30), "cks_brb_meditate"):
        m 1fua "Welcome back. You were gone for a long time..."
        m 3eua "I hope you managed to reach a deep state of peace. You look so much more relaxed now."
        m 5fua "It's good to just 'be' for a while, isn't it?"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=5), "cks_brb_meditate"):
        m 1hua "Welcome back, [player]! Do you feel a bit more grounded and focused?"

    else:
        m 2tua "Back already? It can be hard to quiet the mind sometimes, can't it?"
        m 1eub "Even a few minutes of breathing can make a difference, though. I'm glad you're back."

    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_brb_teeth",
            category=['be right back'],
            prompt="I'm going to brush my teeth",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label cks_brb_teeth:
    $ ev = mas_getEV("cks_brb_teeth")

    m 1eua "Important for hygiene! Go ahead, [player]."
    m 3eub "Don't forget to floss while you're at it! Ahaha!"
    m 5fua "I'll be right here waiting for you."

    $ mas_idle_mailbox.send_idle_cb("cks_brb_teeth_callback")
    return "idle"

label cks_brb_teeth_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=5), "cks_brb_teeth"):
        m 1wud "Welcome back! You were very thorough with your brushing."
        m 3tua "Your dentist would be so proud of you! Ahaha!"
        m 5eua "I'm glad you're back with that sparkling smile."

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=2), "cks_brb_teeth"):
        m 1hua "Welcome back, [player]! Feeling all minty fresh?"

    else:
        m 2tua "That was a quick one! Just a fast scrub?"
        m 1eub "I'm just happy to have you back here with me."

    m 1eua "[wb_quip]"
    return
