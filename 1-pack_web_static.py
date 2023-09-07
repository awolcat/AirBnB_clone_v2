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
    try:
        """prepare directory for archive"""
        local("mkdir -p versions")
        """create the archive"""
        result = local(f"tar cvzf {archive_path} web_static/")
        return f'web_static_{time}.tgz'
    except Exception:
        return None
