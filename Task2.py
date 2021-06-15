# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:24:04 2021

@author: kiran
"""
import pandas as pd
import os
os.chdir("C:\\Users\\kiran\\OneDrive\\Desktop\\Projects-ML\\nunam")


DetailVol_sample = pd.read_csv("DetailVol.csv",index_col=0)

#index is set as DatetimeIndex to easily resample the data
DetailVol_sample.index = pd.to_datetime(DetailVol_sample.index)

#data is downsampled by sample/min by the means of the whole polpulation per
#sample
detailVolDownsampled = DetailVol_sample.resample("1Min").mean()

#Data is exported to csv file
detailVolDownsampled.to_csv("C:\\Users\\kiran\\OneDrive\\Desktop\\Projects-ML\\nunam\\detailVolDownsampled.csv")



Detail_sample = pd.read_csv("Detail.csv",index_col=0)

#index is set as DatetimeIndex to easily resample the data
Detail_sample.index = pd.to_datetime(Detail_sample.index)

#data is downsampled by sample/min by the means of the whole polpulation per
#sample
detailDownsampled = Detail_sample.resample("1Min").mean()

#Data is exported to csv file
detailDownsampled.to_csv("C:\\Users\\kiran\\OneDrive\\Desktop\\Projects-ML\\nunam\\detailDownsampled.csv")



DetailTemp_sample = pd.read_csv("DetailTemp.csv",index_col=0)

#index is set as DatetimeIndex to easily resample the data
DetailTemp_sample.index = pd.to_datetime(DetailTemp_sample.index)

#data is downsampled by sample/min by the means of the whole polpulation per
#sample
detailTempDownsampled = DetailTemp_sample.resample("1Min").mean()

#Data is exported to csv file
detailTempDownsampled.to_csv("C:\\Users\\kiran\\OneDrive\\Desktop\\Projects-ML\\nunam\\detailTempDownsampled.csv")