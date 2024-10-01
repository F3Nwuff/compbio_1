accepted = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

table = {
    "UUU": "Phe (F)", "UUC": "Phe (F)", "UUA": "Leu (L)", "UUG": "Leu (L)",
    "CUU": "Leu (L)", "CUC": "Leu (L)", "CUA": "Leu (L)", "CUG": "Leu (L)",
    "AUU": "Ile (I)", "AUC": "Ile (I)", "AUA": "Ile (I)", "AUG": "Met (M)",
    "GUU": "Val (V)", "GUC": "Val (V)", "GUA": "Val (V)", "GUG": "Val (V)",
    "UCU": "Ser (S)", "UCC": "Ser (S)", "UCA": "Ser (S)", "UCG": "Ser (S)",
    "CCU": "Pro (P)", "CCC": "Pro (P)", "CCA": "Pro (P)", "CCG": "Pro (P)",
    "ACU": "Thr (T)", "ACC": "Thr (T)", "ACA": "Thr (T)", "ACG": "Thr (T)",
    "GCU": "Ala (A)", "GCC": "Ala (A)", "GCA": "Ala (A)", "GCG": "Ala (A)",
    "UAU": "Tyr (Y)", "UAC": "Tyr (Y)", "CAU": "His (H)", "CAC": "His (H)",
    "CAA": "Gln (Q)", "CAG": "Gln (Q)", "AAU": "Asn (N)", "AAC": "Asn (N)",
    "AAA": "Lys (K)", "AAG": "Lys (K)", "GAU": "Asp (D)", "GAC": "Asp (D)",
    "GAA": "Glu (E)", "GAG": "Glu (E)", "UGU": "Cys (C)", "UGC": "Cys (C)",
    "UGG": "Trp (W)", "CGU": "Arg (R)", "CGC": "Arg (R)", "CGA": "Arg (R)",
    "CGG": "Arg (R)", "AGU": "Ser (S)", "AGC": "Ser (S)", "AGA": "Arg (R)",
    "AGG": "Arg (R)", "GGU": "Gly (G)", "GGC": "Gly (G)", "GGA": "Gly (G)",
    "GGG": "Gly (G)"
}

def complement(dna):
    return ''.join(accepted[x] for x in dna)

def dnamrna(dna):
    return dna.replace("T", "U")

def mrnaprotein(mrna):
    protein = []
    for i in range(0, len(mrna), 3):
        codon = mrna[i:i + 3]
        if codon in table:
            protein.append(table[codon])
    return ' - '.join(protein)

def main():
    while True:
        dna = input("Enter DNA sequence : ").upper()
        if any(base not in 'ATCG' for base in dna):
            print("Invalid input only accepts input made of A, T, C, or G")
            continue
        if len(dna) % 3 != 0:
            print("invalid input, please input in multiples of 3")
            continue

        comp = complement(dna)
        mrna = dnamrna(comp)
        aminoacid= mrnaprotein(mrna)

        print(f"Complement = {comp}")
        print(f"mRna = {mrna}")
        print(f"Aminoacid = {aminoacid}")
        break

main()
