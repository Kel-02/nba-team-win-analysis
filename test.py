from nba_api.stats.endpoints import leaguedashteamstats

print("Connecting to NBA API...")

stats = leaguedashteamstats.LeagueDashTeamStats(
    season="2024-25"
)

df = stats.get_data_frames()[0]

print(df[["TEAM_NAME", "W", "L"]].head())