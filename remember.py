#!/usr/bin/python
# -*- coding: utf-8 -*-
#Import our libraries
import argparse, os, subprocess, json
from subprocess import Popen, PIPE

#Here we begin parsing our arguments.
parser = argparse.ArgumentParser(description='Store notes in a dictionary.')
parser.add_argument('note', metavar='note', type=str, nargs='?', help='The note to save.  Put in between "".')
parser.add_argument('--list', help="List all notes.", dest="list", action="store_true", default=False)
parser.add_argument('--delete=', type=int, help="Delete a note based on number.", dest="delete", action="store", default=False)

#Here we initialize the arguments.
args = parser.parse_args()

#Here we try to open up our dictionary stored in a file, if it doesn't exist create a new one.
try:
    f = open('./.remember', 'r')
    m = json.loads(f.read())
    x = 0
    for key in m:
        x+=1
    x+=1
    f.close()
except (RuntimeError, TypeError, NameError, ValueError, AttributeError, IOError):
    m = {}
    x = 1

#If the list argument is used show all notes.
if args.list:
    for key, value in m.iteritems():
        print key + ": " + value
    exit(0)

#If the delete argument is used delete the # of the note.  The try except throws an exception of the note # does not exist.
if args.delete:
    try:
        del m["%s" % args.delete]
        print "Note " + str(args.delete) + " has been removed."
        f = open('./.remember', 'w+')
        f.write(json.dumps(m))
        f.close()
        exit(0)
    except:
        print "Note #%s does not exist." % args.delete
        exit(0)

#if neither one of the other 2 arguments are given, we save a note to our dictionary file.
m[x] = args.note
f = open('./.remember', 'w+')
f.write(json.dumps(m))
f.close()
