from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils.translation import activate, get_language
from django.urls import reverse


class Home(View):
    template_name = "index.html"
    context = {}

    def get(self, request):
        products = Product.objects.all().order_by('id')
        self.context['products'] = products
        return render(request, self.template_name, context=self.context)


class ProductDetail(LoginRequiredMixin, View):
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
        product_info = ProductInfo.objects.get(product=product)
        print(product.address)
        self.context['product'] = product
        self.context['product_info'] = product_info
        return render(request, self.template_name, context=self.context)


    def post(self, request, pk):
        update_or_delete = request.POST.get('update_or_delete', None)

        if update_or_delete == 'update':
            address = request.POST.get('address', None)
            price = request.POST.get('price', None)
            image1 = request.POST.get('image1', None)
            image2 = request.POST.get('image2', None)
            image3 = request.POST.get('image3', None)
            image4 = request.POST.get('image4', None)
            image5 = request.POST.get('image5', None)
            description = request.POST.get('description', None)
            sale_rent = request.POST.get('sale_rent', None)

            product = Product.objects.get(pk=pk)

            if address:
                product.address = address
            if price:
                product.price = price
            if image1:
                product.image1 = image1
            if image2:
                product.image2 = image2
            if image3:
                product.image3 = image3
            if image4:
                product.image4 = image4
            if image5:
                product.image5 = image5
            if description:
                product.description = description
            if sale_rent:
                product.sale_rent = sale_rent
            product.save()

            return redirect(f'/product-detail/{pk}')
        else:
            Product.objects.get(pk=pk).delete()
            return redirect('/')


class About(View):
    template_name = 'about.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)


class Contact(View):
    template_name = 'contact.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)
    
    def post(self, request):

        full_name = request.POST.get('full_name', None)
        email = request.POST.get('email', None)
        subject = request.POST.get('subject', None)
        message = request.POST.get('message', None)

        msg = f"""
            From: {full_name}
            Email: {email}
            Message: {message}
        """

        send_mail(
            subject=subject,
            message=msg,
            from_email=email,
            recipient_list=['rahmetruslanov6797@gmail.com'],
            fail_silently=True
        )

        msg = Message.objects.create(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message
        )
        msg.save()

        return redirect('/contact')


def set_language(request):
    if request.method == 'POST':
        language = request.POST.get('language', None)
        if language:
            request.session[LANGUAGE_SESSION_KEY] = language
            activate(language)
        return redirect(request.META.get('HTTP_REFERER', reverse('home')))