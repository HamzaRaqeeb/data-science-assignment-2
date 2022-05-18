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


def population_growth(df):
     pop_china = df.loc[(df['Country Name'] == "China") & (df['Indicator Code'] == "SP.POP.GROW")]

     '''china is country and indicator name is population growth and from 2000 onward'''
     v_df = pop_china.iloc[:, 35:-1].values
     v_df = v_df[np.logical_not(np.isnan(v_df))]
     plt.figure(figsize=(12, 8))

     pop_gld = df.loc[(df['Country Name'] == "Greenland") & (df['Indicator Code'] == "SP.POP.GROW")]
     gv_df = pop_gld.iloc[:, 35:-1].values
     gv_df = gv_df[np.logical_not(np.isnan(gv_df))]

     plt.title("Total population of ")
     plt.hist(v_df)
     plt.hist(gv_df)
     plt.show()


def frequency(df):
    df_canada = df.loc[(df['Country Name'] == "Pakistan") & (df['Indicator Name'] == "Agricultural land (% of land area)")]
    y_df = df_canada.iloc[:,5:-1].values
    y_df=y_df[np.logical_not(np.isnan(y_df))]
    data = list(y_df)
    plt.figure(figsize=(15,8))
    plt.title("Pakistan's Agricultural land")
    plt.plot(data)
    plt.show()

def piechart():
    df1 = main_df.loc[(main_df['Country Name'] == "Aruba") & (main_df['Indicator Code'] == "SP.URB.TOTL.IN.ZS")]
    data1 = df1.iloc[:,60:61].values

    df2 = main_df.loc[(main_df['Country Name'] == "Armenia") & (main_df['Indicator Code'] == "SP.URB.TOTL.IN.ZS")]
    data2 = df2.iloc[:,60:61].values

    df3 = main_df.loc[(main_df['Country Name'] == "Bangladesh") & (main_df['Indicator Code'] == "SP.URB.TOTL.IN.ZS")]
    data3 = df3.iloc[:,60:61].values

    df4 = main_df.loc[(main_df['Country Name'] == "Switzerland") & (main_df['Indicator Code'] == "SP.URB.TOTL.IN.ZS")]
    data4 = df4.iloc[:,60:61].values

    df5 = main_df.loc[(main_df['Country Name'] == "Spain") & (main_df['Indicator Code'] == "SP.URB.TOTL.IN.ZS")]
    data5 = df5.iloc[:,60:61].values

    df6 = main_df.loc[(main_df['Country Name'] == "China") & (main_df['Indicator Code'] == "SP.URB.TOTL.IN.ZS")]
    data6 = df6.iloc[:,60:61].values



    plt.figure(figsize=(10,8))
    plt.title("Pie chart of urban population of 2017")

    country_names = ["Aruba", "armenia", "Bangladesh","switzerland","Spain","China"]
    values = [43.192, 63.082, 35.083, 73.739, 79.84,56.736]

    plt.pie(values, labels = country_names,autopct='%1.2f%%')
    plt.show()
def main():
    population_growth(main_df)
    frequency(main_df)
    piechart()
if __name__ == "__main__":
    main()
