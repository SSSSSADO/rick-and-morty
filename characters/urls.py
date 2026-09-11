from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from characters.views import get_random_character_view, CharacterListView


app_name = "characters"

urlpatterns = [
    path("characters/random/", get_random_character_view, name="character-random"),
    path("characters/", CharacterListView.as_view(), name="character-list"),
    path("doc/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "doc/swagger/",
        SpectacularSwaggerView.as_view(url_name="characters:schema"),
        name="swagger-ui",
    ),
]
