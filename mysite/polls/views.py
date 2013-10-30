from django.http import HttpResponse

from polls.models import Question
from django.template.context import RequestContext
from django.shortcuts import render_to_response, redirect
from polls.models import Author,Book
from django.forms.models import modelformset_factory
from django.forms import ModelForm
from django.shortcuts import get_object_or_404

class AuthorForm(ModelForm):
    class Meta:
        model = Author     

BookFormset = modelformset_factory( Book, 
    fields=('book_name', 'publisher_name'), extra=1, 
    can_delete=False) 


class UserSubmittedBookForm(ModelForm):
    class Meta:
        model = Book


def index1(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question_text for p in latest_question_list])
    return HttpResponse(output)


def index(request):
    queryset = Members.objects.all()

    template = 'polls/index.html'
    kwvars = {
        'data': queryset,
    }
    return render_to_response(template, kwvars, RequestContext(request))


def update_book(request,author_id):

    book_formset = BookFormset()

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save(commit=False)
            book_formset = BookFormset(request.POST, instance=author)
            if book_formset.is_valid():
                author.save()
                book_formset.save()
                return redirect('/index/')

    return render_to_response('updatebook.html',{
        'form': form, 'formset': book_formset
    },context_instance=RequestContext(request)) 






def submit_book(request):
    if request.POST:

        form = UserSubmittedBookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            return redirect('/index/')
    else:
        form = UserSubmittedBookForm()
    return render_to_response('submit.html', {
        "form": form,
    }, context_instance=RequestContext(request))
