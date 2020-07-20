import tweepy
print("This is a twitter bot")

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = str(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

last_seen_id = retrieve_last_seen_id(FILE_NAME)

CONSUMER_KEY = 'aEJ7ak1He92OmylKnMR2pVLJz'
CONSUMER_SECRET = 'FjB1TAYLBqZyHA78VZ8QUn4TbCPA0TUQ8HMMvMd7qh2LP0EDJL'
ACCESS_KEY = '340466606-jCo9Ti4iCRRGQ7oUN0vRABXvtE3LW46DrPCkuyDV'
ACCESS_SECRET = '25D9WFzmR5iANXVNPiCo9fdSSYC8osaqxhqufD6pWt7Z2'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
last_seen_id = retrieve_last_seen_id(FILE_NAME)

mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

for mention in reversed(mentions):
    print(mention.user.screen_name + ' - ' + str(mention.id) + ' - ' + mention.full_text)
    last_seen_id = mention.id
    store_last_seen_id(last_seen_id, FILE_NAME)
    if('#beenis' in mention.full_text.lower()):
        print('beenis found')
        api.update_status('@' + mention.user.screen_name + ' beenisBot online', mention.id)
    else:
        print("beenis not found")
