import twitter
from Tkinter import *
import shelve
from twitterauth2 import *
from runpy import * 
#main window
class MainClient:
    def __init__(self, master):
        self.master = master
        try:
            credshelf = shelve.open('twittercreds.db')
            self.tokenkey = credshelf['oauthtoken']
            self.tokensecret = credshelf['oauthsecret']
            credshelf.close()
            self.cons_key = 'BFdo8gKwAddEcFUvxVFR9di4n'
            self.cons_secret = 'L8lk6ASO6gXYVAADZGqHK76ro2KwrnuXXUQrLWLqxcoSnatVUh'
            self.api = twitter.Api(consumer_key=self.cons_key,
                        consumer_secret=self.cons_secret,
                          access_token_key=self.tokenkey,
                          access_token_secret=self.tokensecret)
            #top frame
            self.tframe = Frame(self.master, width=160)
            self.tframe.pack()
            #top menu bar
            self.menubar = Menu(self.master)
            #call gethometl function
            self.menubar.add_command(label="Your Timeline",
                                     command = self.gethometl)
            #call getdms function
            #self.menubar.add_command(label="Direct Messages",
                                     #command = self.getdms)
            #'pack' menu bar
            self.master.config(menu=self.menubar)
            #user lookup field
            self.user = Entry(self.tframe, width=50, borderwidth=2)
            self.user.pack(side=LEFT)
            #main frame
            self.mframe = Frame(self.master, width=160)
            self.mframe.pack()
            #scrollbar
            self.scroll = Scrollbar(self.mframe)
            self.scroll.pack(side=RIGHT, fill=Y)
            #timeline text
            self.tl = Text(self.mframe, width=150, wrap=WORD)
            self.tl.pack()
            self.tl.config(state=DISABLED)
            #button to switch to another user's timeline
            self.usersearch = Button(self.tframe, text="Find User",
                                     command=self.getusername)
            self.usersearch.pack(side=RIGHT)
            #make scrollbar scroll timeline
            self.tl.config(yscrollcommand=self.scroll.set)
            self.scroll.config(command=self.tl.yview)
            #field to enter new tweets
            self.tweet = Entry(self.mframe, width=160, borderwidth=2)
            self.tweet.pack(side=LEFT)
            self.submit = Button(self.mframe, text="Submit", command=self.gettext)
            self.submit.pack(side=RIGHT)
            #user info field
            self.screenname = self.getthisuser('@jerkbot7').screen_name
            self.statusesnum = self.getthisuser('@jerkbot7').statuses_count
            self.followersnum = self.getthisuser('@jerkbot7').followers_count   
            self.namelabel = Label(self.mframe, text = self.screenname)
            self.namelabel.pack()
            self.statuslabel = Label(self.mframe, text = "Tweets: " + str(self.statusesnum))
            self.statuslabel.pack()
            self.followlabel = Label(self.mframe, text = "Followers: " + str(self.followersnum))
            self.followlabel.pack()
            self.gethometl()
        except KeyError:
            self.openlogin()
    def getmediaurl(self, tweet):
        tweet = tweet
        if tweet.media:
            listone = tweet.media[0]
            url = listone["expanded_url"]
            return "\n" + url
        else:
            return " "
    def getthisuser(self, user_id):
        self.id = user_id
        self.thisuser = self.api.GetUser(screen_name = self.id)
        return self.thisuser
    #get "home" timeline - everyone you follow + yourself
    #api call can be in this function because it's always run from the main
    #window's init function
    def gethometl(self):
        #main code is under a 'try' statement, if a TwitterError is thrown in this code
        #(usually when the access_token_key or secret are wrong)
        #'except' code will be run
            self.tl.config(state=NORMAL)
            self.hometl = self.api.GetHomeTimeline(count=100)
            self.hlist = [h.user.name + "\n" + h.text + "\n" +
                          h.created_at + str(self.getmediaurl(h)) for h in self.hometl]      
            self.hstr = "\n \n".join(self.hlist) 
            self.tl.delete(1.0, END)
            self.tl.insert(END,self.hstr)
            self.tl.config(state=DISABLED)
    #get a username from the username field and pass it to gettimeline
    #must be defined BEFORE the button that calls it
    def getusername(self):
        self.username = self.user.get()
        self.gettimeline(self.username)
     #function to get DMs
    def getdms(self):
        self.tl.config(state=NORMAL)
        self.dms = self.api.GetDirectMessages(count = 100)
        self.dmlist = [m.text + "\n" + m.created_at for m in self.dms]
        self.m = "\n \n".join(self.dmlist)
        self.tl.delete(1.0, END)
        self.tl.insert(END, self.m)
        self.tl.config(state=DISABLED)
    #this function has to be below the timeline text field to insert text into it
    #must also be defined BEFORE the getusername function that calls it
    def gettimeline(self,username):
        self.user = self.username
        #return to hometl if a blank user is searched
        if self.user == "":
            self.gethometl()
        else:
            self.tl.config(state=NORMAL)
            #get tweets for a user with all info
            self.statuses = self.api.GetUserTimeline(screen_name = self.user,
                                       exclude_replies = True, count = 100)
            #turn tweets into list containing strs of text and creation time
            self.slist = [s.text + "\n" + s.created_at for s in self.statuses]
            #turn list into string
            self.x = "\n \n".join(self.slist)
            #insert list at end of tl field (need to make this REPLACE previous tweets)
            self.tl.delete(1.0, END)
            self.tl.insert(END, self.x)
            self.tl.config(state=DISABLED)
    #get text from new tweet field and pass to sendtweet
    def gettext(self):
        self.tweettext = self.tweet.get()
        self.sendtweet(self.tweettext)
    #use api to post new tweet
    def sendtweet(self,post):
        self.text = post
        self.status = self.api.PostUpdate(self.text)
    def openlogin(self):
        self.newWindow = Toplevel(takefocus = True)
        lapp = AuthWindow(self.newWindow)
        #the frame is the ROOT WINDOW, closing it entirely would close the program
        #therefore it has to be withdrawn (hidden)
        self.master.withdraw()
    def reopen(self):
        #unhide the main window
        self.master.deiconify()

#load home timeline by default at runtime
def main():
    root = Tk()
    root.wm_title("Twitter Client")
    app = MainClient(root)
    root.mainloop()
if __name__ == '__main__':
  main()


