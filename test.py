#!/usr/bin/env python3
import pycococreatortools as pct
home = "/home/fares/testmask/shapes/train/"
pct.cut2trte(home+"/shapes_train2018", home+"/annotation", home+"/cut", rm=True)