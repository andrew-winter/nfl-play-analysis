import os
import requests

# %%
def download_nflverse_csv(url: str, directory: str, label: str):
    """Download nflverse play-by-play season data as a csv.

    Use requests to scrape the pbp data and download to a directory.
    Specify the label in the URL that categorizes the nflverse data type.
    """
    file = os.path.join(directory, url.split(f"{label}/")[1])
    r = requests.get(url, stream=True)
    if r.ok:
        print("saving file to:\t", os.path.abspath(file))
        with open(file, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())

# %%
#download_nflverse(url=f'{PBP_URL}_2024.csv', directory=PBP_DIR, label='pbp')
