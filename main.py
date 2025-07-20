from nicegui import ui
from httpx import get

class NASAGallery:
    def __init__(self):
        self.search_text = "quasar"
        self.search_result = {}

    def search_image_request(self) -> None:
        result = get("https://images-api.nasa.gov/search", params={"q": self.search_text})
        self.search_result = result.json()
        print(self.search_result)


def main():

    ng = NASAGallery()
    ui.input("Search for images", value="quasar").bind_value(ng, "search_text").props("outlined")

    ui.button("Search", on_click=lambda: ng.search_image_request())
    ui.run()

if __name__ in {"__main__", "__mp_main__"}:
    main()
