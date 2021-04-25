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

    def show(self):
        r = "{}|{}".format(self.l, self.dir)
        return r


class Parent:
    def __init__(self, base):
        self.base = base
        self.children = []

    def addKid(self, kid):
        if kid not in self.children:
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


def step1_gatherData():
    step1 = []
    i = 0
    for root, dirs, files in os.walk(rootPath):
        # root = root.replace(os.sep, "|")
        l = getLetterFromNumber(i)
        i += 1
        for filename in fnmatch.filter(files, pattern):
            x = "{}|{}".format(root, filename)
            x = x.replace(os.sep, "|")
            x = x.replace("||", "|")
            # print(x)
            step1.append(Node(l, x))
    return step1


def step2_makeGenerations(deepest, results_from_step1):
    generations = []
    for j in range(1, deepest):
        map = {}
        for n in results_from_step1:
            if j < len(n.ary):
                a = n.ary[j - 1]
                b = n.ary[j]
                if a not in ignore:
                    if a not in map:
                        p = Parent(a)
                        map[a] = p
                    map[a].addKid(b)
        generations.append(map)
    return generations


def step3_emit_raw_graph(generations):
    collect = "["
    # for g in generations:
    for i in range(len(generations)):
        g = generations[i]

        for nodeFrom in g:
            # print(nodeFrom)
            parent = g[nodeFrom]
            # nodeFrom = parents
            for nodeTo in parent.children:
                # collect += "('{}','{}'),".format(nodeFrom, nodeTo)
                print("('{}','{}'),".format(nodeFrom, nodeTo))
    # collect += "]"
    # print(collect)
    # print("{} {}".format(i, parent.base))
    # print("{}".format(parent.base))
    # for kid in parent.children:
    #     print("\t" + kid)


if __name__ == "__main__":
    step1 = step1_gatherData()
    deepest = getMaxDepth(step1)
    generations = step2_makeGenerations(deepest, step1)
    step3_emit_raw_graph(generations)

    # parent = generations[1]["src"]
    # print(parent.show())
    # print(parent)
    # for g in generations:
    #     for k in g:
    #         p = g[k]
    #         print(p.show())
