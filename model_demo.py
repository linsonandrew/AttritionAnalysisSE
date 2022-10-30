import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import datetime
from datetime import datetime

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt
from sklearn.metrics import plot_roc_curve
from sklearn.metrics import roc_auc_score

from collections import Counter
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from collections import Counter

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from io import StringIO
import seaborn as sns
import sys
import warnings

def dummy_model():

#########################################################
# MAKE SURE THIS IS THERE SO WARNINGS ARE NOT DISPLAYED #
#########################################################

    warnings.filterwarnings("ignore")
    ###########################
    # CLASS NULLIO(STRINGIO): #
    #  DEF WRITE(SELF, TXT):  #
    #          PASS           #
    #  SYS.STDOUT = NULLIO()  #
    ###########################

    data = pd.read_csv('Dummy.csv')
    print(data.head(5))




    objects = data.select_dtypes(include=[object])
    numericals = data.select_dtypes(exclude=[object])



    categoricals = ['country','gender']

    numericals= ['credit_score','age','products_number','tenure','balance','estimated_salary','credit_card','active_member','churn']


#################################
# A LIST TO SAVE ALL THE IMAGES #
#################################

    a=[]

########################################################
# JUST SAVE PLOT IN A VARIABLE AND APPEND FOR MATHPLOT #
########################################################

    fig = plt.figure(figsize=(12,6))
    features = numericals
    for i in range(0, len(features)):
        plt.subplot(1, len(features), i+1)
        sns.boxplot(y=data[features[i]], color='purple')
        plt.tight_layout()

    a.append(fig)




    fig = plt.figure(figsize=(12,6))

    features = numericals
    for i in range(0, len(features)):
        plt.subplot(2, len(features)//2 + 1, i+1)
        #plt.subplot(1, len(features), i+1)
        sns.distplot(x=data[features[i]], color='green')
        plt.xlabel(features[i])
        plt.tight_layout()

    a.append(fig)





    correlation = data.corr()
    a.append(sns.heatmap(correlation, annot=True, fmt='.2f').get_figure())


#########################################
# YOU HAVE TO USE .GET_FIGURE() FOR SNS #
#########################################

    _,axss = plt.subplots(2,2, figsize=[15,10])
    a.append(sns.countplot(x='churn', hue='country', data=data, ax=axss[0][0]).get_figure())
    a.append(sns.countplot(x='churn', hue='gender', data=data, ax=axss[0][1]).get_figure())
    a.append(sns.countplot(x='churn', hue='products_number', data=data, ax=axss[1][0]).get_figure())
    a.append(sns.countplot(x='churn', hue='credit_card', data=data, ax=axss[1][1]).get_figure())




    #a.append(sns.catplot(x = 'churn', y="estimated_salary", kind="box", data = data).get_figure())
    #a.append(sns.catplot(x = 'churn', y="balance", kind="box", data = data).get_figure())

###################################################################################
# USE FILENAMES LIKE 0.PNG , 1.PNG ... N.PNG FOR YOUR GRAPH TO BE SAVED AS IMAGES #
###################################################################################

    for i in range(len(a)):
        a[i].savefig(str(i)+".png")

    return len(a)

#########################################
# THINGS TO BE RETURNED FROM YOUR MODEL #
#########################################
####################################################################
# FIRST LIST ==> EMP ID, ATTRITION PERCENTAGE, [ATTRITION REASONS] #
#          SECOND LIST ==> IMAGE TITLE,IMAGE DESCIPRTIONS          #
####################################################################
######################################
#       OPTIONAL IN THIS FILE:       #
# THIRD LIST ==> PROBLEMS, SOLUTIONS #
######################################
