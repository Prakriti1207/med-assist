from django.shortcuts import render,redirect
from . import pool
from django.http import JsonResponse
def Category_Interface(request):

    return render(request,"CategoryInterface.html")


def Submit_Category(request):
    try:
        DB,CMD=pool.ConnectionPooling()
        categoryname=request.POST['category_name']
        categoryicon=request.FILES['category_icon']
        q="insert into categories(categoryname,categoryicon) values('{0}','{1}')".format(categoryname,categoryicon.name)
        F=open("E:/SappalSir's_Folder/Django Projects/medassist_ecom/assets/"+categoryicon.name,'wb')
        for chunk in categoryicon.chunks():
             F.write(chunk)
        F.close()
        CMD.execute(q)
        DB.commit()
        DB.close()
        return render(request,"CategoryInterface.html",{'message':'True'})
    except Exception as e:
        print("Error:",e)
        return render(request, "CategoryInterface.html", {'message':'False'})


def Edit_Category(request):
    try:
        DB,CMD=pool.ConnectionPooling()
        categoryname=request.GET['categoryname']
        categoryid=request.GET['categoryid']
        q="update categories set categoryname='{0}' where categoryid={1}".format(categoryname,categoryid)
        CMD.execute(q)
        DB.commit()
        DB.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print("Error:",e)
        return JsonResponse({'result':False},safe=False)


def Delete_Category(request):
    try:
        DB,CMD=pool.ConnectionPooling()
        categoryid=request.GET['categoryid']
        q="delete from categories where categoryid={0}".format(categoryid)
        CMD.execute(q)
        DB.commit()
        DB.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print("Error:",e)
        return JsonResponse({'result':False},safe=False)



def DisplayAllRecords(request):
    try:
        db,cmd=pool.ConnectionPooling()
        q="select * from categories"
        cmd.execute(q)
        records=cmd.fetchall()
        db.close()
        return render(request,"DisplayCategory.html",{'records':records})


    except Exception as e:
        print('Error:',e)
        return render(request,"DisplayCategory.html")


def Edit_CategoryIcon(request):
    try:
        DB,CMD=pool.ConnectionPooling()
        categoryid=request.POST['categoryid']
        categoryicon=request.FILES['categoryicon']
        q="update categories set categoryicon='{0}' where categoryid={1}".format(categoryicon.name,categoryid)
        F=open("E:/SappalSir's_Folder/Django Projects/medassist_ecom/assets/"+categoryicon.name,'wb')
        for chunk in categoryicon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(q)
        DB.commit()
        DB.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print("Error:",e)
        return JsonResponse({'result':False},safe=False)


def Fetch_All_Category_JSON(request):
    try:
        db,cmd=pool.ConnectionPooling()
        q="select * from categories"
        cmd.execute(q)
        records=cmd.fetchall()
        db.close()
        return JsonResponse({'data':records},safe=False)
    except Exception as e:
        print('Error:',e)
        return JsonResponse({'data':records},safe=False)

