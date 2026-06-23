from nba_api.stats.endpoints import leaguedashteamstats
import pandas as pd
import os

# Seasons to analyze
seasons = [
    "2021-22",
    "2022-23",
    "2023-24",
    "2024-25"
]

all_data = []

for season in seasons:

    print(f"Downloading {season}...")

    stats = leaguedashteamstats.LeagueDashTeamStats(
        season=season
    )

    df = stats.get_data_frames()[0]

    df["SEASON"] = season

    all_data.append(df)

# Combine seasons
final_df = pd.concat(all_data, ignore_index=True)

# Create data folder if needed
os.makedirs("data", exist_ok=True)

# Save CSV
final_df.to_csv(
    "data/nba_team_stats.csv",
    index=False
)

print("\nDone!")
print(final_df.shape)
print("\nFile saved:")
print("data/nba_team_stats.csv")