 # essential libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# function on pandas to read the file of extension .csv
main_df = pd.read_csv("data2.csv")

'''property 01'''
print ("shape of dataset is ", main_df.shape)
print("\n------------------\n")


'''property 02'''
print("data types of each feature\n")

print(main_df.dtypes)
print("\n--------------------\n")
'''property 03'''
print("description of dataset")
print(main_df.describe())

'''here we take few countries for analysis but first we only read all countries in dataframe'''
c_df_all = main_df["Country Name"]
c_df_all

'''this method is used for repeating countries name in dataset so we use user define function to remove repeating countries'''
def kill_repeat(lst):
    new_lst =[]
    new_lst.append("Aruba")
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst

'''here we call the function and store in list because our function return us a list'''
countries = kill_repeat(c_df_all)

'''here we use some selective countries for analysis'''
selective_c = list()
for i in range(0,200,10):
    selective_c.append(countries[i])
selective_c

'''only the years is seperated in this list'''
years = list(np.arange(1960,2020,1))