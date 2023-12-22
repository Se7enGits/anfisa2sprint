from django.shortcuts import get_object_or_404, render

from ice_cream.models import IceCream


def ice_cream_detail(request, pk):
    # template = 'ice_cream/detail.html'
    context = {
        'ice_cream': get_object_or_404(
            IceCream.objects.filter(
                is_published=True,
                category__is_published=True
                ),
            pk=pk
            ),
        }
    return render(request, 'ice_cream/detail.html', context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    context = {
        'ice_cream_list': IceCream.objects.select_related(
            'category').filter(
                is_published=True,
                category__is_published=True
            ).order_by('category'),
    }
    return render(request, template, context)
