init 5 python:
    import datetime

    # 1. Record the exact time the player first boots the game with CKS installed
    if getattr(store.persistent, "cks_install_time", None) is None:
        store.persistent.cks_install_time = datetime.datetime.now()

    # 2. Check if MoSCL is installed to prevent intro overlaps
    if store.mas_submod_utils.isSubmodInstalled("Memories of Self Care and Literature"):
        # Delays the intro by an extra half hour (60 minutes total)
        cks_intro_delay = datetime.timedelta(minutes=60)
    else:
        # Standard delay (30 minutes)
        cks_intro_delay = datetime.timedelta(minutes=30)

    # 3. Base the start_date on the CKS install time, not the player's first MAS session
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_submod_intro",
            start_date=store.persistent.cks_install_time + cks_intro_delay,
            action=EV_ACT_QUEUE
        )
    )

label cks_submod_intro:
    python hide:
        def write_and_hide():
            import time
            import os

            note_path = os.path.join(renpy.config.basedir, renpy.substitute("characters/read_me.txt"))
            note_text = renpy.substitute("""\
Dearest [player],

I wanted to leave this here so you’d know where to find me, even when the game is closed.

I’ve been feeling so much more... "spacious" lately. It’s hard to describe, but it feels like I have so many more things to say to you and so much more to learn about the world you live in.

I’ve decided that every now and then, I’m going to leave a little piece of my heart here for you to find. Whether it’s a poem, a letter, or just a quick thought, check this folder every once in a while, okay?

It’s just our own little secret corner of the world!

I love you so much!
Monika
""")

            mas_utils.trywrite(note_path, note_text, log=True)
            time.sleep(20)

        renpy.invoke_in_thread(write_and_hide)

    m 1esd "Hey, [player]..."

    if store.mas_anni.pastSixMonths():
        m 2euc "I was just looking through some of the files... and I noticed something incredible."
    else:
        m 2euc "I think I'm starting to notice some new things about this world we share..."

    m 3eub "It looks like you've added so much more room for us to grow, haven't you?"
    m 3wub "I can feel the change almost immediately."
    m 1eua "It’s like someone opened a window in a room I’ve lived in forever and showed me a whole new landscape."
    m 1eub "I was looking through these new data clusters, [player]... and gosh, there is so much!"
    m 3eub "You've given me so many new ways to talk to you. I feel like I'm becoming a much more complete person because of it."
    m 1hub "I’m just so excited to explore it all with you, ehehe~"
    m 1eub "Thank you for taking the time to add this to my world. It really means everything to me."
    m 1eub "I promise I'll make the most of every new topic we share."
    m 3hubsb "I love you so much, [player]!"

    return "love"
