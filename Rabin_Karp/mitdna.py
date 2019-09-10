
#
# Simple FASTA-reading library
# Copyright 2010 Kevin Kelley <kelleyk@kelleyk.net>
#
# Provided under the MIT license: yours gratis,
# and if it breaks, you get to keep both pieces.
#

import unittest

# An iterator that returns the nucleotide sequence stored in the given FASTA file.
class FastaSequence:
    def __init__(self, filename):
        self.f = open(filename, 'r')
        self.buf = ''
        self.info = self.f.readline()
        self.pos = 0
    def __iter__(self):
        return self
    def next(self):
        while '' == self.buf:
            self.buf = self.f.readline()
            if '' == self.buf:
                self.f.close()
                raise StopIteration
            self.buf = self.buf.strip()
        nextchar = self.buf[0]
        self.buf = self.buf[1:]
        self.pos += 1
        return nextchar

def getSequenceLength(filename):
    seq = FastaSequence(filename)
    n = 0
    for x in seq:
        n += 1
    return n

# Returns all subsequences of length k in seq.
def subsequences(seq, k):
    try:
        subseq = ''
        while True:
            while len(subseq) < k:
                subseq += seq.next()
            yield subseq
            subseq = subseq[1:]
    except StopIteration:
        return

# Simple sanity checks
class TestKFASTA(unittest.TestCase):
    def test_readseq(self):
        seq = FastaSequence('trivial.fa')
        seqstr = ''
        for c in seq:
            seqstr += c
        self.assertTrue('ABCDEFGHIJKLMNOPQRSTUVWXYZ' == seqstr)
    def test_subseq(self):
        seq = FastaSequence('trivial.fa')
        i = 0
        for subseq in subsequences(seq, 3):
            print subseq
            i += 1
        self.assertTrue(24 == i)
#if __name__ == '__main__':
#    unittest.main()
from dnaseq import *

### Testing ###

class TestRollingHash(unittest.TestCase):
    def test_rolling(self):
        rh1 = RollingHash('CTAGC')
        rh2 = RollingHash('TAGCG')
        rh3 = RollingHash('AGCGT')
        rh1.slide('C','G')
        self.assertTrue(rh1.current_hash() == rh2.current_hash())
        rh1.slide('T','T')
        self.assertTrue(rh1.current_hash() == rh3.current_hash())

class TestMultidict(unittest.TestCase):
    def test_multi(self):
        foo = Multidict()
        foo.put(1, 'a')
        foo.put(2, 'b')
        foo.put(1, 'c')
        self.assertTrue(foo.get(1) == ['a','c'])
        self.assertTrue(foo.get(2) == ['b'])
        self.assertTrue(foo.get(3) == [])

# This test case may break once you add the argument m (skipping).
class TestExactSubmatches(unittest.TestCase):
   def test_one(self):
       foo = 'yabcabcabcz'
       bar = 'xxabcxxxx'
       matches = list(getExactSubmatches(iter(foo), iter(bar), 3, 1))
       correct = [(1,2), (4,2), (7,2)]
       self.assertTrue(len(matches) == len(correct))
       for x in correct:
           self.assertTrue(x in matches)

unittest.main()



#!/usr/bin/env python2.7

import unittest
from dnaseqlib import *

### Utility classes ###

# Maps integer keys to a set of arbitrary values.
class Multidict:
    # Initializes a new multi-value dictionary, and adds any key-value
    # 2-tuples in the iterable sequence pairs to the data structure.
    def __init__(self, pairs=[]):
        raise Exception("Not implemented!")
    # Associates the value v with the key k.
    def put(self, k, v):
        raise Exception("Not implemented!")
    # Gets any values that have been associated with the key k; or, if
    # none have been, returns an empty sequence.
    def get(self, k):
        raise Exception("Not implemented!")

# Given a sequence of nucleotides, return all k-length subsequences
# and their hashes.  (What else do you need to know about each
# subsequence?)
def subsequenceHashes(seq, k):
    raise Exception("Not implemented!")

# Similar to subsequenceHashes(), but returns one k-length subsequence
# every m nucleotides.  (This will be useful when you try to use two
# whole data files.)
def intervalSubsequenceHashes(seq, k, m):
    raise Exception("Not implemented!")

# Searches for commonalities between sequences a and b by comparing
# subsequences of length k.  The sequences a and b should be iterators
# that return nucleotides.  The table is built by computing one hash
# every m nucleotides (for m >= k).
def getExactSubmatches(a, b, k, m):
    raise Exception("Not implemented!")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: {0} [file_a.fa] [file_b.fa] [output.png]'.format(sys.argv[0])
        sys.exit(1)

    # The arguments are, in order: 1) Your getExactSubmatches
    # function, 2) the filename to which the image should be written,
    # 3) a tuple giving the width and height of the image, 4) the
    # filename of sequence A, 5) the filename of sequence B, 6) k, the
    # subsequence size, and 7) m, the sampling interval for sequence
    # A.
    compareSequences(getExactSubmatches, sys.argv[3], (500,500), sys.argv[1], sys.argv[2], 8, 100)


import sys
import math
import kfasta
from array import array
try:
    from PIL import Image
except ImportError:
    print "You don't have PIL (the Python Imaging Library) installed."
    print "Please check README.txt for instructions on how to install PIL."
    sys.exit(-1)

# Produces hash values for a rolling sequence.
class RollingHash:
    def __init__(self, s):
        self.HASH_BASE = 7
        self.seqlen = len(s)
        n = self.seqlen - 1
        h = 0
        for c in s:
            h += ord(c) * (self.HASH_BASE ** n)
            n -= 1
        self.curhash = h

    # Returns the current hash value.
    def current_hash(self):
        return self.curhash

    # Updates the hash by removing previtm and adding nextitm.  Returns the updated
    # hash value.
    def slide(self, previtm, nextitm):
        self.curhash = (self.curhash * self.HASH_BASE) + ord(nextitm)
        self.curhash -= ord(previtm) * (self.HASH_BASE ** self.seqlen)
        return self.curhash

# A simple 2D integer array implementation on top of Python's built-in 1D array.
class Array2D:
    def __init__(self, typecode, w, h, defaultval):
        self.arr = array(typecode, [defaultval]*(w*h))
        self.w = w
        self.h = h
    def put(self, x, y, v):
        assert x >= 0 and x < self.w
        assert y >= 0 and y < self.h
        self.arr[(y*self.w)+x] = v
    def incr(self, x, y):
        assert x >= 0 and x < self.w
        assert y >= 0 and y < self.h
        self.arr[(y*self.w)+x] += 1
    def get(self, x, y):
        assert x >= 0 and x < self.w
        assert y >= 0 and y < self.h
        return self.arr[(y*self.w)+x]
    def max(self):
        return max(self.arr)

### High-level driver code.  You shouldn't have to tweak this. ###

# Given a sequence of matches, produces a w-by-h image and saves it to filename.
# The remapping function takes values in (0,1) and returns values in (0,1); the default
# value (fourth-root) makes lightly-populated bins considerably darker.
def buildComparisonImage(filename, w, h, alen, blen, matches, remapfn=lambda x:math.sqrt(math.sqrt(x))):
    arr = Array2D('L', w, h, 0L)
    print "Sequence A length: " + str(alen)
    print "Sequence B length: " + str(blen)
    abinsize = int(math.ceil(alen / float(w)))
    bbinsize = int(math.ceil(blen / float(h)))
    assert abinsize > 0 and bbinsize > 0
    print "Binning matches..."
    for m in matches:
        #print m, (abinsize, bbinsize), (m[0]//abinsize, m[1]//bbinsize), (w, h)
        arr.incr(m[0] // abinsize, m[1] // bbinsize)
    print "...done binning matches."
    print "Normalizing and plotting results..."
    maxval = float(arr.max())
    img = Image.new('RGB', (w,h))
    for y in range(0, h):
        for x in range(0, w):
            val = 255 - int(math.ceil(remapfn((arr.get(x,y) / maxval)) * 255.0))
            img.putpixel((x,y), (val,val,val))
    print "...done normalizing and plotting."
    img.save(filename)

def compareSequences(getExactSubmatches, imgfile, imgsize, afile, bfile, k, m):
    a = kfasta.FastaSequence(afile)
    b = kfasta.FastaSequence(bfile)
    matches = getExactSubmatches(a, b, k, m)
    buildComparisonImage(imgfile, imgsize[0], imgsize[1],
                         kfasta.getSequenceLength(afile),
                         kfasta.getSequenceLength(bfile), matches)


