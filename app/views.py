from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin


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


class About(LoginRequiredMixin, View):
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