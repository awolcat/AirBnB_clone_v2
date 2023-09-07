#!/usr/bin/python3
"""This module defines a fabfile which  generates a .tgz archive
   from the contents of the web_static folder of the AirBnB Clone
"""
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['100.26.234.115', '52.91.132.168']


def do_pack():
    """This method will create a folder versions
        in the target host containing the contents
        of web_static compressed
    """
    local("mkdir -p versions")
    result = local("tar cf versions/web_static_$(date '+%Y%m%d%H%M%S').tar
                   /data/web_static/*")
    if (result.succeeded):
        archive = local("ls -t versions/ | head -1")
        return archive.stdout
    return None
