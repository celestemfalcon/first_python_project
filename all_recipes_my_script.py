# Instructions from RforDataScience / TidyTuesday

# Using Python
# Option 1: pydytuesday python library
## pip install pydytuesday

import pydytuesday
import pandas


# Download files from the week, which you can then read in locally
pydytuesday.get_date('2025-09-16')

# # Option 2: Read directly from GitHub and assign to an object
# all_recipes = pandas.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-09-16/all_recipes.csv')
# cuisines = pandas.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-09-16/cuisines.csv')

all_recipes = pandas.read_csv('./all_recipes.csv')
cuisines = pandas.read_csv('./cuisines.csv')

# View the data
print(all_recipes.head())
print(cuisines.head())

