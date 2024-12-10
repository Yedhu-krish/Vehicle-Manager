from django.shortcuts import render,redirect

from django.views.generic import View

from vehicle.forms import VehicleCreateForm, SignUpForm,LoginForm

from vehicle.models import Vehicle

from django.http import HttpResponse

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from vehicle.decorators import authenication

from django.utils.decorators import method_decorator

from django.contrib import messages

# Create your views here.


@method_decorator(authenication,name='dispatch')    
class VehicleCreateVIew(View):

    template_name ='vehicle_add.html'

    form_class = VehicleCreateForm

    def get(self,request,*args,**kwargs):

        form = self.form_class()
        return render(request,self.template_name,{'form':form})
    
    def post(self,request,*args,**kwargs):

        form_instance = self.form_class(request.POST)

        if form_instance.is_valid():

            form_data = form_instance.cleaned_data

            messages.success(request,"Vehicle details Added Successfully")
            Vehicle.objects.create(**form_data)
        return redirect('viewvehicle')

        # return redirect('vehicleadd')

@method_decorator(authenication,name='dispatch')
class VehicleView(View):

    template_name='vehicle_view.html'

    def get(self,request,*args,**kwargs):

        a = Vehicle.objects.all()

        fuel_options =  Vehicle.objects.all().values_list('fuel',flat=True).distinct()

        selected_category = request.GET.get('fuel','all')

        if selected_category == 'all' :

            a = Vehicle.objects.all()
        
        else:

            a = Vehicle.objects.filter(fuel=selected_category)
        

        vehicle_category = Vehicle.objects.all().values_list('type',flat=True).distinct()

        print(vehicle_category)
        
        selected_category_type = request.GET.get('vehicle_type','all')

        if selected_category == 'all' :

            a = Vehicle.objects.all()
        
        else:

            a = Vehicle.objects.filter(type=selected_category_type)

        return render(request,self.template_name,{'data':a,'fuel_type':fuel_options,'selected_category':selected_category,'vehicle_type':vehicle_category,'selected_category':selected_category_type})


@method_decorator(authenication,name='dispatch')
class VehicleDetailView(View):

    template_name = 'vehicle_detail.html'

    def get(self,request,*args,**kwargs):

        id = kwargs.get('pk')

        data = Vehicle.objects.get(id=id)

        return render(request,self.template_name,{'data':data})


@method_decorator(authenication,name='dispatch')
class vehicleDeleteView(View):

    def get(self,request,*args,**kwargs):

        id = kwargs.get('pk')

        Vehicle.objects.get(id=id).delete()

        messages.warning(request,"Deleted successfully")
        return redirect('viewvehicle')


@method_decorator(authenication,name='dispatch')
class VehicleUpdateView(View):

    template_name = 'vehicle_update.html'

    form_class = VehicleCreateForm

    def get(self,request,*args,**kwargs):

        id = kwargs.get('pk')

        obj = Vehicle.objects.get(id=id)

        context = {
            'name':obj.name,
            'type':obj.type,
            'fuel':obj.fuel,
            'engine':obj.engine,
            'amount':obj.amount
        }

        form_instance = self.form_class(initial=context)

        return render(request,self.template_name,{'data':form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance = self.form_class(request.POST)

        id = kwargs.get('pk')

        if form_instance.is_valid():

            data= form_instance.cleaned_data


            Vehicle.objects.filter(id=id).update(**data)  # we need to use filter instead of get to update(else error)

            messages.warning(request,"Details Updated !")
            return redirect('viewvehicle')
        
        return render(request,self.template_name,{'form':form_instance})
    



class SignUpView(View):

    template_name = 'register.html'

    form_class = SignUpForm

    def get(self,request,*args,**kwargs):

        form_instance = self.form_class()

        return render(request,self.template_name,{'form':form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance = self.form_class(request.POST)

        if form_instance.is_valid():

            # data = form_instance.cleaned_data

            # User.objects.create_user(**data)

            print('here')

            form_instance.save()

            print('saved')

            return redirect('signin')
        
        return render(request,self.template_name,{'form':form_instance})
    

class SignInView(View):

    form_class = LoginForm

    template_name = 'login.html'

    def get(self,request,*args,**kwargs):

        form_instance = self.form_class()

        return render(request,self.template_name,{'form':form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_instance = self.form_class(request.POST)

        if form_instance.is_valid():

            uname = form_instance.cleaned_data.get('username')

            pwd = form_instance.cleaned_data.get('password')

            user_object = authenticate(request,username=uname,password=pwd)

            if user_object:

                login(request,user_object)

                return redirect('home')
            
        return render(request,self.template_name,{'form':form_instance})


@method_decorator(authenication,name='dispatch')
class LogoutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        messages.success(request,"Logged out Successfully")
        return redirect('signin')
    
def home_view(request):

    return render(request,'home.html')



            
    
        


    


      