def to_rna(dna):
    l = { 'G':'C', 'C':'G', 'T':'A','A':'U'}
    rna = ''
    for i in dna:
        if i not in l:
            return ''
        else:
            rna += l[i]
    return rna