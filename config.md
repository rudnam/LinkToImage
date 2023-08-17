## Link to Image

- `query` - Anki query to narrow down which cards to include in the search, e.g. `deck:日本語::単語` or `note:Mining-JP`.

- `field_to_check` - name of the field the substrings in `image_links` will be compared to. Will compare to tags when left blank.

- `image_field` - field where the image will be added.

- `image_links` - dictionary in the format _substring: link_ to determine what image goes into each note.

- `run_at_sync` - will run the add-on at sync when set to `true`
