import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

#import pygame
st.title('Bienvenue sur notre page festive !')

st.write("C'est où que vous compter passer vos fêtes ?")

df= pd.read_csv('data3.csv', sep=',')
#df
pt = pd.read_csv('pt.csv', sep=',', index_col = 0)
#df = pd.read_csv('data3.csv', sep=',', index_col = 0)
pivot = pd.read_csv('pivot.csv', sep=',', index_col = 0)
#pt

def game(nom_pays):
    try:
        if pt[pt['Country']==str(nom_pays).lower()]['Dec'].values[0]>=15:
            return "chaud"
        elif pt[pt['Country']==str(nom_pays).lower()]['Dec'].values[0]<15:
            return "froid"
        else:
            return "erreur"
    except:
        return "Veuillez rentrer le pays en anglais et sans fautes de frappe"

def temp(nom_pays):
    try:
        return pt[pt['Country']==str(nom_pays).lower()]['Dec'].values[0]
    except:
        return "Veuillez rentrer le pays en anglais et sans fautes de frappe"

def town_info(town_name, country_name):
    try:
        timezone = df[((df['Name']== town_name)|(df['ASCII Name']== town_name))&(df['Country name EN']== country_name.lower())]['Timezone'].values[0]
        population = pivot[pivot['Timezone']==timezone]['Population']
        return population.values[0]
    except:
        return "Combien"
def town_population(town_name, country_name):
    try:
        population = df[((df['Name']== town_name)|(df['ASCII Name']== town_name))&(df['Country name EN']== country_name.lower())]['Population'].values[0]
        return population
    except:
        return "Ah, il y a un problème"



#game('France')

#town_name = st.text_input("Rntrer le nom de votre ville:")
country_name = st.text_input("Rentrer le nom de votre pays (en anglais):")
if country_name:
    st.write("Apparemment, il fait",game(country_name), "là où tu vas fêter! tu veux connaitre la température précise?" )
    #df[df['Country name EN']==country_name]
    #reponse = st.text_input("Tu veux connaitre la température attendue?")
    #if reponse:
    st.write("Et plus précisement, il va faire ", temp(country_name), "degré.")
    city_name = st.text_input("et dans quelle ville vous comptez fêter ?")
    if city_name:
        #st.write(city_name)
        st.write("Alors, il y aura",town_population(city_name, country_name), "dans ta ville" )
        st.write("Mais si la distance ne compte pas pour toi, sache que minimum",town_info(city_name, country_name), "personnes dans le monde entier vont fêter avec toi!" )

        