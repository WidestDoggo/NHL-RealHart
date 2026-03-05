import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("data/processed/skaters_clean.csv")

scaler = MinMaxScaler()

stats_to_scale = [
    "I_F_goals", "I_F_primaryAssists", "I_F_secondaryAssists", "I_F_points",
    "I_F_shotsOnGoal", "I_F_xGoals", "gameScore", "onIce_xGoalsPercentage",
    "onIce_corsiPercentage", "I_F_hits", "I_F_takeaways", "I_F_giveaways", "OnIce_A_xGoals", "games_played", "shotsBlockedByPlayer"
]

df_scaled = df.copy()
df_scaled[stats_to_scale] = scaler.fit_transform(df[stats_to_scale])

weights = {
    "I_F_points":               0.20,
    "I_F_goals":                0.15,
    "I_F_primaryAssists":       0.10,
    "I_F_xGoals":               0.10,
    "gameScore":                0.15,
    "onIce_xGoalsPercentage":   0.09,
    "onIce_corsiPercentage":    0.07,
    "I_F_hits":                 0.04,
    "I_F_takeaways":            0.05,
    "I_F_giveaways":           -0.03,
    "I_F_shotsOnGoal":          0.02,
    "I_F_secondaryAssists":     0.02,
    "OnIce_A_xGoals":          -0.05,
    "shotsBlockedByPlayer":     0.04,
}

df["FAKTOR"] = sum(df_scaled[stat] * weight for stat, weight in weights.items())


df["FAKTOR"] = df["FAKTOR"].round(4)
df = df.sort_values("FAKTOR", ascending=False)

df.to_csv("data/processed/faktor_scores.csv", index=False)

# print(df[["name", "team", "position", "FAKTOR"]].head)

# tor = df[df["team"] == "TOR"]
# edm = df[df["team"] == "EDM"]
# col = df[df["team"] == "COL"]

# print("--- TORONTO ---")
# print(tor[["name", "team", "position", "FAKTOR"]].head(10))

# print("--- EDMONTON ---")
# print(edm[["name", "team", "position", "FAKTOR"]].head(10))

# print("--- COLORADO ---")
# print(col[["name", "team", "position", "FAKTOR"]].head(10))

