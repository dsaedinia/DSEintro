# DSEintro - Daniel (Danny) Saedi Nia

## Set up

To set up the project, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. If using uv as your package manager, run the following command to install the dependencies:

    ```bash
    uv sync
    ```

    Otherwise, if you are using pip, you can install the dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

4. This code relies on environment variables and, more specifically, Spotify API keys to function properly. I have provided the necessary keys in the canvas submission document (notably not pushed to GitHub for security reasons).
Please replace the placeholder values below with the keys given.

    ```env
    SPOTIPY_CLIENT_ID = "CLIENT API KEY PROVIDED GOES HERE"
    SPOTIPY_CLIENT_SECRET = "CLIENT SECRET KEY PROVIDED GOES HERE"
    ```

- Note: This program has been tested on Python 3.12
