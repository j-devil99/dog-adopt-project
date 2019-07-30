from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from .choices import price_choices, bedroom_choices, state_choices

from .models import Pet

def index(request):
  pets = Pet.objects.order_by('-list_date')

  paginator = Paginator(pets, 6)
  page = request.GET.get('page')
  paged_pets = paginator.get_page(page)

  context = {
    'pets': paged_pets
  }

  return render(request, 'pets/pets.html', context)

def pet(request, pet_id):
  pet = get_object_or_404(Pet, pk=pet_id)

  context = {
    'pet': pet
  }

  print(pet.shelter.id)
  return render(request, 'pets/pet.html', context)

# def search(request):
#   queryset_list = Pet.objects.order_by('-list_date')

#   # State
#   if 'state' in request.GET:
#     state = request.GET['state']
#     if state:
#       queryset_list = queryset_list.filter(state__iexact=state)

#   # Breed
#   if 'breed' in request.GET:
#     breed = request.GET['breed']
#     if breed:
#       queryset_list = queryset_list.filter(breed__lte=breed)

#   context = {
#     'pets': queryset_list,
#     'values': request.GET
#   }

#   return render(request, 'pets/search.html', context)
