def count_substring(string, sub_string):
    j = 0
    if len(sub_string)>len(string):
        return 0
    else:
        for i in range(0, len(string)-len(sub_string)):
            if string[i:i+len(sub_string)-1] == sub_string:
                j +=1
            else:
                continue               
    return j


print (count_substring("ABCDCDC", "CDC"))