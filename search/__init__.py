from . import open_ai_upwork_main


def search(input_data, limit_st, offset, keys, stopper, by_artist=False):
    return open_ai_upwork_main.search(input_data, limit_st, offset, keys, stopper, by_artist)


def search_artist(artist_name):
    return open_ai_upwork_main.search_artists(artist_name=artist_name)
