import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import matplotlib.dates as mdates

df = pd.read_excel("Asset1.xlsx")

#Specify the range of years
start_year = 2018
end_year = 2022

# Filter DataFrame for the specified range of years
df_filtered = df[(df['End of period'] >= start_year) & (df['End of period'] <= end_year)]

# Drop non-numeric columns, excluding 'End of period'
df_numeric = df.select_dtypes(include='number').drop(columns=['End of period'], errors='ignore')

# Create a heatmap for the correlation matrix of all numeric columns
plt.figure(figsize=(12, 10))
sns.heatmap(df_numeric.corr(), annot=True, cmap="YlGnBu", fmt=".2f")


plt.title('Correlation Matrix Between All Types of Assets (2018-2022)')
plt.show()