# from django.db.models import Q
from django.shortcuts import render


from ice_cream.models import IceCream


def index(request):
    # template = 'homepage/index.html'
    context = {
        'ice_cream_list': IceCream.objects.values(
            'id', 'title', 'price', 'description').filter(
                is_published=True,
                is_on_main=True,
                category__is_published=True
                ),
        # .values('id', 'title', 'description').filter(
        #     Q(is_published=True)
        #     & Q(is_on_main=True)).order_by('title')[1:4],
    }
    return render(request, 'homepage/index.html', context)
