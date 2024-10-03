from django import forms

class EmployeeForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    options=(
        ("Tester","Tester"),
        ("Engineer","Engineer"),
        ("Python Developer","Python Developer"),
    )
    designation=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2"}))
    department=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2"}))
    salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-2"}))
    contact=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2"}))
    address=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2"}))
    