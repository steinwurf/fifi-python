#! /usr/bin/env python
# encoding: utf-8

import os

APPNAME = 'fifi-python'
VERSION = '5.0.1'


def options(opt):

    if opt.is_toplevel():
        opt.load('python')


def configure(conf):

    # Ensure that Python is configured properly
    if not conf.env['BUILD_PYTHON']:
        conf.fatal('Python was not configured properly')


def build(bld):

    bld.env.append_unique(
        'DEFINES_STEINWURF_VERSION',
        'STEINWURF_FIFI_PYTHON_VERSION="{}"'.format(VERSION))

    # Remove NDEBUG which is added from conf.check_python_headers
    flag_to_remove = 'NDEBUG'
    defines = ['DEFINES_PYEMBED', 'DEFINES_PYEXT']
    for define in defines:
        while(flag_to_remove in bld.env[define]):
            bld.env[define].remove(flag_to_remove)

    bld.env['CFLAGS_PYEXT'] = []
    bld.env['CXXFLAGS_PYEXT'] = []

    CXX = bld.env.get_flat("CXX")
    # Matches both g++ and clang++
    if 'g++' in CXX or 'clang' in CXX:
        bld.env.append_value('CXXFLAGS', '-fPIC')

    bld.recurse('src/fifi_python')

    if bld.is_toplevel():
        if bld.has_tool_option('run_tests'):
            bld.add_post_fun(exec_test_python)


def exec_test_python(bld):
    python = bld.env['PYTHON'][0]
    env = dict(os.environ)
    env['PYTHONPATH'] = os.path.join(bld.out_dir, 'src', 'fifi_python')

    # First, run the unit tests in the 'test' folder
    if os.path.exists('test'):
        for f in sorted(os.listdir('test')):
            if f.endswith('.py'):
                test = os.path.join('test', f)
                bld.cmd_and_log('{0} {1}\n'.format(python, test), env=env)

    # Then run the examples in the 'examples' folder
    if os.path.exists('examples'):
        for f in sorted(os.listdir('examples')):
            if f.endswith('.py'):
                example = os.path.join('examples', f)
                bld.cmd_and_log('{0} {1}\n'.format(python, example), env=env)
