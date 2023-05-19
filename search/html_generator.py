import json
from airium import Airium


def generate_html(json_string):

    print("Generating HTML")
    data = json.loads(json_string)
    # print([val.specific_keyword for key, val in data.items()])

    a = Airium()
    # Generating HTML file
    for song, song_data in data.items():
        song_data["model_response"] = "Nice song!!"

        #   Title
        with a.h2(klass="wp-block-heading"):
            a.span(
                id=f"{song.split(' ')[1]}_{song_data['Track Name'].replace(' ', '_')}_8211_{song_data['Artist'].replace(' ', '_')}",
                _t=f"{song.split(' ')[1]}. {song_data['Track Name']} &#8211;{song_data['Artist']}"
            )

        #   Video
        with a.figure(klass="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"):
            with a.div(klass="wp-block-embed__wrapper"):
                a.div(
                    f'data-src="https://www.youtube.com/embed/{song_data["yt_video_id"]}" data-query="feature=oembed"', klass="rll-youtube-player")

        #   Description
        a.p(_t=song_data["model_response"])

    # Casting the file to a string to extract the value
    html = str(a)
    print(html)

    return html