"""
sitka_high_low_cjc.py

Christopher Craig
CSD-325 - Module 4

Description:
    This program reads daily high and low temperatures for Sitka, AK
    (sitka_weather_2021_simple.csv) and plots them with Matplotlib.
    The user is shown a menu and can choose to view a graph of the
    HIGH temperatures, a graph of the LOW temperatures, or exit the
    program. The menu keeps looping until the user chooses to exit.

Changes made from the original sitka_highs.py (Module 3 version):
    1. Wrapped the CSV-reading/plotting logic for highs in a function,
       get_highs_lows(), that returns both the list of dates and the
       list of highs AND the list of lows (originally only highs were
       collected).
    2. Added a new function, plot_lows(), that plots the low
       temperatures in blue, mirroring the structure of the existing
       plot_highs() function which plots the high temperatures in red.
    3. Added a text-based menu (show_menu()) that lets the user choose
       "highs", "lows", or "exit".
    4. Wrapped the menu in a while True loop so the program keeps
       running and re-displaying the menu until the user selects
       "exit".
    5. Imported sys and called sys.exit() when the user chooses to
       exit, after first printing a friendly exit message.
    6. Added input validation so an unrecognized menu choice reprints
       the menu instead of crashing the program.
"""

import csv
import sys
from datetime import datetime

import matplotlib.pyplot as plt

FILENAME = "sitka_weather_2021_simple.csv"


def get_highs_lows(filename):
    """Read the weather file and return (dates, highs, lows)."""
    dates, highs, lows = [], [], []

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = float(row[1])
            low = float(row[2])

            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows


def plot_highs(dates, highs):
    """Plot the high temperatures in red."""
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, color="red", alpha=0.7)

    ax.set_title("Daily High Temperatures - 2021", fontsize=20)
    ax.set_xlabel("", fontsize=14)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=14)
    ax.tick_params(labelsize=12)

    plt.show()


def plot_lows(dates, lows):
    """Plot the low temperatures in blue."""
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(dates, lows, color="blue", alpha=0.7)

    ax.set_title("Daily Low Temperatures - 2021", fontsize=20)
    ax.set_xlabel("", fontsize=14)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=14)
    ax.tick_params(labelsize=12)

    plt.show()


def show_menu():
    """Print the menu and return the user's raw choice."""
    print("\nSitka Weather Menu")
    print("-------------------")
    print("  highs - View a graph of the daily high temperatures")
    print("  lows  - View a graph of the daily low temperatures")
    print("  exit  - Quit the program")
    return input("What would you like to do? ").strip().lower()


def main():
    dates, highs, lows = get_highs_lows(FILENAME)

    while True:
        choice = show_menu()

        if choice == "highs":
            plot_highs(dates, highs)
        elif choice == "lows":
            plot_lows(dates, lows)
        elif choice == "exit":
            print("Thanks for checking the Sitka weather. Goodbye!")
            sys.exit()
        else:
            print(f"'{choice}' is not a valid option. Please try again.")


if __name__ == "__main__":
    main()
