from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.db.models.functions import Cast
from django.db.models import FloatField
from .models import LibraryUser, Book
from .forms import LibraryUserForm, BookForm, QueryForm

def home(request):
    users = LibraryUser.objects.all()
    books = Book.objects.all()
    query_form = QueryForm(request.GET or None)
    results = []

    if request.GET and query_form.is_valid():
        table = query_form.cleaned_data['table']
        field = query_form.cleaned_data['field']
        operator = query_form.cleaned_data['operator']
        value = query_form.cleaned_data['value']

        # Validate field based on table
        valid_fields = dict(QueryForm.USER_FIELDS if table == 'library_user' else QueryForm.BOOK_FIELDS)
        if field not in valid_fields:
            query_form.add_error('field', 'Invalid field for selected table')
        else:
            if table == 'library_user':
                queryset = LibraryUser.objects.all()
            else:
                queryset = Book.objects.all()

            try:
                # Convert value to float for numeric fields
                if field in ['age', 'price']:
                    try:
                        value = float(value)
                    except ValueError:
                        query_form.add_error('value', f'Please enter a valid number for {field}')
                        return render(request, 'library/home.html', {
                            'users': users,
                            'books': books,
                            'query_form': query_form,
                            'results': results
                        })

                # Build the filter
                if field in ['age', 'price']:
                    # For numeric fields, use explicit comparison
                    if operator == '=':
                        results = queryset.filter(**{field: value})
                    elif operator == '>':
                        results = [obj for obj in queryset if getattr(obj, field) > value]
                    elif operator == '<':
                        results = [obj for obj in queryset if getattr(obj, field) < value]
                    elif operator == '>=':
                        results = [obj for obj in queryset if getattr(obj, field) >= value]
                    elif operator == '<=':
                        results = [obj for obj in queryset if getattr(obj, field) <= value]
                else:
                    # For text fields, use standard filters
                    if operator == '=':
                        filter_kwargs = {field: value}
                    elif operator == 'contains':
                        filter_kwargs = {f"{field}__contains": value}
                    else:
                        query_form.add_error('operator', 'Invalid operator for text field')
                        return render(request, 'library/home.html', {
                            'users': users,
                            'books': books,
                            'query_form': query_form,
                            'results': results
                        })
                    results = queryset.filter(**filter_kwargs)

            except Exception as e:
                query_form.add_error(None, f'Error performing query: {str(e)}')

    context = {
        'users': users,
        'books': books,
        'query_form': query_form,
        'results': results,
    }
    return render(request, 'library/home.html', context)

class UserCreateView(CreateView):
    model = LibraryUser
    form_class = LibraryUserForm
    template_name = 'library/user_form.html'
    success_url = reverse_lazy('home')

class UserUpdateView(UpdateView):
    model = LibraryUser
    form_class = LibraryUserForm
    template_name = 'library/user_form.html'
    success_url = reverse_lazy('home')

class UserDeleteView(DeleteView):
    model = LibraryUser
    template_name = 'library/user_confirm_delete.html'
    success_url = reverse_lazy('home')

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('home')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('home')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    success_url = reverse_lazy('home')
