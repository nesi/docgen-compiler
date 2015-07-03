#!/usr/bin/python

# This is a work in progress, reimplementing makedoc1 in python.
# Python may be easier for managing module blacklists and mappings than
# shell script.

import os

progname = os.path.basename(__file__)
packagedir = os.path.dirname(__file__)
template = packagedir + "/Template.md"
tmpdir = "/tmp/nesi-makedoc1"
lockfile = "{}/lockfile".format(tmpdir)
versiondir = "{}/versions".format(tmpdir)
blurbdir = "{}/blurbs".format(tmpdir)

try:
    infodir = os.environ['NESIDOC_INFO_DIR']
    versiontabledir = os.environ['NESIDOC_VERSIONS_DIR']
    automoddir = os.environ['NESIDOC_AUTOMOD_DIR']
    suppmoddir = os.environ['NESIDOC_SUPPMOD_DIR']
except KeyError, ke:
    print "{}: error: the environment variable {} is not defined".format(progname,str(ke))
    raise SystemExit(1)

if os.path.realpath(automoddir) == os.path.realpath(suppmoddir):
    print """{}: error: the environment variables 'NESIDOC_AUTOMOD_DIR' and
'NESIDOC_SUPPMOD_DIR' must point to different directories""".format(progname)
    raise SystemExit(1)

# Create temporary directories and a lockfile if needed.
if os.path.lexists(tmpdir) and not os.path.isdir(tmpdir):
    print """{0}: error: {1} exists but is not a directory.
Please remove {1} or ask an administrator to do so.""".format(progname,tmpdir)

try:
    os.makedirs(versiondir)
    os.makedirs(blurbdir)
except OSError:
    pass

if os.path.lexists(lockfile):
    print """{0}: error: {1} exists.
Check to make sure that no other instance of {0} is running.
If necessary, remove {1} or ask an administrator to do so.""".format(progname,lockfile)
    raise SystemExit(1)
open(lockfile, 'w').close()

for modulelist in os.listdir(automoddir),os.listdir(suppmoddir):
    print modulelist

os.rmdir(versiondir)
os.rmdir(blurbdir)
os.remove(lockfile)
