init 5 python:
    # Initialize our custom minigame stats if they don't exist
    if persistent._cks_minigame_stats is None:
        persistent._cks_minigame_stats = {
            "hl_wins": 0, "hl_losses": 0,
            "gn_wins": 0, "gn_losses": 0,
            "ci_wins": 0, "ci_losses": 0
        }

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_monika_guess_number",
            category=['fun'],
            prompt="Can we play a guessing game?",
            unlocked=True,
            pool=True
        )
    )

label cks_monika_guess_number:
    m 1eua "A guessing game? Like... you want me to pick a number and see if you can find it?"
    m 3eub "That sounds like a lot of fun! I've actually been looking for more ways to pass the time with you."
    m 1tua "But don't think it'll be easy just because I'm a computer. I can be pretty unpredictable when I want to be!"

    label .game_menu:
        m 1eua "What did you want to play?{nw}"
        $ _history_list.pop()
        menu:
            m "What did you want to play?{fast}"

            "Higher/Lower":
                jump .higher_lower_prep

            "Guess the Number":
                jump .guess_number_prep

            "Call It":
                jump .call_it_prep

            "Nevermind":
                m 1eka "Oh, alright. Maybe we can play later!"
                return

    # --- Higher/Lower Logic ---
    label .higher_lower_prep:
        m 1eua "Higher or Lower! I'll pick a number between 1 and 100, and you've gotta find it."
        m 3eub "How many tries do you want?{nw}"
        $ _history_list.pop()
        menu:
            m "How many tries do you want?{fast}"

            "Easy (10 guesses)":
                $ tries_limit = 10

            "Normal (7 guesses)":
                $ tries_limit = 7

            "Hard (5 guesses)":
                $ tries_limit = 5

        python:
            target_num = random.randint(1, 100)
            current_guesses = 0

        m 1eua "Alright, I've got my number! Start guessing, [player]."

        label .hl_loop:
            $ guess = mas_input("Enter a number (1-100)", length=3, allow="0123456789")
            $ guess = store.mas_utils.tryparseint(guess, -1)

            if guess < 1 or guess > 100:
                m 1tua "Hey, stay within the range! 1 to 100, silly."
                jump .hl_loop

            $ current_guesses += 1

            if guess == target_num:
                $ persistent._cks_minigame_stats["hl_wins"] += 1
                m 1hub "You got it! It was [target_num]!"
                m 3eub "It only took you [current_guesses] tries. Not bad at all!"
                $ mas_gainAffection(modifier=0.5)
                jump .play_again

            elif current_guesses >= tries_limit:
                $ persistent._cks_minigame_stats["hl_losses"] += 1 # Added
                m 1eka "Aw, you're out of guesses! The number I was thinking of was [target_num]."
                $ mas_gainAffection(modifier=0.5)
                jump .play_again

            elif guess < target_num:
                $ tries_left = max(0, tries_limit - current_guesses)
                m 3eua "My number is higher than [guess]! You've got [tries_left] tries left."
                jump .hl_loop

            else:
                $ tries_left = max(0, tries_limit - current_guesses)
                m 3eua "My number is lower than [guess]! You've got [tries_left] tries left."
                jump .hl_loop

    # --- Guess the Number Logic ---
    label .guess_number_prep:
        m 1eua "One guess, one winner! What range should we use?{nw}"
        $ _history_list.pop()
        menu:
            m "One guess, one winner! What range should we use?{fast}"

            "1 to 5":
                $ g_range = 5

            "1 to 10":
                $ g_range = 10

            "1 to 20":
                $ g_range = 20

        python:
            target_num = random.randint(1, g_range)

        m 3eub "Alright, I've got a number between 1 and [g_range]. What's your guess?"

        $ guess = mas_input("Enter your guess", length=2, allow="0123456789")
        $ guess = store.mas_utils.tryparseint(guess, -1)

        if guess == target_num:
            $ persistent._cks_minigame_stats["gn_wins"] += 1
            m 1hub "Spot on! I was thinking of [target_num]. You're practically a mind reader!"
        else:
            $ persistent._cks_minigame_stats["gn_losses"] += 1
            m 1eka "Close, but no! I was thinking of [target_num]. Better luck next time!"

        $ mas_gainAffection(modifier=0.5)
        jump .play_again

    # --- Call It Logic ---
    label .call_it_prep:
        m 1eua "The classic coin flip. Call it while it's in the air!{nw}"
        $ _history_list.pop()
        menu:
            m "The classic coin flip. Call it while it's in the air!{fast}"

            "Heads":
                $ player_call = "Heads"

            "Tails":
                $ player_call = "Tails"

        python:
            coin_result = random.choice(["Heads", "Tails"])

        m 1eua "And the result is... [coin_result]!"

        if player_call == coin_result:
            $ persistent._cks_minigame_stats["ci_wins"] += 1
            m 1hub "You called it! Nice one, [player]!"
        else:
            $ persistent._cks_minigame_stats["ci_losses"] += 1
            m 1tua "Ahaha! Looks like luck was on my side this time."

        $ mas_gainAffection(modifier=0.5)
        jump .play_again

    label .play_again:
        m 3eub "Want to play something else, or are you finished?{nw}"
        $ _history_list.pop()
        menu:
            m "Want to play something else, or are you finished?{fast}"

            "Let's play another!":
                jump .game_menu

            "I'm finished":
                m 1hub "Thanks for playing with me! I had a lot of fun."

                return

    return
