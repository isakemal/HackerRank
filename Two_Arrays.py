# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for i in xrange(t):
	n, k = map(int,raw_input().split())
	a = sorted(map(int,raw_input().split()))
	b = sorted([k-x for x in map(int,raw_input().split())])
	print 'YES' if len([i for i in xrange(n) if a[i]-b[i]<0])==0 else 'NO'
			    
			      
