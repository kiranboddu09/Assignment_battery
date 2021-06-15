# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 19:48:35 2021

@author: kiran
"""
#pandas library to load the data from excel to dataframes
import pandas as pd
#os library is used to create the directory where the file is located
import os
os.chdir("C:\\Users\\kiran\\OneDrive\\Desktop\\Projects-ML\\nunam")
#As the data is in different sheets and the data has to combined into single csv file
#the data is collected from as shown below
xls = pd.ExcelFile('data.xlsx')
xlx = pd.Excelfile('data_1.xlsx')
df1 = pd.read_excel(xls, 'Detail_67_1_1')
df2 = pd.read_excel(xls, 'Detail_67_1_1_1')
df3 = pd.read_excel(xls, 'Detail_67_1_1_2')
df4 = pd.read_excel(xls, 'Detail_67_1_1_3')
df5 = pd.read_excel(xls, 'Detail_67_1_1_4')
df6 = pd.read_excel(xls, 'Detail_67_1_1_5')
df7 = pd.read_excel(xls, 'Detail_67_1_1_6')
dfv1 = pd.read_excel(xls, 'DetailVol_67_1_1')
dfv2 = pd.read_excel(xls, 'DetailVol_67_1_1_1')
dfv3 = pd.read_excel(xls, 'DetailVol_67_1_1_2')
dfv4 = pd.read_excel(xls, 'DetailVol_67_1_1_3')
dfv5 = pd.read_excel(xls, 'DetailVol_67_1_1_4')
dfv6 = pd.read_excel(xls, 'DetailVol_67_1_1_5')
dfv7 = pd.read_excel(xls, 'DetailVol_67_1_1_6')
dft1 = pd.read_excel(xls, 'DetailTemp_67_1_1')
dft2 = pd.read_excel(xls, 'DetailTemp_67_1_1_1')
dft3 = pd.read_excel(xls, 'DetailTemp_67_1_1_2')
dft4 = pd.read_excel(xlx, 'DetailTemp_67_1_1_3')
dft5 = pd.read_excel(xlx, 'DetailTemp_67_1_1_4')
dft6 = pd.read_excel(xlx, 'DetailTemp_67_1_1_5')
dft7 = pd.read_excel(xlx, 'DetailTemp_67_1_1_6')

#concating the data okaa same type into single dataframe ,
#outer is used as the whole keys of all dataframes are taken

Detail = pd.concat([df1,df2,df3,df4,df5,df6,df7],join='outer')
DetailVol = pd.concat([dfv1,dfv2,dfv3,dfv4,dfv5,dfv6,dfv7],join='outer')
DetailTemp = pd.concat([dft1,dft2,dft3,dft4,dft5,dft6,dft7],join='outer')

#index is set as the column which is having the datetime formate as it will
#be easy to compare and resamlpe iplace is used to entirely change the data 
#and replace it with original file

Detail.set_index("Absolute Time",inplace=True)
DetailVol.set_index("Realtime",inplace=True)
DetailTemp.set_index("Realtime",inplace=True)

#Dataframes are transferred to csv files

Detail.to_csv("C:\\Users\\kiran\\OneDrive\\Desktop\\Projects-ML\\nunam\\Detail.csv")
DetailVol.to_csv("C:\\Users\\kiran\\OneDrive\\Desktop\\Projects-ML\\nunam\\DetailVol.csv")
DetailTemp.to_csv("C:\\Users\\kiran\\OneDrive\\Desktop\\Projects-ML\\nunam\\DetailTemp.csv")

#detailDownsampled=Detail.resample("1Min").mean()
#to check the info of the datasets

Detail.info()
DetailTemp.info()
DetailVol.info()
#Detail.resample("1Min").mean()


