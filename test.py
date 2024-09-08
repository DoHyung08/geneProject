from pig import pig
import numpy as np

state = []
state.append(pig([['A','B']]))
state.append(pig([['B','O']]))
state.append(pig([['O','A']]))
state.append(pig([['O','O']]))


# def get_obs():
#     obs_list = []
#     for pig in state:
#         get_gene_list = np.array(pig.genes)
#         obs_list.extend(np.ravel(get_gene_list,order='C'))

#     for i in range(len(obs_list)):
#         obs_list[i] = pig.alleleInt[obs_list[i]]
#     obs_list = np.array([obs_list],dtype=int)

#     return obs_list

# print(get_obs())




action = [2,3,0,1]

nextGen = []

for i in range(0,len(action)-1,2):
    for j in range(2):
        next_gene = []
        gene1 = state[i].trans()
        gene2 = state[i+1].trans()   

        for g in range(1):
            next_gene.append([gene1[g],gene2[g]])##2 allele
        
        #print(next_gene)
        child = pig(next_gene)
        nextGen.append(child)

for piig in nextGen:
    print(piig.genes,piig.phenotype)

totalPheno = []
for g in range(1):
    phenoCnt = [0 for i in range(len(pig.phenoInt))]

    for babyPig in nextGen:
        phenoCnt[pig.phenoInt[babyPig.phenotype[g]]] += 1
print(phenoCnt)
totalPheno.append(phenoCnt)