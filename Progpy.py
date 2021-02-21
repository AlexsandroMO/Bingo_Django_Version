import pandas as pd
import numpy as np
import openpyxl
import xlrd


def clear_df():
  obj = [[0]]
  col = [['CANTADOS']]
  df = pd.DataFrame(data=obj, columns=col,index=[0])
  df.to_csv('static/excel/BINGO.csv',index=False)

  return df


def list_bingo(num):

  df = pd.read_csv('static/excel/BINGO.csv')

  dados = [
            [num]
          ]
  col = ['CANTADOS']
  df2 = pd.DataFrame(data=dados, columns=col, index=[len(df)])

  new = df.append(pd.concat([df2]))
  new.to_csv('static/excel/BINGO.csv' ,index=False)

  return new['CANTADOS']


def singed():
  df = pd.read_csv('static/excel/BINGO.csv')

  return df


def clear_List():
  lista = np.arange(1, 100)
  col = [['LIS']]
  df = pd.DataFrame(data=lista, columns=col)
  df.to_csv('static/excel/Lista.csv',index=False)

  return df

clear_List()


def actualy_list(canto):

  lista = []
  Lista = pd.read_csv('static/excel/Lista.csv')

  for i in Lista['LIS']:
    lista.append(i)

  listaDois = list(filter(lambda i: i != canto, lista))

  col = ['LIS']
  df = pd.DataFrame(data=listaDois, columns=col)
  df.to_csv('static/excel/Lista.csv',index=False)

  return df

