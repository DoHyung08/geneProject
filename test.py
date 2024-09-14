from pig import pig
import numpy as np
import random

state = []
state.append(pig([['A','B']]))
state.append(pig([['B','O']]))
state.append(pig([['O','A']]))
state.append(pig([['O','O']]))




def make_generation():
    ret_genereation = []

    for i in range(4):
        make_gene = []
        for g in range(2):
            make_one_gene = []
            for j in range(2):
                make_one_gene.append(random.choice(pig.alleleList[g]))
            make_gene.append(make_one_gene)
        
        ret_genereation.append(pig(make_gene))
        print(make_gene)
    
    return ret_genereation

generation = make_generation()

for ppig in generation:
    print(ppig.phenotype)
    















# def get_obs():
#     obs_list = []

#     for pigG in state:
#         for g in range(1):
#             obs_list.append(pigG.phenotype[g])

#     for i in range(len(obs_list)):
#         obs_list[i] = pig.phenoInt[obs_list[i]]
#     obs_list = np.array(obs_list,dtype=int)

#     return obs_list

# print(get_obs())
# print(get_obs().shape)

#print(random.choice(pig.alleleList))




# action = [2,3,0,1]

# nextGen = []

# for i in range(0,len(action)-1,2):
#     for j in range(2):
#         next_gene = []
#         gene1 = state[i].trans()
#         gene2 = state[i+1].trans()   

#         for g in range(1):
#             next_gene.append([gene1[g],gene2[g]])##2 allele
        
#         #print(next_gene)
#         child = pig(next_gene)
#         nextGen.append(child)

# for piig in nextGen:
#     print(piig.genes,piig.phenotype)

# totalPheno = []
# for g in range(1):
#     phenoCnt = [0 for i in range(len(pig.phenoInt))]

#     for babyPig in nextGen:
#         phenoCnt[pig.phenoInt[babyPig.phenotype[g]]] += 1
# print(phenoCnt)
# totalPheno.append(phenoCnt)