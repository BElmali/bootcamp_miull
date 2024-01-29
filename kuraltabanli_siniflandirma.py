
import numpy as np
import pandas as pd
from warnings import filterwarnings
filterwarnings('ignore')
#######Soru1
train = pd.read_csv("kuraltabanlivepandas/kuraltabanli/KuralTabanlıSınıflandırmaProje/persona.csv")
def checkdf(dataframe,head=5):
    print("***********index KAYIT SAYISI******")
    print(dataframe.index)
    print("**********shape******")
    print(dataframe.shape)
    print("***********columns******")
    print(dataframe.columns)
    print("********Head******")
    print(dataframe.head())
    print("********Describe******")
    print(dataframe.describe().T)
    print("********boş kayıt var mı******")
    print(dataframe.isnull().values.any())
    print("********boş kayıt hangilerinde******")
    print(dataframe.isnull().sum())
    print("**********Quantiles******")
    print(dataframe.describe([0,0.05,0.1,0.5,0.75,0.9,0.95,1]))
    print("**********INFO******")
    print(dataframe.info())
    for col in dataframe.columns:
            print("***********"+col)
            print("UNIQUE SAYISI************")
            print(dataframe[col].nunique())
            print("ADET SAYISI************")
            print(dataframe[col].value_counts())
checkdf(train)
#######Soru2
train["SOURCE"].nunique()
train["SOURCE"].unique()
#######Soru3
train["PRICE"].unique()
train["PRICE"].nunique()
#######Soru4
train["PRICE"].value_counts()
#######Soru5
train["COUNTRY"].value_counts()
#######Soru6
train.groupby("COUNTRY")["PRICE"].sum()
#######Soru7
train["SOURCE"].value_counts()
#######Soru8
train.groupby("COUNTRY")["PRICE"].mean()
train.groupby(['COUNTRY']).agg({"PRICE": "mean"})
#######Soru9
train.groupby("SOURCE")["PRICE"].mean()
#######Soru10
train.pivot_table("PRICE","COUNTRY","SOURCE")
train.groupby(by=["COUNTRY", 'SOURCE']).agg({"PRICE": "mean"})

#######Görev2
train.groupby(by=["COUNTRY", 'SOURCE','SEX',"AGE"]).agg({"PRICE": "mean"})

#######Görev3
agg_df=train.groupby(by=["COUNTRY", 'SOURCE','SEX',"AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
agg_df.head()

#######Görev4
agg_df=agg_df.reset_index()
agg_df.head()

#######Görev5
bins = [0, 18, 23, 30, 40, 66]
mylabels = ['0_18', '19_23', '24_30', '31_40', '41_66']
agg_df["age_cat"] = pd.cut(agg_df["AGE"], bins, labels=mylabels)
agg_df.head()


#######Görev6
agg_df['customers_level_based'] = agg_df[['COUNTRY', 'SOURCE', 'SEX', 'age_cat']].agg(lambda x: '_'.join(x).upper(), axis=1)
newdf=train.groupby(by=agg_df["customers_level_based"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
agg_df=agg_df[["customers_level_based", "PRICE"]]
agg_df.head()


#######Görev7
agg_df["SEGMENT"]=pd.cut(agg_df["PRICE"], 4, labels=["D","C","B","A"])
agg_df.groupby(by=["SEGMENT"]).agg({"PRICE": ["sum","min","max","mean"]})
#GÖREV 8
new_user="TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"]==new_user]
new_user2="FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"]==new_user2]








