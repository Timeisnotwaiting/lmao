import asyncio # for running asynchronous func.
import random # for random replies.

ARTICLES = ["a", "the", "an", "in", "on", "of", "at", "am", "i"]

async def exists(query, txt): # txt can be a text or a list or a dict
    query = query.lower()
    for x in txt:
        x = x.lower()
        if query in ARTICLES:
            continue
        if query == x:
            return True
			
    return False

#dict of query with replies.

# common queries.

QUERY_REPLY = {"What is your name ?": ["I'm AI ChatBot", "My name is AI ChatBot"], "Hi": ["Hello !", "How are you !"], "How are you ?": ["Am fine !", "Awesome as always"]} 

# unknown quries.

UNKNOWN_REPLIES = ["Anything more ?", "How are you doing ?", "How can I assist you ?", "Need my assistance?", "Any queries ?"]

ARTICLES = ["a", "the", "an", "in", "on", "of", "at", "am", "i"] 

# assistable quries.

ASSISTABLE = ["restaurant", "hotel", "beach", "college", "school", "railway"]

# main func 

async def  alpha():
    a = 0
    while True:
        print("Hello !, welcome to AIChatBot !\n")
        x = input()
        if not x:
            if a == 3:
                print("Good Bye !") 
                return # sys.exit()
            print(random.choice(UNKNOWN_REPLIES))
            a += 1
        else:
            for c in x:
                j = await exists(c, ASSISTABLE)
                if j:
                    print(f"Yeah there's a {j} near you !")
                else:
                    h = await exists(c, QUERY_REPLY)
                    if h:
                        if c == "name":
                            print(random.choice(QUERY_REPLY["What is your name ?"]))
                        elif c == "How":
                            print(random.choice(QUERY_REPLY["How are you ?"]))
                        else:
                            print(random.choice(QUERY_REPLY["Hi"]))
                    else:
                        if a == 3:
                            print("Good Bye")
                            return
                        print(random.choice(UNKNOWN_REPLIES))
                        
loop = asyncio.get_event_loop()
loop.run_until_complete(alpha())
