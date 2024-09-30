from django import forms
from .models import Vehicle

class VehicleRegistrationForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['make', 'model', 'year', 'license_plate']  # Add other fields as needed

    def clean_year(self):
        year = self.cleaned_data['year']
        current_year = datetime.date.today().year
        if year > current_year:
            raise forms.ValidationError("Year cannot be in the future.")
        return year

    def clean_license_plate(self):
        license_plate = self.cleaned_data['license_plate']
        # Add any license plate format validation here (if applicable)
        return license_plate