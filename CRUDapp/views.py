
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from CRUDapp.forms import productFrom
from CRUDapp.models import Produtc, Delete

#urls 
#list_produtcs create_produtcts update_products delete_produtcts 

# Create your views here.
def insert_products(request):
  data = {}
  data['form'] = productFrom()
  return render( request , 'form.html' , data )

def list_products(request): 
  data = {  }
  data ['db'] = Produtc.objects.all()
  return render( request , 'index.html' , data)

def  dethalis_product( request , pk ):
  data = {}
  data['db'] = Produtc.objects.get(pk=pk)
  return render(request , 'dethalis.html' , data )


def edit_products (request , pk ):

  data = { }
  data['db'] = Produtc.objects.get(pk=pk)
  data['form'] = productFrom(instance=data['db'])
  return render( request , 'form.html' , data )

def update_products(request , pk):

  data  = { }
  data['db'] = Produtc.objects.get(pk=pk)
  form = productFrom(request.POST or None, instance=data['db'])
  if form.is_valid():
    form.save()
  return redirect('success')


def delete_products(request , pk ): 

  db= Produtc.objects.get(pk=pk)
  Data = Delete( pk , db.getName(), db.getProduct() , db.getInventory() )
  Data.save()
  db.delete()
  return redirect('success')

def  create_products(request):
  form = productFrom(request.POST or None)
  if form.is_valid( ):
    form.save( )
  return  redirect('success')



def list_products_delete( request ):
  data = {}
  data ['db'] = Delete.objects.all()
  return render( request  , 'listDelete.html' , data )


def success_page( request ) :
  return render( request, 'success_page.html')
