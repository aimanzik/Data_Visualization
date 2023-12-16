import matplotlib.pyplot as plt
import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel("C:\\Users\\aiman\\Documents\\SQIT3073\\GASSG\\ASSG.xlsx", sheet_name="Sheet3")

# Set 'End of period' as the index
df.set_index('End of period', inplace=True)

# Check if 2022 is in df's index
if 2022 in df.index:
    # Filter data for the year 2022
    data_2022 = df.loc[2022]

    # Drop 'Total Assets' from the data
    data_2022 = data_2022.drop('Total Assets')

    # Plotting
    fig, ax = plt.subplots(figsize=(10,6))
    wedges, texts = ax.pie(data_2022, startangle=90)

    # Define the labels for the legend
    labels = ['{0} - {1:1.1f} %'.format(i,j) for i,j in zip(data_2022.index, 100*data_2022/data_2022.sum())]

    ax.legend(wedges, labels, title="Columns", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    ax.set_title('Percentage of Every Assets for The Year of 2022')
    plt.show()
else:
    print("No data available for the year 2022.")

# Print the DataFrame
print(df)



