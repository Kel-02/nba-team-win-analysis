from nba_api.stats.endpoints import leaguedashteamstats
import pandas as pd
import os

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
        season=season,
        measure_type_detailed_defense="Advanced"
    )

    df = stats.get_data_frames()[0]

    df["SEASON"] = season

    all_data.append(df)

advanced_df = pd.concat(
    all_data,
    ignore_index=True
)

os.makedirs("data", exist_ok=True)

advanced_df.to_csv(
    "data/nba_team_advanced_stats.csv",
    index=False
)

print(advanced_df.columns.tolist())
print(advanced_df.shape)