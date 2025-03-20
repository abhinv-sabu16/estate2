from django import forms

class pricePredictionForm(forms.Form):
    LOCATION_CHOICES = [
        ('kochi', 'Kochi'),
        ('thrissur', 'Thrissur'),
        ('calicut', 'Calicut'),
        ('trivandrum', 'Trivandrum'),
    ]

    location = forms.ChoiceField(choices=LOCATION_CHOICES, required=True, label="Location")
    size = forms.IntegerField(required=True, label="Size (sq ft)", min_value=1)
    bedrooms = forms.IntegerField(required=True, label="Bedrooms", min_value=1)
    bathrooms = forms.IntegerField(required=True, label="Bathrooms", min_value=1)
    amenities = forms.CharField(required=False, label="Amenities (Optional)", widget=forms.TextInput())

