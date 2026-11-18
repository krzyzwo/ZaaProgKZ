import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--city", help="Miasto do wyszukania")
args = parser.parse_args()
if args.city:
    city = (args.city).replace(" ", "_")
    URL = "https://api.openbrewerydb.org/v1/breweries?by_city=" + city + "&per_page=20"
else:
    URL = "https://api.openbrewerydb.org/v1/breweries?per_page=20"


class Brewery:
    def __init__(
        self,
        brew_id: str,
        brew_name: str,
        brew_type: str,
        brew_address1: str,
        brew_address2: str,
        brew_address3: str,
        brew_city: str,
        brew_state_province: str,
        brew_postalcode: str,
        brew_country: str,
        brew_longitude: int,
        brew_latitude: int,
        brew_phone: str,
        brew_url: str,
        brew_state: str,
        brew_street: str,
    ):
        self.brew_id = brew_id
        self.brew_name = brew_name
        self.brew_type = brew_type
        self.brew_address1 = brew_address1
        self.brew_address2 = brew_address2
        self.brew_address3 = brew_address3
        self.brew_city = brew_city
        self.brew_state_province = brew_state_province
        self.brew_postalcode = brew_postalcode
        self.brew_country = brew_country
        self.brew_longitude = brew_longitude
        self.brew_latitude = brew_latitude
        self.brew_phone = brew_phone
        self.brew_url = brew_url
        self.brew_state = brew_state
        self.brew_street = brew_street

    def __str__(self):
        return f"{self.brew_id}: {self.brew_name} - {self.brew_type}. {self.brew_address1} {self.brew_address2} {self.brew_address3}, {self.brew_city}, {self.brew_state_province}, {self.brew_postalcode}, {self.brew_country}. {self.brew_longitude} {self.brew_latitude}. {self.brew_phone}, {self.brew_url}. {self.brew_state}, {self.brew_street}."


def brewing():
    import requests

    r = requests.get(url=URL)
    data = r.json()

    Breweries = []
    for dane in data:
        brews = Brewery(
            dane["id"],
            dane["name"],
            dane["brewery_type"],
            dane["address_1"],
            dane["address_2"],
            dane["address_3"],
            dane["city"],
            dane["state_province"],
            dane["postal_code"],
            dane["country"],
            dane["longitude"],
            dane["latitude"],
            dane["phone"],
            dane["website_url"],
            dane["state"],
            dane["street"],
        )
        print(brews)
        print()
        Breweries.append(brews)


brewing()
