import twitter
from Tkinter import *
#create twitter API with credentials from my account
api = twitter.Api(consumer_key='mJbSUQdokViuAh1h6AuKddRQc',
                  consumer_secret='1wmAUS9MTCOiDo6Pn3mdmA8lnjGP9fGkOWrSrXcfmALFUhrImZ',access_token_key='15650341-3Gm5kfypGmzrJOtYwsYoIbNmfKlAD7kDJtBpmkKRf',
                  access_token_secret='xo38OB2e3VGc8ZhEC4cg9nZHbkbAoiPQr7EepGEnLvFC3')
root = Tk()
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
#timeline text
tl = Text(mframe, width=150)
tl.pack()
#this function has to be below the timeline text field to insert text into it
#must also be defined BEFORE the getusername function that calls it
def gettimeline(username):
    user = username
    #get tweetsfor a user with all info
    statuses = api.GetUserTimeline(screen_name = user)
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
#button to insert tweets from a different timeline
usersearch = Button(tframe, text="Find User", command=getusername)
usersearch.pack(side=RIGHT)
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


root.mainloop()

