#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Clean ODPS table/resource/function/instance')
parser.add_argument('odps', type=str, help='ODPS config file')
parser.add_argument('-k', '--keep', type=str, help='Regex file')
parser.add_argument('-i', '--instance', action='store_true', help='Kill instances as well')
parser.add_argument('-r', '--run', action='store_true', help='Clean! Rather than dry run')
args = parser.parse_args()

def parse_odps_config(f):
    c = dict()
    for line in open(f, 'r'):
        kv = line.strip().split('=', 1)
        if len(kv) < 2:
            continue
        if kv[0] == 'access_id':
            c['access_id'] = kv[1]
        elif kv[0] == 'access_key':
            c['access_key'] = kv[1]
        elif kv[0] == 'end_point':
            c['endpoint'] = kv[1]
        elif kv[0] == 'project_name':
            c['project'] = kv[1]
    return c

import re
keep = []
if args.keep:
    print('-- reading regex file')
    for line in open(args.keep, 'rU'):
        r = re.compile(line.rstrip('\n'))
        print(r)
        keep.append(r)

def keep_match(name, regexs):
    if len(regexs) == 0:
        return False
    for r in regexs:
        if r.match(name):
            return True
    return False

from odps import ODPS
conf = parse_odps_config(args.odps)
o = ODPS(conf['access_id'], conf['access_key'], conf['project'], conf['endpoint'])

if args.run:
    print('>> CLEAN !!!')
else:
    print('>> dry run')

print('cleaning tables ...')
for t in o.list_tables():
    if keep_match(t.name, keep):
        continue
    print('drop table %s' % t.name)
    if args.run:
        t.drop()

print('cleaning functions ...')
for f in o.list_functions():
    if keep_match(f.name, keep):
        continue
    print('drop function %s' % f.name)
    if args.run:
        f.drop()

print('cleaning resources ...')
for r in o.list_resources():
    if keep_match(r.name, keep):
        continue
    print('drop resource %s' % r.name)
    if args.run:
        r.drop()

if args.instance:
    from odps.models import Instance
    print('cleaning instances ...')
    for i in o.list_instances():
        if i.status != Instance.Status.TERMINATED:
            print('kill instance %s' % i.name)
            if args.run:
                i.stop()

print('<< done')
