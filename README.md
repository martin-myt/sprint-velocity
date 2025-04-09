# Sprint Velocity Charts

This project visualizes sprint velocity data for agile teams, showing both commitment and completed story points across sprints, along with average velocity and standard deviation.

## Features

- Visualizes sprint velocity data with side-by-side bar charts
- Shows average completed story points and standard deviation
- Supports multiple teams
- Reads data from a CSV file for easy updates

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Data Format

The project reads team data from a CSV file (`teams_data.csv`) with the following format:

```
Team,Sprint,Commitment,Completed
TeamName,SprintNumber,CommitmentPoints,CompletedPoints
```

Example:
```
Team,Sprint,Commitment,Completed
Lotus,1,29.5,34.5
Lotus,2,45.5,31.5
```

## Usage

1. Make sure your `teams_data.csv` file is properly formatted. **Important:** The file should not contain any comment lines at the beginning.

2. Run the script:

```bash
python sprint_velocity.py
```

3. The script will generate velocity charts for each team in the dataset. Close one chart to view the next one.

## Customizing

- To add new teams or sprints, simply update the CSV file with additional data
- Modify the `plot_velocity_bars` function in the script to change visualization parameters

## Requirements

- Python 3.x
- pandas >= 1.3.0
- matplotlib >= 3.4.0
- numpy >= 1.20.0