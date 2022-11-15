def solutions(row,avg_monthlyHours,avg_numberOfProjects):
    reason=[]
    #workload
    if row['satisfaction_level']<=0.2 and row['last_evaluation']>=0.8:
        reason.append(1)
    #training issues
    if 0.45<=row['satisfaction_level']<=0.6  and 0.35<=row['last_evaluation']<=0.5 :
        reason.append(2)
    #confidence issues
    if row['number_project']<avg_numberOfProjects:
        reason.append(3)
    #workload
    if row['number_project']>avg_numberOfProjects:
        reason.append(4)
    #incentives++
    if row['average_montly_hours']>0.7*avg_monthlyHours:
        reason.append(5)
    #increase salary
    if row['average_montly_hours']>avg_monthlyHours and row['salary']==0:
        reason.append(6)
    return reason


def mega(data): 
    #import all the necessary libraries

    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import confusion_matrix

    #import warnings to ignore warnings
    import warnings
    warnings.filterwarnings('ignore')

    #Read the file
    data1 = pd.read_csv(r'HR_Dataset.xls')
    data = pd.read_csv(r'HR_Dataset.xls')
    data.head(4)

    # Encoding Catogorical Columns (Since we have Catagorical column values )
    # 
    # ###########
    # IMP : in the dummies line try taking drop_first off and check accuracy
    # ###########

    data['salary'].replace('low',0,inplace=True)
    data['salary'].replace('medium',1,inplace=True)
    data['salary'].replace('high',2,inplace=True)

    data['Departments '].replace('IT',0,inplace=True)
    data['Departments '].replace('hr',1,inplace=True)
    data['Departments '].replace('management',2,inplace=True)
    data['Departments '].replace('marketing',3,inplace=True)
    data['Departments '].replace('product_mng',4,inplace=True)
    data['Departments '].replace('sales',5,inplace=True)
    data['Departments '].replace('support',6,inplace=True)
    data['Departments '].replace('technical',7,inplace=True)
    data['Departments '].replace('RandD',8,inplace=True)
    data['Departments '].replace('accounting',9,inplace=True)
    data.head()
    

    #Define the dependent and independent variables
    y=data['left'] #dependent variable
    x=data.drop(['left','Emp_ID'],axis=1)
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
    data.head()

    
    knn = KNeighborsClassifier(metric = 'minkowski', p = 2)
    k_list = list(range(10,31))
    k_values = dict(n_neighbors = k_list)
    from sklearn.model_selection import GridSearchCV
    grid = GridSearchCV(knn, k_values, cv = 5, scoring = 'accuracy')
    grid.fit(x_train, y_train)
    grid.best_params_, grid.best_score_
    from sklearn.metrics import classification_report

    y_pred=grid.predict(x_test)
    classification_knn = (classification_report(y_test, y_pred))
    #print(classification_knn)

    # Model Evaluation 

   
    #print(len(data.columns))
    pred_prob = grid.predict_proba(x)
    #print(pred_prob)
    #print(grid.classes_)
    please=np.zeros(len(x))
    for i in range(len(x)):
        please[i]=pred_prob[i][1]
    
    
    
    data_new = data

    data_new['odds'] = please.tolist()
    
    # Solution Functions 
    # 
    # satisfaction level of below 0.2 and last evaluation of 0.8 and above are likely to leave. (Intense Workload) also salary can be a factor .

    ##taking all rows with left ==1
    left_data = data_new.loc[data_new['left'] == 1]
    left_data = left_data.sort_values(by='odds',ascending =False)

    not_data = data_new.loc[data_new['left'] == 0]
    not_data = not_data.sort_values(by='odds',ascending =False)

    avg_numberOfProjects = np.average(data_new['number_project'])
    avg_monthlyHours = np.average(data_new['average_montly_hours'])


    left_data['reason']=left_data.apply(solutions,axis=1,args=(avg_monthlyHours,avg_numberOfProjects))

    not_data['reason']=not_data.apply(solutions,axis=1,args=(avg_monthlyHours,avg_numberOfProjects))
    data_new['reason']=data_new.apply(solutions,axis=1,args=(avg_monthlyHours,avg_numberOfProjects))

    # ################################# Required Mapping #######################################
    # 
    # 
    # (EmpID -->odds --> reasons )

    left =0
    not_left = 0
    for i in data1['left']:
        if(i==1):
            left=left+1
        else:
            not_left=not_left+1
    

    impLeftData = data_new.tail(3750)
    labels = 'left','not left'
    sizes = [left,not_left]
    explode = (0.1,0)
    #print(not_data)
    fig0,ax1 = plt.subplots()
    ax1.pie(sizes,explode=explode,labels = labels,autopct ='%1.1f%%',shadow=True,startangle=90)
    plt.title("Employees Left v/s Employees not Left", bbox={'facecolor':'0.8', 'pad':5})


    plt.show()
    fig0.savefig('lin0.png', dpi=100)

    sns.set(style = 'whitegrid')
    sns.stripplot(x="satisfaction_level", y="last_evaluation", hue="left")
    
    



    p2=0
    p3=0
    p4=0
    p5=0
    p6=0
    p7=0
    for i in data1['number_project']:
        if(i==2):
            p2=p2+1
        elif(i==3):
            p3=p3+1
        elif(i==4):
            p4=p4+1
        elif(i==4):
            p5=p5+1
        elif(i==5):
            p6=p6+1
        else:
            p7=p7+1


    labels = '2','3','4','5','6','7'
    sizes = [p2,p3,p4,p5,p6,p7]

    fig1,ax1 = plt.subplots()
    ax1.pie(sizes,labels = labels,autopct ='%1.1f%%',shadow=True,startangle=90)
    ax1.axis('equal')
    plt.title("Number of Projects Per Employee", bbox={'facecolor':'0.8', 'pad':5})


    plt.show()
    fig1.savefig('lin1.png', dpi=100)
    impLeftData.to_csv("aks5.csv")
    return not_data


## main stuff :
import pandas as pd
data1 = pd.read_csv(r'HR_Dataset.xls')


###########################################


mega(data1)



#you can use this ##########################
