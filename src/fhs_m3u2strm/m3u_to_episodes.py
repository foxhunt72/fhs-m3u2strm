"""Mp3 to episodes"""
import re
from dataclasses import dataclass


@dataclass
class M3uEpisode:
    """Class for M3uEpisode."""
    serie_name: str
    episode_season: int
    episode_nr: int
    sources: list


def m3u_to_episodes(m3uchannels, debug=False):
    """Import m3u stream."""

    regex_name = re.compile('(.*?) S(\d+) {0,1}E(\d+)')
    for mp3channel in m3uchannels:
        m = regex_name.findall(mp3channel.tvg_name)
        if len(m) == 0:
            if debug is True:
                print(f"{mp3channel.tvg_name=}")
            continue
        yield M3uEpisode(m[0][0].strip(), m[0][1], m[0][2], mp3channel.tvg_sources)

def episodes_to_series(m3u_episodes):
    """Create set of all series."""
    result = set()
    for episode in m3u_episodes:
        result.add(episode.serie_name)
    return result


def m3u_to_series(m3uchannels):
    """Create set of all series from m3uchannel."""
    result1 = m3u_to_episodes(m3uchannels)
    result2 = episodes_to_series(result1)
    return result2
