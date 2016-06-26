# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for i in xrange(t):
	n, k = map(int,raw_input().split())
	a = sorted(map(int,raw_input().split()))
	b = sorted(map(int,raw_input().split()), reverse=True)
	print 'YES' if min([x+y for x,y in zip(a, b)])>=k else 'NO'
			      
