from django import forms

#class SearchForm(forms.Form):
 #   query = forms.CharField(
  #      label=False,
   #     required=False,
    #    widget=forms.TextInput(attrs={'placeholder':'Поиск товаров . . .',})
     #)


class SearchForm(forms.Form):
    # Одно поле для ввода поискового запроса.
    query = forms.CharField(
        label=False, # Не отображать стандартную метку поля (используем placeholder)
        required=False, # Поиск может быть пустым (тогда отобразятся все товары)
        widget=forms.TextInput(attrs={'placeholder': 'Поиск товаров...'})
    )