#!/usr/bin/python3
'''Fabric script to generate .tgz archive'''

from fabric.api import local
from fabric.decorators import runs_once
import datetime


@runs_once
def do_pack():
    '''creates a .tgz archive from the contents of web_static folder'''
    local('mkdir -p versions')
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    path = ('versions/web_static_{}.tgz'.format(date))
    result = local('tar -cvzf {} web_static'.format(path))

    if result.failed:
        return None
    return path
