from django.shortcuts import render
from . import pool
from django.http import JsonResponse
def SubCategory_Interface(request):
    return render(request,'SubCategoryInterface.html')


def Submit_SubCategory(request):
  try:
    db,cmd=pool.ConnectionPooling()
    categoryid=request.POST['category_id']
    subcategoryname=request.POST['subcategory_name']
    subcategoryicon=request.FILES['subcategory_icon']
    q="insert into subcategories(categoryid,subcategoryname,subcategoryicon) values('{0}','{1}','{2}')".format(categoryid,subcategoryname,subcategoryicon.name)
    F=open("E:/SappalSir's_Folder/Django Projects/medassist_ecom/assets/"+subcategoryicon.name,'wb')
    for chunk in subcategoryicon.chunks():
        F.write(chunk)
    F.close()
    cmd.execute(q)
    db.commit()
    db.close()
    return render(request,"SubCategoryInterface.html",{'message':'True'})
  except Exception as e:
      print('Error:',e)
      return render(request,"SubCategoryInterface.html",{'message':'False'})


def display_SubCategory(request):
    try:
        db,cmd=pool.ConnectionPooling()
        q='select SUB.*,(select C.categoryname from categories C where C.categoryid=SUB.categoryid) as cname from subcategories SUB'
        cmd.execute(q) 
        records=cmd.fetchall() 
        db.close()
        return render(request,'DisplaySubCategory.html',{'records':records})
    except Exception as e:
        print('ERROR:',e)
        return render(request,"DisplaySubCategory.html")

def edit_SubCategory(request):
    try:
        db,cmd=pool.ConnectionPooling()
        categoryid=request.GET['categoryid']
        subcategoryid=request.GET['subcategoryid']
        subcategoryname=request.GET['subcategoryname']
        print(subcategoryid)
        q="update subcategories set categoryid={0},subcategoryname='{1}' where subcategoryid={2}".format(categoryid,subcategoryname,subcategoryid)
        cmd.execute(q)
        print(q)
        db.commit()
        db.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print("ERROR:",e)
        return JsonResponse({'result':False},safe=False)

def delete_SubCategory(request):
    try:
        db,cmd=pool.ConnectionPooling()
        subcategoryid=request.GET['subcategoryid']
        q='delete from subcategories where subcategoryid={0}'.format(subcategoryid)
        cmd.execute(q)
        db.commit()
        db.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print("ERROR:",e)
        return JsonResponse({'result':False},safe=False)


def Edit_SubCategoryIcon(request):
    try:
        DB,CMD=pool.ConnectionPooling()
        subcategoryid=request.POST['subcategoryid']
        subcategoryicon=request.FILES['subcategoryicon']
        q="update subcategories set subcategoryicon='{0}' where subcategoryid={1}".format(subcategoryicon.name,subcategoryid)
        F=open("E:/SappalSir's_Folder/Django Projects/medassist_ecom/assets/"+subcategoryicon.name,'wb')
        for chunk in subcategoryicon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(q)
        DB.commit()
        DB.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print("Error:",e)
        return JsonResponse({'result':False},safe=False)



def Fetch_All_Sub_Category_JSON(request):
    try:
        db,cmd=pool.ConnectionPooling()
        categoryid=request.GET['categoryid']
        q="select * from subcategories where categoryid={0}".format(categoryid)
        cmd.execute(q)
        records=cmd.fetchall()
        db.close()
        return JsonResponse({'data':records},safe=False)
    except Exception as e:
        print('Error:',e)
        return JsonResponse({'data':records},safe=False)









