
from django import forms
from .models import RentCar, Cars, Category

from django.forms.widgets import SelectDateWidget

class RentCarForm(forms.ModelForm):
    class Meta:
        model = RentCar
        fields = ('pick_up_location', 'drop_off_location', 'pick_up_date', 'drop_off_date', 'pick_up_time','car')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add "form-control" class to all input fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
            
        # Use SelectDateWidget for date fields
        self.fields['pick_up_date'].widget = SelectDateWidget(empty_label=("Year", "Month", "Day"))
        self.fields['drop_off_date'].widget = SelectDateWidget(empty_label=("Year", "Month", "Day"))
        
        # Filter categories to only show Cars objects
        # self.fields['category'].queryset = Category.objects.all()

class bookingForm(forms.ModelForm):
    class Meta:
        model = RentCar
        fields = ('pick_up_location', 'drop_off_location', 'pick_up_date', 'drop_off_date', 'pick_up_time')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add "form-control" class to all input fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
            
        # Use SelectDateWidget for date fields
        self.fields['pick_up_date'].widget = SelectDateWidget(empty_label=("Year", "Month", "Day"))
        self.fields['drop_off_date'].widget = SelectDateWidget(empty_label=("Year", "Month", "Day"))
        
        # Filter categories to only show Cars objects
        # self.fields['car'].queryset = Cars.objects.all()