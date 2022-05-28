fhs_m3u2strm
============


m3u iptv to strm files for iptv2vod services

Thanks to:
----------
- https://github.com/cmcconomy/iptv-filter.git


Usage
-----
.. code-block:: bash

  fhs-m3u2strm vod-group-to-dir --m3ufile <path_to_local_file> --group 'GROUPNAME'' --output-dir 'OUTPUT_DIR'

  fhs-m3u2strm list-groups --m3ufile <path_to_local_file> [--vod-only]

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

Compatibility
-------------

Licence
-------
MIT License

Authors
-------

`fhs_m3u2strm` was written by `Richard de Vos <rdevos72@gmail.com>`_.
