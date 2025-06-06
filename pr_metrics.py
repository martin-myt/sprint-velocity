import re
from datetime import timedelta

import matplotlib.pyplot as plt
import pandas as pd


# Helper function to convert time strings to total seconds
def time_to_seconds(time_str) -> float:
    if isinstance(time_str, str):
        # Handle 'x days, HH:MM:SS' and 'HH:MM:SS'
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


# Data setup
data = [
    # Microservices
    [
        "Microservices",
        "April",
        "Time to first response",
        "1 day, 10:53:41",
        "1:24:23",
        "2 days, 15:57:38",
    ],
    [
        "Microservices",
        "April",
        "Time to close",
        "1 day, 22:54:54",
        "3:29:15",
        "6 days, 3:53:36",
    ],
    [
        "Microservices",
        "May",
        "Time to first response",
        "1 day, 3:10:47",
        "1:00:44",
        "3 days, 1:31:05",
    ],
    [
        "Microservices",
        "May",
        "Time to close",
        "1 day, 22:25:42",
        "2:35:40",
        "6 days, 17:11:22",
    ],
    # Frontend
    ["Frontend", "April", "Time to first response", "8:10:25", "0:31:33", "22:07:20"],
    ["Frontend", "April", "Time to close", "11:43:58", "2:00:18", "1 day, 0:05:35"],
    [
        "Frontend",
        "May",
        "Time to first response",
        "16:32:54",
        "2:15:27",
        "2 days, 20:03:07",
    ],
    [
        "Frontend",
        "May",
        "Time to close",
        "1 day, 3:40:49",
        "9:20:48",
        "3 days, 5:28:12",
    ],
    # Enterprise Search
    [
        "Enterprise Search",
        "May",
        "Time to first response",
        "12:07:31",
        "3:19:56",
        "1 day, 0:31:37",
    ],
    [
        "Enterprise Search",
        "May",
        "Time to close",
        "1 day, 4:14:33",
        "18:57:52",
        "3 days, 11:32:12",
    ],
]

df = pd.DataFrame(
    data, columns=["Repo", "Month", "Metric", "Average", "Median", "90th Percentile"]
)

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
