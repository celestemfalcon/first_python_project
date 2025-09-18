# Instructions from RforDataScience / TidyTuesday

# Using Python
# Option 1: pydytuesday python library
## pip install pydytuesday

import pydytuesday
import pandas as pd
import matplotlib.pyplot as plt


# Download files from the week, which you can then read in locally
pydytuesday.get_date('2025-09-16')

# # Option 2: Read directly from GitHub and assign to an object
# all_recipes = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-09-16/all_recipes.csv')
# cuisines = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-09-16/cuisines.csv')

all_recipes = pd.read_csv('./all_recipes.csv')
cuisines = pd.read_csv('./cuisines.csv')

# View the data
print(all_recipes.head())
print(cuisines.head())

###############################################################################
# Start of my own code
print(all_recipes.columns)
print(cuisines.columns)


# Which authors are most successful: who is most prolific, who has the highest 
# average ratings or popularity, and do top authors specialize by cuisine, 
# ingredient, or recipe length?

# Get unique entries for each column
unique_entries_per_column = {}
for column in all_recipes.columns:
    unique_entries_per_column[column] = all_recipes[column].unique().tolist()

# Print the unique entries for each column
for column, unique_list in unique_entries_per_column.items():
    print(f"Unique entries in '{column}': {unique_list}")


# Create the bar plot
plt.bar(all_recipes['author'], all_recipes['author'].count())

# Add labels and title
plt.xlabel('Author')
plt.ylabel('Number of recipes')
plt.title('Number of recipes by each author')

# Display the plot
plt.show()


# Actually count number of entries for each author
    counts = all_recipes['author'].value_counts()
    print(counts)
    
    counts = pd.DataFrame(counts)
    counts = counts.reset_index()
    counts = counts.rename(columns={'index': 'author', 'count': 'number_of_recipes'})


plt.bar(counts['author'], counts['number_of_recipes'])
# Add labels and title
plt.xlabel('Author')
plt.ylabel('Number of recipes')
plt.title('Number of recipes by each author')

# Display the plot
plt.show()

  
# Plot again and restrict to top 10 authors by number of recipes contributed
# Also create separate objects for each element of plot (authors, counts)
counts_sorted = counts.sort_values(by='number_of_recipes', ascending=False)
top_10_values = counts_sorted.head(10)

print(top_10_values.head())

plt.bar(top_10_values['author'], top_10_values['number_of_recipes'])

plt.xlabel('Author')
plt.ylabel('Number of recipes')
plt.title('Top 10 authors by number of recipes created')
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.show()

## Not sure why the above is not working right (first was not showing only the 
## top 10, tried rerunning and now shows only top 10 but does not use correct 
## y values)... try a different way for now and get feedback

top_10_values.plot(kind='bar', x='author', legend=False)
plt.xlabel('Author')
plt.ylabel('Number of recipes')
plt.title('Top 10 authors by number of recipes created')
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.tight_layout() # Adjust layout to prevent labels from being cut off
plt.show()



# Is there a relationship between prep/cook time and average rating?
# Which recipe categories or cuisines tend to have the highest average ratings and review counts?
# Which recipes are the most "actionable" — high rating with low total time?

