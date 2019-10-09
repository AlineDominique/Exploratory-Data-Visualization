## 2. Introduction to the data ##

import pandas as pd
# Leia o arquivo fandango_scores.csv no DataFrame com o nome de reviews.
reviews = pd.read_csv('fandango_scores.csv')
#Selecione as seguintes colunas e atribua ao DataFrame norm_reviews:FILM, RT_user_norm, Metacritic_user_nom (note the misspelling of norm), IMDB_norm, Fandango_Ratingvalue e Fandango_Stars.
norm_reviews = reviews[['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']]
print(norm_reviews[:1])

## 4. Creating Bars ##

import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
# Crie apenas um subplot e atribua o retorno ao objeto Figure ao fig, e retorno do objeto Axis ao ax.
fig, ax = plt.subplots()
# Gere um gráfico bar plot com:
    # left defina como bar_positions;
    # height(largura) defina como bar_heights;
    # width(comprimento) defina como 0.5;
ax.bar(bar_positions, bar_heights, 0.5)
#Use o plt.show() para mostrao grafico.
plt.show()


## 5. Aligning Axis Ticks And Labels ##

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)
# Crie apenas um subplot e atribua o retorno ao objeto Figure ao fig, e retorno do objeto Axis ao ax.
fig, ax = plt.subplots()
# Gere um gráfico bar plot com:
    # left defina como bar_positions;
    # height(largura) defina como bar_heights;
    # width(comprimento) defina como 0.5;
ax.bar(bar_positions, bar_heights, 0.5)
#Defina o x-axis tick positions como tick_positions
ax.set_xticks(tick_positions)
#Defina o x-axis tick labels como num_cols e rotacione em 90 graus.
ax.set_xticklabels(num_cols, rotation=90)
#Defina o x-axis label como "Rating Source".
ax.set_xlabel("Rating Source")
#Defina o y-axis label como "Average Rating".
ax.set_ylabel("Average Rating")
#Defina o título do gráfico como "Average User Rating For Avengers: Age of Ultron (2015)".
ax.set_title("Average User Rating For Avengers: Age of Ultron (2015)")
#Use o plt.show() para mostrao grafico.
plt.show()

## 6. Horizontal Bar Plot ##

import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_widths = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)
# Crie apenas um subplot e atribua o retorno ao objeto Figure ao fig, e retorno do objeto Axis ao ax.
fig, ax = plt.subplots()
# Gere um gráfico bar plot com:
    # left defina como bar_positions;
    # width(comprimento) defina como bar_widths;
    # height(largura) defina como 0.5;
ax.barh(bar_positions, bar_widths, 0.5)
#Defina o y-axis tick positions como tick_positions
ax.set_yticks(tick_positions)
#Defina o y-axis tick labels como num_cols.
ax.set_yticklabels(num_cols)
#Defina o y-axis label como "Rating Source".
ax.set_ylabel("Rating Source")
#Defina o x-axis label como "Average Rating".
ax.set_xlabel("Average Rating")
#Defina o título do gráfico como "Average User Rating For Avengers: Age of Ultron (2015)".
ax.set_title("Average User Rating For Avengers: Age of Ultron (2015)")
#Use o plt.show() para mostrao grafico.
plt.show()

## 7. Scatter plot ##

import matplotlib.pyplot as plt
# Crie apenas um gráfico e atribua o retorno ao objeto Figure e Axes, como seguientes nomes expectivamente fig,ax.
fig, ax = plt.subplots()
# Gere um gráfico de dispersão com a coluna Fandango_Ratingvalue como x-axis e a coluna RT_user_norm como y-axis.
ax.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
# Defina o label x-axis como "Fandango" e o label y-axis como "Rotten Tomatoes"
ax.set_xlabel('Fandango')
ax.set_ylabel('Rotten Tomatoes')
# Use o plt.show() para mostrar o gráfico.
plt.show()

## 8. Switching axes ##

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews[cols]
#Para o subgráfico como o nome ax1:
    #Gere um gráfico de dispersão com a coluna Fandango_Ratingvalue e com a coluna RT_user_norm,x-axis e y-axis respectivamente.
    #Defina a label x-axis como Fandango e label y-axis como Rotten Tomatoes.
ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
ax1.set_xlabel('Fandango')
ax1.set_ylabel('Rotten Tomatoes')
#Para o subgráfico como o nome ax2:
    #Gere um gráfico de dispersão com a coluna RT_user_norm e com a coluna Fandango_Ratingvalue,x-axis e y-axis respectivamente.
    #Defina a label x-axis como Rotten Tomatoes e label y-axis como Fandango.
ax2.scatter(norm_reviews['RT_user_norm'],norm_reviews['Fandango_Ratingvalue'])
ax2.set_xlabel('Rotten Tomatoes')
ax2.set_ylabel('Fandango')
# Use o plt.show() para mostrar os gráficos.
plt.show()

## 9. Benchmarking correlation ##

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)
#Para o subgráfico como o nome ax1:
    #Gere um gráfico de dispersão com a coluna Fandango_Ratingvalue e com a coluna RT_user_norm,x-axis e y-axis respectivamente.
    #Defina a label x-axis como Fandango e label y-axis como Rotten Tomatoes.
    #Defina o x-axis e y-axis com a data limite de 0 a 5. 
ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
ax1.set_xlabel('Fandango')
ax1.set_ylabel('Rotten Tomatoes')
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 5)
#Para o subgráfico como o nome ax2:
    #Gere um gráfico de dispersão com a coluna Fandango_Ratingvalue e com a coluna Metacritic_user_nom,x-axis e y-axis respectivamente.
    #Defina a label x-axis como Fandango e label y-axis como Metacritic.
    #Defina o x-axis e y-axis com a data limite de 0 a 5. 
ax2.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['Metacritic_user_nom'])
ax2.set_xlabel('Fandango')
ax2.set_ylabel('Metacritic')
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 5)
#Para o subgráfico como o nome ax3:
    #Gere um gráfico de dispersão com a coluna Fandango_Ratingvalue e com a coluna IMDB_norm,x-axis e y-axis respectivamente.
    #Defina a label x-axis como Fandango e label y-axis como IMDB.
    #Defina o x-axis e y-axis com a data limite de 0 a 5. 
ax3.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['IMDB_norm'])
ax3.set_xlabel('Fandango')
ax3.set_ylabel('IMDB')
ax3.set_xlim(0, 5)
ax3.set_ylim(0, 5)
#Use o plt.show() para mostrar os gráficos.
plt.show()