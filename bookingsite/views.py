from django.shortcuts import render
from django.views.generic import TemplateView
from bookingsite.models import Hotel,Customer
from .form import CreateHotelForm,HomeForm,CreateBookingForm

class Homeview(TemplateView):
    template_name = 'test.html'
    temp_array = ["","","","",""]
    def get(self,request):
        if request.method =="GET" :
            people = request.GET.get('people')
            self.temp_array[0] = people
            room = request.GET.get('room')
            self.temp_array[1] = room
            district = request.GET.get('district')
            self.temp_array[2] = district
            checkinDay = request.GET.get('checkinDay')
            self.temp_array[3] = checkinDay
            checkoutDay = request.GET.get('checkoutDay')
            self.temp_array[4] = checkoutDay
            hotels = Hotel.objects.all().order_by('name')
            #lay gia tri cua 1 tag co name= people
            args = {'people':people,'room':room,'district':district,'checkinDay':checkinDay,'checkoutDay':checkoutDay,
            'hotels':hotels
            }
            return render(request,self.template_name,args)
        return render(request,self.template_name,{})
    def post(self,request):
        if request.method =="POST":
            name = request.POST.get('name')
            customer_id = request.POST.get('ID')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            inputAddress = request.POST.get('inputAddress')
            hotel = request.POST.get('hotel')
            district = request.GET.get('district')
            if len(self.temp_array) ==5:
                people = self.temp_array[0]
                room = self.temp_array[1]
                district = self.temp_array[2]
                checkInDay = self.temp_array[3]
                checkOutDay = self.temp_array[4]
                form = CreateBookingForm()
                newBooking = form.save(commit=False)
                newBooking.people = people
                newBooking.room = room
                newBooking.checkinday = checkInDay
                newBooking.checkoutday = checkOutDay
                newBooking.name = name
                newBooking.id_number = customer_id
                newBooking.email = email
                newBooking.phone = phone
                newBooking.current_address = inputAddress
                newBooking.hotel_name = hotel
                newBooking.save()
            hotels = Hotel.objects.all().order_by('name')
            

        return render(request,self.template_name,{})
