from abc import ABC, abstractmethod
import matplotlib
import matplotlib.pyplot as plt


class WordPlotter(ABC):
    """Handles plotting functionality for word frequency data."""

    LABELS = ["Low Reviews", "Medium Reviews", "High Reviews"]

    def __init__(self) -> None:
        self.x_vals = [0, 1, 2]  # x axis labels for the three categories

    @abstractmethod
    def plot(
        self,
        word: str,
        word_data: dict[str, str],
        max_frequency: int,
        subplot: matplotlib.axes._axes.Axes,
    ) -> None:
        """
        This function takes the word_data dictionary, the word, and the max_frequency, and
        plots the frequencies for this word's use in low, medium, and high reviews when
        rating professors.

        Args:
            word_data (dict): Dictionary containing word frequency data for all words
            word (str): The word to plot
            max_frequency (int): Maximum frequency for y-axis scaling
            subplot (matplotlib.axes._axes.Axes): The subplot to plot on
        """

        # Hint: make sure to set the scale for the y-axis using max_frequency

        # Please replace the word_data argument's type to reflect the nested dictionary.
        # You may remove the @abstractmethod decorator if it makes sense for your implementation.

        pass


class WomenWordPlotter(WordPlotter):
    """Plotting functionality for word frequency data associated with women"""

    pass


class MenWordPlotter(WordPlotter):
    """Plotting functionality for word frequency data associated with men"""

    pass
