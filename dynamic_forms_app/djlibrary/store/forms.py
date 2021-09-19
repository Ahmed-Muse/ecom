from django import forms
from django.forms import (formset_factory, modelformset_factory)

from .models import (Book, Author)


class BookForm(forms.Form):
    name = forms.CharField(
        label='Book Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
        })
    )
    isbn_number = forms.CharField(
        label='Book isbn_number',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book isbn_number here'
        })
    )

    isbn_number = forms.CharField(
        label='Book isbn_number',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book isbn_number here'
        })
    )


class BookModelForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name','isbn_number', )
        labels = {
            'name': 'Book Name'
        }
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Book Name here'
                }
            )
        }


BookFormset = formset_factory(BookForm)
BookModelFormset = modelformset_factory(
    Book,
    fields=('name','isbn_number',),
    extra=1,
    widgets={
        'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
            }
        )
    }
)

AuthorFormset = modelformset_factory(
    Author,
    fields=('name', ),
    extra=1,
    widgets={'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Author Name here'
        })
    }
)
