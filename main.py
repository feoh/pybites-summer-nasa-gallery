from nicegui import ui
from httpx import get

class NASAGallery:
    def __init__(self):
        self.search_text = "quasar"
        self.search_results = {}

    def search_image_request(self) -> None:
        result = get("https://images-api.nasa.gov/search", params={"q": self.search_text})
        if result:
            raw_result = result.json()
            self.search_results = raw_result.get("collection", {}).get("items", [])
            print(self.search_results)


def main():

    ng = NASAGallery()
    ui.input("Search for images", value="quasar").bind_value(ng, "search_text").props("outlined")

    ui.button("Search", on_click=lambda: ng.search_image_request())

    with ui.row():
        for result in ng.search_results:
            image_url = result["links"][2]["href"]
            ui.image(image_url)

    ui.run()

if __name__ in {"__main__", "__mp_main__"}:
    main()
