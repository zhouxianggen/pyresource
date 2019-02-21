#!/usr/bin/env python
#coding=utf8

try:
    from  setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
        name = 'pyresource',
        version = '1.0',
        install_requires = [], 
        description = 'resources (ecs, mysql, redis, mongo, vps) interface',
        url = 'https://github.com/zhouxianggen/pyresource', 
        author = 'zhouxianggen',
        author_email = 'zhouxianggen@gmail.com',
        classifiers = [ 'Programming Language :: Python :: 3.7',],
        packages = ['pyresource'],
        data_files = [ ],  
        entry_points = { }   
        )
