class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += str(len(word)) + '#' + word

        return string


    def decode(self, s: str) -> List[str]:
        # ok so how are we going to decode this
        # we iterate through the string until we find our delimiter
            # we know its index and so we assume the previous index is of type number
            # we take a slice from the delimiter index + the number index and append this string to an arary
            # repeat the loop until the next delimter

        print(s)
        array = []
        starting_index = 0
        for i, char in enumerate(s):
            if char == '#' and i >= starting_index and starting_index < len(s):
                previous_char = s[starting_index:i]
                word_size = int(previous_char)
                final_index = i + 1 + word_size
                word = s[i + 1 : final_index]
                array.append(word)
                starting_index = final_index
        
        return array



