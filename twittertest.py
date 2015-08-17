import twitter
from Tkinter import *
#create twitter API with credentials from my account
api = twitter.Api(consumer_key='mJbSUQdokViuAh1h6AuKddRQc',
                  consumer_secret='1wmAUS9MTCOiDo6Pn3mdmA8lnjGP9fGkOWrSrXcfmALFUhrImZ',
                  access_token_key='15650341-CF8D2cuItlTLJp4u1vGAHiGFeetz1k1D3hdj56DMy',
                  access_token_secret='m51CmIZAIpHavfB25swfMFyy7ZVQMVRjbzYvLY5iTgtAf')
root = Tk()
root.wm_title("Twitter Client")
#top frame
#objects at top are in a different frame so they remain above everything else
#in the ui
#regardless of where they must be in the code to interact with functions
tframe = Frame(root, width=160)
tframe.pack()

#user lookup field
user = Entry(tframe, width=50, borderwidth=2)
user.pack(side=LEFT)
#main frame
mframe = Frame(root, width=160)
mframe.pack()
#scrollbar
scroll = Scrollbar(mframe)
scroll.pack(side=RIGHT, fill=Y)
#get "home" timeline - everyone you follow + yourself
def gethometl():
    hometl = api.GetHomeTimeline(count=100)
    hlist = [h.user.name + "\n" + h.text + "\n" + h.created_at for h in hometl]
    hstr = "\n \n".join(hlist)
    tl.delete(1.0, END)
    tl.insert(END,hstr)
#button to call the gethometl function
return_home = Button(tframe, text="Your Timeline", command=gethometl)
return_home.pack()
#timeline text
tl = Text(mframe, width=150, wrap=WORD)
tl.pack()
#this function has to be below the timeline text field to insert text into it
#must also be defined BEFORE the getusername function that calls it
def gettimeline(username):
    user = username
    #return to hometl if a blank user is searched
    if user == "":
        gethometl()
    else:
        #get tweets for a user with all info
        statuses = api.GetUserTimeline(screen_name = user,
                                   exclude_replies = True, count = 100)
        #turn tweets into list containing strs of text and creation time
        slist = [s.text + "\n" + s.created_at for s in statuses]
        #turn list into string
        x = "\n \n".join(slist)
        #insert list at end of tl field (need to make this REPLACE previous tweets)
        tl.delete(1.0, END)
        tl.insert(END, x)
#get a username from the username field and pass it to gettimeline
#must be defined BEFORE the button that calls it
def getusername():
    username = user.get()
    gettimeline(username)
#button to switch to another user's timeline
usersearch = Button(tframe, text="Find User", command=getusername)
usersearch.pack(side=RIGHT)
#function to get DMs
def getdms():
    dms = api.GetDirectMessages(count = 100)
    dmlist = [m.text + "\n" + m.created_at for m in dms]
    m = "\n \n".join(dmlist)
    tl.delete(1.0, END)
    tl.insert(END, m)
#button to show DMs
dmbutton = Button(tframe, text="Direct Messages", command=getdms)
dmbutton.pack()
#make scrollbar scroll timeline
tl.config(yscrollcommand=scroll.set)
scroll.config(command=tl.yview)
#field to enter new tweets
tweet = Entry(mframe, width=160, borderwidth=2)
tweet.pack(side=LEFT)
#get text from new tweet field and pass to sendtweet
def gettext():
    tweettext = tweet.get()
    sendtweet(tweettext)
#use api to post new tweet
def sendtweet(post):
    text = post
    status = api.PostUpdate(text)
submit = Button(mframe, text="Submit", command=gettext)
submit.pack(side=RIGHT)
#load home timeline by default at runtime
gethometl()
root.mainloop()

