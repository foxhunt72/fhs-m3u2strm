"""Console script for fhs_m3u2strm."""
import sys
from pprint import pprint

import typer
main = typer.Typer()

@main.command()
def test(
        m3ufile: str,
):
    """Console script for fhs_m3u2strm."""
    from .import_m3u import import_m3u_file
    from .subgroup import subgroup_m3uchannels
    from .clean import clean_tvg_name, clean_name
    from .m3u_to_episodes import m3u_to_episodes
    from .strm_files import strm_files_for_episodes

    result = import_m3u_file(m3ufile)
    if result == None:
        print(f"no result for file {m3ufile}")
        return 1
    #pprint(result)
    print(len(result))
    result2 = subgroup_m3uchannels(result, '[NL] VIDEOLAND')
    result3 = list(clean_tvg_name(result2))
    pprint(len(result3))
    #pprint(result3)

    result4 = m3u_to_episodes(result3)
    strm_files_for_episodes('/tmp/videoland', result4)

    return 0

@main.command()
def vod_group_to_dir(
    m3ufile: str = typer.Option(..., envvar="fhs_m3ufile"),
    group: str = typer.Option(...),
    output_dir: str = typer.Option(...),
    rm_end_name: str = typer.Option("", help="remove text from end of serie name"),
    rm_in_name: str = typer.Option("", help="remove text in tvg_name"),
):
    """Console script for fhs_m3u2strm."""
    from .import_m3u import import_m3u_file
    from .subgroup import subgroup_m3uchannels
    from .clean import clean_tvg_name, clean_name, remove_text_from_tvg_name, remove_text_from_end_serie_name
    from .m3u_to_episodes import m3u_to_episodes
    from .strm_files import strm_files_for_episodes

    result = import_m3u_file(m3ufile)
    if result is None:
        print(f"no result for file {m3ufile}")
        return 1
    subgroup = subgroup_m3uchannels(result, group)
    if rm_in_name != "":
        subgroup = remove_text_from_tvg_name(subgroup, rm_in_name)
    m3u_episodes = m3u_to_episodes(subgroup)
    if rm_end_name != "":
        m3u_episodes = remove_text_from_end_serie_name(m3u_episodes, rm_end_name)
    strm_files_for_episodes(output_dir, m3u_episodes)

    return 0

@main.command()
def list_groups(
    m3ufile: str = typer.Option(..., envvar="fhs_m3ufile"),
    vod_only: bool = typer.Option(False)
):
    """Console script for fhs_m3u2strm."""
    from .import_m3u import import_m3u_file, return_tvg_group_titles

    result = import_m3u_file(m3ufile)
    if result == None:
        print(f"no result for file {m3ufile}")
        return 1
    groups = return_tvg_group_titles(result, vod_only=vod_only)
    for i in groups:
        print(i)

    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
