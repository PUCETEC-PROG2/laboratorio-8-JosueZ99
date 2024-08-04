from django.urls import path

from . import views
app_name= "pokedex"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.CustomLoginView.as_view(), name='login'),
    
    path("pokemon/", views.pokemon, name="pokemon"),
    path("pokemon/<int:pokemon_id>/", views.display_pokemon, name="display_pokemon"),
    path("pokemon/add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path("pokemon/edit_pokemon/<int:id>/", views.edit_pokemon, name="edit_pokemon"),
    path("pokemon/delete_pokemon/<int:id>/", views.delete_pokemon, name="delete_pokemon"),
    
    path("trainer/", views.trainer, name="trainer"),
    path("trainer/<int:trainer_id>/", views.display_trainer, name="display_trainer"),
    path("trainer/add_trainer/", views.add_trainer, name="add_trainer"),
    path("trainer/edit_trainer/<int:id>/", views.edit_trainer, name="edit_trainer"),
    path("trainer/delete_trainer/<int:id>/", views.delete_trainer, name="delete_trainer"),
]
