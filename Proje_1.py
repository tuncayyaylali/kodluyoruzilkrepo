def flatten_list(l):
    flat_list = []
    for element in l:
        if type(element) is list:
            for item in element:
                if type(item) is list:
                    for iten in item:
                        if type(iten) is list:
                            for iteo in iten:
                                flat_list.append(iteo)
                        else:
                            flat_list.append(iten)
                else:
                    flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(f"input: {flatten_list(liste)}\noutput: {flatten_list(liste)}")