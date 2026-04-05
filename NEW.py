import pandas as pd

df = pd.read_csv("C:/Users/yoeshwar/OneDrive/Pictures/Desktop/internships/Sample - Superstore.csv", encoding='latin1')

print(df.head())
print("shape",df.shape)
print("information",df.info())
print("null values sum",df.isnull().sum())
duplicates = df.duplicated().sum()
df = df.drop_duplicates()
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
print(df.describe())
q1 = df['Sales'].quantile(0.25)
q2 = df['Sales'].quantile(0.75)
iqr = q2 - q1
outliers = df[(df['Sales'] < q1 - 1.5 * iqr) | (df['Sales'] > q2 + 1.5 * iqr)]
print("\nNumber of Sales Outliers:", len(outliers))
df.to_csv("cleaned_superstore.csv", index=False)
print("\nCleaned dataset saved successfully!")