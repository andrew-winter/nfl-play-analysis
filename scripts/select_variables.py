# %%
def select_variables():
    """Focus on tens of variables instead of sifting through hundreds.

    Specify vars below. Output is a list of strings.
    """
    pbp_columns = [
        "time", "play_type", "quarter_seconds_remaining", "desc",
        "yardline_100", "ydstogo", "yards_gained", "yrdln",
        "side_of_field", "down", "drive", "qtr", "game_date",
        "week", "season_type", "season", "game_id", "play_id",

        "passer", "complete_pass", "pass_attempt", "passing_yards",
        "pass", "incomplete_pass", "air_yards", "yards_after_catch",
        "qb_dropback", "qb_kneel", "qb_spike", "qb_scramble", "pass_location",
        "receiver", "receiving_yards",
        "interception", "sack",

        "rusher", "rush_attempt",  "rushing_yards", "rush",

        "timeout", "timeout_team",
        "penalty", "penalty_team", "penalty_yards", "first_down_penalty",
        "posteam", "defteam", "home_team", "away_team",
        "home_timeouts_remaining", "away_timeouts_remaining",
        "wp", "def_wp",

        "kicker_player_name", "kick_distance",
        "kickoff_attempt", "kickoff_returner_player_name",

        "posteam_score", "defteam_score",
        "posteam_score_post", "defteam_score_post",
        "sp", "touchdown", "td_team",
        "pass_touchdown", "rush_touchdown", "td_player_name",
        "field_goal_attempt", "field_goal_result",
        "extra_point_attempt", "extra_point_result",
        "two_point_attempt", "two_point_conv_result"]

    return pbp_columns

# %%
#select_variables()
