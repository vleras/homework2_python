# Write code to:
# •	Count how many times each word appears 
# •	Output result as a dictionary 
# •	Ignore case sensitivity 
text = "Data pipelines are important because data is everywhere and data is growing"

def word_count(text):
    if not text.strip():
        return "Text is empty"
    
    words = text.lower().split()  
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(word_count(text))
