# DSEintro - Daniel (Danny) Saedi Nia

## Fun Fact

I have lived many different places in my life. From Northeast Ohio, where I was born, to Southern Iran, where I spent 7 years. From there I moved back to the U.S., to Southern California, where I spent the next 11 years of my life. I am now living here in East Tennessee and have been for the past 2 years, and I will continue to be for at least as long as this PhD takes me.

I think that finding out someone's music taste is as good an introduction to a person as any, and so I thought I would share a small script to that retrieves and displays my top 10 Spotify artists right now.

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
pip install .
```

or

```bash
pip install -r requirements.txt
```

4.This code relies on environment variables and, more specifically, Spotify API keys to function properly. I have provided the necessary keys in the canvas submission document (notably not pushed to GitHub for security reasons). I will push a template .env file to the repo meant to be filled with the keys provided.

Please replace the placeholder values below with the keys given through the canvas submission:

```bash
SPOTIPY_CLIENT_ID = "CLIENT API KEY PROVIDED GOES HERE"
SPOTIPY_CLIENT_SECRET = "CLIENT SECRET KEY PROVIDED GOES HERE"
```

## Usage

Once everything is set up you can navigate to the project folder and run the following command  in your terminal:

```bash
python background.py
```

The program will begin to display images and artist info of Danny's (my) top 10 Spotify artists by using Spotify's API to search for artists given a specific ID. These IDs were also obtained using Spotify's developer API, but needed to be retrieved beforehand due to some safety restrictions on Spotify's side (I have left in the code to do so commented out in the main python file). Once the program is running, you must close the image window to continue to the next artist or if you're done you can close out the program by typing `Ctrl + C` in the terminal.

## Note

- This program has been tested on Python 3.12
- This code requires an active internet connection to function properly, as it interacts with the Spotify API.
