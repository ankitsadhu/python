from collections import Counter
a = "aaaabbbccc"
my_counter = Counter(a)
print(my_counter.items()) # dict_items([('a', 4), ('b', 3), ('c', 3)])
print(my_counter.keys()) # (['a', 'b', 'c'])
print(my_counter.values()) # ([4, 3, 3])
print(my_counter.most_common(1)[0]) #('a', 4)

def longest_palindrome(s):
    char_count = Counter(s)
    length = 0

    for count in char_count.values(): # abccccdd -> ([1, 1, 4, 2])
        length += count

    if length < len (s):
        print(f"---> {s}")
        length += 1

    return length


def main():
    input_string = ["abccccdd", "abcdefg", "BbBbBbBb", "REaccaR", "AbcDeFGhAachDeFG"]

    for i in range(len(input_string)):        
        print(i + 1, ".\tInput string: '", input_string[i], "'", sep="")        
        print("\tLength of longest palindrome is: ", longest_palindrome(input_string[i]), sep="")        
        print("-" * 100)
        
if __name__ == "__main__":    main()