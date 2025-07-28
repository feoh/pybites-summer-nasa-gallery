from nicegui import ui
from httpx import get
from pprint import pprint

class NASAGallery:
    def __init__(self):
        self.search_text = "quasar"
        self.search_results = {}

    def display_results(self):
        results_card = ui.card()
        with results_card:
            results_card.clear()
            for result in self.search_results:
                image_title = result['data'][0]['title']
                image_description = result['data'][0]['description']
                image_links = result['links']
                image_url = image_links[0]['href']
                with ui.row():
                    with ui.card():
                        ui.label(image_title)
                        ui.interactive_image(image_url)



    def search_image_request(self) -> None:
        result = get("https://images-api.nasa.gov/search", params={"q": self.search_text})
        if result:
            print(f"got results: {result}")
            raw_result = result.json()
            self.search_results = raw_result.get("collection", {}).get("items", [])
            
            self.display_results()



def main():

    ng = NASAGallery()

    with ui.card():
        ui.input("Search for images", value="quasar").bind_value(ng, "search_text").props("outlined")
        ui.button("Search", on_click=lambda: ng.search_image_request())

    ui.run()

if __name__ in {"__main__", "__mp_main__"}:
    main()
