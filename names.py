import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

df = pd.read_csv('names.csv')

def countNames(names):
    males = names.loc[names["Sex"]=='M'].groupby('Sex').sum()['Count'].to_numpy()
    females = names.loc[names["Sex"]=='F'].groupby('Sex').sum()['Count'].to_numpy()
    return males[0],females[0]

def theMostCommonNameIn2003(names):
    name = names.loc[names["Year"]==2003].head(1)
    return name

def theLeastCommonName1897(names):
    count = names.loc[names["Year"]==1987]['Count'].min()
    nonCommonNames = names.loc[(names['Year']==1987) & (names["Count"]==count)]
    return nonCommonNames

def moreThen300timesIn2018(names):
    _300timesNames = names.loc[(names["Year"]==2018) & (names['Count']>300)]
    return _300timesNames

def countNamesIn2003(names):
    males = len(names.loc[(names["Year"]==2003) & (names["Sex"]=='M')].index)
    females = len(names.loc[(names["Year"]==2003) & (names["Sex"]=='F')].index)
    return males,females

def wereBorn(names):

    count = [[year,names.loc[names["Year"]==year]['Count'].sum()] for year in range(names["Year"].min(),names["Year"].max()+1)]
    #count = names.groupby('Year').sum()

    return count

def topFiveMostCommonNames(names):
    #names = names.groupby('Name').sum().sort_values(by=['Count'], ascending=False)
    names = names.groupby('Name').sum().sort_values(by=['Count'])
    return names[0:5]['Count']

def mostCommonNameFrom1980To1990(names):
    name = names[names[names['Year']==1980].index[0]:names[names['Year']==1991].index[0]].groupby('Name').sum().sort_values(by=['Count'], ascending=False).iloc(0)[0]

    #name = names[names[names['Year']==1980].index[0]:names[names['Year']==1991].index[0]].groupby('Name').sum()

    return name

def mostCommonMaryAlexJohn(names):
    years = names[names['Name'].isin(['Mary','John', 'Alex'])].sort_values(by=['Count'],ascending=False)
    Mary = years[years['Name']=='Mary']['Year'].iloc(0)[0]
    Alex = years[years['Name']=='Alex']['Year'].iloc(0)[0]
    John = years[years['Name']=='John']['Year'].iloc(0)[0]
    return Mary, Alex, John

def countDifferentNames(names):
    count = len(names.loc[names['Sex']=='M'].groupby('Name').sum().index)
    return count

def histogramNameJohnPopulation(df):    
    names = df.loc[(df['Name']=='Ivan') & (df['Sex']=='F')]

    names[['Year', 'Count']].plot(kind='bar', x='Year', y='Count')

    #years = names['Year'].to_numpy()[::5]

    #plt.locator_params(axis='x', nbins=5)

    return plt.show()

def countBoysAndGirlsFrom1930To1940(df):
    df = df[df[df['Year']==1930].index[0]:df[df['Year']==1941].index[0]]
    boysCount = df.loc[df['Sex']=='M'].groupby('Year').sum()
    girlsCount = df.loc[df['Sex']=='F'].groupby('Year').sum()
    boysCount.plot(title='Boys Count')
    girlsCount.plot(title='Girls Count')
    return plt.show()


            
# print(f'Male names: {countNames(df)[0]}. Female names: {countNames(df)[1]}')
# print(f'The most common name in 2003 is: {theMostCommonNameIn2003(df)}')
# print(f"The least common names in 1987 are: {theLeastCommonName1897(df)}")
# print(f'Names mentioned more then 300 times in 2018: {moreThen300timesIn2018(df)}')
# print(f"There were {countNamesIn2003(df)[0]} male names and {countNamesIn2003(df)[1]} female names in 2003")
# print(f'List of year,born: {wereBorn(df)}')
#print(f'Top Five most common names thru yrs: {topFiveMostCommonNames(df)}')
# print(f'The most common name from 1980 to 1990: {mostCommonNameFrom1980To1990(df)}')
# print(f'Years when Mary Alex and John were the most common names: {mostCommonMaryAlexJohn(df)}')
# print(f'Different male names: {countDifferentNames(df)}')
#print(histogramNameJohnPopulation(df))
#print(countBoysAndGirlsFrom1930To1940(df))
print(df)






