import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',15)
pd.set_option('display.max_rows',100)

df = pd.read_csv("CardioGoodFitness.csv")

df.columns      #Checking the column name(features)

df.head()       #Checking the first five elements of each columns

df.dtypes       #Checking the dtypes.

col=['Product','Age','Education','MaritalStatus','Usage','Fitness']     #Checking the unique elements of each columns.
for x in col:
    print(' \n{}:{}'.format(x.upper(),df[x].unique()))          #The unique() function is used to find the unique elements.
    
col1=['Product','MaritalStatus','Usage','Fitness','Education','Gender']
for x in col1:
    print(df[x].value_counts())         #Return a Series containing counts of unique values. 

df.isnull().sum()       #Checking the null or Nan values. Sum() is applied as if not then in boolean form it will return.
#Observation: No null values was there.

for i in df.columns:                #Checking the zeros as age, gender, etc can''t be zero in this case.
    print(i,len(df[df[i] == 0]))    
#Observation: No zero values was there.

df.describe()
'''
count - The number of not-empty values.
mean -  The average (mean) value.
std -   The standard deviation. A standard deviation is a statistic that measures the 
        dispersion of a dataset relative to its mean. The standard deviation is calculated as 
        the square root of variance by determining each data point's deviation relative to the
        mean. If the data points are further from the mean, there is a higher deviation within 
        the data set; thus, the more spread out the data, the higher the standard deviation.
min -   the minimum value.
25% -   The 25% percentile*. Also known as the first, or lower, quartile. The 25th percentile 
        is the value at which 25% of the answers lie below that value, and 75% of the answers lie above that value.
50% -   The 50% percentile*. Also known as the Median. The median cuts the data set in half.  
        Half of the answers lie below the median and half lie above the median
75% -   The 75% percentile*. Also known as the third, or upper, quartile. The 75th percentile is 
        the value at which 25% of the answers lie above that value and 75% of the answers lie below that value.
max -   the maximum value.
'''

list = ['TM195', 'TM498', 'TM798']
for i in list:    
    print(df[df['Product'] == i].describe())
    
#PIE Plot
explode=(0.08,0.02,0.02)        #Gapping between each parts
fig = plt.figure(figsize=(200, 200))
plt.figure(figsize=(14,7))
df['Product'].value_counts().plot.pie(autopct='%1.2f%%',figsize=(5,5),explode=explode)  #figsize, increasing or decreasing size of circle.
plt.title("Pie chart of Product Sales", fontsize=30)    #fontsize of title
plt.show()  #To show pieplot as in some IDE not shows without this.
#Observation: TM195 is most purchased followed by TM498.

#Bar Graph
plt.bar(df['Product'].unique(), df["Product"].value_counts(), color = ['r', 'g','b'])
plt.title("Product wise sale")
plt.grid(True)
plt.show()
#Observation: As we observed in pie plot, here, in bar plot, also we can see that TM195 is most purchased one.

#Sale of each product gender wise
plt.figure(figsize=(10,10))     #Fixing the size of fig
prd_gender=pd.crosstab(df['Product'],df['Gender'])
print(prd_gender)
prd_gender.plot(kind='bar')
plt.title("PRODUCT BY GENDER")
plt.show()
#OR, by using sns.countplot(),
plt.figure(figsize=(7,7))
sns.countplot(df['Product'],hue=df["Gender"]).set(title='Product By Gender')
plt.show()
#Observation: In terms of gender, TM195 is equally used by male and female. While TM498 is more used by female but difference between male and female use is smaller. TM798 is more used by female, only few male using TM798.

#Sale of each product martialstatus wise
plt.figure(figsize=(10,10))
prd_MaritalStatus=pd.crosstab(df['Product'],df['MaritalStatus'] )
print(prd_MaritalStatus)
prd_MaritalStatus.plot(kind='bar')
plt.title("Product By MaritalStatus")
plt.show()
#OR, by using sns.countplot(),
plt.figure(figsize=(7,7))
sns.countplot(df['Product'],hue=df["MaritalStatus"]).set(title='Product By MaritalStatus')
plt.show()
#Observation: Couple using TM195 followed by TM498 and TM798. Unmarried peoples using this product lesser than married one.

#Sale of each product maritalstatus and gender wise
prd_mar_gen= pd.crosstab(index=df["Product"], columns=[df["MaritalStatus"],df["Gender"]])
print(prd_mar_gen)
prd_mar_gen.plot(kind='bar',figsize=(10,7))
#TM195: Female Partnered buying more this product than others. TM498: Male Partenered buying more this product but count of female partnered buying TM195 is more than others in TM498 and TM798. TM798: Male Partenered buying more this product.
#This can be understand by carefully observing above two graphs.

#Sale of each product usage rating wise
plt.figure(figsize=(10,10))
prd_usage=pd.crosstab(df['Product'],df['Usage'] )
print(prd_usage)
prd_usage.plot(kind='bar')
plt.title("Product By Usage")
plt.show()
#OR, by using sns.countplot(),
plt.figure(figsize=(7,7))
sns.countplot(df['Product'],hue=df["Usage"]).set(title='Product By Usage')
#Observation: Most of the people using TM195 and TM498 given self rating fitness 3 while people using TM798 given self rated fitness 4.

#Sale of each product education wise
prd_education=pd.crosstab(df['Product'],df['Education'] )
print(prd_education)
prd_education.plot(kind='bar')
plt.title("Product By Education")
plt.show()
#OR, by using sns.countplot(),
plt.figure(figsize=(7,7))
sns.countplot(df['Product'],hue=df["Education"]).set(title='Product By Education')
#Observation: People with 14 and 16 years education using TM195 more but they also using TM489 but counts is less than TM195, while 18 years of education people choosing TM798 rather than TM195 and TM498.

#Sale of each product Fitness wise
plt.figure(figsize=(10,10))
prd_Fitness=pd.crosstab(df['Product'],df['Fitness'] )
print(prd_Fitness)
ax=prd_Fitness.plot(kind='bar')
plt.title("Product By Fitness")
plt.show()
#OR, by using sns.countplot(),
plt.figure(figsize=(7,7))
sns.countplot(df['Product'],hue=df["Fitness"]).set(title='Product By Fitness')
#Most of the people using TM798 gave fitness rating '5' while most of the people using other two gave fitness rating '3'.

#Pairplot
pp = sns.pairplot(df, height=1.8, aspect=1.8, plot_kws=dict(edgecolor="k", linewidth=0.5), diag_kind="kde", diag_kws=dict(shade=True))
fig = pp.fig 
fig.subplots_adjust(top=0.93, wspace=0.3)
t = fig.suptitle('CardioGoodFitness', fontsize=30)

#Boxplot
fig1, axes1 =plt.subplots(3,2,figsize=(14, 19))
list1_col=['Age','Income','Education','Usage','Fitness','Miles']
for i in range(len(list1_col)):
    row=i//2
    col=i%2
    ax=axes1[row,col]
    sns.boxplot(df[list1_col[i]],df['Product'],ax=ax).set(title='PRODUCT BY ' + list1_col[i].upper())
#People with age more than 37 and using TM798 are outlier. It can be easily observed in above Boxplot.
    
#sns.pointplot of education vs income product wise
plt.figure(figsize=(12,7))
sns.pointplot(x=df["Education"],y=df["Income"],hue=df['Product']).set(title='EDUCATION  BY INCOME ') 
#Observation: People with more income is purchasing TM798 also people with more than 19 years education purchasing TM798 as clearly seen in above plotted graph.

#sns.pointplot of fitness vs miles product wise
plt.figure(figsize=(12,7))
sns.pointplot(x=df["Fitness"],y=df["Miles"],hue=df['Product']).set(title='EDUCATION  BY INCOME ') 
#People using TM498 didn't give fitness more than '4'. People using TM798 gave fitness rating between '3' and '5' and also they used to run more miles than others.

#Two graph gender wise
plt.figure(figsize=(12,7))
sns.catplot(x='Usage', y='Income', col='Gender',hue='Product' ,kind="bar", data=df) 

#Two graph MaritalStatus wise
plt.figure(figsize=(12,7))
sns.catplot(x='Gender',y='Income', hue='Product', col='MaritalStatus', data=df,kind='bar')






