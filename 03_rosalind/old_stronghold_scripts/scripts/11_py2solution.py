#!/usr/bin/env python

n = 90
k = 17

f = [1]*100

for i in xrange(2,n):
	f[i] = f[i-1] + f[i-2]

	if i >= k:
		f[i] -= f[(i-k)-1]
	
print(f[i])
