class BinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def percUp(self, i):
        while i//2 > 0:
            if self.heap[i] < self.heap[i//2]:
                self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]

    def insert(self, k):
        self.heap.append(k)
        self.size += 1
        self.percUp(self.size)

    def percDown(self, i):
        while (i * 2) <= self.size:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.heap = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
