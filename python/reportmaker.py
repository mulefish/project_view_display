import fnmatch
import os
import json
from letters import getLetterFromNumber

pattern = "*.js"
rootPath = "../src/"


# class Node:
#     def __init__(self, a, b, family, letter):
#         self.a = a
#         self.b = b
#         self.family = family
#         self.letter = letter

#     def show(self):
#         x = {
#             "a": self.a,
#             "b": self.b,
#             "l": self.letter,
#             "f": self.family
#         }
#         return json.dumps(x)


def readFS_makeDotGraph():
    nodes = []
    k = 0
    i = 0
    for root, dirs, files in os.walk(rootPath):
        root = root.replace(os.sep, "|")
        obj = {}
        obj["id"] = getLetterFromNumber(i)
        obj["dir"] = root
        # print("{}".format(obj))
        i += 1
        for filename in fnmatch.filter(files, pattern):
            x = "{}|{}".format(root, filename)
            print("{}     {}".format(i, x))


if __name__ == "__main__":
    readFS_makeDotGraph()
