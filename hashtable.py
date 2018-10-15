class HashTable:
	def __init__(self, size, fill_factor):
		self.fill_factor = fill_factor
		self.fill = 0
		self.table = [[] for _ in range(size)]

	def resize(self):
		self.fill = 0
		newTable = [[] for _ in range(len(self.table) * 2)]
		for bucket in self.table:
			for item in bucket:
				newBucket = newTable[item[0] % len(newTable)]
				if newBucket == []:
					self.fill += 1
				newBucket.append(item)
		self.table = newTable

	def add(self, k, v):
		bucket = k % len(self.table)
		if self.table[bucket] == []:
			self.fill += 1
		self.table[bucket].append((k, v))
		if self.fill / len(self.table) > self.fill_factor:
			self.resize()

	def get(self, k):
		bucket = k % len(self.table)
		for item in self.table[bucket]:
			if item[0] == k:
				return item[1]
		return None

	def remove(self, k):
		bucket = k % len(self.table)
		for item in self.table[bucket]:
			if item[0] == k:
				self.table[bucket].remove(item)
				if self.table[bucket] == []:
					self.fill -= 1
				return item[1]
		return None

	def toString(self):
		ans = ""
		for bucket in range(len(self.table)):
			ans += str(bucket) + ':\t' + str(self.table[bucket]) + "\n"
		return ans


# testing
ht = HashTable(7, 0.5);
for i in range(10):
	ht.add(i**2, i)
print(ht.toString())

print(ht.get(16));
print(ht.remove(16));
print(ht.fill)
print(ht.get(16));
print(ht.remove(16));

print(ht.remove(36));
print(ht.fill)
print();

ht.add(36, 36);
ht.add(28, 28);
print(ht.fill)
print(ht.toString())
