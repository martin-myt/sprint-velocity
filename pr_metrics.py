import re
from datetime import timedelta

import matplotlib.pyplot as plt
import pandas as pd


def time_to_seconds(time_str) -> float:
    if isinstance(time_str, str):
        day_match = re.match(r"(\d+) day[s]?, (.+)", time_str)
        if day_match:
            days = int(day_match.group(1))
            hms = day_match.group(2)
        else:
            days = 0
            hms = time_str
        h, m, s = map(int, hms.split(":"))
        return timedelta(days=days, hours=h, minutes=m, seconds=s).total_seconds()
    return 0


# Load data from CSV
df = pd.read_csv("pr_metrics_data.csv")

# Convert time columns to seconds
df["Average_sec"] = df["Average"].apply(time_to_seconds)
df["Median_sec"] = df["Median"].apply(time_to_seconds)
df["90th Percentile_sec"] = df["90th Percentile"].apply(time_to_seconds)

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))
for repo in df["Repo"].unique():
    for metric in ["Time to first response", "Time to close"]:
        subset = df[(df["Repo"] == repo) & (df["Metric"] == metric)]
        ax.plot(
            subset["Month"],
            subset["Average_sec"] / 3600,
            marker="o",
            label=f"{repo} - {metric} (Avg)",
        )

ax.set_title("Average Time Metrics per Repo (in Hours)")
ax.set_ylabel("Time (Hours)")
ax.legend()
ax.grid(True)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
