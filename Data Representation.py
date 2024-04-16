import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('ChargsheetedDetails.csv')

# Convert 'Year' and 'Month' into a datetime object for better time series handling
df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'].astype(str))

# Group by date and count the FIRs to see trends over time
date_counts = df.groupby('Date').size()

# Plotting the FIR counts over time
plt.figure(figsize=(12, 6))
plt.plot(date_counts.index, date_counts.values, marker='o', linestyle='-', color='#993399')
plt.title('FIR Counts Over Time')
plt.xlabel('Date')
plt.ylabel('Number of FIRs')
plt.grid(True)
plt.show()

# Scatter plot for visualizing the distribution of FIRs across different months and years
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['Month'], alpha=0.6, color='#993399')
plt.title('Scatter Plot of FIRs by Year and Month')
plt.xlabel('Year')
plt.ylabel('Month')
plt.grid(True)
plt.show()

# Histogram to visualize the frequency of FIRs filed each year
plt.figure(figsize=(10, 6))
plt.hist(df['Year'], bins=range(min(df['Year']), max(df['Year']) + 1), edgecolor='black',  color='#993399')
plt.title('Histogram of FIRs by Year')
plt.xlabel('Year')
plt.ylabel('Count of FIRs')
plt.xticks(range(min(df['Year']), max(df['Year']) + 1))  # Ensure every year is marked
plt.show()

# Box plot to observe the distribution of FIRs across different months for each year
plt.figure(figsize=(10, 6))
sns.boxplot(x='Year', y='Month', data=df, color='#993399')
plt.title('Box Plot of FIRs by Year and Month')
plt.xlabel('Year')
plt.ylabel('Month')
plt.show()
