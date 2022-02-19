
def build_profile(motif):
    rows, cols = (4, k)
    profile = [[1 for n in range(cols)] for m in range(rows)]

    for i in range(0, k):
        for j in range(0, len(motif)):
            if (motif[j][i] == 'A'):
                profile[0][i] += 1
            elif (motif[j][i] == 'C'):
                profile[1][i] += 1
            elif (motif[j][i] == 'G'):
                profile[2][i] += 1
            elif (motif[j][i] == 'T'):
                profile[3][i] += 1

    for r in range(0, 4):
        for c in range(0, k):
            profile[r][c] = profile[r][c] / (len(motif) + 4)

    return profile

def most_probable(string, profile):
    best_kmer = ""
    highest_prob = 0

    for i in range(0, len(string) - k + 1):
        curr_kmer = string[i:i + k]
        curr_prob = 1

        for j in range(0, k):
            if (curr_kmer[j] == 'A'):
                curr_prob = curr_prob * profile[0][j]
            elif (curr_kmer[j] == 'C'):
                curr_prob = curr_prob * profile[1][j]
            elif (curr_kmer[j] == 'G'):
                curr_prob = curr_prob * profile[2][j]
            elif (curr_kmer[j] == 'T'):
                curr_prob = curr_prob * profile[3][j]

        if (curr_prob > highest_prob):
            highest_prob = curr_prob
            best_kmer = curr_kmer

    return best_kmer

def score_motif(motif):
    score = 0

    for i in range(0, k):
        count = [0] * 4
        for j in range(0, t):
            if (motif[j][i] == 'A'):
                count[0] += 1
            elif (motif[j][i] == 'C'):
                count[1] += 1
            elif (motif[j][i] == 'G'):
                count[2] += 1
            elif (motif[j][i] == 'T'):
                count[3] += 1
        count.sort(reverse = True)
        score = score + count[1] + count[2] + count[3]

    return score



reader = open("input", "r")
writer = open("output", "w")

temp = reader.readline().split()
k = int(temp[0])
t = int(temp[1])
dna = reader.readlines()
for i in range(0, t):
    dna[i] = dna[i].strip()


best_motifs = [""] * t
for i in range(0, t):
    best_motifs[i] = dna[i][0:k]

for i in range(0, len(dna[0]) - k + 1):
     first_motif = dna[0][i:i + k]
     motifs = []
     motifs.append(first_motif)
     for j in range(1, t):
         profile = build_profile(motifs)
         motif_j = most_probable(dna[j], profile)
         motifs.append(motif_j)
     if (score_motif(motifs) < score_motif(best_motifs)):
         best_motifs = motifs


for m in best_motifs:
    writer.write(m + "\n")

reader.close()
writer.close()
