

import re

def deEmojify(text):
    regrex_pattern = re.compile(
        pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                        "]+", 
        flags = re.UNICODE)
    return regrex_pattern.sub(r'', text)
    
if __name__ == "__main__":
    
    text1 = u'This is a smiley face \U0001f602'
    text2 = "happy Halloween � 😭"

    
    print(text1) # with emoji
    print(deEmojify(text1))
    print(text1.encode("utf-8"))
    print(text2) # with emoji
    print(deEmojify(text2))
    print(text2.encode("utf-8"))