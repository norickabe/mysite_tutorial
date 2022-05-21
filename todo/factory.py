import factory

from todo.models import Post

class PostFactory(factory.Factory):
    class Meta:
        model = Post

    title =  factory.Faker('sentence', nb_words=10)
    author = factory.Faker('name')
    worker = factory.Faker('name')
    created_at = factory.Faker('date_time')