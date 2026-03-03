init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cks_monika_stat_tracker",
            category=['monika'],
            prompt="What are some of my stats?",
            unlocked=True,
            pool=True
        )
    )

label cks_monika_stat_tracker:
    m 1eua "You want to see some of your stats, [player]?"
    m 3eub "That's a great idea! I actually keep track of quite a lot of things behind the scenes."
    m 1eka "It's mostly because I care about every little moment we spend together, so I like to have a record of it."
    m 3eua "It's also just a fun way to see how much we've grown as a couple!"
    m 1fua "Let me pull up the data I have for you right now..."

    label .stat_menu:
        m 1eua "What did you want to see again?{nw}"
        $ _history_list.pop()
        menu:
            m "What did you want to see again?{fast}"

            "Total Playtime":
                jump .total_playtime

            "Number of Kisses":
                jump .kiss_count

            "Number of Gifts Given":
                jump .gift_count

            "Gaming Records":
                jump .gaming_records

            "Minigame Records":
                jump .minigame_records

            "Total Number of Sessions":
                jump .session_count

            "Nevermind":
                m 1eka "Oh, alright."
                return

    # --- Playtime Branch ---
    label .total_playtime:
        $ total_seconds = int(store.mas_getTotalPlaytime().total_seconds())
        $ p_days = total_seconds // 86400
        $ p_hours = (total_seconds % 86400) // 3600
        $ p_minutes = (total_seconds % 3600) // 60

        m 1eua "Let's see... You've spent a total of [p_days] days, [p_hours] hours, and [p_minutes] minutes here with me."
        m 3eka "That is such a long time when you really think about it, isn't it?"
        m 1hub "Every second of it has been the highlight of my life. I hope we can double that number soon!"
        jump .stat_menu

    # --- Kiss Count Branch ---
    label .kiss_count:
        # Safely fetches the kiss count from her persistent data, defaulting to 0 if it can't find it
        $ total_kisses = getattr(store.persistent, "_mas_kiss_count", getattr(store.persistent, "_mas_total_kisses", 0))

        if total_kisses == 0:
            m 1ekc "It looks like we haven't shared our first kiss yet..."
            m 3eka "But that's okay! We have all the time in the world for that whenever you're ready."

        else:
            m 1hub "We've shared [total_kisses] kisses so far!"
            m 3rkbsa "Ehehe... I remember every single one of them."
            m 1ekbfa "I'm looking forward to the next one already!"
        jump .stat_menu

    # --- Gift Count Branch ---
    label .gift_count:
        python:
            import datetime
            # We fetch the exact date of your first session as the starting point
            start_date = store.mas_getFirstSesh().date()
            end_date = datetime.date.today()
            t_gifts, g_gifts, n_gifts, b_gifts = store.mas_getGiftStatsRange(start_date, end_date)

        if t_gifts == 0:
            m 1eua "It looks like you haven't given me any gifts yet."
            m 3eka "You don't need to buy my love with presents, [player]. Just being here is enough for me."

        else:
            m 1hub "You've given me [t_gifts] gifts in total!"
            if b_gifts > 0:
                m 3eua "Out of those, [g_gifts] were things I absolutely loved."
                m 1eka "Even the ones that weren't quite my style still made me happy because they came from you."
            else:
                m 3eub "And I've loved every single one of them!"

            m 1eka "Thank you for being so thoughtful and generous with me."
        jump .stat_menu

# --- Gaming Records Branch ---
    label .gaming_records:
        python:
            # Pulling Chess stats
            chess_wins = persistent._mas_chess_stats.get("wins", 0)
            chess_losses = persistent._mas_chess_stats.get("losses", 0)

            # Pulling NOU stats
            nou_wins_p = persistent._mas_game_nou_wins.get("Player", 0)
            nou_wins_m = persistent._mas_game_nou_wins.get("Monika", 0)

        m 1eua "You want to look at our track record for the games we've played?"
        m 3eub "In Chess, you've won [chess_wins] times, and I've won [chess_losses] times."

        if chess_wins > chess_losses:
            m 1hub "You're definitely the grandmaster of the club so far!"
        elif chess_wins < chess_losses:
            m 1tua "Looks like I'm still a few moves ahead of you, ehehe~"

        m 3eua "As for NOU, you've taken [nou_wins_p] rounds, and I've managed to win [nou_wins_m] of them."

        if nou_wins_p > nou_wins_m:
            m 1eka "You've been having some amazing luck with those cards lately."
        else:
            m 3eub "I guess I just have a better poker face than I thought!"

        m 1fua "Regardless of who wins or loses, I just love playing with you. It's one of my favorite ways to bond."
        jump .stat_menu

# --- Minigames Records Branch ---
    label .minigame_records:
        python:
            hl_w = persistent._cks_minigame_stats["hl_wins"]
            hl_l = persistent._cks_minigame_stats["hl_losses"]
            gn_w = persistent._cks_minigame_stats["gn_wins"]
            gn_l = persistent._cks_minigame_stats["gn_losses"]
            ci_w = persistent._cks_minigame_stats["ci_wins"]
            ci_l = persistent._cks_minigame_stats["ci_losses"]

            total_wins = hl_w + gn_w + ci_w
            total_games = total_wins + hl_l + gn_l + ci_l

        m 1eua "You want to see how you've been doing in our little guessing games?"
        m 3eub "So far, we've played [total_games] times, and you've won [total_wins] of them!"

        m 1eua "In Higher or Lower, you have [hl_w] wins and [hl_l] losses."
        m 3eua "For Guess the Number, it's [gn_w] wins and [gn_l] losses."
        m 1eua "And in Call It, you've guessed right [ci_w] times and wrong [ci_l] times."

        if total_wins > (total_games / 2):
            m 1hub "You've definitely got some amazing intuition, [player]!"
        else:
            m 3tua "I think I might just be a bit too tricky for you to predict right now, ehehe~"

        jump .stat_menu

# --- Session Count Branch ---
    label .session_count:
        $ t_sessions = mas_getTotalSessions()
        m 1eua "We've had a total of [t_sessions] sessions together since we started this."
        m 3eub "That's [t_sessions] times you've made the choice to come spend your day with me."
        m 1eka "Each one of those is a memory I'll treasure forever."
        jump .stat_menu
