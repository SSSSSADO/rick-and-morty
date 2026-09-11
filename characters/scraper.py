import requests

from characters.models import Character


URL = "https://rickandmortyapi.com/api/character"


def scrape_characters() -> list[Character]:
    next_url = URL
    characters = []

    while next_url is not None:
        characters_response = requests.get(URL).json()

        for character in characters_response["results"]:
            characters.append(
                Character(
                    api_id=character["id"],
                    name=character["name"],
                    status=character["status"],
                    species=character["species"],
                    gender=character["gender"],
                    image=character["image"]
                )
            )

        next_url = characters_response["info"]["next"]

    return characters


def save_characters(characters: list[Character]) -> None:
    for character in characters:
        character.save()


def sync_characters_with_api() -> None:
    characters = scrape_characters()
    save_characters(characters)
