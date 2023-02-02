from django.shortcuts import render, redirect

from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):

    template = 'catalog.html'

    key = request.GET.get('sort',None)

    order_key_val = {'name': 'name', 'max_price': '-price', 'min_price': 'price'}

    phones_object = Phone.objects.order_by(order_key_val[key]) if key != None else Phone.objects.all()
    
    phones = [{'name':c.name, 
               'price': c.price,
               'image': c.image,
               'slug': c.slug,

            } for c in phones_object]

    context = {
              'phones': phones,

              }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phones_object = Phone.objects.filter(slug=slug)

    for c in phones_object:
        phone = {
        'name':c.name, 
        'price': c.price,
        'image': c.image,
        'release_date': c.release_date,
        'lte_exists': c.lte_exists,
        }

    print(phone)

    context = { 
            'phone': phone,
            }



    return render(request, template, context)
