
from django.shortcuts import render,redirect
from django.contrib import messages
import pandas as pd
from base.models import Data

# render home template.
def home(request):
    return render(request, 'base/home.html')

#To upload a CSV data and all data import in app models
def upload_csv(request):
    template = "base/home.html"
    #check if method is get
    if request.method == 'GET':
        return render(request, template)

    #here we pick csv file on aire
    csv_file = request.FILES['file']
    #check if file is not .csv then a message error show on templates
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This is not a csv file! please upload a .csv file.")
        return render(request,template)
    #read csv with pandas
    df = pd.read_csv(csv_file)
    for NAME,OBJECTS,TIMESTAMP in zip(df.image_name, df.objects_detected, df.timestamp):
        models = Data(image_name=NAME, objects_detected=OBJECTS,timestamp=TIMESTAMP)
        models.save()
    messages.success(request, "Successfully uploaded")
    return render(request, template)

#to Fatch the data between dates and export a report.csv
def fatch_data(request):
    template = "base/home.html"
    #check method in get return to templates
    if request.method == 'GET':
        return render(request, template)

    #if method is post the perform
    if request.method == 'POST':
        #get data from form in html template
        start_date = request.POST['from-datepicker']
        end_date = request.POST['from-datepickerend']
        #perform a query on sqplite database
        all_datas = Data.objects.filter(timestamp__range=(start_date,end_date))
        #check if data in null
        if not all_datas:
            #A Message show on templates
            #use django template messages feature
            messages.error(request, f"No data available between{start_date} and {end_date}")
            return redirect(home)
        else:
            #createing a empty dictonery
            dic = {}
            #use loop in query set data
            for data in all_datas:
                #store values in obj variable
                obj = data.objects_detected
                #create all data into strings
                obj=str(obj)
                #split word with ,
                obj_list=obj.split(",")
                #again run loop to store all the data in dictnery
                for i in obj_list:
                    if i in dic:
                        dic[i]+=1
                    else:
                        dic[i]=1
                #report save in project folder
                (pd.DataFrame.from_dict(data=dic, orient='index').to_csv('report.csv', header=False))
            #fatch query value in context
            context = {'all_datas':all_datas}
            return render(request, 'base/home.html',context)




        
            
            


