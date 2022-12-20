from django import forms

class ProjectFilmsForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Название'}))
    first_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Дата выпуска(Пример: 2022-12-20)'}))
    show_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Дата показа(Пример: 2022-12-20)'}))
    actors = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Актеры(Пример: Александр Жирёнкин)'}))

