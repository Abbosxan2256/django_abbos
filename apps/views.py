from django.shortcuts import render

from apps.models import Person


# x = 0
# y = 1000
#
#
# def index_view(request):
#     global x, y
#     x = 0
#     y = 1000
#     product = Product.objects.all()[0:y]
#     context = {
#         "category": product
#     }
#     return render(request, 'apps/index.html', context)
#
#
# def nxt_view(request):
#     global x, y
#     x += 1000
#     y += 1000
#     product_nxt = Product.objects.all()[x:y]
#     context = {
#         "product_nxt": product_nxt
#     }
#     return render(request, 'apps/next.html', context)
#
#
# def prv_view(request):
#     global x, y
#     x -= 1000
#     y -= 1000
#     print(x, y)
#     product_prv = Product.objects.all()[x:y]
#     context = {
#         'product_prv': product_prv
#     }
#     return render(request, 'apps/prv.html', context)
#
#
# def index_tables(request):
#     product_next = Product.objects.all()[:1]
#     prodct_next = Product.objects.all()[1:2]
#     prodt_next = Product.objects.all()[2:3]
#     context = {
#         'prd_next': product_next,
#         'prd_nxt': prodct_next,
#         'prodt_next': prodt_next
#     }
#     return render(request, 'apps/tablets/index_table.html', context)
#

def index_prc(requset):
    context = {
        'person': Person.objects.all()
    }
    return render(requset, 'apps/index_practs.html', context)
