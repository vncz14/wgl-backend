from .elo import MODEL


def create_match(teams, game):
    from .models import Match, Team, TeamPlayer, Elo

    # start a match
    match = Match.objects.create(
        game=game,
    )

    # add teams to match
    for team in teams:
        t = Team.objects.create(match=match)
        for player in team:
            # add players to teams
            tp = TeamPlayer.objects.create(match=match, team=t, player=player)
            t.players.add(tp)

            # make players not queue anymore
            player.in_queue = False
            player.save()

            # find the player's elo or create a new one if it doesn't exist
            elo = Elo.objects.filter(player=player, game=game).first()
            if not elo:
                elo = Elo.objects.create(player=player, game=game)

            tp.mu_before = elo.mu
            tp.sigma_before = elo.sigma
            tp.save()

        match.teams.add(t)

    return match


def ms_to_time(ms):
    seconds = ms / 1000
    minutes = seconds // 60
    hours = minutes // 60

    seconds = seconds % 60
    minutes = int(minutes % 60)
    hours = int(hours)

    if hours != 0:
        return f"{hours}:{minutes:02}:{seconds:06.3f}"
    elif minutes != 0:
        return f"{minutes}:{seconds:06.3f}"
    else:
        return f"{seconds:.3f}"


def format_score(score, game):
    if score is None:
        return None

    if game.speedrun:  # if the game is a speedrun category
        return ms_to_time(score)
    else:  # it is a score category
        if score > 0:
            return f"+{score}"
        elif score == 0:
            return "±0"
        else:
            return f"{score}"  # e.g. -18
