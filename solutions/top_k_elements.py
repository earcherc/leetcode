def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Create hashmap of frequencies 
    freqs = {}
    for i in nums:
        if i in freqs:
            freqs[i] = freqs[i] + 1
        else:
            freqs[i] = 1

    def sift_up(index):
        # Using floor division to get thet index
        parent = (index - 1) // 2

        # While loop to make sure we trickle up to the top
        while index >  0 and heap[parent][0] < heap[index][0]:
            # Swap positions
            tmp = heap[parent]
            heap[parent] = heap[index]
            heap[index] = tmp

            # Move index up a level for next iteration
            index = parent
            parent = (index - 1) // 2

    heap = []

    # Iterate over items 
    for key,value in freqs.items():
        # Convert item to tuple and add to last index of array
        # Insert item to heap
        heap.append((value,key))
        
        # Use sift up to correclty position the last node
        sift_up(len(heap) - 1)

    def heapify_down():
        # Swap root and last item
        tmp = heap[len(heap) - 1]
        heap[len(heap) - 1] = heap[0]
        heap[0] = tmp

        # Remove the last item of list
        heap.pop()

        max_index = len(heap) - 1
        index = 0
        left_child = 1
        right_child = 2

        if max_index == left_child and (heap[index][0] < heap[left_child][0]):
            tmp = heap[index]
            heap[index] = heap[left_child]
            heap[left_child] = tmp

            # update the index
            index = left_child
            left_child = (index * 2) + 1
            right_child = (index * 2) + 2
            
            return

        # While loop to trickle the root node into correct position
        while (max_index >= right_child) and (heap[index][0] < heap[left_child][0] or heap[index][0] < heap[right_child][0]):
            current_node = heap[index]

            # if the right node is larger
            if heap[left_child] > (heap[right_child] or current_node):
                # swap with the left child
                tmp = current_node
                heap[index] = heap[left_child]
                heap[left_child] = tmp

                # update the index
                index = left_child
                left_child = (index * 2) + 1
                right_child = (index * 2) + 2

            else:
                # swap right node with parent
                tmp = current_node
                heap[index] = heap[right_child]
                heap[right_child] = tmp

                # update the index
                index = right_child
                left_child = (index * 2) + 1
                right_child = (index * 2) + 2                    

    # Now we need to get the k most freq
    result = []
    for i in range(k):
        result.append(heap[0][1])

        print(heap)
        
        heapify_down()

    return result
