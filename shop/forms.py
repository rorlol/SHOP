from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(
        label=False,
        required=False,
        widget=forms.TextInput(attrs={'placeholder':'Поиск товаров . . .',})
    )