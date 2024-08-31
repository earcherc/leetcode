class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # So we solved with a max heap which wasn't ideal
        # A min heap is ideal because it allows us to minimise sorting operations

        freqs = {}
        for i in nums:
            if i in freqs:
                freqs[i] = freqs[i] + 1
            else:
                freqs[i] = 1

        # heapify up 
        def heapify_up(index): 
            parent = (index - 1) // 2

            # trickle the node up until heap conditions satisfied
            while index > 0 and (heap[parent][0] > heap[index][0]):
                # Swap parent and current node
                tmp = heap[parent]
                heap[parent] = heap[index]
                heap[index] = tmp

                # increment counter
                index = parent
                parent = (index - 1) // 2

        # heapify down
        def heapify_down(index):
            max_index = len(heap) - 1

            while True:
                smallest = index
                left_child = 2 * index + 1
                right_child = 2 * index + 2

                # check if left child is smaller than current element 
                if left_child <= max_index and heap[left_child][0] < heap[smallest][0]:
                    smallest = left_child
                
                # check and overwrite if right child is smaller than left child
                if right_child <= max_index and heap[right_child][0] < heap[smallest][0]:
                    smallest = right_child
                
                # if we remain the smallest after these checks, break the loop
                if smallest == index:
                    break

                # swap the smallest and the index                
                tmp = heap[index]
                heap[index] = heap[smallest]
                heap[smallest] = tmp

                index = smallest
                
        heap = []
        for key, value in freqs.items():
            tuple = (value, key)
            if len(heap) < k:
                heap.append(tuple)
                heapify_up(len(heap) - 1)
            else:
                if tuple[0] > heap[0][0]:
                    heap[0] = tuple
                    heapify_down(0)
        
        result = []
        for x in heap:
            result.append(x[1])

        return result
