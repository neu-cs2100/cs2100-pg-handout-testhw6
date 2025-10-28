import sys
from typing import Optional

sys.path.append(".")

from src.data_loader import DataLoader
from src.word_plotter import WomenWordPlotter, MenWordPlotter


def main() -> None:
    """Main function to run the word analysis program."""

    if len(sys.argv) < 2:
        print("Usage: python main.py <word>")
        sys.exit(1)

    word = sys.argv[1]

    if len(sys.argv) > 2:
        data_filename = sys.argv[2]
    else:
        data_filename = "word_data.json"

    # YOUR CODE HERE:
    # 1. Load the data from the file whose name is data_filename
    # 2. Extract gender data for the word from the loaded dictionary
    # 3. Calculate maximum frequency for consistent y-axis scaling across both plots
    # 4. Create and display both plots


if __name__ == "__main__":
    main()
