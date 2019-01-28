import requests
import json
import time
import random
from timeit import default_timer as timer
import settings
import sys

####
# Start script
####
startTs = time.gmtime()
start = timer()
print "============================"
print "Generating HTTP GET Requests"
print "============================"
print "\nStarting " + time.strftime("%Y-%m-%d %H:%M:%S", startTs) + "\n"

####
# Main start function
####
def main():

    print('NUM REQUESTS TO GENERATE: ' + str(NUM_REQUESTS))

    for numRequest in range(NUM_REQUESTS):
        print 'Running request: ' + str(numRequest)

        user = random.choice(USERS)
        productId = random.randrange(1, 100)

        req = requests.get(URL + SECRET + '&user=' + user + '&productId=' + str(productId))

        if req.ok :
            json_response = json.loads(req.content)
            print(json.dumps(json_response, indent=4, sort_keys=True))
        else:
            print 'Invalid response! ' + req.content
            sys.exit('Exiting!')

        if SLEEP_SECONDS > 0:
            print('\nSleeping for ' + str(SLEEP_SECONDS) + ' seconds.\n')
            time.sleep(SLEEP_SECONDS)



####
# Constants (URL, SECRET, and NUM_REQUESTS loaded from .env file)
####
URL = settings.URL
SECRET = settings.SECRET
NUM_REQUESTS = int(settings.NUM_REQUESTS)
SLEEP_SECONDS = int(settings.SLEEP_SECONDS)

USERS = ['user1', 'user2', 'user3']

####
# Main
####
if __name__ == '__main__':
    main()

####
# Indicate end of script
####
end = timer()
endTs = time.gmtime()
print "\nEnding " + time.strftime("%Y-%m-%d %H:%M:%S", endTs)
print '==============================='
print 'Total Time Elapsed (in seconds): ' + str(end - start)
print '==============================='
