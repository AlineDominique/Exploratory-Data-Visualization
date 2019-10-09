## 2. Frequency Distribution ##

#Use o método value_counts() para retornar a frequência da coluna Fandango_Ratingvalue. Ordene o resultado por index, e atribua a variavel fandango_distribution.
fandango_distribution = norm_reviews['Fandango_Ratingvalue'].value_counts()
fandango_distribution = fandango_distribution.sort_index()
#Use o método value_counts() para retornar a frequência da coluna IMDB_norm. Ordene o resultado por index, e atribua a variavel imdb_distribution.
imdb_distribution = norm_reviews['IMDB_norm'].value_counts()
imdb_distribution = imdb_distribution.sort_index()
#Usa função print() para mostrar a tabela de distribuição nas variaveis fandango_distribution e imdb_distribution.
print(fandango_distribution)
print(imdb_distribution)


## 4. Histogram In Matplotlib ##

#Crie apenas um subgrafico e atribua o retorno aos objetos Figure e Axis como os nomes fig e ax.
fig,ax = plt.subplots()
#Gere o histograma com os valores da coluna Fandango_Ratingvalue e os valores entre 0 e 5.
ax.hist(norm_reviews['Fandango_Ratingvalue'], range=(0, 5))
#Use o plt.show para mostrar o gráfico.
plt.show()

## 5. Comparing histograms ##

fig = plt.figure(figsize=(5,20))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)
#Para o gráfico com o nome ax1:
    #Gere um histograma com os valores da coluna Fandango_Ratingvalue e usando o bins = 20 e o range = (0,5).
    #Defina o título como Distribution of Fandango Ratings.
ax1.hist(norm_reviews['Fandango_Ratingvalue'], 20, range=(0, 5))
ax1.set_title('Distribution of Fandango Ratings')
ax1.set_ylim(0,50)
#Para o gráfico com o nome ax2:
    #Gere um histograma com os valores da coluna RT_user_norm e usando o bins = 20 e o range = (0,5).
    #Defina o título como Distribution of Rotten Tomatoes Ratings.
ax2.hist(norm_reviews['RT_user_norm'], 20, range=(0, 5))
ax2.set_title('Distribution of Rotten Tomatoes Ratings')
ax2.set_ylim(0,50)
#Para o gráfico com o nome ax3:
    #Gere um histograma com os valores da coluna Metacritic_user_nom e usando o bins = 20 e o range = (0,5).
    #Defina o título como Distribution of Metacritic Ratings.
ax3.hist(norm_reviews['Metacritic_user_nom'], 20, range=(0, 5))
ax3.set_title('Distribution of Metacritic Ratings')
ax3.set_ylim(0,50)
#Para o gráfico com o nome ax4:
    #Gere um histograma com os valores da coluna IMDB_norm e usando o bins = 20 e o range = (0,5).
    #Defina o título como Distribution of IMDB Ratings.
ax4.hist(norm_reviews['IMDB_norm'], 20, range=(0, 5))
ax4.set_title('Distribution of IMDB Ratings')
ax4.set_ylim(0,50)
#Para todos os gráficos:
    #Defina o y-axis entre 0 e 50 usando o Axes.set_ylim().
#Use o plt.show() para mostrar os gráficos.
plt.show()

## 7. Box Plot ##

#Crie apenas um subgrafico e atribua o retorno aos objetos Figure e Axis como os nomes fig e ax.
fig,ax = plt.subplots()
#Gere um box plot com os valores da coluna RT_user_norm.
    #Defina o y-axis com o limite entre 0 e 5.
    #Defina o x-axis com o tick label como Rotten Tomatoes.
ax.boxplot(norm_reviews['RT_user_norm'])
ax.set_ylim(0,5)
ax.set_xticklabels(["Rotten Tomatoes"])
#Use o plt.show() para mostrar o grafico.
plt.show()

## 8. Multiple Box Plots ##

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
#Crie apenas um grafico e atribua o retorno aos objetos Figure e Axis como os nomes fig e ax.
fig,ax = plt.subplots()
#Gere um box plot que contenha com os valores de cada coluna da variavel num_cols.
ax.boxplot(norm_reviews[num_cols].values)
#Defina o x-axis com o tick label como o nomes da colunas e rotacione em 90° graus.
ax.set_xticklabels(norm_reviews[num_cols],rotation = 90)
#Defina o y-axis com o limite entre 0 e 5.
ax.set_ylim(0,5)
#Use o plt.show() para mostrar o grafico.
plt.show()