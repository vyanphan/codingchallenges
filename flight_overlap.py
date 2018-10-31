'''
Given a list of scheduled flights, determine the
maximum number of flights in the air at anytime.

Assume all flights are given in one timezone.

	1:00	2:00	3:00	4:00	5:00
f1    |----------|
f2            |------------|
f3              |----------^-|
f4                 |  |      
f5                      |--^------|
f6                        |^----|  
f7                        |^----|
                           4 flights: f3, f5, f6, f7 overlap
'''


# Pseudocode: basically find the max overlap
# assume that time comparisons work, so 12pm < 1pm
def compute_overlap(s1, e1, s2, e2): # start/end times of two flights
	'''
	compute_overlap(1pm, 3pm, 2pm, 4pm)
	>>> (2pm, 3pm)
	compute_overlap(1pm, 3pm, 4pm, 5pm)
	>>> (4pm, 3pm)  // NOT ALLOWED
	'''
	start, end = max(s1, s2), min(e1, e2)
	if start < end:
		return (start, end)
	return (s2, e2)

def max_overlap(flights): # O(n^2)
	if len(flights) < 1:
		return 0


	overlaps = list(flights) # holds overlap time and amount
	while len(overlaps) > 1:
		new_overlaps = []
		for i in range(1, len(overlaps)):
			o1 = overlaps[i-1] # (o1.start, o1.end)
			o2 = overlaps[i]   # (o2.start, o2.end)
			new_overlaps += compute_overlap(o1[0], o1[1], o2[0], o2[1])
		overlaps = new_overlaps
	o_max = overlaps[0]

	ans = []
	for f in flights:
		if max(f[0], o_max[0]) < min(f[1], o_max[1]):
			ans += [f]
	return ans


'''
       0123456789012345678901234567
f1    |----------|
f2            |-----------^|
f3              |---------^--|
f4                 |--|
f5                     |--^|      
f6                      |-^-------|
f7                        ^-----|  
f8                        ^-----|

[12:       7-9,   23:      9-19,  34:     12-14, 45:    15-19, 56:   16-19, 67:  19-24, 78: 19-24]
[123:      9-9,   234:     12-14, 345:    12-14, 456:   16-19, 567:  19-19, 678: 19-24]
[1234:     12-14, 2345:    12-14, 3456:   16-19, 4567:  19-19, 5678: 19-19]
[12345:    12-14, 23456:   16-19, 34567:  19-19, 45678: 19-19]
[123456:   16-19, 234567:  19-19, 345678: 19-19]
[1234567:  19-19, 2345678: 19-19]
[12345678: 19-19]

(19-19): f1 no, f2 yes, f3 yes, f4 no, f5 yes, f6 yes, f7 yes, f8 yes
'''