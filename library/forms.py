from django import forms
from .models import LibraryUser, Book

class LibraryUserForm(forms.ModelForm):
    class Meta:
        model = LibraryUser
        fields = ['name', 'age', 'liked_books']
        widgets = {
            'liked_books': forms.CheckboxSelectMultiple()
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'price']

class QueryForm(forms.Form):
    TABLES = [
        ('library_user', 'User'),
        ('book', 'Book'),
    ]

    USER_FIELDS = [
        ('name', 'Name'),
        ('age', 'Age'),
    ]

    BOOK_FIELDS = [
        ('name', 'Name'),
        ('price', 'Price'),
    ]
    
    table = forms.ChoiceField(choices=TABLES)
    field = forms.ChoiceField(choices=[])  # Empty initial choices
    operator = forms.ChoiceField(choices=[
        ('=', 'Equals'),
        ('>', 'Greater than'),
        ('<', 'Less than'),
        ('>=', 'Greater than or equal to'),
        ('<=', 'Less than or equal to'),
        ('contains', 'Contains'),
    ])
    value = forms.CharField(max_length=100, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get the current table value from the submitted data or default to first choice
        table_value = self.data.get('table', self.TABLES[0][0])
        # Set field choices based on the selected table
        self.fields['field'].choices = self.USER_FIELDS if table_value == 'library_user' else self.BOOK_FIELDS 