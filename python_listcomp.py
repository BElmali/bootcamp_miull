import pandas as pd
import numpy as np
############# 1
x = 8
type(x)
y = 3.2
type(y)
z = 8j + 18
type(z)
a = "Hello World"
type(a)
b = True
type(b)
c = 23 < 22
type(c)
l = [1, 2, 3, 4]
type(l)
d = {"Name": "Jake",
      "Age": 27,
      "Adress": "Downtown"}
type(d)
t = ("Machine Learning", "Data Science")
type(t)
s = {"Python", "Machine Learning", "Data Science"}
type(s)

############# 2
text = "The goal is to turn data into information, and information into insight."
text = text.upper()
text = text.replace(",","")
text = text.replace(".","")
print(text.split())


############# 3
lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
print(len(lst))
print(lst[0])
print(lst[10])
lst2 = lst[0:4]
print(lst2)
lst.pop(8)
lst.append("!")
lst.insert(8, "N")

############# 4
dict = {"Christian" : ["America" ,18],
         "Daisy"    : ["England", 12],
         "Antonio"  : ["Spain" ,22],
         "Dante"    : ["Italy" ,25]}
dict.keys()
dict.values()
dict["Daisy"]= ["England", 13]
dict.update({"Ahmet": ["Turkey", 24]})
dict.pop("Antonio")

############# 5
l = [2,13,18,93,22]
eve=[]
odd=[]
def func(list):
    for i in list:
        if i % 2 == 0:
            eve.append(i)
        else:
            odd.append(i)
    return eve,odd
even_list, odd_list = func(l)

############# 6
ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]
M = []
T = []
j=0
for i, o in enumerate(ogrenciler):
    if i <= 2:
        print("Mühendislik Fakültesi ", i+1 , ". ögrenci:",o)
    else:
        j=j+1
        print("Tıp Fakültesi ", j , ". ögrenci:",o)

############# 7
ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]
a= list(zip(kredi, ders_kodu, kontenjan))
for i in range(len(a)):
    print("Kredisi", a[i][0], "olan", a[i][1], "kodlu dersin kontenjanı", a[i][2], "kişidir.")

############# 8
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

if kume1.issuperset(kume2) == True:
    print(kume2.intersection(kume1))
else:
    print(kume2.symmetric_difference(kume1))



import seaborn as sns
df = sns. load_dataset("car_crashes")
df.columns
df.columns=["NUM_"+col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]
df.columns=[col.upper() if "no" in col else col.upper()+"_FLAG" for col in df.columns]



og_list=["abbrev","no_previous"]
newdf = [col for col in df.columns if col not in og_list]
df[newdf]
















