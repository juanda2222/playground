

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
    
    text2 = "happy Halloween �😭"

    text = u'This is a smiley face \U0001f602'
    print(text) # with emoji

    

    print(deEmojify(text))