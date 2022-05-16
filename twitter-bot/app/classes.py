class Tweet(object):
    def __init__(self, id, text, in_reply_to_status_id):
        self.id = id
        self.text = str(text)
        self.in_reply_to_status_id = in_reply_to_status_id

class HyperGeo(object):
    def __init__(self, numCards, numTargets, numDraws, reqSuccess):
        self.numCards = int(str(numCards).strip())
        self.numTargets = int(str(numTargets).strip())
        self.numDraws = int(str(numDraws).strip())
        self.reqSuccess = int(str(reqSuccess).strip())