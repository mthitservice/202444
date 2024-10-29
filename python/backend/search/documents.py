from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Movie

@registry.register_document
class MovieDocument(Document):
    class Index:
        name='movies'
        settings={

            'number_of_shards':1,
            'number_of_replicas':0
        }
    class Django:
            model=Movie
            fields=[
    'title',
    'director',
    'plot',
    'year'

            ]