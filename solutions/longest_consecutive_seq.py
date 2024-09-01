class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # This is tricky
        # Could we do this with a binary search tree?
        # best case building a tree is n log n because of the sorting?

        # I think we need to keep track of things
        # O(n) time makes me think it has to be simple 
        # we create a hashmap with all the items
        # hashmap is unordered
        # we loopthrough again 
        # with each number we do an instant lookup to see if there is a next number in the sequence
        # we keep track of longest_seq[], current_seq[], starting_from
        # for key, value in hashmap.items:
            # add current number from hashmap to current_seq
            # current_num = value
            # while True
                # if there is a next number
                    # add next number current_seq the amount of times it's counted, update current_number to next_number 
                # if there isn't
                    # set longest_seq to current_seq
                    # reset current_seq
                    # break 


        map = {}
        for i in nums:
            map[i] = 1
        
        current_seq = []
        longest_seq = []

        for key in map.keys():
            current_seq.append(key)
            current_num = key
            while True:
                next_key = current_num + 1
                if next_key in map:
                    current_num = next_key
                    current_seq.append(next_key)
                else:
                    if len(current_seq) > len(longest_seq):
                        longest_seq = current_seq
                        current_seq = []
                    else:
                        current_seq = []
                    break

        return len(longest_seq)
