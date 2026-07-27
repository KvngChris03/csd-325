"""
Christopher Craig
CSD-325, Module 7

city_functions.py - defines a function that formats a city and
country into a single readable string, then calls it a few times
to demonstrate it working.
"""


def city_country(city, country, language=None, population=None):
    """Return 'City, Country', optionally followed by a population
    figure and/or a language."""
    formatted = f"{city.title()}, {country.title()}"
    if population:
        formatted += f" - population {population}"
    if language:
        formatted += f", {language.title()}"
    return formatted


if __name__ == "__main__":
    print(city_country("santiago", "chile"))
    print(city_country("tokyo", "japan", population=37400000))
    print(city_country("paris", "france", language="french", population=2161000))
