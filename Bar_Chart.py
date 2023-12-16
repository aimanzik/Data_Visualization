import matplotlib.pyplot as plt
import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel("C:\\Users\\aiman\\Documents\\SQIT3073\\GASSG\\ASSG.xlsx", sheet_name="Sheet3")

# Assuming 'End of period' and 'Gold and Foreign Exchange' are column names in your DataFrame
years = df['End of period']
gold_foreign_exchange = df['Gold and Foreign Exchange']

plt.figure(figsize=(10, 6))
plt.bar(years, gold_foreign_exchange, color='gold')
plt.xlabel('End of Period (Year)', fontsize=12)
plt.ylabel('RM/Million', fontsize=12)
plt.title('Gold and Foreign Exchange Over Years', fontsize=14)
plt.xticks(rotation=45)
plt.show()

# Print the DataFrame
print(df)




