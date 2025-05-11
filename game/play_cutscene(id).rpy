# call this whenever you want to play a cutscene:
label play_cutscene(id):
    # find the entry
    $ entry = next(e for e in VIDEO_DATA if e["id"] == id)
    # mark it seen
    $ persistent.seen_videos.add(id)
    # play it
    $ renpy.movie_cutscene(entry["video"])
    return
