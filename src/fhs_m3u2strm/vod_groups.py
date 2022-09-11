####

import yaml
import sys
import os

def load_yamlconfig(yamlconfig):
    try:
        with open(os.path.expanduser(yamlconfig), "r") as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
    except Exception as e:  # noqa:B902
        sys.stderr.write(f"can't open config file: {yamlconfig}  {e}")
        print("please create it....")
        help_yamlfile()
        quit(1)
    return config


def help_yamlfile():
    print("""

Example yaml file.
---
config:
  season_folders: true
  square_brackets: true
  m3ufile: path to m3ufile   (optional also posible by argument)
  base_dir: base directory   (optional also posible by argument)
groups:
  - group: 'GROUP1'
    output_dir: "{PATH}/group1"
    rm_in_name:  "GRP "
    rm_end_name: " STAGE"
  - group: 'GROUP2'
    output_dir: "{PATH}/group2"
    rm_in_name:  "EN "
""")


def check_yamlconfig(config, m3ufile, base_dir):
    if 'config' not in config:
        print('ERROR: missing config in yaml config.')
        help_yamlfile()
        quit(1)

    if 'season_folders' not in config['config']:
        config['config']['season_folders'] = True

    if 'square_brackets' not in config['config']:
        config['config']['square_brackets'] = True

    if m3ufile != "":
        config['config']['m3ufile'] = m3ufile
    else:
        if 'm3ufile' not in config['config']:
            print('ERROR: missing   config m3ufile in yaml config')
            help_yamlfile()
            quit(2)

    if base_dir != "":
        config['config']['base_dir'] = base_dir
    else:
        if 'base_dir' not in config['config']:
            print('ERROR: missing   config base_dir in yaml config')
            help_yamlfile()
            quit(3)
    if 'groups' not in config:
        config['groups'] = []

    return config

def convert_group_2_strm(config, m3u_records, group, table=None):
    from .subgroup import subgroup_m3uchannels
    from .clean import remove_text_from_tvg_name, remove_text_from_end_serie_name, remove_square_brackets_from_serie_name, strip_serie_name
    from .m3u_to_episodes import m3u_to_episodes
    from .strm_files import strm_files_for_episodes

    base_dir = config['base_dir']
    output_dir = group['output_dir'].replace('{PATH}', base_dir)
    if 'rm_in_name' in group:
        rm_in_name = [group['rm_in_name']] if type(group['rm_in_name']) == str else group['rm_in_name']
    else:
        rm_in_name = []
    if 'rm_end_name' in group:
        rm_end_name = [group['rm_end_name']] if type(group['rm_end_name']) == str else group['rm_end_name']
    else:
        rm_end_name = []
    if 'group' not in group:
        print(f"ERROR: missing 'group' in group: {str(group)}")
        quit(3)
    subgroup = subgroup_m3uchannels(m3u_records, group['group'])
    for i in rm_in_name:
        subgroup = remove_text_from_tvg_name(subgroup, i)
    m3u_episodes = m3u_to_episodes(subgroup)
    if config['square_brackets'] is True:
        m3u_episodes = remove_square_brackets_from_serie_name(m3u_episodes)
    for i in rm_end_name:
        m3u_episodes = remove_text_from_end_serie_name(m3u_episodes, i)
    m3u_episodes = strip_serie_name(m3u_episodes)  # clean whitespaces around serie name
    count = strm_files_for_episodes(output_dir, m3u_episodes, season_folder=config['season_folders'], verbose=False)
    if table is not None:
        if count == 0:
            table.add_row(group['group'], str(count))
        else:
            table.add_row(group['group'], str(count))
    else:
        print(f"{group['group']}: episodes {count}")
    return count


