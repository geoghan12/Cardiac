import pandas as pd
import numpy as np
from Clean_Fun import *
from Meta_fun import *
from scipy.stats import mode

# %% Load dataset
df=pd.read_csv('Data/after_merge.csv',index_col=0)
# %% test patients, determing Response Value
df.columns
import matplotlib.pyplot as plt

df=meta_clean(df)
plt.hist(train(df).cr)
# %%

keep_cols=['patient_gender', 'ef','admit_weight', 'acute_or_chronic',
       'weight','this_weight_change','weight_change_since_admit', 'bnp',
       'this_bnp_change','ace', 'bb', 'diuretics',
       'anticoagulant', 'ionotropes', 'other_cardiac_meds', 'bun',
       'cr', 'potasium', 'this_cr_change',
       'resting_hr', 'systolic', 'diastolic', 'outcome',
       'cad/mi', 'heart_failure_unspecfied', 'diastolic_heart_failure',
       'systolic_chf', 'atrial_fibrilation', 'cardiomyoapthy', 'lvad',
       'chf', 'duration', 'age' ,'F_5nKZ993n', 'F_71ADiKaS', 'F_Fy1r9IXM',
       'F_KYzNhByH', 'F_L1V04aB0', 'F_US4llDDz', 'F_Xxk5Yn3E', 'F_kIUZIzRp',
       'F_mB0G57bu']
df=df[keep_cols]

temporary_imputation(df)
# there remains 20 annoying patients with many missing values
train(df).isnull().sum()
df.dropna(inplace=True)

###### any transformations will go here ########

# %%

from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.metrics import confusion_matrix

# %%
x=train(df).drop('outcome',axis=1)
y=train(df).outcome

x_train, x_test, y_train, y_test = train_test_split(x,y)

model = XGBClassifier()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
predictions = [round(value) for value in y_pred]
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))


# print(para_search.best_score_)
# print(para_search.best_params_)
# prediction=para_search.predict(x_test)
cnf_matrix = confusion_matrix(y_test, predictions)
cnf_matrix
