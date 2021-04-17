import fnmatch
import os
import json
from letters import getLetterFromNumber

pattern = "*.js"
rootPath = "../src/"
ignore = ["", ".."]


class Node:
    def __init__(self, l, dir):
        self.l = l
        self.dir = dir
        self.ary = dir.split("|")

    # def show(self):
    #     r = "{}|{}".format(self.l, self.dir)
    #     return r


class Parent:
    def __init__(self, base):
        self.base = base
        self.children = []

    def addKid(self, kid):
        self.children.append(kid)

    def show(self):
        return {
            self.base: self.children
        }


def getMaxDepth(ary_of_objs):
    most = 0
    for x in ary_of_objs:
        if len(x.ary) > most:
            most = len(x.ary)
    return most


def readFS_makeDotGraph():
    step1 = []
    i = 0
    for root, dirs, files in os.walk(rootPath):
        root = root.replace(os.sep, "|")
        l = getLetterFromNumber(i)
        for filename in fnmatch.filter(files, pattern):
            x = "{}|{}".format(root, filename)
            # print("{}     {}".format(family, x))
            step1.append(Node(l, x))
    deepest = getMaxDepth(step1)

    generations = []
    for j in range(1, deepest):
        map = {}
        for n in step1:
            if j < len(n.ary):
                a = n.ary[j - 1]
                b = n.ary[j]
                # print(a, b)
                if a not in ignore:
                    if a not in map:
                        p = Parent(a)
                        map[a] = p
                    map[a].addKid(b)
        # print("...")
        generations.append(map)
    for map in generations:
        for k in map:
            print("|{}|".format(k))
            # print(map[k].show())


if __name__ == "__main__":
    readFS_makeDotGraph()
