def chr_in_str(str):
    '''
    Count char in input str
    '''
    chr_counts = {}
    for chr in str:
        if chr in chr_counts:
            chr_counts[chr] += 1
        else:
            chr_counts[chr] = 1
        
    return chr_counts

print(chr_in_str("hello"))    