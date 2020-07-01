def tokenc(code):
    print(type(code))
    listg = code.split()
    listg=''.join(listg)
    print(type(listg))
    lis=listg.split("\n")
    lis=''.join(lis)
    ll=lis.split("\t")
    ll=''.join(ll)
    l=ll.split("\r")
    l=''.join(l)
    c=l.replace("(", " ( ").replace(")", " ) ")
    ret_list = []
    print(c)
    c=c.split()
    print(c)
    for i in range(len(c)):
        if len(c[i]) > 0:
            ret_list.append(c[i])
        i+=1
    return ret_list
l=tokenc("print('vg')")
