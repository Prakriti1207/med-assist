from django.shortcuts import render
from django.http import JsonResponse
from . import pool
def Brand_Interface(request):
    return render(request,'BrandInterface.html')

def Submit_Interface(request):
    try:
        db,cmd=pool.ConnectionPooling()

        categoryid=request.POST['category_id']
        subcategoryid=request.POST['subcategory_id']
        brandname=request.POST['brand_name']
        contactperson=request.POST['contact_person']
        mobileno=request.POST['mobile_no']
        status=request.POST['status']
        brandlogo=request.FILES['brand_logo']
        q="insert into brand(categoryid,subcategoryid,brandname,contactperson,mobileno,status,brandlogo) values({0},{1},'{2}','{3}','{4}','{5}','{6}')".format(categoryid,subcategoryid,brandname,contactperson,mobileno,status,brandlogo.name)
        F=open("E:/SappalSir's_Folder/Django Projects/medassist_ecom/assets/"+brandlogo.name,'wb')
        for chunk in brandlogo.chunks():
            F.write(chunk)
        F.close()
        cmd.execute(q)
        db.commit()
        db.close()
        return render(request,"BrandInterface.html",{'message':'True'})
    except Exception as e:
        print("ERROR:",e)
        return render(request,"BrandInterface.html",{'message':'False'})


def DisplayRecords(request):
    try:
        db,cmd=pool.ConnectionPooling()
        q="select B.*,(select C.categoryname from categories C where C.categoryid=B.categoryid) as catname,(select S.subcategoryname from subcategories S where S.subcategoryid=B.subcategoryid) as subcatname from brand B"
        cmd.execute(q)
        records=cmd.fetchall()
        db.commit()
        db.close()
        return render(request,"DisplayBrand.html",{'records':records})
    except Exception as e:
        print("ERROR:",e)
        return render(request,"DisplayBrand.html")

def editRecord(request):
    try:
        db,cmd=pool.ConnectionPooling()
        brandid=request.GET['brandid']
        categoryid=request.GET['categoryid']
        subcategoryid=request.GET['subcategoryid']
        brandname=request.GET['brandname']
        brandperson=request.GET['brandperson']
        mobileno=request.GET['mobileno']
        status=request.GET['status']
        q="update brand set categoryid={0},subcategoryid={1},brandname='{2}',contactperson='{3}',mobileno='{4}',status='{5}' where brandid={6}".format(categoryid,subcategoryid,brandname,brandperson,mobileno,status,brandid)
        cmd.execute(q) 
        db.commit()
        db.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print("ERROR:",e)
        return JsonResponse({'result':False},safe=False)

def deleteRecord(request):
    try:
        db,cmd=pool.ConnectionPooling()
        brandid=request.GET['brandid']
        q='delete from brand where brandid={0}'.format(brandid)
        cmd.execute(q) 
        db.commit()
        db.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print("ERROR:",e)
        return JsonResponse({'result':False},safe=False)

def Edit_BrandIcon(request):
    try:
        DB,CMD=pool.ConnectionPooling()
        brandid=request.POST['brandid']
        brandicon=request.FILES['brandlogo']
        q="update brand set brandlogo='{0}' where brandid={1}".format(brandicon.name,brandid)
        F=open("E:/SappalSir's_Folder/Django Projects/medassist_ecom/assets/"+brandicon.name,'wb')
        for chunk in brandicon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(q)
        DB.commit()
        DB.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print("Error:",e)
        return JsonResponse({'result':False},safe=False)

def fetch_All_Brand_Json(request):
    try:
        db,cmd=pool.ConnectionPooling()
        subcategoryid=request.GET['subcategoryid']
        q="select * from brand where subcategoryid={0}".format(subcategoryid) 
        cmd.execute(q)
        records=cmd.fetchall() 
        db.close()
        return JsonResponse({'data':records},safe=False)
    except Exception as e:
        print("ERROR:",e)
        return JsonResponse({'data':None},safe=False)





