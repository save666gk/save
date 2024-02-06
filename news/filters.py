from django_filters import FilterSet
from .models import Post

# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
   class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {

           'title': ['icontains'],
            'author':['exact'],
           'dateCreation':['date__gt', ],
           'category':['exact']
       }