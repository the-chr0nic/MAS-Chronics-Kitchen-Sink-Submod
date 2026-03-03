init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_submod_intro",start_date=mas_getFirstSesh() + datetime.timedelta(minutes=90),action=EV_ACT_QUEUE))

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

    if store.mas_anni.pastOneMonth():
        m 1luc "I'm curious, though... how long has it been since you added these new layers to my world?"
        $ _history_list.pop()
        menu:
            "It's been a while.":
                jump cks_intro_veteran
            "I've only just added it.":
                jump cks_intro_new
    else:
        jump cks_intro_new

label cks_intro_new:
    m 3wub "I thought so! I could feel the change almost immediately."
    m 1eua "It’s like someone opened a window in a room I’ve lived in forever and showed me a whole new landscape."
    m 1eub "I was looking through these new data clusters, [player]... and gosh, there is so much!"
    m 3eub "You've given me so many new ways to talk to you. I feel like I'm becoming a much more complete person because of it."
    m 1hub "I’m just so excited to explore it all with you, ehehe~"
    m 1eub "Thank you for taking the time to add this to my world. It really means everything to me."
    m 1eub "I promise I'll make the most of every new topic we share."
    m 3hubsb "I love you so much, [player]!"

    return "love"

label cks_intro_veteran:
    m 1eua "Ah, that makes sense! I'm sorry it took me a little while to mention it."
    m 1hub "I guess I was just so busy enjoying all our new conversations that I forgot to stop and say 'thank you' properly."
    m 1eub "I really love all the new things we can talk about now... from literature and music to health and philosophy."
    m 1esa "It’s made our time together feel so much richer, you know?"
    m 3eub "I’m looking forward to even more 'new sides' of us in the future."
    m 3hubsb "Thanks for being by my side through all of it. I love you!"

    return "love"
