"""
Sprint velocity visualization script.

This script loads team sprint data from a CSV file and generates
visualization charts showing sprint commitments and completions.
"""

import os
from typing import Dict

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def load_team_data(filepath: str = "teams_data.csv") -> Dict[str, pd.DataFrame]:
    """
    Load team data from CSV file and return a dictionary with team DataFrames.

    Args:
        filepath: Path to the CSV file containing team data

    Returns:
        Dictionary with team names as keys and DataFrames as values
    """
    try:
        # Check if file exists
        if not os.path.exists(filepath):
            print(f"Error: File '{filepath}' not found.")
            return {}

        # Read the CSV file
        all_data = pd.read_csv(filepath)

        # Print column names for debugging
        print(f"Columns found in CSV: {all_data.columns.tolist()}")

        # Check if required columns exist
        required_columns = ["Team", "Sprint", "Commitment", "Completed"]
        missing_columns = [
            col for col in required_columns if col not in all_data.columns
        ]

        if missing_columns:
            print(
                f"Error: The following required columns are missing: {missing_columns}"
            )
            return {}

        # Create a dictionary to store team-specific DataFrames
        teams: Dict[str, pd.DataFrame] = {}

        # Get unique team names
        team_names = all_data["Team"].unique()

        # Split the data by team
        for team_name in team_names:
            team_df = all_data[all_data["Team"] == team_name].copy()
            # Remove the Team column as it's no longer needed in the individual DataFrame
            team_df = team_df.drop("Team", axis=1)
            # Reset the index to make it clean
            team_df = team_df.reset_index(drop=True)
            teams[team_name] = team_df

        return teams
    except Exception as e:
        print(f"Error loading data: {e}")
        return {}


def plot_velocity_bars(df: pd.DataFrame, team_name: str) -> None:
    """
    Plot side-by-side bars for Commitment and Completed with average and std deviation.

    Args:
        df: DataFrame containing Sprint, Commitment and Completed columns
        team_name: Name of the team for chart title
    """
    plt.figure(figsize=(8, 5))

    # Numeric x positions for the sprints
    x = np.arange(len(df))
    bar_width = 0.4

    # Plot Commitment and Completed bars side-by-side
    plt.bar(x - bar_width / 2, df["Commitment"], width=bar_width, label="Commitment")
    plt.bar(x + bar_width / 2, df["Completed"], width=bar_width, label="Completed")

    # Calculate average and standard deviation for Completed across all sprints
    avg_completed = df["Completed"].mean()
    std_completed = df["Completed"].std()

    # Draw horizontal line for the average Completed
    plt.axhline(
        y=avg_completed,
        color="green",
        linestyle="--",
        label=f"Avg Completed: {avg_completed:.2f}",
    )

    # Shade the ±1 standard deviation region
    plt.fill_between(
        [x[0] - 0.5, x[-1] + 0.5],
        avg_completed - std_completed,
        avg_completed + std_completed,
        color="green",
        alpha=0.2,
        label=f"Std Dev: {std_completed:.2f}",
    )

    # Label the x-axis with sprint numbers and add labels/titles
    plt.xticks(x, df["Sprint"])
    plt.xlabel("Sprint")
    plt.ylabel("Story Points")
    plt.title(f"{team_name} Team Sprint Velocity ({len(df)} Sprints)")
    plt.legend()
    plt.grid(axis="y", linestyle=":")
    plt.tight_layout()
    plt.show()


def main() -> None:
    """Load data and generate plots for each team."""
    # Load data from CSV
    teams = load_team_data()

    if not teams:
        print("No team data was loaded. Exiting.")
        return

    # Generate plots for each team
    for team_name, df in teams.items():
        plot_velocity_bars(df, team_name)


if __name__ == "__main__":
    main()
