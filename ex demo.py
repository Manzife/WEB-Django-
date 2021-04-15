import pandas as pd
import seaborn as sns

df= pd.read_excel(r"C:\Users\usuario\Downloads\Exercício_TFT_PIBpc_ALC.xlsx")

#%%
#data cleaning
df.rename(columns = {"Unnamed: 0": "país","Unnamed: 1" : "TFT 2005-2010", "Unnamed: 3": "TFT 2015-2020", "Unnamed: 6" : "PIBPC em log 2019"}, inplace = True)

df  = df.loc[3:35, ["país", "TFT 2005-2010", "TFT 2015-2020", "PIBPC em log 2019"]]

#%%

Q1 = sns.regplot(x = "TFT 2015-2020", y = "PIBPC em log 2019", data = df  )
Q1.set_xlabel("TFT 2015-2020")
Q1.set_ylabel("PIBPC em log 2019")

# %%
