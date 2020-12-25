# dataToResult



## Motivation

This is a quick guide for running the code of classifying GPCRs based on machine learning methods in all levels. The code is for the features that have been extracted using the ".FASTA" format.

 
## Instructions
The dataset of GPCRs is set as "new_data".   
  
If you have the formatted dataset, you can only change the path form the 7th line in read_data.py
(the deault path is "./new_data")and then, you can use the shell with:
  
If you want to switch the classfifier, you can change the param of function "classifier_name" in 63th line main.py, we can use "MLPClassifier","RandomForestClassifier", "GaussianNB" and "SVC" in this program.
``` shell
python3 main.py
```
The program will do all the training and prediction work, it will use a long time, maybe hours or 1 day, it depends on the performance of your CPU.  
   
Then, the results will appear in the "result.txt" file, in this file, There is the accuracy in 4 different levels, which are subtype level, family level, subfamily level, sub-subfamily level.