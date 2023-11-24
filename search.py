import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import warnings
#warnings.filterwarnings("ignore")
st.title('Et peut-être que vous savez pas encore où aller passer les fêtes?')

pt = pd.read_csv('pt.csv', sep=',', index_col = 0)
df = pd.read_csv('data_tot2.csv', sep=',')
#df['Country name EN'] = df['Country name EN'].apply(lambda x: str(x).lower())
pivot = pd.read_csv('pivot.csv', sep=',', index_col = 0)
#st.write(pt['Dec'].min())


values = st.slider(
    'Choisissez les températures souhaitables pour vous: ',
    pt['Dec'].min(), pt['Dec'].max(), (pt['Dec'].min(), pt['Dec'].max()))

values_population = st.slider(
    'Choisissez la population souhaitée dans la ville: ',
    df['Population'].min(), df['Population'].max(), (df['Population'].min(), df['Population'].max()))


#st.write('Values:', values)
#st.write('Value:', values[0])
st.write("Apparemment les températures recherchées sont accessibles dans ",len(pt[(pt['Dec']>=values[0])&(pt['Dec']<=values[1])]), "pays")
#pt[(pt['Dec']>=values[0])&(pt['Dec']<=values[1])]
#pt[(pt['Dec']>=values[0])&(pt['Dec']<=values[1])]
country_list = pt[(pt['Dec']>=values[0])&(pt['Dec']<=values[1])]['Country'].values.tolist()
#st.write('list des pays', country_list)

st.write("Et dans ces pays vous pourrez choisir entre",len(df[df['Country name EN'].isin(country_list)]), "villes")
#df[df['Country name EN'].isin(country_list)]
st.write("Par contre, si vous chercher le nombre d'habitants précis, ce sera dans ",len(df[(df['Country name EN'].isin(country_list)) & ((df['Population']>=values_population[0]) & (df['Population']<values_population[1]))]), "villes")

df_result = df[(df['Country name EN'].isin(country_list)) & ((df['Population']>=values_population[0]) & (df['Population']<values_population[1]))]
#df_result

st.map(df_result,
    latitude='lat',
    longitude='lon',
    size='size',
    #color='Dec'
    )

for city in df_result['Name']:
    st.write("Soyez bienvenus à", city, "qui est une ville de ", df_result[df_result['Name']==city]['Country name EN'].values[0])