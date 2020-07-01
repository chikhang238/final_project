from django.shortcuts import render
from django.views.generic import TemplateView
from bookingsite.models import Hotel,Customer
from .form import CreateHotelForm,HomeForm,CreateBookingForm
# Create your views here.
# def homepage(request):
#     a = request.POST.get('drop1')
## lay gia tri dc cua droplist
#     print(a)
#     hotels = Hotel.objects.all().order_by('name')
#     return render(request,'booking.html',{'hotels':hotels})

# def homepage(request):
#     return render(request,'booking.html',{})
# class Homeview(TemplateView):
#     template_name = 'test.html'
#     def get(self,request):
#         district = request.GET.get('people')
#         #lay gia tri cua 1 tag co name= people
#         form = CreateHotelForm()
#         print(district)
#         if request.GET :
#             if(district != ""):
#                 post = form.save(commit=False)
#                 post.name = district
#                 post.district = "a"
#                 post.capacity = "a"
#                 # tao 1 form theo boostrap
#                 post.save()
#         return render(request,self.template_name,{'district':district,'form':form})
#     def post(self,request):
#         form = CreateHotelForm(request.POST)
#         post = form.save(commit=False)
#         print("abc")
#         post.name = "a"
#         post.district = "a"
#         post.capacity = "a"
#         #tao 1 form theo boostrap
#         post.save()
#         text = form.cleaned_data['name']
#         text1 = form.cleaned_data['district']
#         args = {'form':form,'text':text,'text1':text1}
#         return render(request,self.template_name,args)


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
            # args = {
            # 'hotels':hotels, 'name':name, 'ID':customer_id,'email':email,'phone':phone,'inputAddress':inputAddress
            # }

        return render(request,self.template_name,{})