

# In[85]:


import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


# In[86]:


df = pd.read_csv("C:\\Users\\vigne\\OneDrive\\Desktop\\python project\\SugarCane.csv")


# In[87]:


df.shape


# In[88]:


df.head()


# # Data Cleaning

# In[89]:


df["Production (Tons)"] = df["Production (Tons)"].str.replace(".","")
df["Production per Person (Kg)"] = df["Production per Person (Kg)"].str.replace(".","").str.replace(",",".")
df["Acreage (Hectare)"] = df["Acreage (Hectare)"].str.replace(".","")
df["Yield (Kg / Hectare)"]= df["Yield (Kg / Hectare)"].str.replace(".","").str.replace(",",".")


# In[90]:


df.head()


# In[91]:


df = df.drop( "Unnamed: 0", axis = 1)


# In[92]:


df.rename(columns= {"Production (Tons)": "Production(Tons)"}, inplace = True)
df.rename(columns= {"Production per Person (Kg)": "Production_per_person(Kg)"}, inplace = True)
df.rename(columns= {"Acreage (Hectare)": "Acreage(Hectare)"}, inplace = True)
df.rename(columns= {"Yield (Kg / Hectare)": "Yield(Kg/Hectare)"}, inplace = True)


# In[93]:


df.head()


# In[94]:


df.isna().sum()


# In[95]:


df[df["Acreage(Hectare)"].isnull()]


# In[96]:


df = df.dropna().reset_index().drop("index", axis = 1)


# In[97]:


df


# In[98]:


df.nunique()


# In[99]:


df.dtypes


# In[100]:


df["Production(Tons)"] = df["Production(Tons)"].astype(float)
df["Production_per_person(Kg)"] = df["Production_per_person(Kg)"].astype(float)
df["Acreage(Hectare)"] = df["Acreage(Hectare)"].astype(float)
df["Yield(Kg/Hectare)"] = df["Yield(Kg/Hectare)"].astype(float)


# In[101]:


df.dtypes


# # Univariate Analysis

# In[102]:


df.head()


# ## How many countries produce sugarcane from each continent?

# In[103]:


df["Continent"].value_counts()


# In[104]:


df["Continent"].value_counts().plot(kind = "bar")


# Africa has maximum number of countries which produces sugarcane.

# In[105]:


df.describe()


# ## Checking outliers

# In[106]:


plt.figure(figsize = (10,8))
plt.subplot(2,2,1)
sns.boxplot(df["Production(Tons)"])
plt.title("Production(Tons)")
plt.subplot(2,2,2)
sns.boxplot(df["Production_per_person(Kg)"])
plt.title("Production_per_person(Kg)")
plt.subplot(2,2,3)
sns.boxplot(df["Acreage(Hectare)"])
plt.title("Acreage(Hectare)")
plt.subplot(2,2,4)
sns.boxplot(df["Yield(Kg/Hectare)"])
plt.title("Yield(Kg/Hectare)")
plt.show()


# we have outliers in the data but outliers are required here as it shows the countries which has maximum production. And then we can see what are the reasons for outliers.

# ## Distribution of the columns

# In[107]:


plt.figure(figsize = (10,10))
plt.subplot(2,2,1)
sns.distplot(df["Production(Tons)"])
plt.title("Production(Tons)")
plt.subplot(2,2,2)
sns.distplot(df["Production_per_person(Kg)"])
plt.title("Production_per_person(Kg)")
plt.subplot(2,2,3)
sns.distplot(df["Acreage(Hectare)"])
plt.title("Acreage(Hectare)")
plt.subplot(2,2,4)
sns.distplot(df["Yield(Kg/Hectare)"])
plt.title("Yield(Kg/Hectare)")
plt.show()


# In[108]:


sns.violinplot(df["Production(Tons)"])


# # Bivariate Analysis

# In[109]:


df.head()


# ## Which country produces maximum sugarcane?

# In[110]:


df_new = df[["Country","Production(Tons)"]].set_index("Country")


# In[111]:


df_new


# In[112]:


df_new["Production(Tons)_percent"] = df_new["Production(Tons)"]*100/df_new["Production(Tons)"].sum()


# In[113]:


df_new


# In[114]:


df_new["Production(Tons)_percent"].plot(kind = "pie", autopct = "%.2f")


# Brazil, India and China have 65% of production of sugarcane

# In[115]:


df[["Country","Production(Tons)"]].set_index("Country").sort_values("Production(Tons)", ascending = False).head(15).plot(kind = "bar")


# In[116]:


ax = sns.barplot(data = df.head(15),  x= "Country", y = "Production(Tons)")
ax.set_xticklabels(ax.get_xticklabels(),rotation =90)
plt.show()


# The country "Brazil" produces maximum sugarcane out of all countries.

# ## Which country has highest land?

# In[117]:


df_acr = df.sort_values("Acreage(Hectare)", ascending = False).head(15)
ax = sns.barplot(data = df_acr,  x= "Country", y = "Acreage(Hectare)")
ax.set_xticklabels(ax.get_xticklabels(),rotation =90)
plt.show()


# ## Which country has highest yield per hectare?

# In[118]:


df_yield = df.sort_values("Yield(Kg/Hectare)", ascending = False).head(15)
ax = sns.barplot(data = df_yield,  x= "Country", y = "Yield(Kg/Hectare)")
ax.set_xticklabels(ax.get_xticklabels(),rotation =90)
plt.show()


# Guatemala has the highest yield(kg/hectare)

# ## Which country has highest production? 

# In[119]:


df_yield = df.sort_values("Production_per_person(Kg)", ascending = False).head(15)
ax = sns.barplot(data = df_yield,  x= "Country", y = "Production_per_person(Kg)")
ax.set_xticklabels(ax.get_xticklabels(),rotation =90)
plt.show()


# Production per Person is highest in Paraguay

# ## Correlation 

# In[120]:


"df.corr()"


# In[121]:


"""sns.heatmap(df.corr(), annot = True, cmap="Greens")"""


# ## Do countries with highest land produce more sugarcane? 

# In[122]:


sns.scatterplot(data = df, x = "Acreage(Hectare)", y = "Production(Tons)", hue = "Continent" )


# Overall increase in land increases the production

# ## Do countries which yield more sugarcane per hectare produces more sugarcane in total? 

# In[123]:


sns.scatterplot(data = df, x = "Yield(Kg/Hectare)" , y = "Production(Tons)", hue = "Continent")


# In[124]:


df.head()


# # Analysis for Continent

# In[125]:


df_continent = df.groupby("Continent").sum()


# In[126]:


df_continent["number_of_countries"] = df.groupby("Continent").count()["Country"]


# In[127]:


df_continent


# ## Which continent produces maximum sugarcane? 

# In[128]:


df_continent["Production(Tons)"].sort_values(ascending =  False).plot(kind = "bar")


# ## Do number of countries in a Continent effects production of sugarcane?

# In[129]:


continent_names = df_continent.index.to_list()
sns.lineplot(data = df_continent,x = "number_of_countries", y= "Production(Tons)" )
plt.xticks(df_continent["number_of_countries"], continent_names, rotation =90)
plt.show()


# ## Do continent with highest land produces more sugarcane?

# In[130]:


sns.lineplot(data = df_continent,x = "Acreage(Hectare)", y= "Production(Tons)" )


# ## Production distribution by continent

# In[131]:


df_continent["Production(Tons)"].plot(kind = "pie", autopct = "%.2f%%")
plt.title('Production Distribution by Continent')
plt.show()


# ## Correlation for continent

# In[133]:


"df_continent.corr()"

