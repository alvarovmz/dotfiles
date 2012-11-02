# This file is part of alvarovmz's dotdfiles
# Alvaro Vila <alvarovmz@gmail.com>

import os
from optparse import OptionParser
import fnmatch


def link(source, dest):
    try:
        os.symlink(source, dest)
        print "Created: ", dest
    except OSError:
        print 'Detected existing: "%s"' % dest


def install(option, opt, value, parser):
    print "Installing..."

    HOME = os.environ['HOME']
    CURRENT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    for root, dirnames, filenames in os.walk(CURRENT):
        if ".git" in dirnames:
            dirnames.remove(".git")
        for filename in fnmatch.filter(filenames + dirnames, '*.symlink'):
            link(os.path.join(root, filename),
                 os.path.join(HOME, "." + filename.split(".")[0]))


def uninstall(option, opt, value, parser):
    print "Uninstalling..."


parser = OptionParser()
parser.add_option("-i", "--install", help="Install environment",
                  action="callback", callback=install)
parser.add_option("-u", "--uninstall", help="Unnstall environment",
                  action="callback", callback=uninstall)

(options, arguments) = parser.parse_args()
