import twitter
from Tkinter import *
import shelve
#first window that opens - 'login' window
class Login:
    def __init__(self, master):
        self.master = master
        self.loginframe = Frame(self.master)
        self.loginframe.pack()
        #entry fields for user's api keys
        self.userkey = Entry(self.loginframe, width = 60)
        self.userkey.pack()
        self.userkey.insert(0, "Your API User Key")
        self.usersecret = Entry(self.loginframe, width = 60)
        self.usersecret.pack()
        self.usersecret.insert(0, "Your API User Secret")
        #button to save credentials using save_creds method
        self.submit = Button(self.loginframe, text = "Save API Credentials", command = self.save_creds)
        self.submit.pack()
        #button to open main window using saved credentials
        self.tomain = Button(self.loginframe, text = "Open Twitter", command = self.open_main)
        self.tomain.pack()
    #creates new window for main client
    def open_main(self):
        self.newWindow = Toplevel(self.master)
        self.app = MainClient(self.newWindow)'
    #gets entered credentials and saves them to a dict
    #dict is saved to a db file using shelve and reopened by the main client's init function
    def save_creds(self):
        self.apikey = self.userkey.get()
        self.apisecret = self.usersecret.get()
        creds = {'key':self.apikey, 'secret':self.apisecret}
        credshelf = shelve.open('twittercreds.db')
        credshelf['creds'] = creds
        credshelf.close()
#main window
class MainClient:
    def __init__(self, master):
        #main code is under a 'try' statement, if a TwitterError is thrown in this code
        #(usually when the access_token_key or secret are wrong)
        #'except' code will be run
        try:
            credshelf = shelve.open("twittercreds.db")
            self.creds = credshelf['creds']
            self.api = twitter.Api(consumer_key='mJbSUQdokViuAh1h6AuKddRQc',
                      consumer_secret='1wmAUS9MTCOiDo6Pn3mdmA8lnjGP9fGkOWrSrXcfmALFUhrImZ',
                      access_token_key=self.creds['key'],
                      access_token_secret=self.creds['secret'])
            self.master = master
            #top frame
            self.tframe = Frame(self.master, width=160)
            self.tframe.pack()
            #top menu bar
            self.menubar = Menu(self.master)
            #call gethometl function
            self.menubar.add_command(label="Your Timeline",
                                     command = self.gethometl)
            #call getdms function
            self.menubar.add_command(label="Direct Messages",
                                     command = self.getdms)
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
            self.gethometl()
        except twitter.TwitterError:
            self.tl.insert(END, "Twitter error! (Probably invalid API credentials)")
    #get "home" timeline - everyone you follow + yourself
    def gethometl(self):
        self.hometl = self.api.GetHomeTimeline(count=100)
        self.hlist = [h.user.name + "\n" + h.text + "\n" + h.created_at for h in self.hometl]
        self.hstr = "\n \n".join(self.hlist)
        self.tl.delete(1.0, END)
        self.tl.insert(END,self.hstr)
    #get a username from the username field and pass it to gettimeline
    #must be defined BEFORE the button that calls it
    def getusername(self):
        self.username = self.user.get()
        self.gettimeline(self.username)
     #function to get DMs
    def getdms(self):
        self.dms = self.api.GetDirectMessages(count = 100)
        self.dmlist = [m.text + "\n" + m.created_at for m in self.dms]
        self.m = "\n \n".join(self.dmlist)
        self.tl.delete(1.0, END)
        self.tl.insert(END, self.m)
    #this function has to be below the timeline text field to insert text into it
    #must also be defined BEFORE the getusername function that calls it
    def gettimeline(self,username):
        self.user = self.username
        #return to hometl if a blank user is searched
        if self.user == "":
            self.gethometl()
        else:
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
    #get text from new tweet field and pass to sendtweet
    def gettext(self):
        self.tweettext = self.tweet.get()
        self.sendtweet(self.tweettext)
    #use api to post new tweet
    def sendtweet(self,post):
        self.text = post
        self.status = self.api.PostUpdate(self.text)
#load home timeline by default at runtime
def main(): 
    root = Tk()
    root.wm_title("Twitter Client")
    app = Login(root)
    root.mainloop()
if __name__ == '__main__':
    main()


