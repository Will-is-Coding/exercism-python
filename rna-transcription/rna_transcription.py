def to_rna(DNA):
    """Return a DNA strand's complement RNA strand"""

    if (len(DNA) % 4 == 0 or len(DNA) == 1) and DNA:
        dnaNucleotides = set('ACGT')
        if set(DNA).issubset(dnaNucleotides):
            rnaDict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
            rna = ''

            for nucleotide in DNA:
                rna += rnaDict[nucleotide]

            return rna

        else:
            return ''

    else:
        return ''
