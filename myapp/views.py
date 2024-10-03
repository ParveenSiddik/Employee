from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.forms import EmployeeForm

from myapp.models import employee

from django.contrib import messages

class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):

        form_instance=EmployeeForm()
        
        return render(request,"employee.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            employee.objects.create(**data)

            messages.success(request,"Registration Successful")

            # return render(request,"employee.html",{"form":form_instance})
            return redirect ("employee_list")
        else:

            messages.error(request,"Registration Failed")

            return render(request,"employee.html",{"form":form_instance})

class EmployeeListView(View):

    def get(self,request,*args,**kwargs):

        qs=employee.objects.all()

        return render(request,"emp_list.html",{"employees":qs})

class EmployeeDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=employee.objects.get(id=id)

        return render(request,"emp_detail.html",{"employee":qs})
    
class EmployeeDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        employee.objects.get(id=id).delete()

        messages.success(request,'Removed Successfully')

        return redirect("employee_list")
    
class EmployeeUpdateView(View):

    def get(self,request,*args,**kwargs):


        id=kwargs.get("pk")

        emp_obj=employee.objects.get(id=id)

        data={

            "name":emp_obj.name,
            
            "designation":emp_obj.designation,
            "department":emp_obj.department,
            "salary":emp_obj.salary,
            "contact":emp_obj.contact,
            "address":emp_obj.address
        }

        form_instance=EmployeeForm(initial=data)

        return render(request,"emp_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():

            id=kwargs.get("pk")

            data=form_instance.cleaned_data

            employee.objects.filter(id=id).update(**data)

            messages.success(request,"Updated Successfully")

            return redirect('employee_list')  

        else:

            messages.error(request,"Updation Failed")

            return render(request,"emp_edit.html",{"form":form_instance})

