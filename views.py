from django.shortcuts import render
from django.http import Http404

from models import Person, Text

def authorDetail(request, authorName):

    # Retrieve all unidentified authors
    # Specific to the MongoDB
    author = Person.objects.raw_query({'ids': {'$size': 0}, 'name': authorName})
    if author:

        author = author[0]
        context = {'author': author}

    else:

        controlledAuthor = Person.objects.raw_query({'name': authorName})
        if controlledAuthor:

            controlledAuthor = controlledAuthor[0]
            context = {'author': controlledAuthor}
        
            if not controlledAuthor:

                raise Http404

    return render(request, 'authorprofile/author_detail.html', context)

def textList(request, textId):

    # ListView.as_view(queryset=Person.objects.raw_query({'texts': {'$in': []}}), context_object_name='authorListByText')

    # Retrieve all unidentified authors
    # Specific to the MongoDB

    authorList = Person.objects.raw_query({'texts': {'$in': [{'textId': textId}]}})
    if authorList:

        context = {'textId': textId, 'authorList': authorList}

    else:
        raise Http404

    return render(request, 'authorprofile/text_list.html', context)

def textDetail(request, textId):

    # Indexing support? (http://django-mongodb-engine.readthedocs.org/en/latest/reference/model-options.html#indexes)
    #text = Text.objects.get(textId=textId)
    # Specific to the MongoDB
    text = Text.objects.raw_query({'textId': textId})
    if text:

        text = text[0]
        context = {'text': text}

    else:

        raise Http404

    return render(request, 'authorprofile/text_detail.html', context)
