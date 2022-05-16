import re
from typing import Union
from scipy.stats import hypergeom
from .classes import HyperGeo
from .constants import HYPERGEO_RESULT, HYPERGEO_REGEX

#M Total number of cards
#n Number of Type I cards (e.g. red cards) 
#N Number of draws (5 cards dealt in one poker hand)
#k Number of Type I cards we want in one hand
def hyperGeometeric(values: HyperGeo):
    hpd = hypergeom(values.numCards, values.numTargets, values.numDraws)
    probability = round(hpd.pmf(values.reqSuccess) * 100.0, 3)
    result = HYPERGEO_RESULT.format(
        values.numTargets, 
        values.numCards, 
        values.reqSuccess,
        values.numDraws,
        probability
    )
    return result

def hyperGeoValuesFromText(query: str) -> Union[HyperGeo, None]:
    match = re.search(HYPERGEO_REGEX, query)
    if match:
        return HyperGeo(
            match.group(1),
            match.group(2),
            match.group(3),
            match.group(4)
        )
    return None