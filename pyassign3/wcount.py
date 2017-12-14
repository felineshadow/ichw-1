#!/usr/bin/env python3

"""wcount.py: to count the words of the file derived from the Internet .

__author__ = "XiongJie"
__pkuid__  = "1700011827"
__email__  = "xiongjie1999@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines,topn=10):
    """count words from lines of text string, then sort by their counts
        in reverse order, output the topn (word count), each in one line.
        """
    
    text = lines.lower()
    text = text.split()
    new_text = []
    for string in text:
        new_string=''
        for i in string:
            if 97 <= ord(i) <= 122:
                new_string += i
            
        new_text.append(new_string)
    
    counts = {}
    for word in new_text:
        counts[word] = counts.get(word,0) + 1
    del counts['']
    ##to delete blank unnecessary
    new_counts = [(v, k) for (k, v) in counts.items()]
    new_counts.sort(reverse=True)
    list_to_be_printed = new_counts[:topn]
    ##to get the top n words in a list
    for (a,b) in list_to_be_printed:
        print(b,'\t\t',a)


if __name__ == '__main__':
    
    ##to comfirm the output
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    
    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)
    
    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)







