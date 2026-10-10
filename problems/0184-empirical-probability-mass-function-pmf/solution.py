def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    term_count_dict={}
    for i in samples:
        if i in term_count_dict.keys():
            term_count_dict[i]+=1
        else:
            term_count_dict[i]=1
    list_a=[[k,v] for k,v in term_count_dict.items()]
    for i in range(len(list_a)):
        list_a[i][1]=list_a[i][1]/len(samples)
        list_a[i]=(list_a[i][0],list_a[i][1])
    return list_a
    # TODO: Implement the function
    pass