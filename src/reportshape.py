# TODO: Convert this to DOT graphvis
import fnmatch
import os
pattern = '*.js'
rootPath = '.'
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        x = os.path.join(root, filename)
        x = x.replace('.', 'src')
        print(os.path.join(x, filename))


#
#  xxxxx> yyyyy: re: Python - I've used the same snippet for years to wrap os.walk: `def allfiles(top): for root, dirs, files in os.walk(top): for fname in files: yield               os.path.join(root, fname)`
#
#
