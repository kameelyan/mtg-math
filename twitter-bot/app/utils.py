import re
from typing import Union
from scipy.stats import hypergeom
from .classes import HyperGeo
from .constants import *

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
    regEx = re.compile(HYPERGEO_REGEX, re.DOTALL | re.IGNORECASE)
    match = regEx.search(query)
    if match:
        return HyperGeo(
            match.group(1),
            match.group(2),
            match.group(3),
            match.group(4)
        )
    return None

def valuesExtractor(query:str):
    #First, check for hypergeo
    result = hyperGeoValuesFromText(query)
    if result != None: return hyperGeometeric(result)

    #Next check for Colored Sources
    regEx = re.compile(COLORED_SOURCES_REGEX, re.IGNORECASE)
    match = regEx.search(query)
    if match: return COLORED_SOURCES_RESULT

    #Next check for Land Count
    regEx = re.compile(LAND_COUNT_REGEX, re.IGNORECASE)
    match = regEx.search(query)
    if match: return LAND_COUNT_RESULT

    #Return None to take no action
    return None
    