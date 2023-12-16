import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import matplotlib.dates as mdates

df = pd.read_excel("NewAssetFile.xlsx")

#Create subplots to combine all line chart
fig, axs = plt.subplots(4, 1)


axs[0].plot(df["Gold and Foreign Exchange  ^"])
axs[0].set_title("Gold and Foreign Exchange Stats from Jan to Oct of 2023")
axs[0].set_xlabel("Months")
axs[0].set_ylabel("RM/Million")

axs[1].plot(df["IMF Reserve Tranche Position"])
axs[1].set_title("IMF Reserve Tranche Position Stats from Jan to Oct of 2023")
axs[1].set_xlabel("Months")
axs[1].set_ylabel("RM/Million")

axs[2].plot(df["Loans and Advances"])
axs[2].set_title("Loans and Advances Stats from Jan to Oct of 2023")
axs[2].set_xlabel("Months")
axs[2].set_ylabel("RM/Million")

axs[3].plot(df["Other Assets"])
axs[3].set_title("Other Assets Stats from Jan to Oct of 2023")
axs[3].set_xlabel("Months")
axs[3].set_ylabel("RM/Million")



plt.tight_layout()
plt.show()
 