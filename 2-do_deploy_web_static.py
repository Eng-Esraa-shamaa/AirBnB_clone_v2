#!/usr/bin/python3
# deploy fabfile and distribute archive to web servers.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["34.207.188.239", "54.174.238.110"]


def do_deploy(archive_path):
    """
    deploy web servers
    """
    if os.path.exists(archive_path) is False:
        return False
    arch_name = archive_path.split('/')[1]
    arch_name_nex = arch_name.split(".")[0]
    re_path = "/data/web_static/releases/" + arch_name_nex
    up_path = '/tmp/' + arch_name
    put(archive_path, up_path)
    run('mkdir -p ' + re_path)
    run('tar -xzf /tmp/{} -C {}/'.format(arch_name, re_path))
    run('rm {}'.format(up_path))
    mv = 'mv ' + re_path + '/web_static/* ' + re_path + '/'
    run(mv)
    run('rm -rf ' + re_path + '/web_static')
    run('rm -rf /data/web_static/current')
    run('ln -s ' + re_path + ' /data/web_static/current')
    return True
