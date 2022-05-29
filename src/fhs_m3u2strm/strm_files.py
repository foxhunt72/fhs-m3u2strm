"""Save files"""
from dataclasses import dataclass
from .clean import clean_weird_characters
import pathlib


@dataclass
class M3uEpisode:
    """Class for M3uEpisode."""
    serie_name: str
    episode_season: int
    episode_nr: int
    sources: list


def strm_files_for_episodes(start_dir, m3u_episodes, season_folder=True):
    """Create episodes m3u stream."""

    for e in m3u_episodes:
        name = clean_weird_characters(e.serie_name)
        path = pathlib.Path(start_dir)
        path = path.joinpath(name)
        filename = f"{name} S{e.episode_season:02}E{e.episode_nr:02}.strm" 
        if season_folder is True:
            path = path.joinpath(f"Season {e.episode_season}")
        path = path.joinpath(filename)
        path.parent.mkdir(parents=True, exist_ok=True)
        print(path)
        with path.open("w") as f:
            f.write(e.sources[0])
            f.write("\n")
