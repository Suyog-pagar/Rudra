


from random import choice

hello = ('hello how are you', 'hey', 'hii', 'hi', 'hai' , 'whu are you' , 'hu r u' , 'who are you' , 'who r u')
replyForHello = ('Hello Sir , I Am Rudra .', "Hello Sir , , Nice To Meet You Again .")

bye = ('bye', 'goodbye', 'tata')
replyForBye = ('Bye Sir.', "It Will Be Nice to Meet You again .", "Bye Sir.", "Okay Sir")

appreciate = ("cool", "nice", "awesome", "amazing", "good",)
appreciateReply = ("That's my Pleasure sir", "Thank you sir", "You're welcome sir")

stateEnquiry = ('how are you', 'are you fine', 'are you okay', 'are you ok')
replyForStateEnquiry = ('I Am Fine Sir', "I'm doing Great sir.", "I'm Absolutely Fine sir.",
                        "My only regret I'm feeling is I'm limited with set of codings sir")

question = ("what can i do for that", "what should i do now", 'do you need a update')
replyForQuestion = ("Update me more sir", "Code me with machine learning algorithms Sir", "Code me with Deep Learning algorithms sir")

nice = ('nice', 'good', 'thanks')
replyForNice = ("Ohh , It's Okay sir.", "That's my pleasure ", "I can do more sir")

functions = ['functions', 'abilities', 'what can you do', 'features', 'what can you do for me', 'what are your abilities', 'what is your ability', 'what else can you do']
replyForFunctions = ('I Can Perform Many Task Or Varieties Of Tasks as coded sir',
                     'I can do a community post on your channel that you are simply gaming without making videos',
                     'My programs are limited by codes',
                     "I'll display the list of features i can perform if you type 'features' in my command box")

jokeReplyQuery = ["Sir, I don't think this is a joke", "Sorry for this bad joke sir I got this from Google", "Sir, This is really a nice joke I love this one"]

sorryReply = ("Sir,I'm not Programmed to do that", "Sir, That's beyond my abilities", "Sorry Sir, My codes are limited", 'Sir, I dont get your point')


def jarvyChatBot(Text):
    Text = str(Text).lower()
    try:
        Text = Text.replace("Rudra", "")
        Text = Text.replace("rudra", "")
    except:
        Text = str(Text)
    for word in Text.split():
        if word in hello:
            reply = choice(replyForHello)
            return reply
        elif word in bye:
            reply = choice(replyForBye)
            return reply
        elif word in appreciate:
            reply = choice(appreciateReply)
            return reply
        elif word in nice:
            reply = choice(replyForNice)
            return reply

    if Text in question:
        reply = choice(replyForQuestion)
        return reply
    elif Text in stateEnquiry:
        reply = choice(replyForStateEnquiry)
        return reply
    elif Text in functions:
        reply = choice(replyForFunctions)
        return reply
    else:
        reply = choice(sorryReply)
        return reply
