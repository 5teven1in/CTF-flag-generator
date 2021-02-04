#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import random
import math

char_map = [
        ['A', 'a', '4', '@'],
        ['B', 'b', '8'],
        ['C', 'c'],
        ['D', 'd'],
        ['E', 'e', '3'],
	['F', 'f'],
	['G', 'g', '6', '9'],
	['H', 'h'],
	['I', 'i', '1'],
	['J', 'j'],
	['K', 'k'],
	['L', 'l', '1'],
	['M', 'm'],
	['N', 'n'],
	['O', 'o', '0'],
	['P', 'p'],
	['Q', 'q'],
	['R', 'r'],
	['S', 's', '5', '$'],
	['T', 't', '7'],
	['U', 'u'],
	['V', 'v'],
	['W', 'w'],
	['X', 'x'],
	['Y', 'y'],
	['Z', 'z', '2'],
        ]

def change(c):
    if c.isalpha():
        c = c.upper()
        char_set = char_map[ord(c) - ord('A')]
        new_c = char_set[random.randint(0, len(char_set) - 1)]
        return new_c, (c == new_c) * math.log2(len(char_set))
    else:
        return c, 0

def main():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("string", help = "origin flag string")
    args = parser.parse_args()
    entropy = 0
    for c in args.string:
        new_c, e = change(c)
        print(new_c, end = '')
        entropy += e
    print()
    print(f"Added entropy: {entropy:.2f} bits")

if __name__ == "__main__":
    main()
