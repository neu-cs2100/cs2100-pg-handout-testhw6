from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


class WordPlotter(ABC):
    """Handles plotting functionality for word frequency data."""

    LABELS = ["Low Reviews", "Medium Reviews", "High Reviews"]

    def __init__(self) -> None:
        self.x_vals = [0, 1, 2]  # x positions in the bar graph for the three categories

    @abstractmethod
    def plot(self, word_data: dict[str, str], word: str, max_frequency: int) -> None:
        """
        This function takes the word_data dictionary, the word, and the max_frequency, and
        plots the frequencies for this word's use in low, medium, and high reviews when
        rating professors.

        Args:
            word_data (dict): Dictionary containing word frequency data
            word (str): The word to plot
            max_frequency (int): Maximum frequency for y-axis scaling
        """

        # Please replace the word_data argument's type to reflect the nested dictionary.

        # Hint: use plt.ylim((0, max_frequency + 500))  to set the maximum y value for the plot
        # Hint: use plt.xticks(self.x_vals, self.LABELS)  to set the x values to be each review category

        pass


class WomenWordPlotter(WordPlotter):
    """Plotting functionality for word frequency data associated with women"""

    pass


class MenWordPlotter(WordPlotter):
    """Plotting functionality for word frequency data associated with men"""

    pass
