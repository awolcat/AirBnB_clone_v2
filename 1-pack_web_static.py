#!/usr/bin/python3
"""This module defines a fabfile which  generates a .tgz archive
   from the contents of the web_static folder of the AirBnB Clone
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """This method will create a folder versions
        in the target host containing the contents
        of web_static compressed
    """
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_path = f'versions/web_static_{time}.tgz'

    """prepare directory for archive"""
    local("mkdir -p versions")
    """create the archive"""
    result = local(f"tar cf {archive_path} /data/web_static/*")
    if result.succeeded:
        return archive_path
    return None
