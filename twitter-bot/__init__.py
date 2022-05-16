import datetime
import logging
import azure.functions as func
from .app.twitter import getMentions, getRecentTweets, postTweet
from .app.utils import hyperGeometeric, hyperGeoValuesFromText
from .app.classes import Tweet, HyperGeo

def respondToTweets():
    #Get Mentions and Recent Tweet IDs
    mentions = getMentions()
    recentTweets = getRecentTweets()
    #Check against existing tweets to see if we've replied already
    for mention in mentions:
        found = False
        for tweet in recentTweets:
            if tweet.in_reply_to_status_id == mention.id:
                found = True
                break

        #Check for valid syntax if we haven't replied
        #TODO Return GitHub ReadMe link if couldn't parse?
        if found == False:
            hyperGeo = hyperGeoValuesFromText(mention.text)
            #Reply with Answer
            if hyperGeo != None:
                try:
                    newTweet = hyperGeometeric(hyperGeo)
                    logging.info(postTweet(newTweet, mention.id).id)
                except Exception as err:
                    print(err)

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    respondToTweets()

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
