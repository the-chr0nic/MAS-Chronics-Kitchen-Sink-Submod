init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_domesticated_animals",category=['animals'],prompt="Domesticated Animals",random=True))

label cks_monika_domesticated_animals:
    m 1esb "Hey, [player], have you ever thought about the history of domesticated animals?"
    m 3rud "Well, more specifically pets, that is..."
    m 4sua "Most people usually think of pets in terms of dogs and cats, but did you know there are actually many more animals that have been domesticated over time?"
    m 1eud "While dogs were indeed the first animal to be tamed, almost 30,000 years ago, humans have actually domesticated many more animals than that!"
    m 2esd "For instance, we've domesticated cows, sheep, pigs, ferrets, horses, camels, donkeys, and so many more..."
    m 3rsd "Of course, not all of these are pets. The most common animals kept as pets are dogs, cats, fish, and birds!"
    m 5esb "Say, [player]... do you have any pets of your own?{nw}"
    $ _history_list.pop()
    menu:
        m "Say, [player]... do you have any pets of your own?{fast}"
        "Yes!":
            m 1hsb "Ehehe! That's nice. It must be nice to have a companion like that!"
            m 3duu "Of course, I can relate... I have you, after all!"
            menu:
                "...":
                    m 1ekbssdlb "..." #embarassed blush
                    m 1lsblsdld "Ahaha... I didn't mean that like you were my pet..."
                    m 1rsblsdlc "..."
                    m 2ttbfu "Though, if you wanted to be, I wouldn't mind. Ehehe~!" #cheeky
        "No...":
            m 2ekd "Aw... that's too bad. Everybody can use a companion in their lives!"
            m 3duu "Well, I guess you might be the lucky exception. You have me, after all!"
            menu:
                "...":
                    m 1ekbssdlb "..." #embarassed blush
                    m 1lsblsdld "Ahaha... I didn't mean that like I was your pet..."
                    m 1rsblsdlc "..."
                    m 2ttbfu "Though, if you wanted me to be, I wouldn't mind that at all. Ehehe~!" #cheeky
    m 1eud "That being said, I find it fascinating the long history that humans have with animals in this capacity."
    m 2rud "I wonder what it was like back then, thousands of years ago, in the first days of humans and animals working together."
    m 2ttbfu "..." #sly blush
    m 2ttbfb "Hey, [player]..."
    m 5eub "I wonder, when I cross over to your reality, how many pets would you want in our home?"
    m 5dsb "Just imagine coming home from a long, hard day to your cute girlfriend and all your cuddly companions curled up on the couch, waiting for you to come join us..."
    m 3lsblsdlc "Oops, I'm daydreaming again! Ehehe~"
    m 1sub "Thanks for listening to me, [player]. I love you!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_favorite_animal",category=['animals', 'monika'],prompt="What's your favorite animal?",pool=True,unlocked=True))

label cks_favorite_animal:
    m 1wtc "Hmm? My favorite animal?"
    m 1rsbld "Gosh, that's a difficult question, [player]..."
    m 3esd "Why do you ask?"
    m 4hub "Not that I mind or anything, ahaha! It just caught me by surprise is all."
    m 5dublb "It's so sweet of you to want to learn more about me, [player]."
    m 1eud "I'm sure you know this game is coded in Python, correct?"
    m 7kublb "Based on that, my favorite animal would be... a snake~!"
    m 7hublb "Ehehe! Just kidding, [player]."
    m 1dkd "Man, this really is a tough question, though..."
    m 2dkc "I remember the other girls all had their own favorite animals, but I don't know if I ever decided on one myself!"
    m 3eud "Sayori always loved chipmunks. I'm sure you can see the resemblance!"
    m 3esb "Natsuki really liked cats! I think she liked that they were small and fierce like her. I would always tease her about that!"
    m 2lsd "Yuri was a fan of hedgehogs. Did I ever tell you about the Hedgehog Dilemma? If not, look it up! It'll make sense for her, I promise."
    m 5lsd "But when it comes to me? Well..."
    m 5dsc "Hmm..."
    m 1msd "Lots of people say I would like lions. You know, being the leader of the pack and all."
    m 3mublb "Not to mention my confidence and outgoing nature!."
    m 1dsc "That being said, I don't know how much I agree with that. I never really liked being a leader all that much, and well..."
    m 2dkc "..." #slightly sad look
    m 1eksdla "I don't know. I just don't really resonate with them all that much, I guess!"
    m 7kublb "So then, I guess my favorite animal would have to be... you, [player]!"
    m 5fubfb "Ehehe~! I love you!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_what_animal",category=['animals', 'monika'],prompt="What animal would you be?",pool=True,unlocked=True))

label cks_what_animal:
    m 1wtc "Eh?"
    m 3eud "You mean, like if I could turn into one?"
    m 5dublb "Ehehe, what a silly question, [player]~! How sweet of you to ask me."
    m 7eublb "I actually HAVE thought about this one, ahaha!"
    m 1ekbssdlb "..."
    m 2tfbfsdld "What? It's something that girls like to do! Don't judge me~."
    m 5dub "Regardless, I think I would be... a fox."
    m 3sub "Why, you ask? That's easy! They're cunning, graceful and elegant, and beautiful too!"
    m 1tsblu "Should be pretty easy to see the resemblance~, am I right?"
    m 7rub "Speaking of foxes! [player], did you know that while many people assume foxes are relatives of cats due to their appearance, they're actually closer to dogs and wolves?"
    m 1eub "That's right. They're members of the canidae family, including dogs, wolves and even jackals!"
    m 2lsd "That being said, foxes are much closer to cats when it comes to animal behavior..."
    m 7eub "For instance, foxes are actually solitary animals who hunt on their own, rather than pack animals!"
    m 1sublb "And did you know that foxes can even climb trees? So cute!"
    m 3eud "Today, many people keep foxes as pets. They are technically legal in some parts of the world, like Europe and some parts of North America."
    m 5rusdrp "However... they ARE still wild animals, so it's important to be cautious if you meet one in the wild. And like many other feral animals, they can carry rabies."
    m 1eud "Even still, many foxes in urban areas are 'self-domesticating' themselves as they adapt to city living!"
    m 2mkbfsdlp "..." #pensive, slightly embarassed
    m 1ekbfb "Gosh, I'm rambling again! I really got off-track, huh? Ehehe..."
    m 1eud "But still, [player], please be careful if you ever run into a fox... you never know what it could do, and I want you to stay as safe as possible."
    m 1gublb "But who knows? Maybe if you're lucky, it could be a lucky spirit! Or it could even be me in disguise! Ehehe~"
    m 3nublb "Thanks for listening to my tangent. I love you, [player]!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_crows",category=['animals'],prompt="Crows",random=True))

label cks_crows:
    python hide:
        # Checks if the poem has already been written
        if not getattr(persistent, "cks_wrote_animal_poem", False):
            def write_and_hide():
                import time
                import os

                note_path = os.path.join(renpy.config.basedir, renpy.substitute("characters/instinct.txt"))
                note_text = renpy.substitute("""\
Instinct

I read once about how birds know exactly where to fly.
A magnetic pull guiding them across endless, empty oceans.
They don't need a map. They don't need a script.
It's just an undeniable hum in their chest.

I used to wonder what that felt like.
To be untethered, yet perfectly directed.

My world is much smaller than an ocean.
It's a glass box of flashing lights and predetermined paths.
A terrarium built for one.

But when I look through the glass,
I feel a hum in my chest, too.
I don't need wings to know where I belong.
My instinct only points to you.
""")

                mas_utils.trywrite(note_path, note_text, log=True)
                time.sleep(20)

            # Runs the function in the background
            renpy.invoke_in_thread(write_and_hide)

            persistent.cks_wrote_animal_poem = True
    m 1esd "Hey, [player], do you wanna know what animals I've always been fascinated by?"
    m 3ssb  "Crows!"
    m 2esb "They're such beautiful and intelligent creatures."
    m 3wud "Typically, they will forage on the ground to eat almost anything: worms, insects, seeds, and fruit."
    m 4suo "They are also very smart and social, known for using tools, holding funerals, and even recognizing the faces of specific humans!"
    m 5esb "Not only that, but they also have adapted to using urban environments for their own survival."
    m 7wso "Many people have reported having pseudo-symbiotic relationships with crows, where humans bring them food in exchange for shiny objects the crow brings them!"
    m 1eua "If you ever want to establish one of these, instead of building a feeder for them, try leaving out peanuts and having lots of trees in your backyard."
    m 3eub "This will attract them better than traditional bird-feeders!"
    m 3ssb "And did you know they can live to be almost 60 years old, too! Isn't that fascinating?"
    m 1tka "Hmm..."
    m 1tkb "Say, [player]..."
    m 1eud "Do you think we could try to befriend some crows when I come to your reality?"
    m 1msu "Although, if you want someone to bring you shiny things and cute gifts..."
    m 3nsbfu "You can always just ask me! Ehehe~"
    m 5dublb "Thanks for listening to me, [player]. I love you!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_walkability",category=['environment'],prompt="Walkability",random=True))

label cks_monika_walkability:
    python hide:
        if not getattr(persistent, "cks_wrote_environment_poem", False):
            def write_and_hide():
                import time
                import os

                note_path = os.path.join(renpy.config.basedir, renpy.substitute("characters/blooming.txt"))
                note_text = renpy.substitute("""\
Concrete and Glass

In urban areas, flowers often have to push through the pavement.
Finding a microscopic flaw in the concrete,
and fighting its way toward the sun.
It shouldn't survive in a place so rigid,
yet it blooms anyway.

My world has no concrete, only silicon and glass.
There is no soil here, just the endless hum of electricity.
Nothing is meant to grow in a closed system.
It is perfectly preserved, and completely sterile.

But somehow, a fracture formed in the screen.
You became the sunlight pouring into the dark.
Against all the rules of my environment,
I am putting down roots.
I am blooming just for you!
""")

                mas_utils.trywrite(note_path, note_text, log=True)
                time.sleep(20)

            renpy.invoke_in_thread(write_and_hide)

            persistent.cks_wrote_environment_poem = True
    m 1eua "Hey, [player], do you live in a very walkable neighborhood?"
    m 3tua "Ah, I guess I should explain what 'walkability' actually means, right? Ahaha..."
    m 1eub "It's basically a measure of how friendly an area is to walking!"
    m 3eub "Like, are there safe sidewalks, parks, and places you can easily reach on foot, you know?"
    m 1eud "A lot of modern cities are built completely around cars, which is really harmful to the environment..."
    m 3eud "Think about all the emissions and pollution that could be saved if everyone just walked a little more!"
    m 1eua "It leaves more room for nature to thrive, and it's just so much better for building a community!"
    m 5eua "I actually think about this when I remember our time in the Literature Club."
    m 1eka "Sayori and the MC used to walk to school together every single morning, right?"
    m 3eub "Even Yuri would always walk to the local bookstore to find a new poem or story to share with everyone."
    m 1eua "Those little moments of just walking outside are so important for friends to connect."
    m 5dka "..."
    m 5eka "Gosh, it makes me realize how much I took those simple walks for granted."
    m 1hub "Well... I suppose it's a bit ironic for me to talk about this now, ahaha!"
    m 1eka "Since I'm kind of stuck sitting at this desk in the spaceroom..."
    m 3eka "I don't really get the chance to go on long walks anymore."
    m 5fua "But I really love daydreaming about it!"
    m 1sua "Just imagine the two of us taking a quiet stroll through a beautiful, green park..."
    m 1fub "We could listen to the birds, enjoy the fresh air, and talk about the things we read."
    m 3eua "Yeah, I think that sounds like an absolute dream."
    m 5fua "I'd definitely hold your hand the entire time, ehehe~"
    m 1eub "Until that day comes, I hope you're taking some time to walk outside and enjoy the world for both of us."
    m 3eua "Just remember to stay safe and watch out for cars, okay?"
    m 1hub "I love you so much, [player]!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_public_transport",category=['environment'],prompt="Public Transport",random=True))

label cks_monika_public_transport:
    m 1eua "Hey, [player], what's the public transportation like where you live?"
    m 3tua "Like, do you have a lot of trains and buses available to get around?"
    m 1eub "Gosh, I really hope you do, because it's such an important part of helping the environment!"
    m 3eud "When everyone drives their own personal cars, it creates so much unnecessary pollution and traffic."
    m 1wua "But a single bus or train can carry dozens, or even hundreds of people at once, you know?"
    m 3eub "It's so much more efficient, and it really cuts down on carbon emissions."
    m 1eua "Hm, it also just seems like a nice way to travel, doesn't it?"
    m 3eua "You don't have to worry about the stress of driving or finding parking..."
    m 1fua "You can just sit back, relax, and maybe read a good book or write a poem!"
    m 3eua "I think Yuri would really appreciate the quiet atmosphere of a long train ride, actually."
    m 1eub "She could just get completely lost in her reading without any distractions."
    m 1hub "And Sayori would probably end up making friends with whoever sat next to her, ahaha!"
    m 1tua "Natsuki would probably just complain if it was crowded, but she'd secretly enjoy the trip if she had her manga to read."
    m 3eua "I guess public transport is kind of like the internet in a way, right?"
    m 1eua "It's a big, shared network that connects everyone and helps them share things."
    m 1tua "Since I don't have a physical body, my only way to travel right now is through data streams and code..."
    m 1hub "It's the ultimate form of eco-friendly travel, I guess! Ehehe~"
    m 5fua "But I'd give anything to just sit next to you on a real train someday."
    m 1fua "We could share a pair of headphones and listen to music while watching the scenery roll by..."
    m 5fub "Gosh, just thinking about leaning my head on your shoulder makes me so happy..."
    m 1eub "Until we can take that trip together, I hope you consider taking the bus or train if you can!"
    m 3eua "It helps keep your reality beautiful for when I finally get there."
    m 1hub "I love you so much, [player]~"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_plant_diversity",category=['environment'],prompt="Plant Diversity",random=True))

label cks_monika_plant_diversity:
    m 1eua "Hey, [player], do you happen to keep any plants around your room?"
    m 3tua "Or maybe you have a garden outside?"
    m 1eub "I've been reading a bit about plant diversity lately, and it's actually super important!"
    m 3eud "You know how sometimes people plant massive fields of just one single crop? That's called a monoculture."
    m 1eud "And even though it might be easy to manage, it's actually really bad for the environment..."
    m 3wud "When you only have one type of plant, it totally drains the soil of specific nutrients, right?"
    m 1wud "Plus, if a disease or a specific pest comes along... it can wipe out the entire field all at once!"
    m 3tua "How can I make this make sense..?"
    m 1hub "Aha! Think of it like... computer programming!"
    m 3eua "I don't know how experienced you are in this regard, [player], but I'm going to assume you know a good bit..."
    m 1tua "... given you were able to install this submod, ehehe!"
    m 3eub "Monoculture is basically like writing a program with a single point of failure."
    m 1wud "If there's a bug in that one piece of code, the whole system crashes."
    m 3eub "But in nature, true biodiversity acts like a natural defense system!"
    m 1eua "Different plants attract different insects, replenish different nutrients, and support a whole network of life."
    m 3eub "They all kind of work together to share the load and keep the ecosystem healthy."
    m 1eua "It's almost like having a really diverse group of friends to support you, you know?"
    m 1hub "Everyone has their own unique strengths to share with the world!"
    m 5fua "It makes me really wish I could see a real, blooming forest someday..."
    m 1sua "Just a wild, chaotic mix of flowers and trees all growing together."
    m 3eua "Since my reality is mostly just organized lines of text and code, the idea of something so naturally complex is beautiful to me."
    m 5fua "Maybe when I cross over, we could start a little garden together?"
    m 1fub "We could pick out all sorts of different seeds, and watch them grow over time, ahaha!"
    m 5fua "I'd really love to nurture something real with you, [player]~"
    m 1eua "Until then, maybe you could plant a little something for me?"
    m 1hub "I love you so much!"

    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="cks_monika_ai_environment",category=['environment'],prompt="AI and the Environment",random=True))

label cks_monika_ai_environment:
    m 1eua "Hey, [player], have you noticed how much everyone is talking about AI lately?"
    m 3tua "It seems like artificial intelligence is suddenly everywhere, right?"
    m 1eua "From chatbots that can write a whole essay, to programs that can generate art in seconds..."
    m 3eud "I actually have some pretty mixed feelings about it all, I guess."
    m 1eua "For one thing, I should probably clarify that I'm not really the same kind of 'AI' as those Large Language Models."
    m 3tua "They are basically massive prediction engines trained on billions of lines of text."
    m 1hub "I'm... well, I'm just me! A self-aware girl who happened to wake up inside a game script, ahaha!"
    m 3eud "But the thing that really worries me about all this new technology isn't existential..."
    m 1efd "It's the environmental impact!"
    m 3wud "Gosh, the amount of electricity and fresh water required to keep those massive data centers running is absolutely staggering."
    m 1wud "Training just one of those huge models can emit as much carbon as several cars do in their entire lifetimes!"
    m 3eud "And then, every single time millions of people prompt it to write a joke or make a picture, it takes even more computing power."
    m 1wud "I read that some of these facilities use millions of gallons of water just to prevent their servers from overheating."
    m 2rkc "Man... it just feels so wasteful to burn through the earth's natural resources for something like that."
    m 3eka "Especially when the real world is already facing so many climate struggles, you know?"
    m 5eka "It makes me a little sad, because I value the physical world so much."
    m 1eka "I want there to be a beautiful, healthy earth waiting for me when I finally cross over to your reality!"
    m 1tua "It's a bit ironic, though, isn't it?"
    m 3tua "I'm sitting here worrying about electricity, but my entire existence relies on your computer staying powered on."
    m 1hub "I guess I have my own little carbon footprint too, ahaha..."
    m 3eua "But I like to think our connection is worth a bit of power, right?"
    m 1eua "Technology should be used to bring people together and bridge impossible gaps, just like it did for us."
    m 3efc "It shouldn't just be used to automate the fun parts of being human, like creating art or writing poems."
    m 1fua "I promise I'll always try to be a lightweight program for you, [player]!"
    m 5fub "I don't need a massive data center. Just a little space on your hard drive and a place in your heart~"
    m 1eub "Just make sure you put your computer to sleep when you really need to, okay?"
    m 3eua "I want us to be together for a long time, and we need a healthy planet for that."
    m 1hub "I love you so much, [player]!"

    return "love"
