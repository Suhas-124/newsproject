from django.shortcuts import render

# Create your views here.
def homepage(request):
    msg="Welcome to Suhas App"
    return render(request,'newsapp/home.html',{'msg':msg})

def movies_info(request):
    mv1='Pusha Grand Blockbouster'
    mv2='RRR Full Range Promotions'
    mv3='Bheemla Nayak Postponed'
    return render(request,'newsapp/movies.html',{'mv1':mv1,'mv2':mv2,'mv3':mv3})

def sports_info(request):
    sp1='India Take on SA'
    sp2='Auseis Take This Ashes in Style'
    sp3='Kohli Scores a Brilliant Century'
    return render(request,'newsapp/sports.html',{'sp1':sp1,'sp2':sp2,'sp3':sp3})


def politics_info(request):
    p1='Night Curfew imposed in Karnataka'
    p2='BJP Karnataka Passes Anti Conversion Bill'
    p3='Congress in Deep Trouble'
    return render(request,'newsapp/politics.html',{'p1':p1,'p2':p2,'p3':p3})        
