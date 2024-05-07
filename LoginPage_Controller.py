from django.shortcuts import render
from . import pool

def LoginPage(request):
    return render(request,"LoginPage.html")

def CheckLogin(request):
    try:
        db,cmd=pool.ConnectionPooling()
        emailid=request.POST['emailid'] 
        mobileno=request.POST['emailid'] 
        password=request.POST['password']
        q="select * from admins where (emailid='{0}'or mobileno='{1}') and passwords='{2}'".format(emailid,mobileno,password)
        cmd.execute(q) 
        records=cmd.fetchall() 
        db.close()
        if(records):
            return render(request,"Dashboard.html",{'record':records})
        else:
            return render(request,"LoginPage.html",{"message":'Incorrect emailid/mobileno/password...'})
    except Exception as e:
        print('ERROR:',e)
        return render(request,"LoginPage.html",{'message':"Server Error!"})
 

      