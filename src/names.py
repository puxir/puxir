#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

import itertools

cc = {''.join(n) for n in itertools.permutations('bcdfghjlmnpqrstvxz', 3)
      }  # Letters 'k', 'w' and 'y' removed (aesthetics).
vv = {''.join(n) + '_' for n in itertools.permutations('aeiou', 2)
      }  # Vowels...

tmp = [list(zip(*[c, v])) for c in cc for v in vv]
lim, lt = 4999, len(tmp)
print('Some {0} random domain names from {1} total:'.format(lim, lt))
print()

names = [''.join([''.join(m) for m in n])[:-1] for n in tmp]
for n in sorted(names[:lim]): print(n + '.com')
print()
print('Availability & prices? [ namebright.com/BulkSearch ]')
