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

########## Who is most prolific?
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

##########  Who has the highest average ratings? or popularity?
mean_avg_ratings = pd.DataFrame(all_recipes.groupby('author')['avg_rating'].mean())
mean_avg_ratings_sorted = mean_avg_ratings.sort_values(by='avg_rating', ascending=False)
top_avg_ratings = mean_avg_ratings_sorted.head(10)
top_avg_ratings = top_avg_ratings.reset_index()
top_avg_ratings = top_avg_ratings.rename(columns={'index': 'author', 'count': 'avg_rating'})

top_avg_ratings.plot(kind='bar', x='author', legend=False)
plt.xlabel('Author')
plt.ylabel('Average rating')
plt.title('Top 10 authors by average rating')
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.tight_layout() # Adjust layout to prevent labels from being cut offplt.show()
plt.show()

sum_total_ratings = pd.DataFrame(all_recipes.groupby('author')['total_ratings'].sum())
sum_total_ratings_sorted = sum_total_ratings.sort_values(by='total_ratings', ascending=False)
top_total_ratings = sum_total_ratings_sorted.head(10)
top_total_ratings = top_total_ratings.reset_index()
top_total_ratings = top_total_ratings.rename(columns={'index': 'author', 'count': 'total_ratings'})
    
top_total_ratings.plot(kind='bar', x='author', legend=False)
plt.xlabel('Author')
plt.ylabel('Average rating')
plt.title('Top 10 authors by total rating values')
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.tight_layout() # Adjust layout to prevent labels from being cut offplt.show()
plt.show()

########## Do top authors specialize by cuisine, ingredient, or recipe length?
authors_to_include = top_total_ratings['author']
cuisines_top_authors = cuisines[cuisines['author'].isin(authors_to_include)]
cuisines_top_authors_count = cuisines_top_authors.groupby(['author', 'country']).size()


### below is a work in progress ###
plt.bar(cuisines_top_authors_count['country'], segment1_data, label='Segment 1')
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.show()
    
    
import numpy as np
categories = ['Category A', 'Category B', 'Category C']
segment1_data = [10, 15, 7]
segment2_data = [5, 8, 12]
segment3_data = [3, 6, 9]
    
plt.figure(figsize=(8, 6)) # Optional: set figure size
plt.bar(categories, segment1_data, label='Segment 1')
plt.bar(categories, segment2_data, bottom=segment1_data, label='Segment 2')
plt.bar(categories, segment3_data, bottom=np.array(segment1_data) + np.array(segment2_data), label='Segment 3')
    
plt.ylabel('Values')
plt.title('Stacked Bar Chart Example')
plt.legend()
plt.show()
        
## or use pandas plotting
df.plot(x='Category', kind='bar', stacked=True, title='Stacked Bar Chart from DataFrame')
plt.ylabel('Values')
plt.show()
    


# Is there a relationship between prep/cook time and average rating?
# Which recipe categories or cuisines tend to have the highest average ratings and review counts?
# Which recipes are the most "actionable" — high rating with low total time?


