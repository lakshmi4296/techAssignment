# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 14:42:13 2021

@author: Lakshmi
"""
import pandas as pd
from pymongo import MongoClient
mongodbClient =  MongoClient("mongodb://localhost:27017/")

db = mongodbClient["jtc"]
DimProd_col = db["DimProducts"]

DimProd = pd.read_csv('DimensionData/DimProduct.txt',sep = '\t',encoding = 'ISO-8859-1')
DimProd_dict = DimProd.to_dict("rows")
DimProd_col.insert_many(DimProd_dict)


DimStore_col = db["DimStores"]

DimStore = pd.read_csv('DimensionData/DimStores.txt',sep = ',',encoding = 'ISO-8859-1')
DimStore_dict = DimStore.to_dict("rows")
DimStore_col.insert_many(DimStore_dict)



DimDate_col = db["DimDate"]

DimDate = pd.read_csv('DimensionData/DimDate.txt',sep = ',',encoding = 'ISO-8859-1')
DimDate_dict = DimDate.to_dict("rows")
DimDate_col.insert_many(DimDate_dict)