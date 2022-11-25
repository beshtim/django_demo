from django import forms
from .models import Category, News
import re 
from django.core.exceptions import ValidationError


# Форма не связанная с моделью
class NewsFormNotConnectedWithDB(forms.Form):
    title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Контент', required=False, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5,
        }))
    is_published = forms.BooleanField(label='Опубликовано', initial=True)
    category = forms.ModelChoiceField(Category.objects.all(), label='Категория', empty_label='Выберете категорию', widget=forms.Select(attrs={
        "class": "form-control",
    }))

# Форма связанная с моделью
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={
                        "class": "form-control",
                        "rows": 5,
                        }),
            'category': forms.Select(attrs={"class": "form-control"})
        }

    # Кастомный валидатор
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        else:
            return title