table = {
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'N': ['AAU', 'AAC'],
    'D': ['GAU', 'GAC'],
    'C': ['UGU', 'UGC'],
    'Q': ['CAA', 'CAG'],
    'E': ['GAA', 'GAG'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'H': ['CAU', 'CAC'],
    'I': ['AUU', 'AUC', 'AUA'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'K': ['AAA', 'AAG'],
    'M': ['AUG'],
    'F': ['UUU', 'UUC'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'W': ['UGG'],
    'Y': ['UAU', 'UAC'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    '*': ['UAA', 'UAG', 'UGA']
}

def makemrna(aminoacid, index=0, current_mrna='', all_mrna=[]):
    if index == len(aminoacid):
        all_mrna.append(current_mrna)
        return

    amino_acid = aminoacid[index]

    if amino_acid in table:
        for codon in table[amino_acid]:
            makemrna(aminoacid, index + 1, current_mrna + codon, all_mrna)
    else:
        print(f"Invalid amino acid: {amino_acid}")

    return all_mrna

def codonf(mrna_seq):
    codonc = {}
    for i in range(0, len(mrna_seq), 3):
        codon = mrna_seq[i:i + 3]
        if codon in codonc:
            codonc[codon] += 1
        else:
            codonc[codon] = 1
    return codonc


# Main program
def main():
    valid_amino_acids = {'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y',
                         'V', '*'}

    while True:
        aminoacid = input("Input amino acid sequence (max 3 letters): ").upper()

        if len(aminoacid) > 3:
            print("Invalid index. Please enter a sequence with a maximum of 3 letters.")
            continue

        if not all(aa in valid_amino_acids for aa in aminoacid):
            print("Invalid input. Please enter a sequence that only have valid amino acids.")
            continue

        allmrna = makemrna(aminoacid)

        if allmrna:
            print("\nPossible mRNA sequences:")
            for mrna in allmrna:
                print(mrna)

            print("\nCodon frequencies for each mRNA sequence:")
            for mrna in allmrna:
                frequencies = codonf(mrna)
                print(f"\nmRNA = {mrna}")
                for codon, count in frequencies.items():
                    print(f"{codon} = {count}")
            break

main()
