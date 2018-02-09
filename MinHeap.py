import sys

class MinHeap:    
    def __init__(self,list):
        self.internalStorage = [-1 for x in range(10000)]
        self.size = 0
        for i in range(0,len(list)):
            self.put(list[i])

    def is_empty(self):
        return self.size <= 0
    
    def heapify(self):
        current = 0
        min = current
        while True:
            left = self.__get_left_child_index__(min)
            right = self.__get_right_child_index__(min)            
            if left != -1 and self.internalStorage[min][0] > self.internalStorage[left][0]:
                min = left
            if right != -1 and self.internalStorage[min][0] > self.internalStorage[right][0]:
                min = right
            if min != current:
                self.__switch_nodes__(min,current)        
                current = min       
            else:
                break

    def __switch_nodes__(self,node1,node2):
        temp = self.internalStorage[node1]
        self.internalStorage[node1] = (self.internalStorage[node2][0],self.internalStorage[node2][1])
        self.internalStorage[node2] = temp

    def extract_min(self):
        min = self.internalStorage[0] if self.size > 0 else -1
        if min != -1:            
            if self.size > 0:
                self.internalStorage[0] = (self.internalStorage[self.size-1][0],self.internalStorage[self.size-1][1])
                self.size -= 1
                self.heapify()
        return min

    def put(self,item):
        self.size += 1
        self.internalStorage[self.size-1] = item
        self.__move_up___(self.size-1)

    def __move_up___(self,i):
        current = i        
        while True:
            parent = self.__get_parent_index__(current)
            if parent != -1 and self.internalStorage[current][0] < self.internalStorage[parent][0]:
                self.__switch_nodes__(current,parent)
                current = parent
            else:
                break

    def decrease_key(self, key, value):
        for i in range(0,self.size):
            if self.internalStorage[i][1] == key:
                self.internalStorage[i] = (value,key)
                self.__move_up___(i)
                break
        

    def __get_parent_index__(self,index):
        parentIndex = (index - 1) / 2
        return int(parentIndex) if parentIndex >= 0 else -1

    def __get_left_child_index__(self,index):
        leftIndex = (2 * index) + 1
        return leftIndex if leftIndex < self.size else -1  

    def __get_right_child_index__(self,index):
        rightIndex = (2 * index) + 2
        return rightIndex if rightIndex < self.size else -1
