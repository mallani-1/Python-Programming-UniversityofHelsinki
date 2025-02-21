# Write your solution to exercise 2 here
def find_gene_positions(gene, genome):
    list = []
    i = 0
    if genome.find(gene,i,len(genome)) == -1 :
        return None
    while True:
        c = genome.find(gene,i,len(genome))
        if c == -1:
            break
        i = c + len(gene) -1
        list.append(c)
    return list

if __name__ == "__main__":
    genome = "ATCGAGATCGACGATCGTAGCTAGCTAGCTAGCGATCGA"
    gene1 = "TAGCTA"
    gene2 = "ATCGA"
    gene3 = "X"

    print(find_gene_positions(gene1, genome))
    print(find_gene_positions(gene2, genome))
    print(find_gene_positions(gene3, genome))
    print(type((find_gene_positions(gene3, genome))))