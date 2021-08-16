from django.shortcuts import render, redirect
from .models import Provider
from django.http import JsonResponse
from .forms import *




def dashboard_view(request):
    form1 = ProviderForm(request.POST or None)
    providers= Provider.objects.all()

    if form1.is_valid():
        form1.save()
    else:
        form1 = ProviderForm()

    context = {
        'form1':form1,
        'providers':providers
    }

    return render(request, 'dashboard.html', context)


def provider_view(request, provider_id):
    
    providers= Provider.objects.all()
    pro__vider = Provider.objects.get(id=provider_id)
    areas = Polygon.objects.filter(polygon_provider=pro__vider.id)

    form = PolygonForm()


    context = {
        'form':form,
        'areas':areas,
        'pro__vider':pro__vider,
        'providers':providers
    }


    return render(request, 'provider.html', context)


def polygon_view(request, provider_id, polygon_id):
    providers= Provider.objects.all()
    polygon = Polygon.objects.get(id=polygon_id)

    form = PolygonFormUpdate(request.POST or None)
    if form.is_valid():
        pro__vider = Provider.objects.get(id=provider_id)
        
        polygon.polygon_name = form.cleaned_data.get('polygon_name')
        polygon.polygon_area = form.cleaned_data.get('polygon_area')
        polygon.save()

        return redirect('provider-view', provider_id=pro__vider.id)
    else:
        form = PolygonForm(instance=polygon)

    context = {
        'form':form,
        'polygon':polygon,
        'providers':providers
    }

    
    return render(request, 'polygon.html', context)


def delete_polygon_view(request, provider_id, polygon_id):
    
    pro__vider = Provider.objects.get(id=provider_id)

    polygon = Polygon.objects.get(id=polygon_id)
    polygon.delete()

    return redirect('provider-view', provider_id=pro__vider.id)


def get_provider(request):

    form = GetProviderForm()

    context = {
        'form':form
    }

    return render (request, 'get_provider.html', context)
