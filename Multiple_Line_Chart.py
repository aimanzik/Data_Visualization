import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# Assuming 'data' is your DataFrame
df = pd.read_excel("C:\\Users\\aiman\\Documents\\SQIT3073\\GASSG\\ASSG.xlsx", sheet_name="Sheet2")

# Convert 'End of period' to datetime
df['End of period'] = pd.to_datetime(df['End of period'], format='%d/%m/%Y')

# Filter data for the two periods
df_2021 = df[(df['End of period'] >= '2021-01-01') & (df['End of period'] <= '2021-12-01')]
df_2022 = df[(df['End of period'] >= '2022-01-01') & (df['End of period'] <= '2022-12-01')]

# Extract month from 'End of period'
df_2021['Month'] = df_2021['End of period'].dt.month
df_2022['Month'] = df_2022['End of period'].dt.month

plt.figure(figsize=(10, 6))

# Plot data
plt.plot(df_2021['Month'], df_2021['Total Assets'], label='2021')
plt.plot(df_2022['Month'], df_2022['Total Assets'], label='2022')

plt.xlabel('Month')
plt.ylabel('Total Assets (RM/Million)')
plt.title('Total Assets for 2021 and 2022')
plt.legend()

# Set xticks to show all months
plt.xticks(range(1, 13))

plt.show()

# Print the DataFrame
print(df)



