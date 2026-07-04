import pandas as pd
import numpy as np

# Series
s = pd.Series([10, 20, 30, 40, 50])
s_named = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# prediction: what does s[2] return? 30
# prediction: what does s_named['b'] return? 20
print(s[2])
print(s_named['b'])

# DataFrame from dict
df = pd.DataFrame({
    'mass':     [1.2, 3.4, 2.1, 5.6, 4.3],
    'velocity': [10, -20, 15, -5, 30],
    'charge':   [-1, 1, -1, 1, -1]
})

# Print these — predict before running
print(df.shape)       # prediction: (5, 3)
print(df.dtypes)      # prediction: mass          float64
                      #           velocity      int64
                      #           charge        int64
print(df.head(3))     # prediction: first 3 rows 0 1.2 10 -1
                      #                         1 3.4 -20 1
                      #                          2 2.1 15 -1
print(df.describe())  # prediction: what statistics appear?
                      # prediction: count, mean, std, min, 25%, 50%, 75%, max

# loc = label-based indexing
# iloc = integer position-based indexing

print(df.loc[0])           # prediction: mass        1.2
                           #             velocity   10
                           #             charge     -1  
print(df.iloc[0])          # prediction: mass        1.2
                           #             velocity   10
                           #             charge     -1
print(df.loc[0, 'mass'])   # prediction: 1.2
print(df.iloc[0, 0])       # prediction: 1.2

# Boolean filtering
heavy = df[df['mass'] > 3]
positive = df[df['charge'] == 1]
combined = df[(df['mass'] > 2) & (df['velocity'] > 0)]

# prediction: how many rows in each?
print(heavy.shape)     # prediction: (2, 3)
print(positive.shape)  # prediction: (2, 3)
print(combined.shape)  # prediction: (2, 3)

# Add computed columns
df['ke']       = 0.5 * df['mass'] * df['velocity']**2
df['momentum'] = df['mass'] * df['velocity']

# Apply a custom function to a column
df['speed'] = df['velocity'].apply(abs)

# prediction: what does df.columns return now?
print(df.columns)    # prediction: Index(['mass', 'velocity', 'charge', 'ke', 'momentum', 'speed'], dtype='object')
print(df.head())

# Read from URL directly — no download needed
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic = pd.read_csv(url)

print(titanic.shape)           # prediction: rows and columns 891 12
print(titanic.columns.tolist())
print(titanic.isnull().sum())  # missing values per column # Age: 177 missing, Cabin: 687 missing, Embarked: 2 missing
print(titanic.describe())

# Drop rows with missing Age
titanic_clean = titanic.dropna(subset=['Age'])
print(titanic_clean.shape)     # prediction: fewer rows than before 714 12

# Group Titanic data by Pclass and compute survival stats
survival_by_class = titanic.groupby('Pclass')['Survived'].agg(['mean', 'sum', 'count'])
print(survival_by_class)

# Group by Sex
survival_by_sex = titanic.groupby('Sex')['Survived'].mean()
print(survival_by_sex)

# Group by both
survival_by_class_sex = titanic.groupby(['Pclass', 'Sex'])['Survived'].mean()
print(survival_by_class_sex)