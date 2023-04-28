from django.shortcuts import render

# Create your views here.

def Built_in_filters(request):
    import datetime
    date=datetime.datetime.now()
    d={'data':'''Mahendra Singh Dhoni,commonly known as MS Dhoni, 
                is a former Indian cricketer and captain of the Indian 
                national team in limited-overs formats from 2007 to 2017 
                and in Test cricket from 2008 to 2014, who plays as a Wicket-keeper-Batsman.''', 'date':date, 'Count':2}
    
    return render(request, 'Built_in_filters.html', d)
