#regex patterns
HYPERGEO_REGEX = r'.*(?:hypergeo|odds)(?:[\( ]?|: )([\d ]+)[, ]([\d ]+)[, ]([\d ]+)[, ]([\d ]+)\.*'
COLORED_SOURCES_REGEX = r'!?colored ?sources'
LAND_COUNT_REGEX = r'!?land ?count'

#results strings
HYPERGEO_RESULT = 'For {} targets in {} cards, the chance to hit {} in {} draws is: {}%'
COLORED_SOURCES_RESULT = "You can find Frank Karsten's article on colored sources here: https://strategy.channelfireball.com/all-strategy/mtg/channelmagic-articles/how-many-colored-mana-sources-do-you-need-to-consistently-cast-your-spells-a-guilds-of-ravnica-update"
LAND_COUNT_RESULT = "You can find Frank Karsten's article on land count here: https://strategy.channelfireball.com/all-strategy/mtg/channelmagic-articles/how-many-lands-do-you-need-to-consistently-hit-your-land-drops"