## 2. Introduction To The Data ##

import pandas as pd
#Leia o arqquivo unrate.csv dentro o DataFrame e atribua ao unrate.
unrate = pd.read_csv('unrate.csv')
#Use a função do pandas.to_datetime para converter a coluna DATE em uma series de valores de datetime.
unrate['DATE']=pd.to_datetime(unrate['DATE'])
#Mostre as 12 primeiras do unrate.
unrate.head(12)

## 6. Introduction to Matplotlib ##

import matplotlib.pyplot as plt
#Gere um plot vazio usando plt.plot() e mostre com o plt.show()
plt.plot()
plt.show()

## 7. Adding Data ##

# Gere um gráfico com as informações dos desempregados de 1948:
    # x-values deve ser os 12 primeiros valores da coluna DATE.
    # y-values desve ser os 12 primeiros valores da coluna VALUE.
first_twelve = unrate[:12]
plt.plot(first_twelve["DATE"],first_twelve["VALUE"])
#Mostre o plot.
plt.show()

## 8. Fixing Axis Ticks ##

# Gere o mesmo gráfico da tela anterior com as informações dos desempregados de 1948:
    # x-values deve ser os 12 primeiros valores da coluna DATE.
    # y-values desve ser os 12 primeiros valores da coluna VALUE.
first_twelve = unrate[:12]
plt.plot(first_twelve["DATE"],first_twelve["VALUE"])
#Use o pyplot.xticks() para rotacionar o x-axis em 90 graus.
plt.xticks(rotation=90)
#Mostre o plot.
plt.show()

## 9. Adding Axis Labels And A Title ##

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
#Mostre o plot.
plt.show()