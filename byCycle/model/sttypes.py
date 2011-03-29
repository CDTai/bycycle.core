###############################################################################
# $Id$
# Created ???.
#
# Street types.
#
# Copyright (C) 2006, 2007 Wyatt Baldwin, byCycle.org <wyatt@bycycle.org>.
# All rights reserved.
#
# For terms of use and warranty details, please see the LICENSE file included
# in the top level of this distribution. This software is provided AS IS with
# NO WARRANTY OF ANY KIND.
###############################################################################
"""
Provides a map of full street types to USPS abbreviations,
``street_types_ftoa``, and a map of abbreviations to full types,
``street_types_atof``.

TODO
- Add other common abbreviations to `street_types_atof` (av, pky, ...)
- Make sure sttypes in the DB are using the USPS abbreviations

"""
from byCycle.util import swapKeysAndValues


street_types_ftoa = {
    'alley': 'aly',
    'annex': 'anx',
    'arcade': 'arc',

    'av': 'ave',

    'avenue': 'ave',
    'bayoo': 'byu',
    'beach': 'bch',
    'bend': 'bnd',
    'bluff': 'blf',
    'bluffs': 'blfs',
    'bottom': 'btm',
    'boulevard': 'blvd',
    'branch': 'br',
    'bridge': 'brg',
    'brook': 'brk',
    'brooks': 'brks',
    'burg': 'bg',
    'burgs': 'bgs',
    'bypass': 'byp',
    'camp': 'cp',
    'canyon': 'cyn',
    'cape': 'cpe',
    'causeway': 'cswy',
    'center': 'ctr',
    'centers': 'ctrs',
    'circle': 'cir',
    'circles': 'cirs',
    'cliff': 'clf',
    'cliffs': 'clfs',
    'club': 'clb',
    'common': 'cmn',
    'corner': 'cor',
    'corners': 'cors',
    'course': 'crse',
    'court': 'ct',
    'courts': 'cts',
    'cove': 'cv',
    'coves': 'cvs',
    'creek': 'crk',
    'crescent': 'cres',
    'crest': 'crst',
    'crossing': 'xing',
    'crossroad': 'xrd',
    'curve': 'curv',
    'dale': 'dl',
    'dam': 'dm',
    'divide': 'dv',
    'drive': 'dr',
    'drives': 'drs',
    'estate': 'est',
    'estates': 'ests',
    'expressway': 'expy',
    'extension': 'ext',
    'extensions': 'exts',
    'fall': 'fall',
    'falls': 'fls',
    'ferry': 'fry',
    'field': 'fld',
    'fields': 'flds',
    'flat': 'flt',
    'flats': 'flts',
    'ford': 'frd',
    'fords': 'frds',
    'forest': 'frst',
    'forge': 'frg',
    'forges': 'frgs',
    'fork': 'frk',
    'forks': 'frks',
    'fort': 'ft',
    'freeway': 'fwy',
    'garden': 'gdn',
    'gardens': 'gdns',
    'gateway': 'gtwy',
    'glen': 'gln',
    'glens': 'glns',
    'green': 'grn',
    'greens': 'grns',
    'grove': 'grv',
    'groves': 'grvs',
    'harbor': 'hbr',
    'harbors': 'hbrs',
    'haven': 'hvn',
    'heights': 'hts',
    'highway': 'hwy',
    'hill': 'hl',
    'hills': 'hls',
    'hollow': 'holw',
    'inlet': 'inlt',
    'island': 'is',
    'islands': 'iss',
    'isle': 'isle',
    'junction': 'jct',
    'junctions': 'jcts',
    'key': 'ky',
    'keys': 'kys',
    'knoll': 'knl',
    'knolls': 'knls',
    'lake': 'lk',
    'lakes': 'lks',
    'land': 'land',
    'landing': 'lndg',
    'lane': 'ln',
    'light': 'lgt',
    'lights': 'lgts',
    'loaf': 'lf',
    'lock': 'lck',
    'locks': 'lcks',
    'lodge': 'ldg',
    'loop': 'loop',
    'mall': 'mall',
    'manor': 'mnr',
    'manors': 'mnrs',
    'meadow': 'mdw',
    'meadows': 'mdws',
    'mews': 'mews',
    'mill': 'ml',
    'mills': 'mls',
    'mission': 'msn',
    'motorway': 'mtwy',
    'mount': 'mt',
    'mountain': 'mtn',
    'mountains': 'mtns',
    'neck': 'nck',
    'orchard': 'orch',
    'oval': 'oval',
    'overpass': 'opas',
    'park': 'park',
    'parks': 'park',

    'pky': 'pkwy',

    'parkway': 'pkwy',
    'parkways': 'pkwy',
    'pass': 'pass',
    'passage': 'psge',
    'path': 'path',
    'pike': 'pike',
    'pine': 'pne',
    'pines': 'pnes',
    'place': 'pl',
    'plain': 'pln',
    'plains': 'plns',
    'plaza': 'plz',
    'point': 'pt',
    'points': 'pts',
    'port': 'prt',
    'ports': 'prts',
    'prairie': 'pr',
    'radial': 'radl',
    'ramp': 'ramp',
    'ranch': 'rnch',
    'rapid': 'rpd',
    'rapids': 'rpds',
    'rest': 'rst',
    'ridge': 'rdg',
    'ridges': 'rdgs',
    'river': 'riv',
    'road': 'rd',
    'roads': 'rds',
    'route': 'rte',
    'row': 'row',
    'rue': 'rue',
    'run': 'run',
    'shoal': 'shl',
    'shoals': 'shls',
    'shore': 'shr',
    'shores': 'shrs',
    'skyway': 'skwy',
    'spring': 'spg',
    'springs': 'spgs',
    'spur': 'spur',
    'spurs': 'spur',
    'square': 'sq',
    'squares': 'sqs',
    'station': 'sta',
    'stravenue': 'stra',
    'stream': 'strm',
    'street': 'st',
    'streets': 'sts',
    'summit': 'smt',
    'terrace': 'ter',
    'throughway': 'trwy',
    'trace': 'trce',
    'track': 'trak',
    'trafficway': 'trfy',
    'trail': 'trl',
    'tunnel': 'tunl',
    'turnpike': 'tpke',
    'underpass': 'upas',
    'union': 'un',
    'unions': 'uns',
    'valley': 'vly',
    'valleys': 'vlys',
    'viaduct': 'via',
    'view': 'vw',
    'views': 'vws',
    'village': 'vlg',
    'villages': 'vlgs',
    'ville': 'vl',
    'vista': 'vis',
    'walk': 'walk',
    'walks': 'walk',
    'wall': 'wall',
    'way': 'way',
    'ways': 'ways',
    'well': 'wl',
    'wells': 'wls'
}
street_types_atof = swapKeysAndValues(street_types_ftoa)
street_types_atof['ave'] = 'avenue'
street_types_atof['pkwy'] = 'parkway'
street_types_atof['walk'] = 'walk'