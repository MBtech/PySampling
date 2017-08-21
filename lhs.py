import random
import numpy as np
import numpy.random
from pyDOE import *
import math
from collections import OrderedDict
import yaml
import decimal

#Roundoff to a multiple (Integer Version)
def roundInt(number, multiple):
    num = number + (multiple-1)
    return int(num - (num % multiple))

#Roundoff Float version
def roundFloat(number, multiple):
    places = abs(decimal.Decimal(str(multiple)).as_tuple().exponent)
    return round(round(number/multiple) * multiple, places)

#Check bounds to make sure that a number if not out of range
def checkBounds(number, start, end):
    if number<start:
        return start
    if number>end:
        return end    
    return number

class LHS:
    def __init__(self, yamlFile, criteria='maximin'):
        self.yamlFile = yamlFile 
        self.criteria = criteria
        fileRef = open(yamlFile, "r")
        self.bounds = self.ordered_load(fileRef, yaml.SafeLoader)
    
    def ordered_load(self, stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
         class OrderedLoader(Loader):
             pass
         def construct_mapping(loader, node):
             loader.flatten_mapping(node)
             return object_pairs_hook(loader.construct_pairs(node))
         OrderedLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,construct_mapping)
         return yaml.load(stream, OrderedLoader)

    def createSample(self, lhsSample, start,end, step, type):
         s = start+((end-start)*lhsSample)
         if step==0:
             s = checkBounds(s, start, end)
         elif type=='float':
             s = roundFloat(s, step)
             s = checkBounds(s, start, end)
         elif type=='int':
             s = roundInt(s, step)
             s = checkBounds(s, start, end)
         return s
        
    def createSamples(self, size):
        lhm = lhs(len(self.bounds), samples=size, criterion=self.criteria) 
        b = self.bounds
        samples = list(OrderedDict())
        for k in range(0, len(lhm)):
            i = 0
            ls = lhm[k]
            sample = OrderedDict()
            for c in self.bounds.keys():
                start = b[c]['start']
                end = b[c]['end']
                step = b[c]['step']
                type = b[c]['type']
                s = self.createSample(ls[i],start,end,step,type)
                i+=1  
                sample[c] = s
            samples.append(sample)
        self.samples = samples

    def getSamplesAsList(self):
        result=list()
        for sample in self.samples:
            result.append(sample.values()) 
        return result

    def getSamplesAsDict(self):
        result = self.samples
        return result
    
    def printYaml(self):
        print self.bounds

