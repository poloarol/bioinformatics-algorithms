### mendel.py
### Detemine the probability of choosing having dominant offspring


import os

def calc_probability_dominant(dominant: int, hetero: int, recessive: int) -> float:
    """Calculates the probability having a dominant offspring"""

    all_individuals: int = dominant + recessive + hetero

    prob_recessive_parents: float = (recessive/all_individuals) * ((recessive-1)/(all_individuals-1))
    prob_hetero_parents: float = (hetero/all_individuals) * ((hetero-1)/(all_individuals-1))

    prob_recessive_hetero_parents: float = (recessive/all_individuals) * (hetero/(all_individuals-1))
    prob_hetero_recessive_parents: float = (hetero/all_individuals) * (recessive/(all_individuals-1))
    all_hetero_recessive: float = prob_recessive_hetero_parents + prob_hetero_recessive_parents

    print(prob_recessive_parents, prob_hetero_parents, all_hetero_recessive)

    recessive_child: float = prob_recessive_parents + (prob_hetero_parents * 0.25) + (all_hetero_recessive * 0.5)

    return 1 - recessive_child

if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), 'input/rosalind_iprb.txt'), 'r') as lines:
        for line in lines:
            a, b, c = line.split(' ')
            dom, het, rec = int(a), int(b), int(c)

            probability: float = calc_probability_dominant(dom, het, rec)

            with open(os.path.join(os.getcwd(), "output/rosalind_iprb.txt"), 'w') as outs:
                outs.write(f"{probability: .5f}\n")