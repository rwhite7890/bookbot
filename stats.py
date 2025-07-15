def get_num_words(text):
    split_txt = text.split()
    num_words = len(split_txt)
    print(f"Found {num_words} total words")

def get_num_char(text):
    results = {}
    characters_list = list(text.lower())
    for character in characters_list:
        if character in results:
            results[character] += 1
        else:
            results[character] = 1
    return results 

def sort_on(items):
    return items["num"]    

def sort_dict(dict):
    sorted_dict = []
    
    for value in dict:
        if value.isalpha():
            new_dict = {"char": value, "num": dict[value]}
            sorted_dict.append(new_dict)
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict