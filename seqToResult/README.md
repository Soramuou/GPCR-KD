# dataToResult

## Motivation

This code is for the features that have been extracted using the ".FASTA" format.

 
## Instructions
We will provide dataset of GPCR named "new_data".   
  
If you have the format dataset, you can only change the path form the 7th line in read_data.py
(the deault path is "./new_data")and then, you can use the shell with:
  
If you want to switch the classfifier, you can change the param of function "classifier_name" in 63th line main.py, we can use "MLPClassifier","RandomForestClassifier", "GaussianNB" and "SVC" in this program.
``` shell
python3 main.py
```
The program will do all the train and prodict work, it will use a long time, maybe hours or 1 day, it depends on your performance of CPU.  
   
Then, the results will appear in the "result.txt" file, in this file, There will show four level's accuary, in order: subtype level, family level, subfamily level, sub-subfamily level.