import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Team Lotus data (7 sprints) ---
lotus_data = {
    "Sprint": [1, 2, 3, 4, 5, 6, 7],
    "Commitment": [29.5, 45.5, 32, 52, 52, 43.5, 43.5],
    "Completed": [34.5, 31.5, 30, 34, 47, 46, 63.5]
}
df_lotus = pd.DataFrame(lotus_data)

# --- Team Cactus data (7 sprints) ---
cactus_data = {
    "Sprint": [1, 2, 3, 4, 5, 6, 7],
    "Commitment": [70, 117, 67, 48, 43, 37, 80],
    "Completed": [38, 31, 14, 12, 31, 59, 1]
}
df_cactus = pd.DataFrame(cactus_data)

# --- Team Basil data (7 sprints) ---
basil_data = {
    "Sprint": [1, 2, 3, 4, 5, 6, 7],
    "Commitment": [45, 33, 50, 4, 0, 24, 24],
    "Completed": [14, 35, 79, 11, 26, 65.5, 65.5]
}
df_basil = pd.DataFrame(basil_data)

teams = {
    "Lotus": df_lotus,
    "Cactus": df_cactus,
    "Basil": df_basil
}

def plot_velocity_bars(df, team_name):
    """Plot side-by-side bars for Commitment and Completed along with the average and std deviation shading."""
    plt.figure(figsize=(8, 5))

    # Numeric x positions for the 7 sprints
    x = np.arange(len(df))
    bar_width = 0.4

    # Plot Commitment and Completed bars side-by-side
    plt.bar(x - bar_width/2, df['Commitment'], width=bar_width, label='Commitment')
    plt.bar(x + bar_width/2, df['Completed'], width=bar_width, label='Completed')

    # Calculate average and standard deviation for Completed across all 7 sprints
    avg_completed = df['Completed'].mean()
    std_completed = df['Completed'].std()

    # Draw horizontal line for the average Completed
    plt.axhline(y=avg_completed, color='green', linestyle='--',
                label=f'Avg Completed: {avg_completed:.2f}')

    # Shade the ±1 standard deviation region
    plt.fill_between(
        [x[0] - 0.5, x[-1] + 0.5],
        avg_completed - std_completed,
        avg_completed + std_completed,
        color='green', alpha=0.2,
        label=f'Std Dev: {std_completed:.2f}'
    )

    # Label the x-axis with sprint numbers and add labels/titles
    plt.xticks(x, df['Sprint'])
    plt.xlabel("Sprint")
    plt.ylabel("Story Points")
    plt.title(f"{team_name} Team Sprint Velocity (7 Sprints)")
    plt.legend()
    plt.grid(axis='y', linestyle=':')
    plt.tight_layout()
    plt.show()

# Generate plots for each team
for team_name, df in teams.items():
    plot_velocity_bars(df, team_name)
