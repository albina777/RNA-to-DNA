def convert_dna_to_rna(dna) -> str:
    rna = ""
    for i in dna:
        # Replace all occurrences of T with U
        if i == "T":
            rna += "U"
        else:
            rna += i

    return rna
