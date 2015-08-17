import urlparse
import oauth2 as oauth
#app's api keys
consumer_key = 'BFdo8gKwAddEcFUvxVFR9di4n'
consumer_secret = 'L8lk6ASO6gXYVAADZGqHK76ro2KwrnuXXUQrLWLqxcoSnatVUh'
#twitter urls to call
request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'

consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)

# Step 1: Get a request token. This is a temporary token that is used for 
# having the user authorize an access token and to sign the request to obtain 
# said access token.
#send GET request to twitter's request token url
resp, content = client.request(request_token_url, "GET")
#response is http and contains a status code variable
#if this is NOT 200, the request failed
if resp['status'] != '200':
    raise Exception("Invalid response %s." % resp['status'])
#parse http response to a dict
request_token = dict(urlparse.parse_qsl(content))
#print oauth_token and oauth_token_secret elements of the dict
print "Request Token:"
print "    - oauth_token        = %s" % request_token['oauth_token']
print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']
print 

# Step 2: Redirect to the provider. Since this is a CLI script we do not 
# redirect. In a web application you would redirect the user to the URL
# below.
#give user the link to go to to get their pin
#twitter's default auth url with the oauth_token added to the end
print "Go to the following link in your browser:"
print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
print 

# After the user has granted access to you, the consumer, the provider will
# redirect you to whatever URL you have told them to redirect to. You can 
# usually define this in the oauth_callback argument as well.
#ask user if they have completed verification
accepted = 'n'
while accepted.lower() == 'n':
    #if user changes 'accepted' from n to anything else, move on
    accepted = raw_input('Have you authorized me? (y/n) ')
#request pin given by twitter's site
oauth_verifier = raw_input('What is the PIN? ')

# Step 3: Once the consumer has redirected the user back to the oauth_callback
# URL you can request the access token the user has approved. You use the 
# request token to sign this request. After this is done you throw away the
# request token and use the access token returned. You should store this 
# access token somewhere safe, like a database, for future use.
#init token class containing the oauth_token and oauth_token_secret
token = oauth.Token(request_token['oauth_token'],
    request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
#init client class (takes consumer, which contains consumer keys,
#and request token)
client = oauth.Client(consumer, token)
#send POST request for access token to twitter
resp, content = client.request(access_token_url, "POST")
#parse response into access token
access_token = dict(urlparse.parse_qsl(content))
#print access token's elements
print "Access Token:"
print "    - oauth_token        = %s" % access_token['oauth_token']
print "    - oauth_token_secret = %s" % access_token['oauth_token_secret']
print
print "You may now access protected resources using the access tokens above." 
print
