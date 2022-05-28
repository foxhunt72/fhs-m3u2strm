"""Import m3u"""
import re
from pprint import pprint
from dataclasses import dataclass, field
from .subgroup import subgroup_vod_only

@dataclass
class M3uChannel:
    """Class for M3uChannel."""
    tvg_id: str
    tvg_name: str
    tvg_logo: str
    tvg_group_title: str
    vod: bool = False
    tvg_sources: list = field(default_factory=list)

def import_m3u_stream(input_str):
    """Import m3u stream."""

    m3uchannels = []
    # regex found on iptv-filter
    infopattern = re.compile('(?i)#EXTINF:-1 tvg-id="(.*?)" tvg-name="(.*?)" tvg-logo="(.*?)" group-title="(.*?)",(.*?)')
    urlpattern = re.compile('(?i)^http')
    for line in input_str:
        clean_line = line.rstrip()
        m = infopattern.findall(clean_line)
        if len(m) > 0:
            # #EXTINF line
            tvg_id   = m[0][0]
            tvg_name = m[0][1]
            tvg_logo = m[0][2]
            tvg_group_title = m[0][3]
            m3uchannels.append(M3uChannel(tvg_id=tvg_id, tvg_name = tvg_name, tvg_logo = tvg_logo, tvg_group_title = tvg_group_title))
        else:
            if urlpattern.match(clean_line):
                # This is the URL Line
                m3uchannels[-1].tvg_sources.append(clean_line)
                if clean_line.endswith('.mkv') is True:
                    m3uchannels[-1].vod = True
    if len(m3uchannels) == 0:
        return None
    return m3uchannels

def import_m3u_file(m3u_file):
    """Import m3u_file"""
    try:
        with open(m3u_file, 'r') as input_stream:
            return(import_m3u_stream(input_stream))
    except FileNotFoundError:
        print(f"file {m3u_file} not found.")
    return None


def return_tvg_group_titles(m3u_channels, vod_only=False):
    tvg_groups = set()
    if vod_only is True:
        channels = subgroup_vod_only(m3u_channels)
    else:
        channels = m3u_channels
    for ch in channels:
        tvg_groups.add(ch.tvg_group_title)
    return sorted(tvg_groups)
