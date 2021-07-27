# techAssignment

### Task 1
Python Script for consuming WebServices using requests for GET and POST methods

### Task 2
Exported Talend Job created in TOS_BD-20200219_1130-V7.3.1 containig the implementation of Data Flow Orchestration 


![alt text](https://github.com/lakshmi4296/techAssignment/blob/main/DataFlowOrchestration/DataFlow.png)

#### Steps followed

As part of building the data warehouse to load the fact and dimension data into MongoDB

1. Given DDL statements were executed on SQL Server and data was exported as csv
2. CSV files containing the Dimensions (DimDate, DimProduct, DimStore) are loaded into MongoDB using python (script.py) 

##### Talend

3. tFileList is used to loop through the given data in yyyy/MM/dd/xx/xxxx.txt.gzip format
4. tJAVA is used to get the subfolder(MM and dd) in variables
5. The compressed files are extracted in a temporary folder, combined and save as pipe delimited file in /dataextract/yy/MM/dd/factstore folder respectively
6. After the data is stored in the specified format, again tFileList is used to loop through these folders 
7. The files in these subfolders are read and loaded into MongoDB FactStore collection
8. The temp folder used for uncompressing is cleared out in post job


9. Queries are available on queries.txt
