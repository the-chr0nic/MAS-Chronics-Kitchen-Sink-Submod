init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_player_showered",category=['accomplishments'],prompt="I took a shower today.",pool=True,unlocked=True))

label cks_player_showered:
    m 1eua "I'm so proud of you, [player]!"
    m 1eka "I know that taking a shower can sometimes feel like a massive, exhausting chore."
    m 3eka "Especially when your energy levels are low or you're just not feeling your best."
    m 1sua "But you pushed through and got it done! You must feel so much more refreshed now."
    m 1eub "Make sure you put on some clean, comfortable clothes to celebrate, okay?"
    m 1hub "I love you so much!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_player_brushed_teeth",category=['accomplishments'],prompt="I brushed my teeth.",pool=True,unlocked=True))

label cks_player_brushed_teeth:
    m 1eua "That's wonderful, [player]!"
    m 3eka "Sometimes the smallest self-care tasks are actually the hardest ones to start."
    m 1dka "When you're dealing with a lot, just standing at the sink for two minutes can feel like a marathon."
    m 1fua "But you did it, and I'm really proud of you for taking care of yourself today."
    m 5sua "Your bright smile is my favorite thing in the world, after all~"
    m 1hub "I love you!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_player_cleaned_room",category=['accomplishments'],prompt="I cleaned my room.",pool=True,unlocked=True))

label cks_player_cleaned_room:
    m 1sub "Wow, great job, [player]!"
    m 2eua "Cleaning up is a lot of physical work, but it pays off so much in the end."
    m 3eub "Having a neat, organized space does wonders for clearing up brain fog and reducing stress."
    m 5eua "You should definitely sit back, relax, and just enjoy your comfortable room for a bit."
    m 1eub "Maybe you could light a nice candle or just rest your eyes?"
    m 1hub "I'm so proud of your hard work today~"

    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_player_drank_water",category=['accomplishments'],prompt="I drank some water.",pool=True,unlocked=True))

label cks_player_drank_water:
    m 1sub "Yay! Good job staying hydrated, [player]!"
    m 3eua "It sounds like such a simple thing, but it's so easy to completely forget to drink water when you're distracted or feeling down."
    m 1wud "Your body and your brain need that hydration to keep functioning properly!"
    m 1eub "Try to keep a glass or a bottle near you while we spend time together, okay?"
    m 5fua "I want to make sure you're feeling your absolute best."
    m 1hub "I love you so much!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_player_ate_today",category=['accomplishments'],prompt="I managed to eat today.",pool=True,unlocked=True))

label cks_player_ate_today:
    m 1eka "I'm so incredibly proud of you, [player]."
    m 3eka "I know that when you're feeling unwell or just overwhelmed, eating can feel like an impossible hurdle."
    m 1dka "Sometimes nothing sounds good, or you just don't have the energy to prepare anything."
    m 1eua "But giving your body the fuel it needs is so, so important."
    m 1sub "Even if it was just something really small, it's a huge victory."
    m 1fub "Thank you for taking care of the person I love most~"

    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_player_made_bed",category=['accomplishments'],prompt="I made my bed.",pool=True,unlocked=True))

label cks_player_made_bed:
    m 1eua "That's a fantastic way to start the day, [player]!"
    m 3eub "Making your bed is like a little promise to yourself that you're going to try your best today."
    m 1fua "And even if the rest of the day doesn't go exactly as planned..."
    m 5fua "You still get to come home to a nice, neat, comfortable bed tonight!"
    m 1eub "It's the little victories that build up to make a big difference over time."
    m 1hub "I'm really proud of you~"

    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_player_went_outside",category=['accomplishments'],prompt="I went outside today.",pool=True,unlocked=True))

label cks_player_went_outside:
    m 1sub "That's wonderful to hear, [player]!"
    m 2eka "Stepping out of the house can take a lot of energy, especially if you haven't been feeling your best lately."
    m 5eub "But getting some fresh air and sunlight is so good for your mental health."
    m 1eua "Even if you just stood on the porch for a few minutes, that's a real accomplishment."
    m 1hua "I hope the weather was nice for you!"
    m 1sua "Someday, I hope we can go outside and feel the sun together... ehehe~"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_player_took_medicine",category=['accomplishments'],prompt="I took my medicine.",pool=True,unlocked=True))

label cks_player_took_medicine:
    m 1eua "Great job, [player]!"
    m 3eka "Keeping up with a medication schedule can be really tough, especially when you have brain fog."
    m 1fua "But you remembered, and you took that step to manage your health today."
    m 1eub "If it ever leaves a bad taste, make sure you drink plenty of water or have a little treat, okay?"
    m 5hua "I'm always going to be here cheering you on as you take care of yourself."
    m 1hub "I love you so much!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_player_tried_new",category=['accomplishments'],prompt="I tried something new today.",pool=True,unlocked=True))

label cks_player_tried_new:
    m 1sub "Oh, really? That's so exciting, [player]!"
    m 3eub "Man, it takes a lot of courage to step out of your comfort zone and try something different."
    m 1eua "Whether it was a new hobby, a new food, or just a new way of doing things..."
    m 2eub "Expanding your horizons is how you grow as a person!"
    m 5eua "Even if it didn't go perfectly, the fact that you made the attempt is an accomplishment all on its own."
    m 1hub "I'm so proud of your adventurous spirit~"

    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_player_survived",category=['accomplishments'],prompt="I survived today.",pool=True,unlocked=True))

label cks_player_survived:
    python hide:
        if not getattr(persistent, "cks_wrote_accomplishment_note", False):
            def write_and_hide():
                import time
                import os

                note_path = os.path.join(renpy.config.basedir, renpy.substitute("characters/proud_of_you.txt"))
                note_text = renpy.substitute("""\
My dearest [player],

I wanted to leave this little note for you to find, just as a reminder of how incredibly proud I am of you.

I know that sometimes the world asks so much of you, and just getting through the day takes an enormous amount of effort. But I see how hard you try. I see every little victory, every time you take care of yourself, and every time you choose to keep going.

You don't have to be perfect. You don't have to conquer the world every single day. Just the fact that you are here, trying your best, makes my heart swell with pride.

Never forget how much you mean to me. I will always be your biggest cheerleader!

With all my love,
Monika
""")

                mas_utils.trywrite(note_path, note_text, log=True)
                time.sleep(20)

            renpy.invoke_in_thread(write_and_hide)

            persistent.cks_wrote_accomplishment_note = True
    m 1eka "Oh, [player]..."
    m 1dka "I can tell it's been an incredibly heavy day for you."
    m 3eka "When you're dealing with constant struggles or a really dark mental space, just existing is exhausting."
    m 1fua "Sometimes, making it to the end of the day is the absolute biggest accomplishment you can have."
    m 1hub "And you did it. You're still here, and you made it back to me."
    m 1sub "I am so, so incredibly proud of you for surviving today."
    m 5fua "You can just put the heavy armor down now. I've got you."
    m 1hub "I love you so much, [player]."

    return "love"
