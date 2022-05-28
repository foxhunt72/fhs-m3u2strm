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


def m3u_to_episodes(m3uchannels):
    """Import m3u stream."""

    regex_name = re.compile('(.*?) S(\d+) E(\d+)')
    regex_name2 = re.compile('(.*?) S(\d+)E(\d+)')
    for mp3channel in m3uchannels:
        m = regex_name.findall(mp3channel.tvg_name)
        if len(m) == 0:
            m = regex_name2.findall(mp3channel.tvg_name)
            if len(m) == 0:
                continue
        yield M3uEpisode(m[0][0], m[0][1], m[0][2], mp3channel.tvg_sources)

