"""Mp3 to movies"""
import re
from dataclasses import dataclass


@dataclass
class M3uMovie:
    """Class for M3uEpisode."""
    movie_name: str
    sources: list


def m3u_to_movies(m3uchannels, debug=False):
    """Import m3u stream."""

    regex_name = re.compile('(.*?) S(\d+) {0,1}E(\d+)')
    for mp3channel in m3uchannels:
        m = regex_name.findall(mp3channel.tvg_name)
        if len(m) == 0:
            yield M3uMovie(mp3channel.tvg_name, mp3channel.tvg_sources)

