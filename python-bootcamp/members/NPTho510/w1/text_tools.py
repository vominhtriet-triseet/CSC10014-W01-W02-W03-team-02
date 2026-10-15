def word_count(text: str) -> dict[str, int]: 
    result = {}
    text1 = text + ' '
    temp = ''
    
    for i in text1:
        if i in {'.', '!', '?', ';', ':'}:
            continue
        
        if i == ' ':
            if temp:
                result[temp] = result.get(temp, 0) + 1
                temp = ''
            continue
        temp += i.lower()
    
    return result
    
def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)

    sorted_counts = sorted(counts.items(),key=lambda item: (-item[1], item[0]))

    return sorted_counts[:k] 
    
temp1 = top_k("hooh haah hooh hiih heeh haah", 2)
print(temp1)