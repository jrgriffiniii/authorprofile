from django.shortcuts import render
from django.http import Http404

from models import Person

def authorDetail(request, name):

    # Retrieve all unidentified authors
    author = Person.objects.raw_query({'ids': {'$size': 0}, 'name': name})
    if author:

        author = author[0]
    else:

        raise Http404

    context = {'author': author}
    return render(request, 'authorprofile/author_detail.html', context)
