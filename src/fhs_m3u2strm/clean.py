"""Clean m3u"""

import re


def clean_weird_characters(name):
    return re.sub(r'[^A-Za-z0-9 _-]+', '', name)


def clean_tvg_name(m3uchannels):
    """Clean title."""

    for x in m3uchannels:
        x.tvg_name = clean_name(x.tvg_name)
        yield x


def remove_text_from_tvg_name(m3uchannels, text):
    for x in m3uchannels:
        x.tvg_name = x.tvg_name.replace(text, '')
        yield x


def remove_text_from_end_tvg_name(m3uchannels, text):
    for x in m3uchannels:
        if x.tvg_name.endswith(text):
            x.tvg_name = x.tvg_name[0:-len(text)]
        yield x


def remove_text_from_end_serie_name(m3u_episodes, text):
    for x in m3u_episodes:
        if x.serie_name.endswith(text):
            x.serie_name = x.serie_name[0:-len(text)]
        yield x

def clean_square_brackets(tekst):
    test = re.compile("(.*)\[(.*?)\](.*)")
    reg = test.findall(tekst)
    if len(reg) > 0:
        tekst = reg[0][0]+reg[0][2]
        tekst = clean_square_brackets(tekst)
        return tekst
    tekst = tekst.replace('  ', ' ').strip()
    return tekst


def remove_square_brackets_from_serie_name(m3u_episodes):
    for x in m3u_episodes:
        x.serie_name = clean_square_brackets(x.serie_name)
        yield x

