fhs_m3u2strm
============


M3u iptv to strm files for iptv2vod services. My current iptv provider delivers a m3u file with a lot of VOD programs into it also. But i wanted to have a nice way to use it from kodi or jellyfin as normal media.

So i created this program which makes it easy to use vod streams from an iptv provider using a mediaserver/player as kodi / plex / jellyfin / emby and a lot more i think. 

- https://pypi.org/project/fhs-m3u2strm/

Thanks to:
----------
- https://github.com/cmcconomy/iptv-filter.git


Usage
-----

- Vod group in m3u_file to directory strm file

  **fhs-m3u2strm** vod-group-to-dir --m3ufile <path_to_local_file> --group 'GROUPNAME'' --output-dir 'OUTPUT_DIR'

  *arguments*
  
  - **m3ufile:** path to m3ufile
  - **group:** group to convert to strm files (see **list-groups** options to show groups in m3ufile)
  - **output-dir:** directory where to put strm files
  
  *optional arguments*
  
  - **rm-end-name:** remove this text from end of episodes text
  - **rm-in-name:** remove this text in the episode and/or serie name
  - **season-folders:** create season folders
  - **square-brackets:** remove all text within square brackets from episode and/or serie name

- Listing groups in m3u_file

  **fhs-m3u2strm** list-groups --m3ufile <path_to_local_file> [--vod-only]

  *arguments*

  - **m3ufile:** path to m3ufile
  - **vod-only:** show only vod from m3ufile 

- Listing groups in m3u_file with details (like movies, channels and episodes)

  **fhs-m3u2strm** list-groups-details --m3ufile <path_to_local_file> [--vod-only]

  *arguments*

  - **m3ufile:** path to m3ufile
  - **vod-only:** show only vod from m3ufile 

- Multiple vod groups in m3u_file to groups

  **fhs-m3u2strm vod-groups-to-dir** --yamlconfig sync.yml --m3ufile <path_to_local_file> --base-dir 'OUTPUT_DIR'

  *arguments*
  
  - **yaml_config:** path to yaml config with groups
  - **m3ufile:** path to m3ufile
  - **base_dir:** is used to replace {PATH} in output_dir (see example yaml file)

Example yaml file 
----------------------------------------
For vod-groups-to-dir

.. code-block:: bash

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


Installation
------------
.. code-block:: bash

  git clone https://github.com/foxhunt72/fhs-m3u2strm
  cd fhs-m3u2strm
  pip3 install .

  pipx install fhs_m3u2strm
  or
  pip3 install fhs_m3u2strm

Requirements
^^^^^^^^^^^^
- typer[all]
- pyyaml
- rich

Compatibility
-------------

Licence
-------
MIT License

Authors
-------

`fhs_m3u2strm` was written by `Richard de Vos <rdevos72@gmail.com>`_.
