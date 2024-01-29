#Pandas Alıştırmalar

#Görev1:  Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()


#Görev2:  Titanic verisetindeki kadın ve erkek yolcuların sayısını bulunuz.
df["sex"].value_counts()


#Görev3:  Her birsutunaaitunique değerlerinsayısınıbulunuz.
df.nunique()


#Görev4:  pclass değişkeninin unique değerlerininsayısınıbulunuz.

df["pclass"].nunique()


#Görev5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
df["parch"].nunique()

#Görev6:  embarked değişkeninintipinikontrolediniz. Tipinicategory olarakdeğiştirinizvetekrarkontrolediniz.
df['embarked'].dtype
df['embarked'] = df['embarked'].astype('category')
df['embarked'].dtype

#Görev7:  embarked değeriC olanlarıntümbilgelerinigösteriniz.
df.loc[df['embarked']=="C"]

#Görev8:  embarked değeriS olmayanlarıntümbilgelerinigösteriniz.
df.loc[df['embarked']!="S"]

#Görev9:   Yaşı30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
df.loc[(df['age']< 30) & (df['sex']=="female")]


#Görev10:  Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
df.loc[(df['fare']> 500) | (df['age']>70)]


#Görev 11:  Her birdeğişkendekiboşdeğerlerintoplamınıbulunuz.
df.isnull().sum()

#Görev 12:  who değişkeninidataframe’dençıkarınız.
df=df.drop(columns="who")
df.columns


#Görev13:  deck değikenindekiboşdeğerlerideck değişkeninençoktekraredendeğeri(mode) iledoldurunuz.
df["deck"].value_counts()
df['deck'].fillna(df['deck'].mode()[0], inplace=True)


#Görev14:  age değikenindekiboşdeğerleriage değişkeninmedyanıiledoldurunuz.
df["age"].value_counts()
df['age'].fillna(df['age'].median(), inplace=True)


#Görev15:  survived değişkeninin pclass ve cinsiyetd eğişkenleri kırılımınında sum, count, mean değerlerinibulunuz.
df.groupby(['pclass', 'sex'])['survived'].agg(['sum', 'count', 'mean'])


#Görev16:  30 yaşın altında olanlar 1, 30a eşitveüstünde olanlara 0 vericek bir fonksiyonyazın.
#Yazdığınız fonksiyonu kullanarak titanik verisetinde age_flag adında bir değişken oluşturunuz oluşturunuz.
#(apply ve lambda yapılarını kullanınız)
df["age_flag"]=df["age"].apply(lambda x: 0 if x >= 30 else 1)

#Görev17:  Seaborn kütüphanesi içerisinden Tipsveri setini tanımlayınız.
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("tips")
df.head()
df.info()

#Görev18:  Time değişkeninin kategorilerine(Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
df.groupby("time")["total_bill"].agg(['min', 'max', 'mean'])

#Görev19:  Günlere ve time göre total_bill değerlerinin toplamını, min, max veortalamasını bulunuz
df.groupby(['day', 'time'])['total_bill'].agg(['sum', 'min', 'max', 'mean'])

#Görev 20:  Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin daye göre toplamını, min, max veortalamasınıbulunuz.
df.groupby([df["day"],df['time'] == 'Lunch',df['sex'] == 'Female']).agg({'total_bill': ['sum', 'min', 'max', 'mean'],
                                                                              'tip': ['sum', 'min', 'max', 'mean']})

#Görev 21: size'i 3'ten  küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
df.loc[(df['size']< 3) & (df['total_bill']>10),"total_bill"].mean()


#Görev22:  total_bill_tip_sum adında yeni birdeğişken oluşturunuz. Her birmüşterinin ödediği totalbill ve tip in toplamını versin.

df["total_bill_tip_sum"]=df['total_bill'] + df['tip']


#Görev23:  total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyiyeni birdataframe'eatayınız.
df_sorted = df.sort_values(by='total_bill_tip_sum', ascending=False)

# İlk 30 kişiyi içeren yeni bir DataFrame oluştur
top_30 = df_sorted.head(30)
