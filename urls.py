"""medassist_ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cmath import log
from django.contrib import admin
from django.urls import path
from . import Category_Controller
from . import SubCategory_Controller
from . import Brand_Controller
from . import Product_Controller
from . import Dashboard_Controller
from . import LoginPage_Controller
urlpatterns = [
    path('admin/', admin.site.urls),


    path('categoryinterface/',Category_Controller.Category_Interface),
    path('submitcategory',Category_Controller.Submit_Category),
    path('displaycategory/', Category_Controller.DisplayAllRecords),
    path('editcategory/', Category_Controller.Edit_Category),
    path('deletecategory/', Category_Controller.Delete_Category),
    path('editcategoryicon', Category_Controller.Edit_CategoryIcon),
    path('fetch_all_category_json/', Category_Controller.Fetch_All_Category_JSON),


    path('subcategoryinterface/',SubCategory_Controller.SubCategory_Interface),
    path('submitsubcategory',SubCategory_Controller.Submit_SubCategory),
    path('displaysubcategory/',SubCategory_Controller.display_SubCategory),
    path('editsubcategory/',SubCategory_Controller.edit_SubCategory),
    path('deletesubcategory/',SubCategory_Controller.delete_SubCategory),
    path('editsubcategoryicon',SubCategory_Controller.Edit_SubCategoryIcon),
    path('fetch_all_subcategory_json/',SubCategory_Controller.Fetch_All_Sub_Category_JSON),




    path('brandinterface/',Brand_Controller.Brand_Interface),
    path('submitbrand',Brand_Controller.Submit_Interface),
    path('displaybrand/',Brand_Controller.DisplayRecords),
    path('editbrand/',Brand_Controller.editRecord),
    path('deletebrand/',Brand_Controller.deleteRecord),
    path('editbrandicon',Brand_Controller.Edit_BrandIcon),
    path('fetch_all_brand_json/', Brand_Controller.fetch_All_Brand_Json),




    path('productinterface/',Product_Controller.Product_Interface),
    path('submitproduct',Product_Controller.Submit_Product),
    path('displayproduct/',Product_Controller.Display_Products),
    path('editproduct/',Product_Controller.Edit_Products),
    path('deleteproduct/',Product_Controller.Delete_Products),
    path('deleteproduct/',Product_Controller.Delete_Products),
    path('editproductimage',Product_Controller.Edit_Product_Image),


    path('dashboard/',Dashboard_Controller.display_Dashboard),


    path('loginpage/',LoginPage_Controller.LoginPage),
    path('checklogin',LoginPage_Controller.CheckLogin),


]
