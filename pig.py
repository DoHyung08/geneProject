import random

class pig:
    phenoPolicy = [{'A':1,'B':1,'O':2}]#우열관계 명시한 표현형 정책
    alleleList = [['A','B','O']]
    alleleInt = {'A':0,'B':1,'O':2}#숫자로 변환하는 딕셔너리
    phenoInt = {'AB':0,'A':1,'B':2,'O':3}

    def __init__(self, genes):
        self.genes = genes #n X 2(일반적) list
        self.phenotype = []

        self.calPheno()

    def calPheno(self): 
        for i in range(len(self.genes)):
            gene = self.genes[i]
            calc = ''
            genePrior = 999
            for allele in gene:#일반적으로 [ , ]

                try:
                    allelePrior = self.phenoPolicy[i][allele]
                    if allelePrior < genePrior:
                        calc = allele
                        genePrior = allelePrior
                    elif allelePrior == genePrior:
                        if(calc != allele):
                            calc = calc + allele
                except:
                    calc = gene[0]
            
            self.phenotype.append(calc)


    def trans(self):
        nextTrans = []
        for i in range(len(self.genes)):
            nextTrans.append(random.choice(self.genes[i]))
        return nextTrans