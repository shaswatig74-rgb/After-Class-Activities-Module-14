import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Importing the dataset using pandas
df = pd.read_csv('IMDB Dataset.csv')

# 2. Printing the first 3 and last 3 rows of the dataset
print(df.head(3))
print(df.tail(3))

# 3. Checking the detailed information of the dataset
print(df.info())

# 4. Checking if any null values are present in the dataset
print(df.isnull().sum())

# 5. Creating a subset of the original dataset with data row number between 41 to 75
print(df.loc[42:74])

# 6. Checking detalis of the movie having highest number of votes
print(df.sort_values(by=['No_of_Votes'], ascending=False ))
print(df.loc[0])

# 7. Create boxplots for features IMDB_Rating and Runtime
sns.boxplot(x=df['IMDB_Rating'])
plt.show()
sns.boxplot(x=df['Runtime'])
plt.show()

# 8. Checking the realtionship between features IMDB_Rating and Runtime using Matplotlib
plt.scatter(df['IMDB_Rating'], df['Runtime'], color = 'red')
plt.title('Comparing IMDB_Rating and Runtime using Scatterplot')
plt.xlabel('IMDB_Rating')
plt.ylabel('Runtime')
plt.show()

# 9. Checking the distribution of features IMDB_Rating and Runtime
sns.histplot(x=df['IMDB_Rating'],color='lime', bins=10)
plt.title('Histogram of IMDB_Rating')
plt.xlabel('IMDB_Rating')
plt.ylabel('Count')
plt.show()
sns.histplot(x=df['Runtime'], color='blue', bins=15)
plt.title('Histogram of Runtime')
plt.xlabel('Runtime')
plt.ylabel('Count')
plt.show()

# 10. Creating a count plot of feature Rating to display no. of movies with a particular rating
sns.countplot(x=df['IMDB_Rating'], color='yellowgreen')
plt.title('Count PLot of IMDB_Rating')
plt.xlabel('IMDB-Rating')
plt.ylabel('No of movies')
plt.show()