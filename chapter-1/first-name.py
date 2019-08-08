def first_name(name, titles):
    name1 = name.split()
    if member(name1[0], titles):
        name1.pop(0)
        name1 = first_name(" ".join(name1), titles)
        return name1
    return name1[0]

def member(x, l):
    for i in l:
        if x == i:
            return True
    return False
