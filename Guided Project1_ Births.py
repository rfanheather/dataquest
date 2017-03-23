
# coding: utf-8

# ## Working with US birth dataset
# The dataset contains the following columns:
# - `year` : Year (1994 to 2003).
# - `month`: Month (1 to 12).
# - `date_of_month`: Day number of the month (1 to 31).
# - `day_of_week`: Day of week (1 to 7).
# - `births`: Number of births that day.

# In[1]:

US_births = open("US_births_1994-2003_CDC_NCHS.csv", 'r').read()
US_births = US_births.split("\n")
US_births[0:10]


# In[2]:

def read_csv(file):
    string = open(file).read()
    string_list = string.split("\n")
    string_list = string_list[1:len(string_list)]
    final_list = []
    for it in string_list:
        int_fields = []
        string_fields = it.split(",")
        for num in string_fields:
            int_fields.append(int(num))
        final_list.append(int_fields)
    return final_list

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_list[0:10]


# In[3]:

def month_births(data_list):
    births_per_month = {}
    for it in data_list:
        month = it[1]
        birth = it[4]
        if month in births_per_month:
            births_per_month[month] = births_per_month[month] + birth
        else:
            births_per_month[month] = birth
    return births_per_month

cdc_month_births = month_births(cdc_list)
cdc_month_births


# In[4]:

def dow_births(data_list):
    day_of_week = {}
    for it in data_list:
        day = it[3]
        birth = it[4]
        if day in day_of_week:
            day_of_week[day] = day_of_week[day] + birth
        else:
            day_of_week[day] = birth
    return day_of_week

cdc_day_births = dow_births(cdc_list)
cdc_day_births


# In[5]:

def calc_counts(data, column):
    lib = {}
    for it in data:
        position = it[int(column)]
        birth = it[4]
        if position in lib:
            lib[position] = lib[position] + birth
        else:
            lib[position] = birth
    return lib

cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dow_births = calc_counts(cdc_list, 3)


# In[6]:

def min_max(lib):
    minv = 0
    maxv = 0
    for it in lib:
        if lib[it] > maxv:
            maxv = lib[it]
        if lib[it] < minv:
            minv = lib[it]
    return minv, maxv


# In[7]:

def trend(data, column, val):
    lib = {}
    
    for row in data:
        year = row[0]
        test = row[int(column)]
        birth = row[4]
        if test == int(val):
            if year in lib:
                lib[year] = lib[year] + birth
            else:
                lib[year] = birth
    
    val_births = 0
    for key in lib:
        val = lib[key]
        if val_births == 0:
            print("Growth of birth in " + str(key) + " is not available.")
        else:
            if val > val_births:
                print("Growth of birth in " + str(key) + " is increasing")
            elif val < val_births: 
                print("Growth of birth in " + str(key) + " is decreasing")
            elif val == val_births:
                print("Growth of birth in " + str(key) + " is the same")
        val_births = val
        
    return lib


# The number of births on Saturday change each year between 1994 and 2003.

# In[8]:

#the number of births on Saturday change each year between 1994 and 2003
a = trend(cdc_list, 3, 6)
a

