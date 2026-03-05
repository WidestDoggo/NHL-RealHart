import pandas as pd

df = pd.read_csv("data/raw/skaters.csv")

df = df[df["situation"] == "all"]

columns_to_keep = [
    "playerId", "name", "team", "position", "season",
    "games_played", "icetime",
    "I_F_goals", "I_F_primaryAssists", "I_F_secondaryAssists", "I_F_points", "I_F_shotsOnGoal",
    "I_F_xGoals", "gameScore", "onIce_xGoalsPercentage", "onIce_corsiPercentage",
    "I_F_hits", "I_F_takeaways", "I_F_giveaways", "OnIce_A_xGoals", "shotsBlockedByPlayer"
]

df = df[columns_to_keep]
print(df)
df = df.fillna(0)

df.to_csv("data/processed/skaters_clean.csv", index=False)

print(df.head())
print(df.shape)