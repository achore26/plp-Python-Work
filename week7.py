import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

sns.set(style="whitegrid")


try:
    iris_data = load_iris()
    df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df['species'] = iris_data.target
    df['species'] = df['species'].apply(lambda x: iris_data.target_names[x])
    
    print("First five rows of the dataset:")
    print(df.head())

    print("\nData types and missing values:")
    print(df.info())

    print("\nMissing values check:")
    print(df.isnull().sum())

except FileNotFoundError:
    print("Dataset file not found.")
except Exception as e:
    print("An error occurred:", e)


print("\nStatistical Summary:")
print(df.describe())

print("\nMean of features grouped by species:")
grouped = df.groupby('species').mean()
print(grouped)

plt.figure(figsize=(10, 5))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.title('Simulated Time-Series of Sepal Length')
plt.xlabel('Index (simulated time)')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal length (cm)', data=df, ci=None)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(df['sepal width (cm)'], kde=True, bins=20)
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

print("\nObservations:")
print("- Setosa generally has shorter petals and sepals compared to Versicolor and Virginica.")
print("- Virginica species tends to have the longest petal lengths.")
print("- There's a visible positive correlation between sepal length and petal length.")
