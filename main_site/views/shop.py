from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from ..forms import ShopCreateForm, BookForm
from ..models import Shop, Booking

import datetime

class ShopCreateView(View):
    template_name = 'create.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = ShopCreateForm

        if request.user.is_authenticated:
            return render(request, self.template_name, self.context)
        else:
            return redirect('login')

    def post(self, request, *args, **kwargs):
        form = ShopCreateForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['shop_name']

            if Shop.objects.filter(shop_name=name).exists():
                messages.info(request, 'Shop Exists.')

                return redirect('/create')

            else:
                description = form.cleaned_data['shop_description']
                shop_user = request.user

                new_shop = Shop(shop_name=name, shop_description=description, shop_owner=shop_user)
                new_shop.save()

                return redirect('shop')
        
        else:
            return redirect('/create')

class ShopView(View):
    template_name = 'shop.html'
    context = {}

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            shop_list = Shop.objects.all()

            if len(shop_list) <= 3:
                self.context['edgecase'] = True
                self.context['shop_list'] = shop_list
            else:
                self.context['edgecase'] = False

                np_arr = []
                count = 0
                while count <= len(shop_list):
                    if count + 3 > len(shop_list) - 1:
                        np_arr.append(shop_list[count:len(shop_list)])
                        break
                    else:
                        np_arr.append(shop_list[count:count+3])
                        count += 3

                self.context['shop_list'] = np_arr
                print(np_arr)

            return render(request, self.template_name, self.context)
        else:
            return redirect('/logout')

    def post(self, request, *args, **kwargs):
        obj_id = request.POST['obj_id']

        # delete the booking
        Shop.objects.filter(id=obj_id).delete()

        return redirect('shop')

class BookView(View):
    template_name = 'book.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['pid'] = self.kwargs['pid']

        if request.user.is_authenticated:
            return render(request, self.template_name, self.context)
        else:
            return redirect('/login')
    
    def post(self, request, *args, **kwargs):

        success_template = 'book_success.html'

        shop_id = self.kwargs['pid']
        shop = Shop.objects.get(id=shop_id)
        
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        status = 'PENDING'

        new_booking = Booking.objects.create(booker=request.user, shop=shop, \
                                    address=address, status=status, \
                                        phone_number=phone_number)


        cnxt = {}
        cnxt['address'] = address
        cnxt['phone_num'] = phone_number
        cnxt['shop_name'] = shop.shop_name

        return render(request, success_template, cnxt)

class ShopBookingTable:
    def __init__(self, shop_name, bookings):
        self.shop_name = shop_name
        self.bookings = bookings

class BookingsView(View):
    template_name = 'bookings.html'

    def get(self, request, *args, **kwargs):
        context = {}

        user = request.user

        if user.is_authenticated:
            final_booking_list = []
            shops_owned = Shop.objects.filter(shop_owner=user)

            for each_shop in shops_owned:
                queryset = Booking.objects.filter(shop=each_shop, status='PENDING')
                ShopBookObj = ShopBookingTable(each_shop.shop_name, queryset)
                final_booking_list.append(ShopBookObj)

            context['final_list'] = final_booking_list

            return render(request, self.template_name, context)
        else:
            return redirect('/login')

    def post(self, request, *args, **kwargs):
        book_id = request.POST['bookid']

        # delete the booking
        Booking.objects.filter(id=book_id).delete()

        return redirect('bookings')
