#!/usr/bin/python3
"""This module defines a fabfile which  generates a .tgz archive
   from the contents of the web_static folder of the AirBnB Clone
"""
from fabric.api import local


def do_pack():
    """This method will create a folder versions
        in the target host containing the contents
        of web_static compressed
    """
    local("mkdir -p versions")
    result = local("tar cf versions/web_static_$(date '+%Y%m%d%H%M%S').tgz\
                   /data/web_static/*")
    if (result.succeeded):
        archive = local("ls -t versions/web_static_* | head -1")
        return archive.stdout
    return None
