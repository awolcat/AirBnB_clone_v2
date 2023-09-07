#!/usr/bin/python3
"""This module defines a fabfile which  generates a .tgz archive
   from the contents of the web_static folder of the AirBnB Clone
"""
from fabric.api import put, run, env
import os


env.user = 'ubuntu'
env.hosts = ['100.26.234.115', '52.91.132.168']
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """This method will upload the web_static archive from do_pack
        and uncompress it and configure nginx to serve the sites there
    """

    if os.path.exists(archive_path) is False:
        return False
    try:
        put(archive_path, '/tmp/')
        archive = archive_path.split('/')[-1]
        archive_name = archive.split('.')[0]
        # Releases directory
        releases = '/data/web_static/releases'
        run('sudo mkdir -p {}/{}/'.format(releases, archive_name))
        run('sudo tar -xzf /tmp/{}.tgz -C {}/{}'.format(archive_name,
                                                        releases,
                                                        archive_name))
        # Delete archive from /tmp/
        run('sudo rm /tmp/{}.tgz'.format(archive_name))
        # Move webstatic file up one level in dir hierarchy
        ws = 'web_static'
        run('sudo mv {}/{}/{}/* {}/{}/'.format(releases, archive_name, ws,
                                               releases, archive_name))
        run('sudo rm -rf {}/{}/{}'.format(releases, archive_name, ws))
        # Remove symbolic link current
        run('sudo rm -rf /data/web_static/current')
        # Create another symbolic link current to releases/archive_name
        run('sudo ln -s {}/{}/ /data/web_static/current'.format(releases,
                                                                archive_name))
        return True
    except Exception:
        return False
