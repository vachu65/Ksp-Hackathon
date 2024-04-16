import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('ChargsheetedDetails.csv')

# Example of a horizontal bar plot for the number of FIRs per UnitName
plt.figure(figsize=(12, 8))  # Increase the figure size
sns.countplot(y='UnitName', data=df, order=df['UnitName'].value_counts().index, color='#993399')  # Use horizontal bar chart
plt.title('Number of FIRs per UnitName')
plt.xlabel('Number of FIRs')
plt.ylabel('UnitName')
plt.tight_layout()
plt.show()
