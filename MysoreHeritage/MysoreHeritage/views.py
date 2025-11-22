from django.shortcuts import render,redirect,get_object_or_404
from Heritagedb.models import Category,Heritage,Location
from django.http import JsonResponse


def heritage_list(request):
    categories = Category.objects.all()
    places = Heritage.objects.all()
    
     # --- SEARCH FUNCTIONALITY ---
    search_query = request.GET.get('search')

    if search_query:
        # Filter matching names
        matched_places = Heritage.objects.filter(name__icontains=search_query)

        # If exactly one result → redirect to detail page
        if matched_places.count() == 1:
            return redirect('heritage_detail', pk=matched_places.first().id)

        # If multiple results → show them in the current page
        places = matched_places
    context = {
        'categories': categories,
        'places': places,
    }

    return render(request, 'heritage_list.html', context)

def category_filter(request, category_name):
    category_name = category_name.strip()   # remove side spaces
    categories = Category.objects.all()

    selected_category = get_object_or_404(
        Category,
        name__iexact=category_name  # case-insensitive match
    )

    places = Heritage.objects.filter(category=selected_category)

    return render(request, 'heritage_list.html', {
        'categories': categories,
        'places': places,
        'selected_category': selected_category
    })



def landing_page(request):
    return render(request,'landing_page.html')

def add_heritage(request):
    name_value =request.GET.get('name')
    category_value =request.GET.get('category')
    description_value=request.GET.get('description')
    image_value=request.GET.get('image')
    timing_value=request.GET.get('timing')
    entryfee=request.GET.get('entry_fee')
    establishedyear=request.GET.get('established_year')

    Heritage.objects.create(
        name=name_value,
        category=category_value,
        description=description_value,
        image=image_value,
        timing=timing_value,
        entry_fee=entryfee,
        established_year=establishedyear
        
    )
    return JsonResponse({'message':'heritage added'})

def update_heritage(request):
    name_value =request.GET.get('name')
    category_value =request.GET.get('category')
    description_value=request.GET.get('description')
    image_value=request.GET.get('image')
    timing_value=request.GET.get('timings')
    entryfee=request.GET.get('entry_fee')
    establishedyear=request.GET.get('established_year')

    heritage=Heritage.objects.get(name=name_value)
    heritage.category=category_value
    heritage.description=description_value
    heritage.image=image_value
    heritage.timings=timing_value
    heritage.entry_fee=entryfee
    heritage.established_year=establishedyear
    heritage.save()
    return JsonResponse({'message':'heritage updated successfully'})

def delete_heritage(request):
    name_value =request.GET.get('name')
    heritage=Heritage.objects.get(name=name_value)
    heritage.delete()
    return JsonResponse({'message':' heritage deleted successfully'})

def fetch_heritage(request):
    result=Heritage.objects.all().values()
    #return JsonResponse(list(result),safe=False)
    return render(request,'heritage.html',context={'heritage':list(result)})

def heritage_detail(request, pk):
    heritage = get_object_or_404(Heritage, pk=pk)
    return render(request, 'heritage_detail.html', {'heritage': heritage})

def add_category(request):
    name_value =request.GET.get('name')
    id_value =request.GET.get('heritage_id')

    Category.objects.create(
        name=name_value,
        heritage_id=id_value,
    )
    return JsonResponse({'message':'category added'})

def update_category(request):
    name_value =request.GET.get('name')
    id_value =request.GET.get('heritage_id')

    categories=Category.objects.get(name=name_value)
    categories.heritage_id=id_value
    categories.save()
    return JsonResponse({'message':' category updated successfully'})

def delete_category(request):
    name_value =request.GET.get('name')
    categories=Category.objects.get(name=name_value)
    categories.delete()
    return JsonResponse({'message':'category deleted successfully'})

def fetch_category(request):
    result=Category.objects.all().values()
    #return JsonResponse(list(result),safe=False)
    return render(request,'categories.html',context={'events':list(result)})




def add_location(request):
    heritage_value =request.GET.get('heritage')
    address_value =request.GET.get('address')
    area_value =request.GET.get('area')

    Location.objects.create(
        heritage=heritage_value,
        address_value=address_value,
        area=area_value
    )
    return JsonResponse({'message':'location added'})

def update_location(request):
    heritage_value =request.GET.get('heritage')
    address_value =request.GET.get('address')
    area_value =request.GET.get('area')

    location=Location.objects.get(heritage=heritage_value)
    location.address=address_value
    location.area=area_value
    location.save()
    return JsonResponse({'message':'location updated successfully'})

def delete_location(request):
    heritage_value =request.GET.get('heritage')

    location=Location.objects.get(heritage=heritage_value)
    location.delete()
    return JsonResponse({'message':'location deleted successfully'})

def fetch_location(request):
    result=Location.objects.all().values()
    #return JsonResponse(list(result),safe=False)
    return render(request,'event.html',context={'events':list(result)})