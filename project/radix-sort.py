import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    words = book_to_words()
    sort = radix_sort(words)
    copy = words
    copy.sort()
    # testing
    if sort is copy:
        print("sucess")
    else:
        for i in range(len(sort)):
            if sort[i] != copy[i]:
                print(sort[i] + " " + copy[i])
        print("fail")
def radix_sort(lst):
    m = len(max(lst,key=len))
    for i in range(m):
        c_sort(lst,i)
    return lst
        
def c_sort(lst,length):
    m = 0
    for i in range(len(lst)):
        try:
            idx = ord(str(lst[i])[length])
        except:
            idx = -1
        m = max(idx,m)
    lst_count = [0]*(m+1)
    lst_count[-1] = 0
    end = [None]*len(lst)
    for i in range(len(lst)):
        try:
            c = str(lst[i])[length]
        except:
            lst_count[-1]+=1
    for i in range (1,m):
        lst_count[i] = lst_count[i]+lst_count[i-1]
    for i in range(len(lst)):
        try:
            idx = ord(str(lst[i])[length])
        except:
            i = -1
        x = lst_count[idx]-1
        end[x] = lst[i]
        lst_count[idx]-=1
    return end
radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt')