## 1. Recap ##

import pandas as pd
import matplotlib.pyplot as plt
#Leia o arquivo unrate.csv.
# Use o Pandas.to_datetime para converter a coluna DATE me uma Series de valores datetime.
unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])

# Gere o mesmo gráfico da tela anterior com as informações dos desempregados de 1948:
    # x-values deve ser os 12 primeiros valores da coluna DATE.
    # y-values desve ser os 12 primeiros valores da coluna VALUE.
    #Use o pyplot.xticks() para rotacionar o x-axis em 90 graus.
first_twelve = unrate[:12]
plt.plot(first_twelve["DATE"],first_twelve["VALUE"])
plt.xticks(rotation=90)
# Coloque o nome da x-axis como Month.
# Coloque o nome da y-axis como Unemployment Rate.
# Colque o título como Monthly Unemployment Trends, 1948.
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
#Mostre o gráfico.
plt.show()

## 3. Matplotlib Classes ##

import matplotlib.pyplot as plt
# Use o plt.figure() para criar uma figura e atribua ao fig.
fig = plt.figure()
# Use Figure.add_subplot() para criar 2 subplots um abaixo do outro.
# Atribua o objeto top Axes para ax1.
ax1 = fig.add_subplot(2,1,1)
# Atribua o objeto top Axes para ax2.
ax2 = fig.add_subplot(2,1,2)
# Use plt.show() para mostrar o resultado do plot.
plt.show()

## 5. Adding Data ##

# Crie dois gráficos de linha em um layout de 2 linhas por 1 coluna:
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
# No gráfico do top, plot a data de 1948.
    #Para o x-axis, use as 12 primeiras linhas da coluna DATE.
    #Para o y-axis, use as 12 primeiras linhas da coluna VALUE.
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
# No gráfico de baixo, plot a data de 1949.
    #Para o x-axis, use as linhas 12 ao 24  da coluna DATE.
    #Para o y-axis, use as linhas 12 ao 24 da coluna VALUE.
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
# Mostre todos os plots.
plt.show()

## 6. Formatting And Spacing ##

fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()
# Para cada plot que nós geramos na tela anterior, coloque a largura da area do gráfico em 12 inches e altura de 5 inches.


## 7. Comparing Across More Years ##

#Defina a largura da área de plotagem para 12 polegadas e a altura para 12 polegadas.
fig = plt.figure(figsize=(12,12))
#Gere uma grade com 5 linhas e 1 coluna e plote dados dos anos individuais. Comece com 1948 na subparcela superior e termine com 1952 na subparcela inferior.
for i in range(5):
    ax = fig.add_subplot(5,1,i+1)
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    ax.plot(subset['DATE'], subset['VALUE'])
#Use plt.show () para exibir os gráficos.
plt.show()

## 8. Overlaying Line Charts ##

unrate['MONTH'] = unrate['DATE'].dt.month
# Defina o plot do gráfico em uma area de 6 polegadas de largura e 3 polegadas de comprimento.
fig = plt.figure(figsize=(6,3))
#Gere duas linhas no gráfico na base do subplot, usando a coluna MONTH para o x-axis e enquanto a coluna DATE:

    # Uma linha para da data de 1948, com a cor vermelha(red)
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c='red')    
    # Uma linha para da data dd 1948, com a cor azul(blue)
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c='blue')
#Use o plt.show() para mostrar o gráfico.
plt.show()


## 9. Adding More Lines ##

#Defina a area do gráfico com largura de 10 polegadas e comprimento de 6 polegadas.
fig = plt.figure(figsize=(10,6))
colors = ['red','blue','green','orange','black']
#Gere um gráfico com os seguintes passos:
    # 1948: defina linha com a cor vermelha(red);
    # 1949: defina linha com a cor azul(blue);
    # 1950: defina linha com a cor verde(green);
    # 1951: defina linha com a cor laranja(orange);
    # 1952: defina linha com a cor preto(black);
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'],c=colors[i])
#Use o plt.sho() para mostrar o plots.
plt.show()

## 10. Adding A Legend ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
year = ['1948','1949','1950','1951','1952']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i],label=year[i])
#Modifiqe o código da última tela reescrevendp os plots e inclua legenda. Use o ano com valor em cada linha do gráfico com label.
#O lugar da legenda no canto do gráfico(upper left).
plt.legend(loc='upper left')
#Mosytrar o gráfico usando plot.show()
plt.show()

## 11. Final Tweaks ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')
plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")
plt.show()
#Modifique o código da última tela:
    #Defina o título como "Monthly Unemployment Trends, 1948-1952".
    #Defina o x-axis como labels como "Month, Integer".
    #Defina o y-axis como labels como "Unemployment Rate, Percent".