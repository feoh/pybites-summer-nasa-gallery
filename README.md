# NASA Image Gallery

A simple web application built with Python and [NiceGUI](https://nicegui.io/) that allows you to search for and display images from the [NASA Images API](https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf).

## Features

- Search for images from the NASA image and video library.
- View search results in a clean, card-based gallery.
- Interactive image display.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) - An extremely fast Python package installer and resolver.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/pybites-summer-nasa-gallery.git
    cd pybites-summer-nasa-gallery
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    uv venv
    source .venv/bin/activate
    ```

3.  **Install the required dependencies using `uv`:**
    ```bash
    uv pip sync pyproject.toml
    ```

## Usage

To run the application, execute the `main.py` script:

```bash
python main.py
```

Once the application is running, open your web browser and navigate to the URL provided in the console (typically `http://localhost:8080`).

You can then use the search bar to find images from NASA's collection.