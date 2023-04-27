from django.shortcuts import render
from .models import *
from django.views import View


class Home(View):
    template_name = "index.html"
    context = {}

    def get(self, request):
        products = Product.objects.all().order_by('id')
        self.context['products'] = products
        return render(request, self.template_name, context=self.context)


class ProductDetail(View):
    template_name = 'single.html'
    context = {}

    def get(self, request, pk):
        if not (request.user.is_authenticated and UserProductView.objects.filter(Q(product_id=pk), Q(user=request.user)).exists()):
            user_product_view = UserProductView.objects.create(
                product_id = pk,
                user = request.user
            )
            user_product_view.save()
        product = Product.objects.get(pk=pk)
        self.context['product'] = product
        return render(request, self.template_name, context=self.context)