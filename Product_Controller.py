from django.shortcuts import render
from . import pool
from django.http import JsonResponse

def Product_Interface(request):
    return render(request,"ProductsInterface.html")

def Submit_Product(request):
    try:
        db,cmd=pool.ConnectionPooling()
        categoryname=request.POST['category_name']
        subcategoryname=request.POST['subcategory_name']
        brandname=request.POST['brand_name']
        productname=request.POST['product_name']
        productprice=request.POST['product_price']
        offerprice=request.POST['offer_price']
        packingtype=request.POST['packing_type']
        quantity=request.POST['qty']
        status=request.POST['product_status']
        rating=request.POST['rate']
        salestatus=request.POST['sale_status']
        image=request.FILES['product_image']
        q="insert into products(categoryid,subcategoryid,brandid,productname,price,offerprice,packingtype,quantity,productimage,statuss,rating,salestatus) values({0},{1},{2},'{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')".format(categoryname,subcategoryname,brandname,productname,productprice,offerprice,packingtype,quantity,image.name,status,rating,salestatus)
    
        F=open("E:/SappalSir's_Folder/Django Projects/medassist_ecom/assets/"+image.name,'wb')
        for chunk in image.chunks():
             F.write(chunk)
        F.close()
        cmd.execute(q) 
        db.commit()
        db.close()
        return render(request,"ProductsInterface.html",{'message':'True'})
    except Exception as e:
        print("Error:",e)
        return render(request, "ProductsInterface.html", {'message':'False'})
    
def Display_Products(request):
      try:
        db,cmd=pool.ConnectionPooling()
        q='select P.*,(select categoryname from categories C where C.categoryid=P.categoryid) as catname,(select subcategoryname from subcategories S where S.subcategoryid=P.subcategoryid) as subcatname,(select brandname from brand B where B.brandid=P.brandid) as brandname from products P'
         
        cmd.execute(q)
        record=cmd.fetchall() 
        db.close()
        return render(request,"DisplayProducts.html",{'records':record})
      except Exception as e:
        print('ERROR:',e)
        return render(request,"DisplayProducts.html",{'records':record})

def Edit_Products(request):
    try:
      db,cmd=pool.ConnectionPooling()
      productid=request.GET['productid']
      categoryid=request.GET['categoryid']
      subcategoryid=request.GET['subcategoryid']
      brandid=request.GET['brandid']
      productname=request.GET['productname']
      price=request.GET['price']
      offerprice=request.GET['offerprice']
      packingtype=request.GET['packingtype']
      quantity=request.GET['quantity']
      status=request.GET['status']
      rating=request.GET['rating']
      salestatus=request.GET['salestatus']

      q="update products set categoryid={0},subcategoryid={1},brandid={2},productname='{3}',price='{4}',offerprice='{5}',packingtype='{6}',quantity='{7}',statuss='{8}',rating='{9}',salestatus='{10}' where productid={11}".format(categoryid,subcategoryid,brandid,productname,price,offerprice,packingtype,quantity,status,rating,salestatus,productid)
      cmd.execute(q) 
      db.commit()
      print(q)
      db.close()
      return JsonResponse({'result':"True"},safe=False)
    except Exception as e:
        print('ERROR:',e)
        return JsonResponse({'result':"False"},safe=False)

def Delete_Products(request):
    try:
        db,cmd=pool.ConnectionPooling()
        productid=request.GET['productid']
        q="delete from products where productid={0}".format(productid)
        cmd.execute(q) 
        db.commit()
        db.close()
        return JsonResponse({'result':"True"},safe=False)
    except Exception as e:
        print('ERROR:',e)
        return JsonResponse({'result':'False'},safe=False)

def Edit_Product_Image(request):
    try:
        db,cmd=pool.ConnectionPooling()
        productid=request.POST['productid']
        productimage=request.FILES['productimage']
        q="update products set productimage='{0}' where productid={1}".format(productimage.name,productid)
        F=open("E:/SappalSir's_Folder/Django Projects/medassist_ecom/assets/"+productimage.name,"wb")
        for chunk in productimage.chunks():
            F.write(chunk)
        F.close()
        cmd.execute(q) 
        db.commit()
        db.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('ERROR:',e)
        return JsonResponse({'result':False},safe=False)

        




