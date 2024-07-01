import pandas as pd
age=[39,50,38,53,28]
workclass=['State-gov','Self-emp-not-inc','Private','Private','Private']
fnlwgt=[77516,83311,215646,234721,338409]
education=["Bachelors","Bachelors",'HS-grad','11th','Bachelors']
education_num=[13,13,9,7,13]
marital_status=['Never-married','Married-civ-spouse','Divorced','Married-civ-spouse','Married-civ-spouse']
occupation=['Adm-clerical','Exec-managerial','Handlers-cleaners','Handlers-cleaners','Prof-specialty']
relationship=['Not-in-family','Husband','Not-in-family','Husband','Wife']
race=['White','White','White','Black','Black']
sex=['Male','Male','Male','Male','Female']
capital_gain=[2174,0,0,0,0]
capital_loss=[0,0,0,0,0]
hours=[40,13,40,40,40]
cont=['United-States','United-States','United-States','United-States','Cuba']
salary=['>=50K','<=50K','>=50K','<=50K','>=50K']
dic={'age':age,'workclass':workclass,'fnlwgt':fnlwgt,'education':education,'education-num':education_num,'marital-status':marital_status,'occupation':occupation,'relationship':relationship,'race':race,'sex':sex,'capital-gain,':capital_gain,'capital-loss':capital_loss,'hours-per-week':hours,'native-country':cont,'salary':salary}

#pd.set_option('display.max_columns',None)
df=pd.DataFrame(dic)

counts={}
for i in df['race']:
    if i not in counts:
        counts[i]=1
    else:
        counts[i]+=1
#Query 1
s1=pd.Series(counts)
print(s1)
print()

#Query 2
x=df[df["sex"]=='Male']['age']
avg=x.mean()
print("The average age of men is",avg)
print()

#Query 3
total=df['education'].count()
bachelor_count=len(df[df['education']=='Bachelors'])
print((bachelor_count/total)*100,"% of people have Bachelors Degree")
print()

#Query 4
count=0
for (row,rowseries) in df.loc[:,('education','salary')].iterrows():
    if rowseries['education']=='Bachelors' and rowseries['salary']=='>=50K':
        print(rowseries)
        count+=1
num=len(df[df['education']=='Bachelors'])
print((count/num)*100,'% of the people with Bachelors make more than 50K')
print()

#Query 5
m=0
for (row,rowseries) in df.loc[:,('education','salary')].iterrows():
    if rowseries['education']!='Bachelors' and rowseries['salary']=='>=50K':
        print(rowseries)
        m+=1
n=len(df[df['education']!='Bachelors'])
print((m/n)*100,'% of the people without Bachelors make more than 50K')
print()

#Query 6
print(df['hours-per-week'].min(),' is the minimum numbers of hours per week')
print()

#Query 7
cont_sal={}
for (row,rowseries) in df.loc[:,['native-country','salary']].iterrows():
    if rowseries['salary']=='>=50K':
        if rowseries['native-country'] not in cont_sal:
            cont_sal[rowseries['native-country']]=1
        else:
            cont_sal[rowseries['native-country']]+=1
            
print(max(cont_sal),' has the most people making more than 50K')
print()

 

