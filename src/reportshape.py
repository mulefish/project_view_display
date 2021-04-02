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
