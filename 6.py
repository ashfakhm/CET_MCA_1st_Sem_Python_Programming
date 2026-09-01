"""
Sports Tournament Points Table Generator

This program processes a list of match scores:
1. Compare the team's score with the opponent's score.
2. Count wins, draws, and losses.
3. Calculate total points.
4. Store the results in a summary dictionary.
5. Print the formatted summary.
"""

# Match results
match_scores = ["3-1", "0-0", "1-2", "2-2", "4-0"]

# Initialize statistics
wins = 0
draws = 0
losses = 0
total_points = 0

# Process each match
for match in match_scores:
    team_score, opponent_score = map(int, match.split("-"))

    if team_score > opponent_score:
        wins += 1
        total_points += 3

    elif team_score == opponent_score:
        draws += 1
        total_points += 1

    else:
        losses += 1

# Create the summary dictionary
summary = {"Wins": wins, "Draws": draws, "Losses": losses, "Total Points": total_points}

# Print the final summary
print(f"Match results: {match_scores}")
print(f"Summary: {summary}")
