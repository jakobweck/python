import urlparse
from Tkinter import *
import oauth2 as oauth
import sys
import shelve
from twittertest4 import *
class AuthWindow:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()
        self.authurl = Text(self.frame)
        self.authurl.pack()
        self.pin = Entry(self.frame)
        self.pin.pack()
        self.authorized = Button(self.frame, command = self.AuthConfirmed, text = "Authorize")
        self.authorized.pack()
        self.getpin = Button(self.frame, command = self.PinConfirmed, text = "Submit PIN")
        self.getpin.pack()
        self.getaccesstokens()
    def getaccesstokens(self):
        print "ass"
        #app's api keys
        self.consumer_key = 'BFdo8gKwAddEcFUvxVFR9di4n'
        self.consumer_secret = 'L8lk6ASO6gXYVAADZGqHK76ro2KwrnuXXUQrLWLqxcoSnatVUh'
        #twitter urls to call
        self.request_token_url = 'https://api.twitter.com/oauth/request_token'
        self.access_token_url = 'https://api.twitter.com/oauth/access_token'
        self.authorize_url = 'https://api.twitter.com/oauth/authorize'
        self.consumer = oauth.Consumer(self.consumer_key, self.consumer_secret)
        self.client = oauth.Client(self.consumer)
        # Step 1: Get a request token. This is a temporary token that is used for 
        # having the user authorize an access token and to sign the request to obtain 
        # said access token.
        #send GET request to twitter's request token url
        self.resp, self.content = self.client.request(self.request_token_url, "GET")
        #response is http and contains a status code variable
        #if this is NOT 200, the request failed
        if self.resp['status'] != '200':
            raise Exception("Invalid response %s." % self.resp['status'])
        #parse http response to a dict
        self.request_token = dict(urlparse.parse_qsl(self.content))
        self.authurl.insert(END, "%s?oauth_token=%s \nGo to the URL displayed above.\nAuthorize this app, then click Authorize"
                                % (self.authorize_url, self.request_token['oauth_token']))

    def AuthConfirmed(self):
        self.authurl.delete(1.0, END)
        self.authurl.insert(END, "Enter your PIN and press Submit")
    def PinConfirmed(self):
        self.oauth_verifier = self.pin.get()
        self.token = oauth.Token(self.request_token['oauth_token'],
                            self.request_token['oauth_token_secret'])
        self.token.set_verifier(self.oauth_verifier)
        self.client = oauth.Client(self.consumer, self.token)
        self.resp, self.content = self.client.request(self.access_token_url, "POST")
        self.access_token = dict(urlparse.parse_qsl(self.content))
        credshelf = shelve.open('twittercreds.db')
        credshelf['oauthtoken'] = self.access_token['oauth_token']
        credshelf['oauthsecret'] = self.access_token['oauth_token_secret']
        credshelf.close()
        self.newWindow = Toplevel(self.master)
        self.app = MainClient(self.newWindow)
def main():
    root = Tk()
    root.wm_title("Twitter Client")
    napp = AuthWindow(root)
    root.mainloop()
if __name__ == '__main__':
  main()

