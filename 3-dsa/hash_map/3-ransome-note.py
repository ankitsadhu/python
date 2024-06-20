def can_construct(ransom_notes: str, magazine: str) -> bool:
    char_freq = {}
    for char in magazine:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    

    for char in ransom_notes:
        if char in char_freq:
            char_freq[char] -= 1
            if char_freq[char] == 0:
                del char_freq[char]
        else:
            return False
        
    return True

def main():
    ransom_notes = [ 
         'aab',        
         'hello',        
         'letsgothere',        
         'weneedtogetitdone'    
    ]    

    magazines = [ 'abcva', 'helhoidde', 'edttsgftothsereleed', 'eunwueeydtwogyewbtitovnxe']

    for index, magazine in enumerate(magazines):
        print(f"ransom_notes = {ransom_notes[index]}, magazine= {magazine} {can_construct(ransom_notes[index], magazine)}")


if __name__ == "__main__":
    main()