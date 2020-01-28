from fabric.api import local, env, run, put, cd, task, lcd, path, sudo, get
from fabric.contrib import project
import pickle
import time
import os

env.roledefs['l'] = ['ericj@lift.cs.uchicago.edu']

env.forward_agent = True

TGT_DIR = 'nmr-respredict-examples'
@task
def deploy(): 
    local('git ls-tree --full-tree --name-only -r HEAD > .git-files-list')
    if 'lift' in env.host:
        tgt_dir = f"/data/ericj/nmr/{TGT_DIR}"

    project.rsync_project(tgt_dir, local_dir="./",
                          exclude=['*.npy', "*.ipynb", 'data'],
                          extra_opts='--files-from=.git-files-list')


    project.rsync_project(tgt_dir, 
                          local_dir=".",
                          extra_opts="--include '*.png' --include '*.pdf' --include '*.ipynb'  --include='*/' --exclude='*' " ,

                      upload=False)
