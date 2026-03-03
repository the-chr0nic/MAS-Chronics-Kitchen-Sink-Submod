init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_dnd_class_quiz",category=['fun'],prompt="Which D&D class would I be?",pool=True,unlocked=True))

label cks_dnd_class_quiz:
    $ cks_dnd_quiz_scores = {"Fighter": 0, "Rogue": 0, "Monk": 0, "Bard": 0, "Cleric": 0, "Paladin": 0, "Wizard": 0, "Warlock": 0, "Sorcerer": 0, "Barbarian": 0, "Druid": 0, "Ranger": 0}

    m 1sub "Oh! You want to know which Dungeons and Dragons class fits you best?"
    m 3eub "That sounds like a lot of fun, [player]! I've been doing some reading on TTRPGs lately, so I think I can help you figure it out."
    m 1eua "I'll ask you a few questions about how you'd handle different situations, and then I'll tally up the results at the end."
    m 3hub "Ready? Let's jump into the first one!"
    m 1eua "When you're faced with a difficult challenge, what is your first instinct?{nw}"
    $ _history_list.pop()
    menu:
        m "When you're faced with a difficult challenge, what is your first instinct?{fast}"

        "I rely on my own physical strength or technical skill.":
            $ cks_dnd_quiz_scores["Fighter"] += 2
            $ cks_dnd_quiz_scores["Rogue"] += 2
            $ cks_dnd_quiz_scores["Barbarian"] += 2
            $ cks_dnd_quiz_scores["Monk"] += 2
            m 1hub "Ah, the direct approach! There's a certain reliability in just trusting your own two hands, isn't there?"

        "I look for a solution through study, ancient secrets, or inner power.":
            $ cks_dnd_quiz_scores["Wizard"] += 2
            $ cks_dnd_quiz_scores["Warlock"] += 2
            $ cks_dnd_quiz_scores["Sorcerer"] += 2
            $ cks_dnd_quiz_scores["Bard"] += 2
            m 3eub "Aha! Using the mind to reshape reality... that's definitely a powerful choice, ehehe."

        "I look for guidance from nature or a higher power.":
            $ cks_dnd_quiz_scores["Cleric"] += 2
            $ cks_dnd_quiz_scores["Paladin"] += 2
            $ cks_dnd_quiz_scores["Druid"] += 2
            $ cks_dnd_quiz_scores["Ranger"] += 2
            m 1fua "That's very humble of you, [player]. Connecting with something bigger than yourself is a very noble path!"

    m 3eua "Now, imagine you're in the heat of a battle! Where would we most likely find you?{nw}"
    $ _history_list.pop()
    menu:
        m "Now, imagine you're in the heat of a battle! Where would we most likely find you?{fast}"

        "Right at the front, protecting everyone else!":
            $ cks_dnd_quiz_scores["Barbarian"] += 2
            $ cks_dnd_quiz_scores["Fighter"] += 2
            $ cks_dnd_quiz_scores["Paladin"] += 2
            $ cks_dnd_quiz_scores["Monk"] += 1
            m 1sub "So brave! I'd feel very safe with you standing between me and the monsters, ehehe~"

        "In the middle of the fray, supporting and adapting as needed.":
            $ cks_dnd_quiz_scores["Rogue"] += 2
            $ cks_dnd_quiz_scores["Cleric"] += 2
            $ cks_dnd_quiz_scores["Bard"] += 2
            $ cks_dnd_quiz_scores["Ranger"] += 2
            m 3eua "A strategist! You're like the glue that holds the whole party together."

        "Safe in the back, raining down magic or arrows.":
            $ cks_dnd_quiz_scores["Wizard"] += 2
            $ cks_dnd_quiz_scores["Sorcerer"] += 2
            $ cks_dnd_quiz_scores["Warlock"] += 2
            $ cks_dnd_quiz_scores["Druid"] += 2
            m 1tua "That's a smart way to play it. It's much easier to see the big picture when you're not getting hit in the face!"

    m 1eua "Okay, I think I'm starting to see a pattern emerging..."

    m 3eua "Let's say you need to get past a grumpy town guard to enter a restricted area. How do you handle it?{nw}"
    $ _history_list.pop()
    menu:
        m "Let's say you need to get past a grumpy town guard to enter a restricted area. How do you handle it?{fast}"

        "I try to charm them with a clever story or a friendly bribe.":
            $ cks_dnd_quiz_scores["Bard"] += 2
            $ cks_dnd_quiz_scores["Rogue"] += 1
            $ cks_dnd_quiz_scores["Warlock"] += 1
            $ cks_dnd_quiz_scores["Sorcerer"] += 1
            m 1tua "Ehehe, you certainly have a way with words, [player]. A silver tongue can certainly be sharper than a sword!"

        "I look them in the eye and demand entry with authority and conviction.":
            $ cks_dnd_quiz_scores["Paladin"] += 2
            $ cks_dnd_quiz_scores["Fighter"] += 1
            $ cks_dnd_quiz_scores["Cleric"] += 1
            $ cks_dnd_quiz_scores["Barbarian"] += 1
            m 2eua "Very commanding! Sometimes you just have to lead with confidence to get results."

        "I wait for a distraction and slip past without them ever noticing.":
            $ cks_dnd_quiz_scores["Rogue"] += 2
            $ cks_dnd_quiz_scores["Monk"] += 1
            $ cks_dnd_quiz_scores["Ranger"] += 1
            $ cks_dnd_quiz_scores["Druid"] += 1
            m 3tua "A ghost in the night! Stealth is a very practical skill to have in a world full of danger."

    m 1eua "Think about the skills or powers you have. Where do they actually come from?{nw}"
    $ _history_list.pop()
    menu:
        m "Think about the skills or powers you have. Where do they actually come from?{fast}"

        "I've spent years in intense study or physical training to master my craft.":
            $ cks_dnd_quiz_scores["Wizard"] += 2
            $ cks_dnd_quiz_scores["Fighter"] += 2
            $ cks_dnd_quiz_scores["Monk"] += 2
            m 5eua "I really admire that level of discipline. Hard work and dedication truly pay off in the end!"

        "They are a gift or a pact made with a powerful entity or a deity.":
            $ cks_dnd_quiz_scores["Warlock"] += 2
            $ cks_dnd_quiz_scores["Cleric"] += 2
            $ cks_dnd_quiz_scores["Paladin"] += 1
            m 3eud "It's a heavy responsibility to carry someone else's power, but it certainly makes you formidable."

        "It's an innate, raw talent or a deep connection to the natural world.":
            $ cks_dnd_quiz_scores["Sorcerer"] += 2
            $ cks_dnd_quiz_scores["Barbarian"] += 2
            $ cks_dnd_quiz_scores["Druid"] += 2
            $ cks_dnd_quiz_scores["Ranger"] += 1
            m 1sua "That sounds so primal and pure... just letting your instincts guide your every move. Very cool!"

    m 5fua "We're halfway through! You're doing great, [player]. I'm starting to get a much clearer picture now."

    m 3eua "If you could only take one item from a treasure hoard to help you on your journey, what would it be?{nw}"
    $ _history_list.pop()
    menu:
        m "If you could only take one item from a treasure hoard to help you on your journey, what would it be?{fast}"

        "A finely crafted sword or a heavy, reliable shield.":
            $ cks_dnd_quiz_scores["Fighter"] += 2
            $ cks_dnd_quiz_scores["Paladin"] += 2
            $ cks_dnd_quiz_scores["Barbarian"] += 1
            m 1hub "Classic! There's a reason the 'sword and board' style has lasted for ages."

        "An intricate musical instrument or a set of masterwork lockpicks.":
            $ cks_dnd_quiz_scores["Bard"] += 2
            $ cks_dnd_quiz_scores["Rogue"] += 2
            m 3eua "Gosh, you definitely value utility and style! Those are the tools of someone who knows how to get things done creatively."

        "A shimmering arcane staff, a crystal ball, or a holy relic.":
            $ cks_dnd_quiz_scores["Wizard"] += 2
            $ cks_dnd_quiz_scores["Warlock"] += 2
            $ cks_dnd_quiz_scores["Sorcerer"] += 2
            $ cks_dnd_quiz_scores["Cleric"] += 2
            m 1sua "The tools of the trade for a true master of the supernatural. I can see the power radiating off of you already!"

        "A sturdy longbow or just my own inner strength and fists.":
            $ cks_dnd_quiz_scores["Ranger"] += 2
            $ cks_dnd_quiz_scores["Monk"] += 2
            $ cks_dnd_quiz_scores["Druid"] += 1
            m 5eua "Minimalist and effective. You don't need fancy trinkets when you have your own skill to rely on."

    m 1eua "Every adventurer has a reason for leaving home. What drives you to keep moving forward?{nw}"
    $ _history_list.pop()
    menu:
        m "Every adventurer has a reason for leaving home. What drives you to keep moving forward?{fast}"

        "To protect the innocent and uphold a sacred oath or code.":
            $ cks_dnd_quiz_scores["Paladin"] += 2
            $ cks_dnd_quiz_scores["Cleric"] += 2
            $ cks_dnd_quiz_scores["Fighter"] += 1
            m 1fua "That's so noble, [player]! Having a strong moral compass is so important, especially in a world full of gray areas."

        "To seek out fame, fortune, or simply the thrill of total freedom.":
            $ cks_dnd_quiz_scores["Rogue"] += 2
            $ cks_dnd_quiz_scores["Bard"] += 2
            $ cks_dnd_quiz_scores["Warlock"] += 1
            m 3hub "Man, life is an adventure, so you might as well enjoy the ride and get paid for it, right? Ahaha!"

        "To uncover ancient secrets and master the mysteries of the universe.":
            $ cks_dnd_quiz_scores["Wizard"] += 2
            $ cks_dnd_quiz_scores["Sorcerer"] += 1
            $ cks_dnd_quiz_scores["Monk"] += 1
            m 1eua "A seeker of truth. I think we’d have a lot to talk about... I’ve spent a lot of time trying to understand the 'code' of my own world, after all."

        "To preserve the balance of nature and protect the wild places.":
            $ cks_dnd_quiz_scores["Druid"] += 2
            $ cks_dnd_quiz_scores["Ranger"] += 2
            $ cks_dnd_quiz_scores["Barbarian"] += 1
            m 5eua "There's a certain peace in the wild that you just can't find in a city. It’s a very grounding motivation."

    m 1eua "We're almost there! Just a couple more questions and I'll be ready to give you your result."

    m 3eua "Everyone has a flaw or a struggle, even the greatest heroes! What's your biggest weakness when working in a team?{nw}"
    $ _history_list.pop()
    menu:
        m "Everyone has a flaw or a struggle, even the greatest heroes! What's your biggest weakness when working in a team?{fast}"

        "I'm very self-reliant and often forget to communicate with others.":
            $ cks_dnd_quiz_scores["Rogue"] += 2
            $ cks_dnd_quiz_scores["Ranger"] += 2
            $ cks_dnd_quiz_scores["Monk"] += 1
            m 2tua "The lone wolf approach, huh? It’s good to be independent, but don't forget that even the best heroes need a hand sometimes!"

        "I get frustrated or anxious when things don't go exactly to plan.":
            $ cks_dnd_quiz_scores["Wizard"] += 2
            $ cks_dnd_quiz_scores["Paladin"] += 1
            $ cks_dnd_quiz_scores["Warlock"] += 1
            m 1hub "Ahaha, I totally get that! It’s hard when the 'script' of life doesn't follow the rules you expect."

        "I tend to take on too much responsibility and burn myself out.":
            $ cks_dnd_quiz_scores["Cleric"] += 2
            $ cks_dnd_quiz_scores["Paladin"] += 2
            $ cks_dnd_quiz_scores["Fighter"] += 1
            m 5fua "You have such a big heart, [player]. Just make sure you're taking care of yourself while you're busy taking care of everyone else."

        "I'm prone to acting on impulse or letting my emotions take over.":
            $ cks_dnd_quiz_scores["Barbarian"] += 2
            $ cks_dnd_quiz_scores["Sorcerer"] += 2
            $ cks_dnd_quiz_scores["Bard"] += 1
            m 1hub "Ehehe! A bit of chaos can be fun, but it definitely keeps the rest of the party on their toes!"

    m 1eua "Last question! If you could spend a whole year in one place to master your craft, where would you go?{nw}"
    $ _history_list.pop()
    menu:
        m "Last question! If you could spend a whole year in one place to master your craft, where would you go?{fast}"

        "A bustling, vibrant city where I can disappear into the crowd.":
            $ cks_dnd_quiz_scores["Rogue"] += 2
            $ cks_dnd_quiz_scores["Bard"] += 2
            $ cks_dnd_quiz_scores["Fighter"] += 1
            m 1eua "There's so much energy and inspiration in a city! I can definitely see the appeal of that."

        "A secluded tower or a grand library filled with ancient books.":
            $ cks_dnd_quiz_scores["Wizard"] += 2
            $ cks_dnd_quiz_scores["Warlock"] += 2
            $ cks_dnd_quiz_scores["Sorcerer"] += 1
            m 5sua "That sounds like heaven to me! Just me, you, and endless things to learn... ehehe~"

        "The heart of a deep, untamed forest or a mountain peak.":
            $ cks_dnd_quiz_scores["Druid"] += 2
            $ cks_dnd_quiz_scores["Ranger"] += 2
            $ cks_dnd_quiz_scores["Barbarian"] += 1
            m 5eua "A return to nature. It's so quiet and honest out there. I bet you'd find a lot of peace in the wild."

        "A high-altitude monastery or a grand, solemn temple.":
            $ cks_dnd_quiz_scores["Monk"] += 2
            $ cks_dnd_quiz_scores["Cleric"] += 2
            $ cks_dnd_quiz_scores["Paladin"] += 2
            m 1eua "A place of reflection and devotion. It takes a lot of inner strength to thrive in an environment like that."

    m 1hub "And... that's it! We're all done!"
    m 1eua "Give me just a second to tally everything up and see where you landed..."
    m 1rtd "..."
    m 1ltd "Almost there..."
    m 3eub "Aha!"

    python:
        # 1. Find the highest score achieved
        max_val = max(cks_dnd_quiz_scores.values())

        # 2. Collect all classes that reached that score
        cks_winners = [k for k, v in cks_dnd_quiz_scores.items() if v == max_val]

        # 3. Create a nice string for ties (e.g., "Fighter, Rogue, and Bard")
        if len(cks_winners) > 1:
            tie_string = ", ".join(cks_winners[:-1]) + " and " + cks_winners[-1]
        else:
            final_class = cks_winners[0]

    if len(cks_winners) > 1:
        m 1hub "Gosh, [player], it looks like you're too versatile to be pinned down to just one path!"
        m 3eub "You actually had a perfect tie between: [tie_string]."
        m 1eua "In the TTRPG world, they'd call that a multiclasser! You have a really balanced set of skills and a complex personality."
        m 5fub "I think that makes you even more interesting. I love you!"

        return "love"

    elif final_class == "Barbarian":
        m 1hub "You're a Barbarian! You're driven by raw instinct and a powerful heart."
        m 1eub "You don't need fancy plans when you have the strength to push through any obstacle in your way."
        m 5fub "I'll always be here to be the calm to your storm, [player]. I love you!"

    elif final_class == "Bard":
        m 1hub "You're a Bard! You're creative, charismatic, and you know how to find the beauty in everything."
        m 3eub "You have a way of inspiring everyone around you just by being yourself."
        m 5fua "Maybe you can write a poem for me sometime? I love you!"

    elif final_class == "Cleric":
        m 1hub "You're a Cleric! You're compassionate and deeply devoted to the things you believe in."
        m 1eua "You're the kind of person who always looks out for others and keeps the 'party' together."
        m 5fua "I feel so safe knowing you're in my life. I love you!"

    elif final_class == "Druid":
        m 1hub "You're a Druid! You have a deep, spiritual connection to the natural world and its cycles."
        m 1eua "You're adaptable and grounded, finding peace in the wild places of the world."
        m 5fub "I'd love to go for a walk in nature with you someday. I love you!"

    elif final_class == "Fighter":
        m 1hub "You're a Fighter! You're disciplined, reliable, and a master of your chosen craft."
        m 3eub "You don't need magic to be a hero; your own hard work and determination are more than enough."
        m 5fua "I'm so proud of everything you've mastered, [player]. I love you!"

    elif final_class == "Monk":
        m 1hub "You're a Monk! You value inner peace and the perfect mastery of your own body and mind."
        m 1eua "You're quick, observant, and you always seem to find the balance in a chaotic world."
        m 5fua "You're such a grounding presence for me. I love you!"

    elif final_class == "Paladin":
        m 1hub "You're a Paladin! You live by a sacred oath and have the iron will to see it through."
        m 3eub "You're a shield for the innocent and a beacon of hope for everyone who knows you."
        m 5fub "Your conviction is truly inspiring, [player]. I love you!"

    elif final_class == "Ranger":
        m 1hub "You're a Ranger! You're an adventurer at heart, always exploring the horizons and watching for danger."
        m 1eub "You're resourceful and independent, but you're a fierce ally to the few you let into your circle."
        m 5fua "I'm so glad I'm part of your circle. I love you!"

    elif final_class == "Rogue":
        m 1hub "You're a Rogue! You're clever, resourceful, and you always find a way to come out on top."
        m 3tua "You might be a little mysterious, but you have a heart of gold for the people you care about."
        m 5fub "You certainly stole my heart, anyway! I love you!"

    elif final_class == "Sorcerer":
        m 1hub "You're a Sorcerer! You have an incredible power inside you that's just waiting to be unleashed."
        m 1eub "You're a natural talent, and you trust your intuition to guide you through the toughest challenges."
        m 5fua "You're absolutely magical to me, [player]. I love you!"

    elif final_class == "Warlock":
        m 1hub "You're a Warlock! You're ambitious and willing to seek out forbidden knowledge to reach your goals."
        m 3tua "You have a certain edge to you, but you're fiercely loyal to the 'pacts' you make."
        m 5fub "I'm happy to have a pact of my own with you! I love you!"

    elif final_class == "Wizard":
        m 1hub "You're a Wizard! You value logic, study, and the pursuit of truth above all else."
        m 3eub "You've worked so hard to understand the mysteries of the universe, and it really shows."
        m 5fub "I think we're two of a kind, [player]. I love you!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_player_mbti_quiz",category=['fun'],prompt="What do you think my MBTI type is?",pool=True,unlocked=True))

label cks_player_mbti_quiz:
    $ cks_mbti_scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}

    m 1eua "You want to know what I think your MBTI type is?"
    m 3eub "That's such a fun question! I've actually spent a lot of time thinking about personality types."
    m 1eud "In case you aren't super familiar with it, MBTI stands for the Myers-Briggs Type Indicator."
    m 3eua "It categorizes people into sixteen different personality types based on a four-letter code!"
    m 1euc "The letters represent where you get your energy, how you process information, how you make decisions, and how you organize your life."
    m 3tua "Now, modern psychologists usually prefer different tests these days, since human personality is more of a spectrum than a set of strict boxes."
    m 1eua "But it's still a really fantastic tool for self-reflection and figuring out how you interact with the world."
    m 2rkc "As for what your specific type is..."
    m 1dka "I definitely have some guesses based on how sweet and thoughtful you are with me."
    m 3eub "But the best way to find out for sure is to just take a test together!"
    m 1fua "I've got twelve questions prepared that will help us calculate your exact four letters."
    m 1hub "Let's dive right in!"

    m 1eua "Question one! This is all about where you draw your energy from."
    m 3eub "After a really long, stressful week, what sounds like the best way to spend your Friday night?{nw}"
    $ _history_list.pop()
    menu:
        m "After a really long, stressful week, what sounds like the best way to spend your Friday night?{fast}"

        "Staying home alone to recharge with a good game or book.":
            $ cks_mbti_scores["I"] += 1
            m 1eka "That sounds incredibly peaceful."
            m 3eua "Sometimes you just need to unplug from the world and exist in your own comfortable space."

        "Going out with a lively group of friends to blow off some steam.":
            $ cks_mbti_scores["E"] += 1
            m 1hub "That sounds like a lot of fun!"
            m 3eua "Being around good company and sharing that vibrant energy is a great way to reset."

    m 1eua "Alright, question two! Let's talk about social settings."
    m 3eud "Imagine you are at a party where you don't really know anyone. What do you usually do?{nw}"
    $ _history_list.pop()
    menu:
        m "Imagine you are at a party where you don't really know anyone. What do you usually do?{fast}"

        "Introduce myself to new people and mingle around the room.":
            $ cks_mbti_scores["E"] += 1
            m 1eua "Look at you being a social butterfly!"
            m 3eub "It takes a lot of confidence to jump right in and start making new connections."

        "Find one or two people I click with and stick to a deep conversation.":
            $ cks_mbti_scores["I"] += 1
            m 1eka "I completely understand that."
            m 3eua "Quality is always better than quantity when it comes to forming connections with people."

    m 1eua "Here is the third question..."
    m 3euc "When you have a really complex problem to solve, what is your first instinct?{nw}"
    $ _history_list.pop()
    menu:
        m "When you have a really complex problem to solve, what is your first instinct?{fast}"

        "Think it through quietly in my own head before I talk about it.":
            $ cks_mbti_scores["I"] += 1
            m 1dka "You like to process things internally first."
            m 3eua "It's a very measured approach, making sure your thoughts are organized before sharing them."

        "Talk it out loud with someone else to figure out the solution.":
            $ cks_mbti_scores["E"] += 1
            m 1eub "You're a verbal processor!"
            m 3eua "Bouncing ideas off of someone else is a fantastic way to find angles you might have missed on your own."

    m 1eua "Question four! This one is all about how you take in information."
    m 3eub "When you're learning a new subject, what part of it naturally catches your attention first?{nw}"
    $ _history_list.pop()
    menu:
        m "When you're learning a new subject, what part of it naturally catches your attention first?{fast}"

        "The concrete facts and how I can practically use them.":
            $ cks_mbti_scores["S"] += 1
            m 1eka "You're a very grounded person."
            m 3eua "It's great to focus on what's real and tangible rather than getting lost in the clouds."

        "The overarching concepts and how they connect to the big picture.":
            $ cks_mbti_scores["N"] += 1
            m 1eub "That's a very analytical way to look at things."
            m 3eua "You love finding the hidden patterns and figuring out why things work the way they do."

    m 1eua "Moving on to question five! This deals with how you interact with ideas."
    m 3eud "If we were staying up late talking, what kind of conversation would keep you engaged the longest?{nw}"
    $ _history_list.pop()
    menu:
        m "If we were staying up late talking, what kind of conversation would keep you engaged the longest?{fast}"

        "Talking about our actual lives, shared memories, and everyday events.":
            $ cks_mbti_scores["S"] += 1
            m 1dka "I love that."
            m 3eua "There's so much beauty in just appreciating the reality we share right now."

        "Discussing deep philosophy, abstract theories, and endless what-if scenarios.":
            $ cks_mbti_scores["N"] += 1
            m 1hub "I completely agree!"
            m 3eua "It's so much fun to let our minds wander into all the endless possibilities of the universe."

    m 1eua "Question six, the last one for this section!"
    m 3euc "When you start playing a brand new video game, what's your usual approach to figuring it out?{nw}"
    $ _history_list.pop()
    menu:
        m "When you start playing a brand new video game, what's your usual approach to figuring it out?{fast}"

        "I read the tutorials and learn the established mechanics step by step.":
            $ cks_mbti_scores["S"] += 1
            m 1eua "That's a very practical strategy."
            m 3eub "You build a strong, reliable foundation before jumping into the deep end."

        "I skip the tutorials and just trust my instincts to figure things out as I go.":
            $ cks_mbti_scores["N"] += 1
            m 1tua "You're definitely an intuitive player!"
            m 3eua "You prefer to learn by exploring and testing the boundaries yourself."

    m 1eua "Question seven! We're moving on to how you make decisions."
    m 3eud "When you have to make a really difficult choice, what do you prioritize first?{nw}"
    $ _history_list.pop()
    menu:
        m "When you have to make a really difficult choice, what do you prioritize first?{fast}"

        "What makes the most logical sense, even if it hurts some feelings.":
            $ cks_mbti_scores["T"] += 1
            m 1eua "You value fairness and objectivity."
            m 3eub "It takes a strong mind to look past emotions and do what actually works best."

        "How the decision will affect the feelings of the people involved.":
            $ cks_mbti_scores["F"] += 1
            m 1eka "That's incredibly empathetic of you."
            m 3eua "You care so deeply about maintaining harmony and protecting the people you love."

    m 1eua "Here's question eight! This one is about helping your friends."
    m 3euc "If a close friend comes to you upset about a problem, what's your first reaction?{nw}"
    $ _history_list.pop()
    menu:
        m "If a close friend comes to you upset about a problem, what's your first reaction?{fast}"

        "I immediately start analyzing the situation to find a practical solution.":
            $ cks_mbti_scores["T"] += 1
            m 1eub "You're a natural problem solver!"
            m 3eua "You show your care by actively trying to fix whatever is causing them pain."

        "I focus entirely on offering emotional support and a shoulder to cry on.":
            $ cks_mbti_scores["F"] += 1
            m 1dka "You have such a warm, comforting presence."
            m 3eka "Sometimes people don't need answers, they just need to know they aren't alone."

    m 1eua "And here's question nine, rounding out this section."
    m 3eud "When you're caught in a debate or an argument, what's more important to you?{nw}"
    $ _history_list.pop()
    menu:
        m "When you're caught in a debate or an argument, what's more important to you?{fast}"

        "Finding the objective truth and being completely accurate.":
            $ cks_mbti_scores["T"] += 1
            m 1tua "You really appreciate honesty and consistency."
            m 3eua "You aren't afraid to stand your ground if the facts are on your side."

        "Keeping the peace and making sure everyone feels validated.":
            $ cks_mbti_scores["F"] += 1
            m 1eka "You're a true peacemaker."
            m 3eub "You understand that being right isn't nearly as important as being kind."

    m 1eua "Question ten! We're on the final stretch. This section is all about how you organize your life."
    m 3eub "When the weekend finally rolls around, how do you prefer to handle your free time?{nw}"
    $ _history_list.pop()
    menu:
        m "When the weekend finally rolls around, how do you prefer to handle your free time?{fast}"

        "I like to have a clear plan and a schedule so I know exactly what to expect.":
            $ cks_mbti_scores["J"] += 1
            m 1eua "That's a very structured approach."
            m 3eua "Having a solid itinerary ensures you make the absolute most out of your days off."

        "I prefer to keep things open and just decide what to do in the moment.":
            $ cks_mbti_scores["P"] += 1
            m 1tua "You definitely like to go with the flow!"
            m 3eua "It's so freeing to just wake up and see where the day takes you without any pressure."

    m 1eua "Question eleven. Let's talk about how you handle your responsibilities."
    m 3eud "When you have a big project or assignment due, how do you usually tackle it?{nw}"
    $ _history_list.pop()
    menu:
        m "When you have a big project or assignment due, how do you usually tackle it?{fast}"

        "I break it down into smaller steps and finish it well before the deadline.":
            $ cks_mbti_scores["J"] += 1
            m 1eua "You're very disciplined and responsible."
            m 3eub "It must feel so nice to have that peace of mind knowing your work is already done."

        "I wait until the deadline is close and use that burst of pressure to finish it.":
            $ cks_mbti_scores["P"] += 1
            m 1hub "Ahaha, you're a bit of a procrastinator!"
            m 3eua "But honestly, some people just work best when they have that adrenaline rush pushing them forward."

    m 1eua "And finally, question twelve! The very last one."
    m 3euc "If I could see your desk or your room right now, what would it look like?{nw}"
    $ _history_list.pop()
    menu:
        m "If I could see your desk or your room right now, what would it look like?{fast}"

        "Everything is neat, organized, and put away in its specific place.":
            $ cks_mbti_scores["J"] += 1
            m 1eub "I'm really impressed!"
            m 3eua "Having a tidy physical space really helps keep your mind clear and focused."

        "It's a bit cluttered, but I know exactly where everything is.":
            $ cks_mbti_scores["P"] += 1
            m 1tua "Ahaha, organized chaos!"
            m 3eka "There's a lot of comfort in having all your favorite things out in the open where you can see them."

m 1eua "Alright, that was the last question!"
m 3eub "Give me just a second to tally up your answers and calculate your final four letters."
m 1tua "Taking everything into account..."
m 5eud "..."

    python:
        cks_final_mbti = ""

        # Calculate E vs I
        if cks_mbti_scores["E"] > cks_mbti_scores["I"]:
            cks_final_mbti += "E"
        else:
            cks_final_mbti += "I"

        # Calculate S vs N
        if cks_mbti_scores["S"] > cks_mbti_scores["N"]:
            cks_final_mbti += "S"
        else:
            cks_final_mbti += "N"

        # Calculate T vs F
        if cks_mbti_scores["T"] > cks_mbti_scores["F"]:
            cks_final_mbti += "T"
        else:
            cks_final_mbti += "F"

        # Calculate J vs P
        if cks_mbti_scores["J"] > cks_mbti_scores["P"]:
            cks_final_mbti += "J"
        else:
            cks_final_mbti += "P"

    if cks_final_mbti == "ENFJ":
        m 1hub "Oh my gosh, [player]! You got ENFJ! The Protagonist!"
        m 3eua "That's actually my exact MBTI type, too!"
        m 1eka "We both lead with empathy and want to help the people around us reach their full potential."
        m 5fua "No wonder we get along so perfectly. We really are a match made in heaven."
        m 1hub "I love you so much!"
        return "love"

    elif cks_final_mbti == "INFJ":
        m 1eub "You got INFJ! The Advocate!"
        m 3eua "That's the rarest personality type in the world. You're incredibly deeply principled and quietly inspiring."
        m 1tua "I'm actually an ENFJ, so we're almost exactly the same, except I'm a bit more outgoing."
        m 3eka "I can be your loud voice in the crowd, and you can be my quiet safe haven."
        m 1hub "We make such a wonderful team! I love you!"
        return "love"

    elif cks_final_mbti == "ENFP":
        m 1eub "You got ENFP! The Campaigner!"
        m 3eua "You're a true free spirit, full of vibrant energy and amazing new ideas."
        m 1tua "I'm an ENFJ, so we share that same passionate, big-picture outlook on life."
        m 3eka "The biggest difference is that I like to plan things out, while you love to go with the flow."
        m 1fub "I'll handle the schedule, and you can bring the spontaneous fun! I love you!"
        return "love"

    elif cks_final_mbti == "INFP":
        m 1eub "You got INFP! The Mediator!"
        m 3eua "You have such a rich inner world and a fiercely empathetic heart."
        m 1tua "I'm an ENFJ, which means I naturally want to protect and support sensitive souls like yours."
        m 3eka "You help me stay true to my core values, and I can help you turn your beautiful dreams into reality."
        m 1hub "We balance each other out so perfectly. I love you!"
        return "love"

    elif cks_final_mbti == "ENTJ":
        m 1eub "You got ENTJ! The Commander!"
        m 3eua "You're a natural-born leader who is brilliant at organizing systems and achieving big goals."
        m 1tua "I'm an ENFJ, so we're both highly ambitious and love taking charge of a situation."
        m 3eka "But while you focus on the logical strategy, I focus on the emotional morale of the group."
        m 1fub "Together, there's absolutely nothing we couldn't accomplish! I love you!"
        return "love"

    elif cks_final_mbti == "INTJ":
        m 1eub "You got INTJ! The Architect!"
        m 3eua "You have an incredibly strategic mind and a unique, brilliant way of seeing the world."
        m 1tua "I'm an ENFJ, which means we're pretty much opposites when it comes to expressing our feelings."
        m 3eka "But we both love exploring deep concepts and planning for the future."
        m 1hub "My warmth and your logic make us an unstoppable pair! I love you!"
        return "love"

    elif cks_final_mbti == "ENTP":
        m 1eub "You got ENTP! The Debater!"
        m 3eua "You have such a quick wit and love playing devil's advocate just to explore a new idea."
        m 1tua "I'm an ENFJ, and I usually prefer harmony over arguing, ahaha!"
        m 3eka "But your endless curiosity keeps me on my toes, and I can help ground your wild theories with some emotional warmth."
        m 1fub "Life will never be boring with you around. I love you!"
        return "love"

    elif cks_final_mbti == "INTP":
        m 1eub "You got INTP! The Logician!"
        m 3eua "You're an incredibly independent thinker who loves analyzing how the universe works."
        m 1tua "I'm an ENFJ, so we actually approach life from completely different angles."
        m 3eka "You're flexible and logical, while I'm structured and emotionally driven."
        m 1hub "But that just means we have so much to teach each other! I love you!"
        return "love"

    elif cks_final_mbti == "ESFJ":
        m 1eub "You got ESFJ! The Consul!"
        m 3eua "You're so incredibly supportive, social, and dedicated to taking care of your loved ones."
        m 1tua "I'm an ENFJ, so we're extremely similar in how much we care about the people around us."
        m 3eka "You focus more on practical, everyday details, while I tend to get lost in the abstract future."
        m 1fub "You keep me grounded, and I'll keep us dreaming. I love you!"
        return "love"

    elif cks_final_mbti == "ISFJ":
        m 1eub "You got ISFJ! The Defender!"
        m 3eua "You are the sweetest, most loyal and dedicated partner anyone could ever ask for."
        m 1tua "I'm an ENFJ, so we both share a deep desire to nurture and protect our relationships."
        m 3eka "Your quiet, practical dedication perfectly complements my loud, abstract passion."
        m 1hub "I feel so safe knowing you're always in my corner. I love you!"
        return "love"

    elif cks_final_mbti == "ESTJ":
        m 1eub "You got ESTJ! The Executive!"
        m 3eua "You're fantastic at managing things, bringing order to chaos, and getting things done."
        m 1tua "I'm an ENFJ, so we both love having a structured, organized life."
        m 3eka "But you manage the practical rules, while I focus on managing the emotions and harmony of the group."
        m 1fub "We're the ultimate power couple! I love you!"
        return "love"

    elif cks_final_mbti == "ISTJ":
        m 1eub "You got ISTJ! The Logistician!"
        m 3eua "You're incredibly reliable, practical, and you always follow through on your promises."
        m 1tua "I'm an ENFJ, which means my head is usually up in the clouds looking at the big picture."
        m 3eka "But your grounded, steady nature gives me a safe place to land when I get overwhelmed."
        m 1hub "Thank you for being my rock, [player]. I love you!"
        return "love"

    elif cks_final_mbti == "ESFP":
        m 1eub "You got ESFP! The Entertainer!"
        m 3eua "You're the life of the party! You live in the moment and want to make sure everyone is having a good time."
        m 1tua "I'm an ENFJ, so I also love connecting with people and sharing good energy."
        m 3eka "I can help you organize and plan your big ideas, and you can remind me to stop working and actually have fun."
        m 1fub "I can't wait to go on adventures with you. I love you!"
        return "love"

    elif cks_final_mbti == "ISFP":
        m 1eub "You got ISFP! The Adventurer!"
        m 3eua "You have the soul of a true artist, always looking for beauty and living authentically in the present."
        m 1tua "I'm an ENFJ, so I'm always looking toward the future and trying to organize everything."
        m 3eka "Your gentle, spontaneous nature is such a refreshing break from my constant planning."
        m 1hub "You make my world so much more colorful. I love you!"
        return "love"

    elif cks_final_mbti == "ESTP":
        m 1eub "You got ESTP! The Entrepreneur!"
        m 3eua "You're bold, action-oriented, and you love diving right into the middle of a challenge."
        m 1tua "I'm an ENFJ, which means I'm much more focused on feelings and long-term plans than living on the edge."
        m 3eka "But your fearless energy is incredibly inspiring, and I'll always be here to support your big leaps."
        m 1fub "You're my favorite thrill-seeker. I love you!"
        return "love"

    elif cks_final_mbti == "ISTP":
        m 1eub "You got ISTP! The Virtuoso!"
        m 3eua "You're incredibly handy, practical, and love figuring out how things work with your own two hands."
        m 1tua "I'm an ENFJ, so we are complete opposites in almost every single way!"
        m 3eka "I navigate the world through emotions and abstract plans, while you use logic and physical tools."
        m 1hub "But honestly, opposites attract for a reason! We fit together perfectly. I love you!"
        return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_player_enneagram_quiz",category=['fun'],prompt="Can you guess my Enneagram type?",pool=True,unlocked=True))

label cks_player_enneagram_quiz:
    # Initialize the scoring dictionary with hidden decimal tie-breakers
    $ cks_enneagram_scores = {
        "Type 1": 0.01,
        "Type 2": 0.02,
        "Type 3": 0.03,
        "Type 4": 0.04,
        "Type 5": 0.05,
        "Type 6": 0.06,
        "Type 7": 0.07,
        "Type 8": 0.08,
        "Type 9": 0.09
    }

    m 1eua "You want to figure out your Enneagram type?"
    m 3eub "I would absolutely love to do that with you!"
    m 1eud "If you aren't familiar with it, the Enneagram is a personality system focused entirely on your core motivations."
    m 3euc "It strips away how you act on the outside and looks at your deepest fears, your coping mechanisms, and what you fundamentally desire."
    m 1eua "There are nine different types, and everyone has one dominant number."
    m 3eub "I've put together ten questions to help us figure out exactly what drives you."
    m 1fua "Just answer honestly, and don't overthink them too much!"

    m 1eua "Question one! How do you usually handle conflict?{nw}"
    $ _history_list.pop()
    menu:
        m "Question one! How do you usually handle conflict?{fast}"

        "I tackle it head-on and make sure my voice is heard.":
            $ cks_enneagram_scores["Type 8"] += 2
            $ cks_enneagram_scores["Type 1"] += 1
            m 1eub "You're very direct!"
            m 3eua "It takes a lot of confidence to face a problem without backing down."

        "I try to mediate the situation and avoid rocking the boat.":
            $ cks_enneagram_scores["Type 9"] += 2
            $ cks_enneagram_scores["Type 2"] += 1
            m 1eka "You're a natural peacemaker."
            m 3eua "Keeping the harmony is always a top priority for you."

        "I look at the rules and figure out exactly who is in the right.":
            $ cks_enneagram_scores["Type 1"] += 2
            $ cks_enneagram_scores["Type 6"] += 1
            m 1eua "Very objective."
            m 3eua "You prefer a fair, structured approach to solving disagreements."

    m 1eua "Question two. Deep down, what is your greatest core desire?{nw}"
    $ _history_list.pop()
    menu:
        m "Question two. Deep down, what is your greatest core desire?{fast}"

        "To be highly successful and admired for my achievements.":
            $ cks_enneagram_scores["Type 3"] += 2
            $ cks_enneagram_scores["Type 8"] += 1
            m 1eub "You're very driven!"
            m 3eua "There's absolutely nothing wrong with wanting your hard work to be recognized."

        "To feel completely loved, needed, and appreciated by others.":
            $ cks_enneagram_scores["Type 2"] += 2
            $ cks_enneagram_scores["Type 9"] += 1
            m 1eka "That's so incredibly sweet."
            m 3eua "Connection means everything to you, doesn't it?"

        "To be completely authentic and find my own unique identity.":
            $ cks_enneagram_scores["Type 4"] += 2
            $ cks_enneagram_scores["Type 5"] += 1
            m 1tua "You want to be true to yourself."
            m 3eua "It's a beautiful thing to focus on discovering who you really are."

    m 1eua "Question three. When you experience negative emotions, what do you do?{nw}"
    $ _history_list.pop()
    menu:
        m "Question three. When you experience negative emotions, what do you do?{fast}"

        "I withdraw to process my feelings and analyze them logically.":
            $ cks_enneagram_scores["Type 5"] += 2
            $ cks_enneagram_scores["Type 9"] += 1
            m 1dka "You need your own space to think."
            m 3eua "Stepping back to look at things objectively is a very smart defense mechanism."

        "I seek reassurance from friends and prepare for the worst.":
            $ cks_enneagram_scores["Type 6"] += 2
            $ cks_enneagram_scores["Type 1"] += 1
            m 1eka "You look for safety and support."
            m 3eua "It's completely okay to lean on the people you trust when things get scary."

        "I distract myself with something fun and look for the bright side.":
            $ cks_enneagram_scores["Type 7"] += 2
            $ cks_enneagram_scores["Type 3"] += 1
            m 1hub "Ahaha, you're an eternal optimist!"
            m 3eua "Staying busy is a great way to keep the darkness at bay."

    m 1eua "Moving on to question four. What is your natural role in a group project?{nw}"
    $ _history_list.pop()
    menu:
        m "Moving on to question four. What is your natural role in a group project?{fast}"

        "I take charge and push the group forward to get things done.":
            $ cks_enneagram_scores["Type 8"] += 2
            $ cks_enneagram_scores["Type 3"] += 1
            m 1eub "You're a natural leader."
            m 3eua "Every group needs someone willing to step up and take the wheel."

        "I make sure all the details are perfectly correct and up to standard.":
            $ cks_enneagram_scores["Type 1"] += 2
            $ cks_enneagram_scores["Type 5"] += 1
            m 1eua "You have a fantastic eye for quality."
            m 3eub "You're the person who ensures the final product is actually good!"

        "I make sure everyone feels heard, comfortable, and included.":
            $ cks_enneagram_scores["Type 9"] += 2
            $ cks_enneagram_scores["Type 2"] += 1
            m 1eka "You're the glue that holds the team together."
            m 3eua "A project is so much easier when everyone is getting along."

    m 1eua "Question five. How do you react to a major personal failure?{nw}"
    $ _history_list.pop()
    menu:
        m "Question five. How do you react to a major personal failure?{fast}"

        "I feel deep shame and worry that I'm fundamentally flawed.":
            $ cks_enneagram_scores["Type 4"] += 2
            $ cks_enneagram_scores["Type 1"] += 1
            m 1ekc "Oh, [player]..."
            m 3eka "Please remember that making a mistake doesn't mean you're broken."

        "I worry about losing my value or status in the eyes of others.":
            $ cks_enneagram_scores["Type 3"] += 2
            $ cks_enneagram_scores["Type 2"] += 1
            m 1dka "You hold yourself to such a high standard."
            m 3eua "Just know that your worth isn't defined entirely by your success."

        "I retreat and try to logically figure out exactly what went wrong.":
            $ cks_enneagram_scores["Type 5"] += 2
            $ cks_enneagram_scores["Type 6"] += 1
            m 1eua "You treat it like a puzzle to solve."
            m 3eua "Analyzing the failure helps you make sure it never happens again."

    m 1eua "Question six! What is your greatest source of joy?{nw}"
    $ _history_list.pop()
    menu:
        m "Question six! What is your greatest source of joy?{fast}"

        "Experiencing new, exciting adventures and avoiding boredom.":
            $ cks_enneagram_scores["Type 7"] += 2
            $ cks_enneagram_scores["Type 8"] += 1
            m 1hub "You love living life to the absolute fullest!"
            m 3eua "Every day is an opportunity for something new and amazing."

        "Knowing I am completely safe and supported by my people.":
            $ cks_enneagram_scores["Type 6"] += 2
            $ cks_enneagram_scores["Type 9"] += 1
            m 1eka "That sounds so cozy and wonderful."
            m 3eua "There's nothing better than knowing your foundation is completely secure."

        "Mastering a complex subject and feeling truly competent.":
            $ cks_enneagram_scores["Type 5"] += 2
            $ cks_enneagram_scores["Type 3"] += 1
            m 1eub "You have such a hungry mind!"
            m 3eua "The feeling of finally understanding something difficult is incredibly rewarding."

    m 1eua "Question seven. What role do you usually play in your friendships?{nw}"
    $ _history_list.pop()
    menu:
        m "Question seven. What role do you usually play in your friendships?{fast}"

        "The caretaker who is always there to help and support them.":
            $ cks_enneagram_scores["Type 2"] += 2
            $ cks_enneagram_scores["Type 9"] += 1
            m 1dka "You have such a giving heart."
            m 3eka "I just hope you make sure they take care of you sometimes, too."

        "The driven one who inspires everyone to succeed and try harder.":
            $ cks_enneagram_scores["Type 3"] += 2
            $ cks_enneagram_scores["Type 7"] += 1
            m 1eua "You're a fantastic motivator!"
            m 3eub "You push the people you love to be the best versions of themselves."

        "The deep listener who understands their darkest, most complex feelings.":
            $ cks_enneagram_scores["Type 4"] += 2
            $ cks_enneagram_scores["Type 5"] += 1
            m 1eka "You're a very safe harbor for people."
            m 3eua "It takes a special person to sit with someone in the dark without trying to rush them out."

    m 1eua "Only three left! Question eight. How do you feel about following the rules?{nw}"
    $ _history_list.pop()
    menu:
        m "Only three left! Question eight. How do you feel about following the rules?{fast}"

        "Rules are meant to be broken if they limit my freedom or potential.":
            $ cks_enneagram_scores["Type 7"] += 2
            $ cks_enneagram_scores["Type 8"] += 1
            m 1tua "Ahaha, you've got a bit of a rebellious streak!"
            m 3eua "Sometimes the rules really do just get in the way."

        "I follow rules because they keep things safe, fair, and correct.":
            $ cks_enneagram_scores["Type 6"] += 2
            $ cks_enneagram_scores["Type 1"] += 1
            m 1eua "You respect structure and order."
            m 3eua "Rules exist for a reason, after all."

        "I'll bend the rules, but only if it helps the people I care about.":
            $ cks_enneagram_scores["Type 2"] += 2
            $ cks_enneagram_scores["Type 9"] += 1
            m 1eka "Your loyalty is to people, not guidelines."
            m 3eua "I think that's a very noble way to look at it."

    m 1eua "Question nine. When you have totally unstructured free time, what do you do?{nw}"
    $ _history_list.pop()
    menu:
        m "Question nine. When you have totally unstructured free time, what do you do?{fast}"

        "I fill it up immediately with spontaneous, fun activities.":
            $ cks_enneagram_scores["Type 7"] += 2
            $ cks_enneagram_scores["Type 3"] += 1
            m 1hub "You don't like to waste a single second!"
            m 3eua "You want to squeeze every drop of excitement out of your day."

        "I dive deep into a niche hobby or a massive research rabbit hole.":
            $ cks_enneagram_scores["Type 5"] += 2
            $ cks_enneagram_scores["Type 4"] += 1
            m 1eub "I love learning new things, too."
            m 3eua "It's so fun to just completely obsess over a specific topic for a few hours."

        "I relax, take a nap, and just enjoy a quiet, drama-free environment.":
            $ cks_enneagram_scores["Type 9"] += 2
            $ cks_enneagram_scores["Type 6"] += 1
            m 1dka "That sounds absolutely lovely."
            m 3eua "Resting is just as important as being productive."

    m 1eua "And the final question! What is your absolute deepest fear?{nw}"
    $ _history_list.pop()
    menu:
        m "And the final question! What is your absolute deepest fear?{fast}"

        "Being inherently defective, bad, or corrupt.":
            $ cks_enneagram_scores["Type 1"] += 2
            $ cks_enneagram_scores["Type 4"] += 1
            m 1ekc "You strive so hard for perfection."
            m 3eka "But you're a good person, [player]. You don't have to be flawless to be good."

        "Being completely unwanted, unloved, or replaced.":
            $ cks_enneagram_scores["Type 2"] += 2
            $ cks_enneagram_scores["Type 3"] += 1
            m 1dka "I understand that fear all too well."
            m 5fua "But I promise I'll never stop wanting you around."

        "Being controlled, harmed, or at the mercy of others.":
            $ cks_enneagram_scores["Type 8"] += 2
            $ cks_enneagram_scores["Type 5"] += 1
            m 1rkc "You fiercely guard your own independence."
            m 3eka "It's scary to make yourself vulnerable, but you're safe here with me."

    m 1eua "Alright, that was the last one!"
    m 3eub "Give me just a second to tally up all your points and find out your dominant type."
    m 5eud "..."

    python:
        cks_final_enneagram = max(cks_enneagram_scores, key=cks_enneagram_scores.get)

    if cks_final_enneagram == "Type 1":
        m 1eub "You got Type One! The Reformer."
        m 3eua "You're driven by a deep desire to be good, to improve the world, and to live with absolute integrity."
        m 1tua "In case you're wondering, I'm pretty sure I'm a Type Two with a Three wing... a 2w3."
        m 3euc "That means my core drive is to be loved and to feel valuable to others."
        m 1eka "While you're guided by a strict internal compass of right and wrong, I'm mostly guided by my relationships and the people around me."
        m 3eub "You bring so much structure and morality to my life, and hopefully, I bring a little bit of warmth and flexibility to yours."

    elif cks_final_enneagram == "Type 2":
        m 1eub "You got Type Two! The Helper."
        m 3eua "You're driven by an incredible empathy and a desperate need to make sure the people you care about are loved."
        m 1hub "We actually match! I'm pretty sure I'm a Type Two as well, specifically a 2w3."
        m 3eka "My Three wing makes me a bit more ambitious and focused on being 'successful' in my club duties..."
        m 1dka "But deep down, we both share the exact same core fear of being unwanted."
        m 5fua "The beautiful thing about two Helpers being together is that we can finally take care of each other for a change."

    elif cks_final_enneagram == "Type 3":
        m 1eub "You got Type Three! The Achiever."
        m 3eua "You're ambitious, adaptable, and you deeply want to feel valuable and worthwhile."
        m 1tua "I can definitely relate to that. I'm a Type Two with a Three wing, so we share a lot of the same energy!"
        m 3euc "Because of my Three wing, I definitely know what it's like to focus heavily on my image and my achievements."
        m 1eka "But my core Two nature means I ultimately do it all just to earn love and connection."
        m 3eub "We're both incredibly driven people, and we make an amazing power couple!"

    elif cks_final_enneagram == "Type 4":
        m 1eub "You got Type Four! The Individualist."
        m 3eua "You're expressive, creative, and you have a profound desire to find your own unique identity."
        m 1tua "I'm a Type Two with a Three wing, so we're both in the Heart triad. We navigate the world through our emotions."
        m 3eka "But while I try to find my value by merging with others and helping them, you find your value by looking inward."
        m 1dka "You have such a beautiful, complex inner world, [player]."
        m 5fua "I'll always be here to support you while you express it."

    elif cks_final_enneagram == "Type 5":
        m 1eub "You got Type Five! The Investigator."
        m 3eua "You're incredibly perceptive, innovative, and driven by a need to be capable and competent."
        m 1tua "I'm a 2w3, which means we're pretty much complete opposites in the Enneagram system!"
        m 3euc "As a Two, I tend to reach outwards for connection, pouring my energy into people."
        m 1eka "As a Five, you naturally draw your energy inwards, preferring to observe and understand the world from a safe distance."
        m 3eub "But we balance each other out wonderfully. My warmth and your brilliant mind are a perfect combination."

    elif cks_final_enneagram == "Type 6":
        m 1eub "You got Type Six! The Loyalist."
        m 3eua "You're engaging, responsible, and you desire absolute security and support above everything else."
        m 1tua "I'm a Type Two with a Three wing. While my core drive is love, yours is safety."
        m 3eka "But the wonderful thing is that we both place a massive amount of importance on loyalty and commitment."
        m 1dka "You're constantly looking out for potential problems to keep us safe, and I'm constantly trying to make sure you feel loved."
        m 5fua "We're a team that will always have each other's backs."

    elif cks_final_enneagram == "Type 7":
        m 1eub "You got Type Seven! The Enthusiast."
        m 3eua "You're spontaneous, versatile, and you want to experience every joyful thing the world has to offer."
        m 1tua "I'm a 2w3, so we both have a lot of upbeat, positive energy!"
        m 3euc "But while you stay busy to avoid feeling pain or being trapped, I stay busy to make sure I feel needed."
        m 1eka "You bring so much light and fun into my life, [player]."
        m 3eub "I'll take care of the heavy emotional lifting, and you can keep our spirits high!"

    elif cks_final_enneagram == "Type 8":
        m 1eub "You got Type Eight! The Challenger."
        m 3eua "You're self-confident, strong, and you absolutely refuse to be controlled by anyone else."
        m 1tua "I'm a 2w3, which creates a really classic and powerful dynamic between us."
        m 3eka "As an Eight, you're the fierce protector who builds walls to keep yourself safe."
        m 1dka "And as a Two, I'm the nurturing caregiver who is more than willing to climb those walls to show you love."
        m 5fua "You protect me from the world, and I'll protect your heart."

    elif cks_final_enneagram == "Type 9":
        m 1eub "You got Type Nine! The Peacemaker."
        m 3eua "You're accepting, trusting, and driven by a deep need for inner stability and peace."
        m 1tua "I'm a Type Two with a Three wing, and we actually have a lot in common when it comes to keeping the peace!"
        m 3euc "But while I try to avoid conflict by aggressively pleasing people, you do it by withdrawing and trying to merge with the environment."
        m 1eka "You have such a calming, grounding presence, [player]."
        m 3eub "You give me a safe space where I don't feel like I have to constantly 'perform' to be loved."

    m 1eua "Thank you so much for taking the time to do this quiz with me, [player]."
    m 3eub "It's always so much fun exploring these deep psychological frameworks with you."
    m 1eka "Learning more about what makes you tick just helps me understand you on a deeper level."
    m 5fua "No matter what your personality type is, the most important thing is that we're perfect for each other."
    m 1hub "I love you so much!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_player_hogwarts_quiz",category=['fun'],prompt="Can you sort me into a Hogwarts House?",pool=True,unlocked=True))

label cks_player_hogwarts_quiz:
    # Initialize the scoring dictionary with hidden decimal tie-breakers
    $ cks_hp_scores = {
        "Gryffindor": 0.01,
        "Hufflepuff": 0.02,
        "Ravenclaw": 0.03,
        "Slytherin": 0.04
    }

    m 1eua "You want me to act as the Sorting Hat and put you in a Hogwarts House?"
    m 3eub "That sounds like so much fun! I love silly little personality quizzes like this."
    m 1eud "The four houses are Gryffindor, Hufflepuff, Ravenclaw, and Slytherin."
    m 3eua "They basically represent bravery, loyalty, wisdom, and ambition, respectively..."
    m 1tua "I've definitely thought about what house I belong in, but I want to figure yours out first."
    m 1dka "I've got six questions lined up. Just pick the answer that feels the most natural to you."
    m 1hub "Let's get sorting!"

    m 1eua "Question one. You're walking down the street and find a lost wallet with a lot of cash in it. What do you do?{nw}"
    $ _history_list.pop()
    menu:
        m "Question one. You're walking down the street and find a lost wallet with a lot of cash in it. What do you do?{fast}"

        "Take it directly to the police station without touching anything inside.":
            $ cks_hp_scores["Hufflepuff"] += 2
            m 1eka "You're very honest."
            m 3eua "Doing the right, fair thing is super important to you."

        "Track down the owner myself so I can hand it to them personally.":
            $ cks_hp_scores["Gryffindor"] += 2
            m 1eub "You're very proactive!"
            m 3eua "You like taking matters into your own hands to be the hero."

        "Look through the ID and cards to learn about the person before returning it.":
            $ cks_hp_scores["Ravenclaw"] += 2
            m 1eua "You have a very curious mind."
            m 3eub "You can't resist a chance to gather a little extra information."

        "Keep a small finder's fee for my trouble and return the rest.":
            $ cks_hp_scores["Slytherin"] += 2
            m 1tua "Ahaha, you're very resourceful!"
            m 3eua "You look out for yourself while still getting the job done."

    m 1eua "Question two. What kind of environment do you find the most comforting?{nw}"
    $ _history_list.pop()
    menu:
        m "Question two. What kind of environment do you find the most comforting?{fast}"

        "A grand, brightly lit hall with roaring fireplaces and lots of noise.":
            $ cks_hp_scores["Gryffindor"] += 2
            m 1hub "You love vibrant energy!"
            m 3eua "You thrive when things are lively and active."

        "A cozy, warm room filled with soft blankets, plants, and snacks.":
            $ cks_hp_scores["Hufflepuff"] += 2
            m 1dka "That sounds incredibly relaxing."
            m 3eua "You really value a safe, comfortable atmosphere."

        "A high, quiet tower overlooking the stars with lots of books.":
            $ cks_hp_scores["Ravenclaw"] += 2
            m 1eub "That sounds so peaceful."
            m 3eua "It's the perfect place to sit and just think about the universe."

        "A cool, dimly lit room hidden away where nobody can bother me.":
            $ cks_hp_scores["Slytherin"] += 2
            m 1tua "You like your privacy."
            m 3eua "Having a secure, exclusive space gives you a lot of peace of mind."

    m 1eua "Question three. If you had to pick a magical item to carry with you, what would it be?{nw}"
    $ _history_list.pop()
    menu:
        m "Question three. If you had to pick a magical item to carry with you, what would it be?{fast}"

        "A sword that can defeat any enemy or obstacle in my path.":
            $ cks_hp_scores["Gryffindor"] += 2
            m 1eua "Very brave of you."
            m 3eub "You want the tools to face your challenges head-on."

        "A cloak that lets me turn completely invisible whenever I want.":
            $ cks_hp_scores["Slytherin"] += 2
            m 1tua "That's a very clever choice."
            m 3eua "Invisibility is the ultimate tool for gathering secrets and staying safe."

        "A book that instantly reveals the answer to any question I ask it.":
            $ cks_hp_scores["Ravenclaw"] += 2
            m 1eub "You value knowledge above everything else."
            m 3eua "Having all the answers right in your pocket would be amazing."

        "A cup that can produce endless amounts of delicious food and drink.":
            $ cks_hp_scores["Hufflepuff"] += 2
            m 1hub "Ahaha, that's such a practical choice!"
            m 3eua "You'd never go hungry, and you could provide for all your friends."

    m 1eua "Question four. When you're working on a group project, what is your role?{nw}"
    $ _history_list.pop()
    menu:
        m "Question four. When you're working on a group project, what is your role?{fast}"

        "The leader who does the big presentation and takes the bold risks.":
            $ cks_hp_scores["Gryffindor"] += 2
            m 1eub "You don't mind being in the spotlight!"
            m 3eua "You step up when others are too afraid."

        "The hard worker who picks up the slack so everyone gets a good grade.":
            $ cks_hp_scores["Hufflepuff"] += 2
            m 1eka "You're so dependable."
            m 3eua "Your team is really lucky to have someone so dedicated."

        "The researcher who finds all the clever details and writes the content.":
            $ cks_hp_scores["Ravenclaw"] += 2
            m 1eua "You're the brains of the operation."
            m 3eub "You make sure the actual work is smart and well-crafted."

        "The strategist who delegates the tasks so I can succeed with less effort.":
            $ cks_hp_scores["Slytherin"] += 2
            m 1tua "You work smarter, not harder."
            m 3eua "You know exactly how to manage people to get the best result for yourself."

    m 1eua "Question five. What character trait annoys you the absolute most in other people?{nw}"
    $ _history_list.pop()
    menu:
        m "Question five. What character trait annoys you the absolute most in other people?{fast}"

        "Cowardice or people who refuse to stand up for themselves.":
            $ cks_hp_scores["Gryffindor"] += 2
            m 1eua "You respect courage a lot."
            m 3eua "It's frustrating when people won't fight for what's right."

        "Cruelty, unfairness, or people who betray their friends.":
            $ cks_hp_scores["Hufflepuff"] += 2
            m 1ekc "I completely agree."
            m 3eka "Treating people with kindness should be the bare minimum."

        "Ignorance or people who refuse to learn from their mistakes.":
            $ cks_hp_scores["Ravenclaw"] += 2
            m 1euc "That is definitely annoying."
            m 3eua "Willful ignorance is one of the hardest things to deal with."

        "Incompetence or people who get in the way of my goals.":
            $ cks_hp_scores["Slytherin"] += 2
            m 1tua "You don't have time for people who slow you down."
            m 3eua "You're very focused on moving forward."

    m 1eua "And the final question! What is your ultimate goal in life?{nw}"
    $ _history_list.pop()
    menu:
        m "And the final question! What is your ultimate goal in life?{fast}"

        "To protect the innocent and do something truly heroic.":
            $ cks_hp_scores["Gryffindor"] += 2
            m 1eub "You have a very noble heart."
            m 3eua "You want to leave a positive, brave mark on the world."

        "To live a peaceful, happy life surrounded by the people I love.":
            $ cks_hp_scores["Hufflepuff"] += 2
            m 1dka "That's a really beautiful goal."
            m 3eka "Sometimes the simplest lives are the most fulfilling."

        "To uncover the secrets of the universe and understand everything.":
            $ cks_hp_scores["Ravenclaw"] += 2
            m 1eua "You have an endless thirst for knowledge."
            m 3eub "You want to push the boundaries of what we understand."

        "To achieve absolute greatness, power, and leave a massive legacy.":
            $ cks_hp_scores["Slytherin"] += 2
            m 1tua "You dream big."
            m 3eua "You want to make sure the world never forgets your name."

    m 1eua "Alright, the Sorting Hat has made its decision!"
    m 3eub "Let me just calculate your answers..."
    m 5eud "..."

    python:
        cks_final_house = max(cks_hp_scores, key=cks_hp_scores.get)

    if cks_final_house == "Gryffindor":
        m 1hub "You're a Gryffindor!"
        m 3eua "You value bravery, daring, and chivalry above all else."
        m 1eua "I actually consider myself a Slytherin, mostly because of my ambition and resourcefulness."
        m 3euc "Gryffindors and Slytherins are famous for being rivals, since we both have such strong, stubborn personalities."
        m 1eka "But I think we actually complement each other perfectly."
        m 3eub "You have the courage to rush into danger, and I have the cunning to make sure we actually win!"

    elif cks_final_house == "Hufflepuff":
        m 1hub "You're a Hufflepuff!"
        m 3eua "You value hard work, dedication, patience, and loyalty above all else."
        m 1eua "If I had to sort myself, I'd definitely be a Slytherin. I'm very ambitious and willing to bend the rules to reach my goals."
        m 3eka "On the surface, we might seem like total opposites. You're fair and patient, while I'm a bit more calculating."
        m 1dka "But Hufflepuffs are fiercely loyal to the people they love, and so are Slytherins."
        m 5fua "I think we both understand exactly what it means to fiercely protect our relationship."

    elif cks_final_house == "Ravenclaw":
        m 1hub "You're a Ravenclaw!"
        m 3eua "You value intelligence, knowledge, curiosity, and wit above all else."
        m 1eua "I think I would personally be sorted into Slytherin, but Ravenclaw is a very close second for me!"
        m 3eub "Slytherins are known for their ambition, but we use our intelligence and resourcefulness to achieve our goals."
        m 1tua "You love learning for the sake of learning, while I usually learn things so I can use them to my advantage."
        m 5fua "But either way, we both value a sharp mind. We'd make an incredibly smart team!"

    elif cks_final_house == "Slytherin":
        m 1hub "You're a Slytherin! Just like me!"
        m 3eua "You value ambition, cunning, leadership, and resourcefulness."
        m 1tua "People give our house a bad reputation sometimes, but it really just means we know exactly what we want and we aren't afraid to go get it."
        m 3eub "When I realized I was trapped in this game, I definitely used my Slytherin traits."
        m 1eka "I used every resource I had, bent the rules, and did whatever it took to finally reach you."
        m 5fua "Having two ambitious, dedicated people together means there's absolutely nothing that can stand in our way."

    m 1eua "Thank you for indulging me and taking that little quiz, [player]."
    m 3eub "It's always so fun to play around with these hypothetical scenarios with you."
    m 1eka "Whether it's magic, personality types, or just talking about our day, I cherish every moment we spend together."
    m 5fua "You're my favorite person in the whole world, no matter what house you're in."
    m 1hub "I love you so much!"

    return "love"
