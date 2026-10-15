def word_count(text: str) -> dict[str, int]:
    text = text.lower()
    
    punctuations = ".,!?;:"
    for char in punctuations:
        text = text.replace(char, "")
        
    words = text.split()
    
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1  
        else:
            counts[word] = 1   
            
    return counts

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    
    counts = word_count(text)
    
    word_list = list(counts.items())
    
    word_list.sort(key=lambda item: item[0])
    
    word_list.sort(key=lambda item: item[1], reverse=True)
    
    return word_list[:k]


print(top_k("Git is fun. Git is fast!", 2))