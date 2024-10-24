from django.shortcuts import render
from django.http import HttpResponse
# Create your tests here.
def func1(request):
    d={'movies':[{'name1':'Rockstar','year1':2011,'director1':'Imtiaz Ali','rating1':8,'genre1':'Melodrama'},
                 {'name2':'Aashiqui2','year2':2013,'director2':'Mohit Suri','rating2':7,'genre2':'Drama'},
                 {'name3':'Sanam Teri Kasam','year3':2016,'director3':'Radhika Roa','rating3':8,'genre3':'Romance'},
                 {'name4':'Yeh Jawaani Hai Dewaane','year4':2013,'director4':'Ayan Mukarji','rating4':7,'genre4':'Comedy'},
                 {'name5':'Ajab Prem Ki Ghazab Kahani','year5':2009,'director5':'Rajkumar Santhoshi','rating5':6,'genre5':'Action'}
 ]
    }
    return render(request,'joy.html',d)

