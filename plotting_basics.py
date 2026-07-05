
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 100)

# Line plot
plt.figure(figsize=(10, 4))
plt.plot(x, np.sin(x), label='sin(x)', color='blue')
plt.plot(x, np.cos(x), label='cos(x)', color='red', linestyle='--')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('line_plot.png', dpi=150)
plt.close()

# prediction: KE shows high variance at all mass levels because KE = 0.5*m*v^2
# velocity is squared so it dominates — mass alone does not determine KE
# color (velocity) will be the stronger visual predictor of KE than mass

# Scatter plot
np.random.seed(42)
masses     = np.random.uniform(0.1, 10, 100)
velocities = np.random.uniform(-50, 50, 100)
ke         = 0.5 * masses * velocities**2

plt.figure(figsize=(8, 6))
plt.scatter(masses, ke, c=velocities, cmap='coolwarm', alpha=0.7)
plt.colorbar(label='velocity (m/s)')
plt.title('Kinetic Energy vs Mass')
plt.xlabel('Mass (kg)')
plt.ylabel('KE (J)')
plt.savefig('scatter_plot.png', dpi=150)
plt.close()

# Bar plot — Titanic survival by class
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic = pd.read_csv(url)

survival = titanic.groupby('Pclass')['Survived'].mean()

plt.figure(figsize=(8, 5))
plt.bar(survival.index, survival.values, color=['gold', 'silver', 'brown'])
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.xticks([1, 2, 3], ['First', 'Second', 'Third'])
plt.savefig('bar_plot.png', dpi=150)
plt.close()

# Histogram — Age distribution
plt.figure(figsize=(8, 5))
plt.hist(titanic['Age'].dropna(), bins=30, color='steelblue', edgecolor='black')
plt.title('Age Distribution of Titanic Passengers')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig('histogram.png', dpi=150)
plt.close()

# prediction: what shape do you expect the age distribution to be?  right-skewed
# prediction: which age group had the most passengers? 20 -23

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Top left — survival by class
survival_class = titanic.groupby('Pclass')['Survived'].mean()
axes[0, 0].bar(survival_class.index, survival_class.values)
axes[0, 0].set_title('Survival by Class')

# Top right — age histogram
axes[0, 1].hist(titanic['Age'].dropna(), bins=30, color='steelblue')
axes[0, 1].set_title('Age Distribution')

# Bottom left — fare distribution
axes[1, 0].hist(titanic['Fare'], bins=40, color='green')
axes[1, 0].set_title('Fare Distribution')

# Bottom right — survival by sex
survival_sex = titanic.groupby('Sex')['Survived'].mean()
axes[1, 1].bar(survival_sex.index, survival_sex.values, color=['pink', 'blue'])
axes[1, 1].set_title('Survival by Sex')

plt.tight_layout()
plt.savefig('subplots.png', dpi=150)
plt.close()

# prediction: what does tight_layout() do? avoids overlap

import seaborn as sns

# Heatmap — correlation matrix
plt.figure(figsize=(8, 6))
numeric_cols = titanic[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']].dropna()
corr = numeric_cols.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Titanic Feature Correlation Heatmap')
plt.savefig('heatmap.png', dpi=150)
plt.close()

# Boxplot — age distribution by class
plt.figure(figsize=(8, 6))
sns.boxplot(data=titanic, x='Pclass', y='Age')
plt.title('Age Distribution by Passenger Class')
plt.savefig('boxplot.png', dpi=150)
plt.close()

# Violinplot
plt.figure(figsize=(8, 6))
sns.violinplot(data=titanic, x='Sex', y='Age', hue='Survived')
plt.title('Age by Sex and Survival')
plt.savefig('violinplot.png', dpi=150)
plt.close()

# prediction: which feature correlates most negatively with Survived in the heatmap?  Pclass
# prediction: which class has the oldest median age? 1st class

# Pairplot — visualize all pairwise relationships
subset = titanic[['Survived', 'Pclass', 'Age', 'Fare']].dropna()
subset['Survived'] = subset['Survived'].astype(str)

sns.pairplot(subset, hue='Survived', diag_kind='hist')
plt.savefig('pairplot.png', dpi=150)
plt.close()

# prediction: which pair of features shows the clearest separation  Fare vs Pclass
# between survivors (1) and non-survivors (0)?
