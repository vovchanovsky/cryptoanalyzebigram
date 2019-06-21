# -*- coding: cp1251 -*-
from collections import Counter
from math import log
from fractions import gcd
from random import randint
from heapq import nlargest
alphabet = "абвгдежзийклмнопрстуфхцчшщыьэюя"
fqbigrams = ["ст", "но", "то", "на", "ен"]
clrtxt = 'clear_text.txt'

def fread(filename):
    file = open(filename)
    text = file.read()
    file.close()
    return text

def clear_text():
    string = fread('text.txt').lower().replace('ё','е').replace('ъ', 'ь')
    for i in string:
        if not(i in alphabet):
            string = string.replace(i, '')
    clear_file = open(clrtxt, 'w')
    clear_file.write(string)
    clear_file.close()
    print('Text cleaned and saved successfully.')
    
def bgToNum(element):
    return alphabet.index(element[0])*len(alphabet)+alphabet.index(element[1])
    
def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
    
def linear_comparison(a, b, n):
    x =[]
    if gcd(a,n) == 1:
        x.append((findModInverse(a, n)*b) % n)
    elif gcd(a,n)= d > 1:
        if b%d!=0:
            return;
        else:
            n1 = n/d
            x0=(b/d*findModInverse(a/d, n))%n1
            for i in range(d):
                x.append(x0+i*n1)
    return x

def findkey(bigrams, y):
    y1 = y[0]
    y2 = y[1]
    a = (findModInverse(bgToNum(fqbigrams[1])-bgToNum(fqbigrams[0]), pow(len(alphabet),2))*(bgToNum(y2)-bgToNum(y1))) % pow(len(alphabet),2)
    b = (bgToNum(y1) - a*bgToNum(fqbigrams[0])) % pow(len(alphabet),2)
    decode(bigrams, a, b)

def freq(bigrams):
    c = Counter()
    for word in bigrams:
        c[word] += 1
    sum1=sum(c.values())
    print 'Sum bg:', sum1
    d = {}
    for i in alphabet:
        mas = []
        for j in alphabet:
            if i+j in c.keys():
                d.update({i+j:(c[i+j] / float(sum1))})
            else:
                d.update({i+j:0})
    for p in nlargest(5, d, key=d.get):
        print p
    return realfindkey(bigrams, nlargest(5, d, key=d.get))
	
def count(filename):
    string = fread(filename)
    print 'Bigrams:'
    bigrams = []
    for j in range(0, len(string)-1, 2):
        bigrams.append(string[j]+string[j+1])
    return freq(bigrams)
        
#clear_text()
#decode(clrtxt)
