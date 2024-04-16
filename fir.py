import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load the dataset
df = pd.read_csv('FIR_Details_Data.csv')  # Update this path to your CSV file

# Prepare the data
df['FIR_Date'] = pd.to_datetime(df['FIR_Date'], errors='coerce')  # Parse FIR dates

# Visualizations

# FIR Counts by District and Unit
plt.figure(figsize=(14, 7))
sns.countplot(y='District_Name', data=df, order = df['District_Name'].value_counts().index, color = '#993399')
plt.title('FIR Counts by District')
plt.xlabel('Count')
plt.ylabel('District')
plt.tight_layout()
plt.show()

# FIR Trends Over Time by Year and Month
df['Year_Month'] = df['Year'].astype(str) + '-' + df['Month'].astype(str).str.zfill(2)
df['Year_Month'] = pd.to_datetime(df['Year_Month'], format='%Y-%m')
fir_trends = df.groupby('Year_Month').size()

plt.figure(figsize=(14, 7))
fir_trends.plot(color = '#993399')
plt.title('Monthly FIR Trends')
plt.xlabel('Date')
plt.ylabel('Number of FIRs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Distribution of FIRs by Crime Type
plt.figure(figsize=(14, 7))
sns.countplot(y='CrimeHead_Name', data=df, order=df['CrimeHead_Name'].value_counts().index, color = '#993399')
plt.title('FIR Distribution by Crime Type')
plt.xlabel('Count')
plt.ylabel('Crime Type')
plt.tight_layout()
plt.show()

# Please note: For the `CrimeHead_Name` plot, if there are too many unique crime types,
# it's recommended to show only the top N for clarity, like this:
top_crimes = df['CrimeHead_Name'].value_counts().nlargest(10).index
filtered_df = df[df['CrimeHead_Name'].isin(top_crimes)]
sns.countplot(y='CrimeHead_Name', data=filtered_df, order=top_crimes)
