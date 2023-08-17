import os
from aqt import mw
from aqt.utils import tooltip
import requests

config = mw.addonManager.getConfig(__name__)

IMAGE_FIELD = config["image_field"]
QUERY = config["query"]
IMAGE_LINKS = config["image_links"]
FIELD_TO_CHECK = config["field_to_check"]


def link_images() -> None:
    notes = [mw.col.get_note(note_id)
             for note_id in mw.col.find_notes(f"{QUERY} -{IMAGE_FIELD}:_*")]

    folder = mw.col.media.dir()
    total_added = 0
    for index, note in enumerate(notes):
        url = get_url(note)
        if (url):
            image_name = download_image(url, folder)
            note[IMAGE_FIELD] = f'<img src="{image_name}"></img>'
            total_added += 1

        # Update progress bar
        mw.taskman.run_on_main(
            lambda: mw.progress.update(
                label=f"{note.fields[0]} ({index}/{len(notes)})",
                value=index,
                max=len(notes)
            )
        )

    tooltip(f"Added {total_added} images")
    return mw.col.update_notes(notes)


def get_url(note):
    for s in IMAGE_LINKS:
        if FIELD_TO_CHECK == "":
            if any(s in tag for tag in note.tags):
                return IMAGE_LINKS[s]
        else:
            if s in note[FIELD_TO_CHECK]:
                return IMAGE_LINKS[s]
    return None


def download_image(url, folder):
    image_name = url.split("/")[-1]
    image_path = os.path.join(folder, image_name)

    if os.path.exists(image_path):
        return image_name

    response = requests.get(url)
    if response.status_code == 200:
        image_data = response.content
        with open(image_path, "wb") as f:
            f.write(image_data)
        return image_name

    return None
