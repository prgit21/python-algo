def count_substring(string, sub_string):
    c= 0
    while sub_string in string:
        c=c+1
        string = string[string.find(sub_string)+1:]     #reduces time compleexity to make it work idk how
        
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
