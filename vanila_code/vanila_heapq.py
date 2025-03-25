class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2 # 부모 노드 계산
    
    def left_child(self, index):
        return 2*index + 1 # 왼쪽 자식
    
    def right_child(self, index):
        return 2*index + 2 # 오른쪾 자식
    
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap)-1) # heapify up 수행

    def _heapify_up(self, index):
        # 부모 노드가 값이 더 작도록 설정
        # 값이 넣어질 때는 위에서 밑으로 확인함
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def extract_min(self):
        # 힙에서 죄소값 제거하고 정렬 유지
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return root_value
    
    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        # 값을 뺄대는 밑에서 위로 확인함

        # 왼쪽 자식이 존재하고, 현재 노드 보다 작으면 갱신
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def display(self):
        print(self.heap)

if __name__ == '__main__':
    heap = MinHeap()
    example = [5, 3, 8, 1, 2]

    for e in example:
        heap.insert(e)
    
    heap.display()
    print('\n 최소값 제거:', heap.extract_min())
    print('\n 최소값 제거:', heap.extract_min())
    heap.display()