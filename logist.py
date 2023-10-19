

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
    if row['average_montly_hours']>avg_monthlyHours and row['salary']==1:
        reason.append(6)
    return reason



def mega(data): 
    #import all the necessary libraries

    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import confusion_matrix, accuracy_score
    







    #import warnings to ignore warnings
    import warnings
    warnings.filterwarnings('ignore')





    #Read the file
    #data1 = pd.read_csv(r'HR_Dataset.xls')
    #data = pd.read_csv(r'HR_Dataset.xls')
    #data.head(4)

    data1=data





    # Encoding Catogorical Columns (Since we have Catagorical column values )
    # 
    # ###########
    # IMP : in the dummies line try taking drop_first off and check accuracy
    # ###########




    # data = pd.get_dummies(data, columns = ['Departments ','salary'])
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




    #Implementing Logistic Regression using sklearn
    model=LogisticRegression()
    model.fit(x_train,y_train)


    # Model Evaluation 




    y_pred = model.predict(x_test)


    y_intercept=model.intercept_
    y_coefficient=model.coef_







    ConfusionMatrix = confusion_matrix(y_test, y_pred)
    




    #x_train.loc[3452,'satisfaction_level']

    y_train.head(5)



    size = len(data)
    

    perc = np.zeros(14999)

    for i in range(size):
        #res =(-0.51325937)-(4.17147337e+00)*(data.loc[i,'satisfaction_level'])+(6.44669928e-02)*(data.loc[i,'last_evaluation'])-(2.82734065e-01)*(data.loc[i,'number_project'])+(3.99991093e-03)*(data.loc[i,'average_montly_hours'])+(2.64838262e-01)*(data.loc[i,'time_spend_company'])-(1.74537427e+00)*(data.loc[i,'Work_accident'])-(6.62230222e-01)*(data.loc[i,'promotion_last_5years'])-(5.43260596e-01)*(data.loc[i,'Departments _RandD'])+(8.65754982e-02)*(data.loc[i,'Departments _accounting'])+(3.20189394e-01)*(data.loc[i,'Departments _hr'])-(6.61176215e-01)*(data.loc[i,'Departments _management'])+(3.89593078e-02)*(data.loc[i,'Departments _marketing'])+(2.00472926e-02)*(data.loc[i,'Departments _product_mng'])+(1.09441711e-01)*(data.loc[i,'Departments _sales'])+(1.58208240e-01)*(data.loc[i,'Departments _support'])+(1.62719089e-01)*(data.loc[i,'Departments _technical'])+(1.35397941e+00)*(data.loc[i,'salary_low'])+(8.01593685e-01)*(data.loc[i,'salary_medium'])
        #res =(-0.59143995)-(4.13222786)*(data.loc[i,'satisfaction_level'])+(0.15148958)*(data.loc[i,'last_evaluation'])-0.28796745*(data.loc[i,'number_project'])+(0.00415672)*(data.loc[i,'average_montly_hours'])+(0.24258173)*(data.loc[i,'time_spend_company'])-1.70204427*(data.loc[i,'Work_accident'])-0.65774787*(data.loc[i,'promotion_last_5years'])-0.58958349*(data.loc[i,'Departments _RandD'])+(0.08908541)*(data.loc[i,'Departments _accounting'])+(0.27885606)*(data.loc[i,'Departments _hr'])-0.62343821*(data.loc[i,'Departments _management'])+(0.0095753)*(data.loc[i,'Departments _marketing'])+(0.01166724)*(data.loc[i,'Departments _product_mng'])+(0.05417304)*(data.loc[i,'Departments _sales'])+(0.28066013)*(data.loc[i,'Departments _support'])+(0.24499242)*(data.loc[i,'Departments _technical'])+(1.37440331)*(data.loc[i,'salary_low'])+(0.80729629)*(data.loc[i,'salary_medium'])

        res = y_intercept + y_coefficient[0][0]*(data.loc[i,'satisfaction_level'])+y_coefficient[0][1]*(data.loc[i,'last_evaluation'])+y_coefficient[0][2]*(data.loc[i,'number_project'])+y_coefficient[0][3]*(data.loc[i,'average_montly_hours'])+y_coefficient[0][4]*(data.loc[i,'time_spend_company'])+y_coefficient[0][5]*(data.loc[i,'Work_accident'])+y_coefficient[0][6]*(data.loc[i,'promotion_last_5years'])+y_coefficient[0][7]*(data.loc[i,'Departments '])+y_coefficient[0][8]*(data.loc[i,'salary'])

        value=1/(1+ 2.71828**(-res))
        perc[i]=value





    perc.max()




    please =np.zeros(size)
    for i in range(size):
        if(perc[i]>=0.5):
            please[i]=1
        else:
            please[i]=0







    please





    ConfusionMatrix = confusion_matrix(y,please)
    




    data_new = data

    data_new['odds'] = perc.tolist()
    




    # Solution Functions 
    # 
    # satisfaction level of below 0.2 and last evaluation of 0.8 and above are likely to leave. (Intense Workload) also salary can be a factor .
    # 
    # 




    #taking all rows with left ==1
    left_data = data_new.loc[data_new['left'] == 1]
    left_data = left_data.sort_values(by='odds',ascending =False)

    not_data = data_new.loc[data_new['left'] == 0]
    not_data = not_data.sort_values(by='odds',ascending =False)

    # data_new = data_new.sort_values(by = 'odds',ascending=False)
    









    



    avg_numberOfProjects = np.average(data_new['number_project'])
    avg_monthlyHours = np.average(data_new['average_montly_hours'])


    left_data['reason']=left_data.apply(solutions,axis=1,args=(avg_monthlyHours,avg_numberOfProjects))

    not_data['reason']=not_data.apply(solutions,axis=1,args=(avg_monthlyHours,avg_numberOfProjects))

    data_new['reason']=data_new.apply(solutions,axis=1,args=(avg_monthlyHours,avg_numberOfProjects))







    # ################################# Required Mapping #######################################
    # 
    # 
    # (EmpID -->odds --> reasons )




    # impLeftData = data_new.loc[:,['Emp_ID','odds','reason']]

    impLeftData= data_new
    


    # **Data Visualisation**


    ###  Pie Chart of the people who leave v/s wo dont

    left =0
    not_left = 0
    for i in data1['left']:
        if(i==1):
            left=left+1
        else:
            not_left=not_left+1


    labels = 'left','not left'
    sizes = [left,not_left]
    explode = (0.1,0)

    fig0,ax1 = plt.subplots()
    ax1.pie(sizes,explode=explode,labels = labels,autopct ='%1.1f%%',shadow=True,startangle=90)
    plt.title("Employees Left v/s Employees not Left", bbox={'facecolor':'0.8', 'pad':5})


    # plt.show()
    fig0.savefig('Employees Left vs Employees not Left.png', dpi=100)
    
    fig4 = sns.catplot(data=data,kind = 'count',x ='left',col='Departments ')
    fig4.savefig('DEPARTMENTS VS LEFT',dpi = 100)

    fig5=sns.catplot(data=data,kind='count',x='left',col='number_project')
    fig5.savefig('number_project VS LEFT', dpi=100)

    # fig,ax = plt.subplots(4,2, figsize=(9,9))                
    # sns.distplot(data['satisfaction_level'], ax = ax[0,0]) 
    # sns.distplot(data['last_evaluation'], ax = ax[0,1]) 
    # sns.distplot(data['number_project'], ax = ax[1,0]) 
    # sns.distplot(data['average_montly_hours'], ax = ax[1,1]) 
    # sns.distplot(data['time_spend_company'], ax = ax[2,0]) 
    # sns.distplot(data['left'], ax = ax[2,1]) 
    # sns.distplot(data['promotion_last_5years'], ax = ax[3,0]) 
    # fig6 = plt.tight_layout()
    # fig6.savefig('REPRESENTATION OF ATTRIBUTES', dpi=100)

    fig6,axss = plt.subplots(2,2, figsize=[15,10])
    sns.countplot(x='left', hue='time_spend_company', data=data, ax=axss[0][0])
    sns.countplot(x='left', hue='promotion_last_5years', data=data, ax=axss[0][1]) 
    sns.countplot(x='left',hue= 'satisfaction_level',data=data, ax=axss[1][0]) 
    sns.countplot(x='left',hue= 'number_project',data=data, ax=axss[1][1])
    fig6.savefig('atrributes vs left', dpi=100)


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


    # plt.show()
    fig1.savefig('Number of Projects Per Employee.png', dpi=100)

    df2 = data_new
    impLeftData["odds"] = df2["odds"].tolist()

    impLeftData['salary'].replace(0,'low',inplace=True)
    impLeftData['salary'].replace(1,'medium',inplace=True)
    impLeftData['salary'].replace(2,'high',inplace=True)
    impLeftData['Departments '].replace(0,'IT',inplace=True)
    impLeftData['Departments '].replace(1,'hr',inplace=True)
    impLeftData['Departments '].replace(2,'management',inplace=True)
    impLeftData['Departments '].replace(3,'marketing',inplace=True)
    impLeftData['Departments '].replace(4,'product_mng',inplace=True)
    impLeftData['Departments '].replace(5,'sales',inplace=True)
    impLeftData['Departments '].replace(6,'support',inplace=True)
    impLeftData['Departments '].replace(7,'technical',inplace=True)
    impLeftData['Departments '].replace(8,'RandD',inplace=True)
    impLeftData['Departments '].replace(9,'accounting',inplace=True)

    return impLeftData


## main stuff :
import pandas as pd
data1 = pd.read_csv(r'HR_Dataset.xls')


###########################################


print(mega(data1))



#you can use this ##########################








