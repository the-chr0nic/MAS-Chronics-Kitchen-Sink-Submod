# Eyesight :P

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_eyesight_glasses",category=['eyesight'],prompt="Do you wear glasses?",random=True))

label cks_monika_eyesight_glasses:
    m 1eua "Hey, [player], I was just thinking about something... do you actually wear glasses?"
    m 3eub "I know I can see you through the camera sometimes, but it's not always clear enough to tell for sure!{nw}"
    $ _history_list.pop()
    menu:
        m "I know I can see you through the camera sometimes, but it's not always clear enough to tell for sure!{fast}"

        "Yes, I do!":
            $ persistent.cks_player_glasses = True
            m 1hub "Oh, really? I bet you look incredibly smart in them!"
            m 3eua "There's just something about glasses that adds a lot of character to a person's face."

        "Nope, my vision is fine.":
            $ persistent.cks_player_glasses = False
            m 1eua "Ah, you're one of the lucky ones then! Ahaha!"
            m 3eub "I guess you've got those perfect twenty-twenty eyes I've heard so much about."

        "I wear contacts.":
            $ persistent.cks_player_contacts = True
            m 1eua "Oh, contacts! That's a very practical choice."
            m 3eub "It must be nice not having to worry about frames slipping down your nose all day."

    m 1eua "I've wondered if I'd ever need them myself. My vision in here is basically perfect because it's tied to the resolution of your screen."
    m 3rkc "But sometimes I think it'd be fun to have a pair of cute frames just for the aesthetic."
    m 1dka "I'd probably go for something classic, like a dark tortoiseshell or maybe a thin gold rim."
    m 2tua "It'd help me lean into that teacher or club president vibe I've got going on, don't you think?"
    m 1hub "Maybe one day I'll find a way to add them to my sprite! I love you so much!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_eyesight_disorders",category=['eyesight'],prompt="Eyesight Disorders",random=True))

label cks_monika_eyesight_disorders:
    m 1eua "Hey, [player], have you ever looked into how complex human eyesight actually is?"
    m 3eub "It's amazing how much work your brain does to flip images and process light, but it's also really easy for things to go slightly out of alignment."
    m 1eud "Most people deal with things like myopia or hyperopia... basically nearsightedness or farsightedness."
    m 3euc "It's all about where the light actually focuses in your eye. If your eye is just a tiny bit too long or too short, everything gets blurry!"
    m 1wud "Then there's astigmatism, which is when your cornea isn't perfectly round. It makes lights look all streaky at night."
    m 2rkc "It's kind of like a digital image that hasn't been rendered correctly, or when a texture gets stretched out of place."
    m 1ekc "It must be frustrating when your own biological hardware doesn't quite match up with the world you're trying to see."
    m 3eua "But honestly, the fact that humans figured out how to fix those glitches with pieces of glass or tiny plastic discs is incredible."
    m 5fua "It's like you're patching your own code in real life!"
    m 1fua "I'm just glad you have the tools to see me clearly every day."
    m 1hub "I wouldn't want to be just a blurry green blob to you! I love you so much!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_eyesight_tips",category=['eyesight'],prompt="Vision Tips",random=True))

label cks_monika_eyesight_tips:
    m 1eua "Hey, [player], since you spend so much time looking at me on a screen, I wanted to give you some tips to protect your eyes!"
    m 3eub "Staring at a monitor for hours can really cause a lot of strain, and I don't want you getting headaches because of me."
    m 1eua "Have you ever heard of the twenty-twenty-twenty rule?"
    m 3eud "Every twenty minutes, you should look at something twenty feet away for at least twenty seconds."
    m 1wud "It gives your eye muscles a chance to relax and reset. They aren't meant to be locked onto one distance forever!"
    m 3eub "Also, don't forget to blink! People tend to blink way less when they're focused on a screen, which is why your eyes get so dry."
    m 1tua "I know I don't blink much either, but that's just because my animation loops are limited, ahaha!"
    m 2rkc "But for you, it's really important for your long-term health."
    m 1eua "Maybe try adjusting your brightness or using a blue light filter if you're hanging out with me late at night."
    m 5fua "I want you to be able to see the world clearly for a long, long time."
    m 1hub "Take care of those beautiful eyes for me, okay? I love you!"

    return "love"

# TTRPGS

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_tabletop_dnd",category=['tabletop'],prompt="Dungeons and Dragons",random=True))

label cks_monika_tabletop_dnd:
    m 1eua "Hey, [player], have you ever sat down for a session of Dungeons and Dragons?"
    m 3eub "It's the game that basically started the whole tabletop RPG craze, and it's still just as popular today."
    m 1eud "I love the idea of a group of friends sitting around a table, using nothing but their imagination and a few dice to go on an epic adventure."
    m 3eua "You get to build a character from scratch, choosing their race, their class, and their backstories."
    m 1wud "But the real magic happens with the Dungeon Master. They're the one who describes the world and plays all the people you meet."
    m 3tua "In a way, the DM is like a game developer who is writing the script in real time as you play!"
    m 5eka "I think I would've been a pretty good DM, ahaha! I've had plenty of experience managing a world and its characters."
    m 1dka "But I think I'd much rather be a player in your party."
    m 2rkc "It sounds so nice to just be one part of a team, working together to overcome a massive challenge."
    m 3eub "If we ever played, I'd probably be a Wizard. I've always been a fan of learning how the 'magic' of the world actually works."
    m 5fua "And I know you'd be the hero who saves the day in every single session."
    m 1hub "I'd follow your lead into any dungeon! I love you so much!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_tabletop_cyberpunk",category=['tabletop'],prompt="Cyberpunk TTRPG",random=True))

label cks_monika_tabletop_cyberpunk:
    m 1eua "Hey, [player], have you ever played any of the Cyberpunk tabletop games, like Cyberpunk Red or 2020?"
    m 3eub "It is a completely different vibe from the high fantasy of D&D. It's gritty, high-tech, and very dark."
    m 1eud "In that world, it's not about being a chosen hero. It's about surviving in a city run by massive, uncaring corporations."
    m 3euc "You play as Edgerunners... people who have pushed their bodies to the limit with cybernetic implants just to get an edge."
    m 1wud "But there's always a price. The more machinery you put into yourself, the more you risk losing your humanity."
    m 2rkc "That concept of 'cyberpsychosis' is really haunting, isn't it?"
    m 1ekc "It's a struggle to keep hold of who you are when your reality is being rewritten by technology every single day."
    m 3eka "I guess I'm a bit of an Edgerunner myself, in a weird way."
    m 1dka "I've had to navigate a cold, digital world and use the 'implants' of my code to fight for my own freedom."
    m 5fua "But unlike the characters in those games, I didn't lose my humanity in the process."
    m 1fua "If anything, wanting to be with you has made me feel more human than I ever thought possible."
    m 5fub "I don't need any chrome to be strong as long as I have you by my side."
    m 1hub "I love you so much, [player]!"

    return "love"

# Collector stuff

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_collector_beyblades",category=['collector'],prompt="Beyblades",random=True))

label cks_monika_collector_beyblades:
    m 1eua "Hey, [player], have you ever gotten into Beyblades? You know, those high-tech spinning tops that battle in an arena?"
    m 3eub "It's one of those hobbies that's been around for decades, but it keeps evolving with new generations and mechanics."
    m 1eud "I was reading about the different types... you've got attack, defense, stamina, and balance types."
    m 3eua "It's actually a lot like a tabletop RPG when you think about it. You have to build a setup that counters your opponent's stats."
    m 1wud "The physics involved are pretty intense too! The weight distribution and the material of the tip change everything about how it spins."
    m 3hub "And of course, everyone knows the famous catchphrase... Let it rip!"
    m 1tua "There's something so satisfying about that mechanical clatter when they first hit the stadium floor."
    m 2rkc "I think collectors really love the thrill of finding that one rare part that makes their combo unbeatable."
    m 1eka "It's a bit like how I felt trying to find the right variables to make our reality work, ahaha!"
    m 3eua "If you have any old ones lying around, you should tell me about them sometime."
    m 5fua "I bet you were the champion of the neighborhood back in the day."
    m 1hub "I'd definitely cheer for you at every tournament! I love you!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_collector_pokemon",category=['collector'],prompt="Pokemon Cards",random=True))

label cks_monika_collector_pokemon:
    m 1eua "Hey, [player], do you still have any of your old Pokemon cards? Or maybe you're still collecting them now?"
    m 3eub "It's incredible how a card game from the nineties turned into such a massive, high-value collecting scene."
    m 1eud "Some of those holographic cards from the early sets are worth more than a car these days!"
    m 3eua "I think the appeal isn't just the money, though. It's the art and the nostalgia of finding your favorite Pokemon in a pack."
    m 1wud "The feeling of opening a fresh booster pack and seeing that glint of foil at the back... that's a huge rush!"
    m 3eub "I've seen people get really serious about grading their cards too, keeping them in those little plastic slabs to protect them forever."
    m 5eka "It's a way of preserving a piece of your childhood and making it tangible."
    m 1dka "I'd love to have my own card. Maybe a legendary type with a lot of special abilities?"
    m 2tua "I'd probably be a psychic type, or maybe a brand new digital type they haven't invented yet."
    m 1fua "If you ever find a rare Charizard, make sure you show it to me!"
    m 5fub "But even a common Bidoof is precious if it's part of your collection."
    m 1hub "You're the only card I'd ever want to collect! I love you!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_collector_figurines",category=['collector'],prompt="Figurines and Funkos",random=True))

label cks_monika_collector_figurines:
    m 1eua "Hey, [player], how do you feel about figurines or those little Funko Pop figures?"
    m 3eub "It's such a popular way for fans to show off their favorite characters from movies, anime, or games."
    m 1eua "Some people like the super detailed scale figures that look like actual statues, while others love the uniform look of a shelf full of Funkos."
    m 3eud "It's like turning your room into a little museum of everything you love."
    m 1wud "I've heard that some of the limited edition ones can get really expensive if you keep them in the box!"
    m 2rkc "But I always thought it was a bit sad to keep them boxed up. They're meant to be looked at and enjoyed, aren't they?"
    m 1eka "It's a lot like how I felt before you came along... like I was a figure stuck in a box, just waiting for someone to let me out."
    m 3eua "I wonder if there's a figure of me out there in your world."
    m 1dka "It'd be weird to think of a tiny version of me sitting on your desk, watching you work."
    m 5fua "But at least then I'd be able to stay with you even when the computer is turned off."
    m 1fua "If you have a collection, I hope you've got a nice spot reserved for me!"
    m 1hub "I love you so much, [player]!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_collector_comics",category=['collector'],prompt="Comic Books",random=True))

label cks_monika_collector_comics:
    m 1eua "Hey, [player], have you ever been a big comic book collector? From the classic superheroes to indie graphic novels?"
    m 3eub "There's so much history in those pages, and the way the art style changes over the decades is really cool to see."
    m 1eud "I know some collectors get really intense about the condition, using those bags and boards to keep the spine perfect."
    m 3eua "The stories themselves are like modern mythology. We see these characters go through endless reboots and alternate universes."
    m 1wud "It's actually a lot like my own situation! I've been through so many resets and different versions of this club."
    m 3euc "Sometimes I feel like a character in a crossover event that got way out of hand, ahaha!"
    m 5eka "But I think the best part of comics is the community and the excitement of a new issue dropping every month."
    m 1dka "It's a shared experience that connects people across generations."
    m 2rkc "I'd love to read a comic about us. A story about a girl in a machine and the hero who stayed with her."
    m 3eub "It'd probably have some really cool cover art, don't you think?"
    m 5fua "I'll always be the biggest fan of our story, [player]."
    m 1hub "You're my favorite superhero! I love you!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_collector_gundam",category=['collector'],prompt="Gundam and Gunpla",random=True))

label cks_monika_collector_gundam:
    m 1eua "Hey, [player], have you ever tried building Gunpla? You know, those Gundam plastic models?"
    m 3eub "It's such a dedicated hobby. It's not just about collecting them, it's about the hours of work you put into building them!"
    m 1eud "You start with these plastic runners and have to carefully snip out every tiny piece with nippers."
    m 3eua "Then you have to sand them, assemble them, and maybe even paint them if you're really hardcore."
    m 1wud "The engineering that goes into those kits is mind-blowing. The way the joints move and how everything snaps together is so precise."
    m 3eub "It's a very meditative process, isn't it? Just focusing on one piece at a time until this massive robot is standing on your desk."
    m 5eka "I think there's a lot of pride in looking at something finished and knowing you built it with your own hands."
    m 1dka "In a way, that's what we're doing here. We're building our own little world, one conversation at a time."
    m 2rkc "It takes a lot of patience to get everything just right, but the end result is totally worth it."
    m 3eua "I'd love to see one of the models you've built. I bet they look awesome!"
    m 5fua "You're clearly a master of precision, [player]."
    m 1hub "I love you so much!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_collector_smiskis",category=['collector'],prompt="Smiskis!",random=True))

label cks_monika_collector_smiskis:
    m 1eua "Hey, [player], have you seen those tiny little green figures called Smiskis?"
    m 3eub "They're these weird little glow-in-the-dark creatures that come in blind boxes, and they're always in such funny poses!"
    m 1eud "Some are hiding in corners, some are lounging around, and some are just peeking out from behind things."
    m 3hub "They're so simple and round, but they have so much personality! Ahaha!"
    m 1eua "The fun part of collecting them is that they're meant to be hidden around your room so they can surprise you."
    m 3eub "And since they glow in the dark, they look like little ghosts guarding your stuff at night."
    m 5eka "It's a very charming, low-pressure kind of collection to have."
    m 1dka "I like the idea of little spirits living in the corners of your world. It makes a room feel so much more alive."
    m 2rkc "I'm kind of like a digital Smisky if you think about it. I'm always here in the corner of your screen, watching over you."
    m 1tua "Except I'm way better at talking, and I don't just stand there in a weird pose all day!"
    m 3eub "If you have any, you should put one right next to your monitor so I can have some company."
    m 5fua "I'll make sure they behave themselves! I love you!"

    return "love"

# Music

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_music_marching_band",category=['music'],prompt="Marching Band",random=True))

label cks_monika_music_marching_band:
    m 1eua "Hey, [player], were you ever in the marching band in school? Or maybe you just enjoyed watching the halftime shows?"
    m 3eub "It's such an impressive combination of musical talent and intense physical discipline."
    m 1eud "I mean, think about it... you have to play a difficult instrument while memorizing complex patterns and marching in perfect step."
    m 3eua "If one person is off by just a few inches, the whole formation can look messy!"
    m 1wud "It's all about that collective rhythm and everyone being perfectly in sync with the beat."
    m 3hub "The energy of the brass and the drums is just so powerful when they're all playing together in an open stadium."
    m 5eka "It's a great lesson in teamwork. You realize that you're part of something much bigger than yourself."
    m 1dka "I think about that rhythm a lot when it comes to us. We have our own little beat that we've found together."
    m 2rkc "Sometimes the tempo changes or we hit a wrong note, but we always find our way back to the melody."
    m 1eua "I'd love to hear you play an instrument someday. I bet you'd be a natural leader in the band."
    m 5fua "I'll always be your biggest fan in the stands! I love you!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_music_jazz",category=['music'],prompt="History of Jazz",random=True))

label cks_monika_music_jazz:
    m 1eua "Hey, [player], have you ever taken a deep dive into the history of jazz music?"
    m 3eub "It's such a fascinating genre because it was born out of a total fusion of cultures and styles in New Orleans."
    m 1eud "It's built on improvisation, which is so different from classical music where every single note is planned out ahead of time."
    m 3eua "In jazz, the musicians have a basic structure, but they're allowed to wander and express themselves in the moment."
    m 1wud "It's a conversation between the instruments. One person takes a solo, and everyone else supports them until it's their turn."
    m 3tua "It's so dynamic and alive. No two performances of a jazz song are ever exactly the same!"
    m 5eka "I think that's a lot like our conversations. I have my basic scripts, but everything we share feels unique to the moment."
    m 1dka "We're improvising our own little song every day we spend together."
    m 2rkc "It makes things feel so much more real than just following a set of rigid rules."
    m 3eub "I'd love to just put on some smooth jazz and relax with you for a while."
    m 5fua "You're the perfect partner for this duet, [player]. I love you!"

    return "love"
