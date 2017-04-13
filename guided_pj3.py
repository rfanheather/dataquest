
# coding: utf-8

# ## Analyzing Thanksgiving dinner
# 
# The dataset is stored in the thanksgiving.csv file. It contains 1058 responses to an online survey about what Americans eat for Thanksgiving dinner. Each survey respondent was asked questions about what they typically eat for Thanksgiving, along with some demographic questions, like their gender, income, and location. This dataset will allow us to discover regional and income-based patterns in what Americans eat for Thanksgiving dinner. The dataset came from FiveThirtyEight, and can be found https://github.com/fivethirtyeight/data/tree/master/thanksgiving-2015 .
# 
# The dataset has 65 columns, and 1058 rows. Most of the column names are questions, and most of the column values are string responses to the questions. Most of the columns are categorical, as a survey respondent had to select one of a few options.

# In[1]:

import pandas as pd
data = pd.read_csv('thanksgiving.csv', encoding="Latin-1")
print(data.head(5))


# In[2]:

print(data.columns)


# ## Filtering Out Rows From A DataFrame

# In[3]:

data["Do you celebrate Thanksgiving?"].value_counts()


# In[4]:

celebrate = data["Do you celebrate Thanksgiving?"] == 'Yes'
data = data[celebrate]


# ## Using Value_counts To Explore Main Dishes

# In[5]:

data['What is typically the main dish at your Thanksgiving dinner?'].value_counts()


# In[6]:

Tofurkey = data[data['What is typically the main dish at your Thanksgiving dinner?'] == 'Tofurkey']
Tofurkey["Do you typically have gravy?"]


# ## Figuring Out What Pies People Eat

# In[7]:

apple_isnull = pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"])
pumpkin_isnull = pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"])
pecan_isnull = pd.isnull(data['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan'])

ate_pies = apple_isnull & pumpkin_isnull & pecan_isnull
ate_pies.value_counts()


# ## Converting Age To Numeric

# In[8]:

def cvt_to_int(series):
    if pd.isnull(series):
        return None
    series = series.split(' ')[0]
    series = series.replace('+', '')
    return int(series)

data['int_age'] = data["Age"].apply(cvt_to_int)
data['int_age'].describe()


# The result is just the approx of ages, it is younger than most of the real ages, but the distribution is even.

# ## Converting Income To Numeric

# In[9]:

def str_to_income(series):
    if pd.isnull(series):
        return None
    series = series.split(" ")[0]
    if series == 'Prefer':
        return None
    series = series.replace('$', '')
    series = series.replace(',', '')
    return int(series)

data['int_income'] = data['How much total combined money did all members of your HOUSEHOLD earn last year?'].apply(str_to_income)


# In[10]:

data['int_income'].describe()


# ## Correlating Travel Distance And Income

# In[11]:

data[data['int_income'] < 150000]['How far will you travel for Thanksgiving?'].value_counts()


# In[12]:

data[data['int_income'] > 150000]['How far will you travel for Thanksgiving?'].value_counts()


# According to the results, people with higher income tend to spend Thanksgiving at home, while people with lower income may travel around.

# ## Linking Friendship And Age

# In[13]:

avg_age = data.pivot_table(index = "Have you ever tried to meet up with hometown friends on Thanksgiving night?", columns = 'Have you ever attended a "Friendsgiving?"', values = "int_age")


# In[14]:

avg_age


# In[15]:

avg_income = data.pivot_table(index = 'Have you ever tried to meet up with hometown friends on Thanksgiving night?', columns = 'Have you ever attended a "Friendsgiving?"', values = "int_income")


# In[16]:

avg_income


# ## Figure out the most common dessert people eat.

# In[17]:

data.columns


# In[18]:

columns = ['Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Apple cobbler','Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Blondies', 'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Brownies','Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Carrot cake','Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Cookies','Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Fudge','Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Ice cream','Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Peach cobbler']
desserts = data[columns]
desserts.head(5)


# In[19]:

dessert_eaten = {}
def fav_dessert(dataframe,d):
    drop_na = dataframe.dropna(axis=0, subset=[d])
    dessert_eaten[d] = drop_na.shape[0]
    return dessert_eaten


# In[20]:

fav_dessert(desserts,'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Apple cobbler')
fav_dessert(desserts,'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Blondies')
fav_dessert(desserts,'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Brownies')
fav_dessert(desserts,'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Carrot cake')
fav_dessert(desserts,'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Cookies')


# According to the result, the most common dessert people eat is cookies.

# ## Identify how many people work on Thanksgiving.

# In[21]:

work = data['Will you employer make you work on Black Friday?']
work.value_counts()


# About 61.4% of people work at Thanksgiving.

# In[ ]:



