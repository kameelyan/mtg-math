
### MTG Math Twitter Bot
Written by: [@kameelyan](https://twitter.com/kameelyan)
Version: 0.01 - Alpha

I wrote this bot to provide the community a way to run probability equations within twitter threads. It's very much a work in progress.

### Usage
The bot will pick up the first match it finds. Multiple matches are not supported at this time.

**Hypergeometric Probability: hypergeo(M,n,N,k)**
**M**: Total number of cards
**n**: Number of Type I cards (e.g. red cards)
**N**: Number of draws (5 cards dealt in one poker hand)
**k**: Number of Type I cards we want in one hand
*Alternatively, you can use "odds" instead of "hypergeo".*

Regular Expression:

    /.*(?:hypergeo|odds)(?:[\( ]?|: )([\d ]+)[, ]([\d ]+)[, ]([\d ]+)[, ]([\d ]+)\.*/gmi

**Colored Sources**
Picks up any tweet that mentions "colored sources".
Regular Expression: 

    /!?colored ?sources/gmi

**Land Count**
Picks up any tweet that mentions "land count".
Regular Expression: 

    /!?land ?count/gmi
