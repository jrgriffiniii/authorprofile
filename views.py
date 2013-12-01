from django.shortcuts import render
from django.http import Http404

from models import Person, Text, TextSet

from django.views.decorators.csrf import csrf_protect

from django.db import connections

database_wrapper = connections['default']
person = database_wrapper.get_collection('authorprofile_person')

def personList(request):

    queryset = Person.objects.raw_query({'ids': {'$not': {'$size': 0}}})

    context = { 'persons': queryset }

    return render(request, 'authorprofile/person_list.html', context)

@csrf_protect
def personDetail(request, personId):
    '''For the consideration of this system, all Persons are potentially, but not necessarily, Authors'''

    # Specific to the MongoDB
    # For the moment, only support searching by ACIS identifiers

    # This avoids breaking PyMongo under certain conditions (i. e. limited client-side resources for large MongoDB Documents)
    # Thus, this breaks the NoSQL model
    author = Person.objects.raw_query({'ids': {'$in': [ {'namespace': "http://acis.openlib.org", "value" : personId } ] }})
    texts = Text.objects.raw_query( {'authors': {'$in': [ { "ids" : [ { "namespace" : "http://acis.openlib.org", "value" : personId } ] } ] }})

    # Taking a PyMongo-based approach requires one to map all dict structures to Django Models
    # This would require that Django-nonrel itself be modified
    #author = person.find_one({'ids': {'$in': [ { "namespace" : "http://acis.openlib.org", "value" : personId } ] }}, {'texts': False})

    #db.authorprofile_text.find({authors: {$in: [ { "ids" : [ { "namespace" : "http://acis.openlib.org", "value" : "pva1" } ], "name" : "Moshe Y. Vardi" } ]}})

    if author:

        author = author[0]
        #texts = author.texts[0]

        # As stated above, this is only undertaken in order to avoid breaking PyMongo
        #if texts:

        #    author.texts = [TextSet(texts=texts, value=1, label='Texts Accepted by ' + author.name)]

        context = {'author': author}
    else:

        raise Http404

    return render(request, 'authorprofile/author_detail.html', context)

    pass

@csrf_protect
def authorDetail(request, authorName):
    '''Retrieve an author by an author name'''

    # Retrieve all unidentified authors
    # Specific to the MongoDB
    # Breaks PyMongo
    # author = Person.objects.raw_query({'ids': {'$size': 0}, 'name': authorName})

    author = Person.objects.raw_query({'name': authorName, 'ids': {'$size': 0}})
    texts = Text.objects.raw_query({'authors': {'$in': [ { "name" : authorName } ] }})
    # texts = Text.objects.raw_query( {'authors': {'$in': [ { "ids" : [ { "namespace" : "http://acis.openlib.org", "value" : personId } ] } ] }})

    # Currently being implemented
    # author = Text.objects.raw_query({'authors': {'$in': { "name" : authorName }}})
    # authorList = person.find({'ids': {'$not': {'$size': 0}}}, {'name': True})
    # db.authorprofile_text.find({authors: {$in: [ { "ids" : [ { "namespace" : "http://acis.openlib.org", "value" : "pva1" } ], "name" : "Moshe Y. Vardi" } ]}})

    if author:

        author = author[0]

        # As stated above, this is only undertaken in order to avoid breaking PyMongo
        if texts:

            author.texts = [TextSet(texts=texts, value=1, label='Texts Accepted by ' + author.name)]

        context = {'author': author }

    else:

        raise Http404

    return render(request, 'authorprofile/author_detail.html', context)

def textList(request, textId):
    '''Retrieve all Persons related to a specified text'''

    # Specific to the MongoDB
    authorList = Person.objects.raw_query({'texts': {'$in': [{'textId': textId}]}})
    if authorList:

        context = {'textId': textId, 'authorList': authorList}

    else:
        raise Http404

    return render(request, 'authorprofile/text_list.html', context)

def textDetail(request, textId):
    '''Retrieve a single text'''

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
