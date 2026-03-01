# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#color="#4c64ce"

define u = Character("You", image = "u")
define p = Character("Phone")
define c = Character("Caller")
define bbg = Character("Random person", image = "bbg")
define g = Character("Another random person")
define sw = Character("Slow walker")
define sbbg = Character("A shady, bad guy", image = "bbg")


# The game starts here.

label end:
    scene bg bedroom
    show u wink


    "You find another job,"
    "And die happily of old age"
    "The end"

    return

label start:

    play music mysterious

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show u speak

    # These display lines of dialogue.

    u "Ugh! Why are there literally NO CASES???"
    u "I'm going to be jobless!"
    u "People don't make crimes like they used to!"
    u "What happened to society?"
    u "What happened to the criminals?"
    u "Why can't someone... like... commit a murder or something?"
    u "I'm sooooo bor..."
    show u basic
    p "RING RING RING"
    u @ speak "FINALLY!!"
    
    menu:
        "Will you answer?"

        "Answer phone":
            "You answer the phone"

        "Just watch it ring until they give up":
            "You just let the phone ring."
            "It rings."
            "And it rings."
            "And it rings.."
            "And finally..."
            "It stops ringing"
            jump end

        "I'm testing let me to sw":
            jump slowWalker

    c "I... I... I..."
    u @ speak "Go on! What happened? A robbery? Arson? Or perhaps even... murder?"
    c "No, nothing like that. It's worse. I... I can't explain it on the phone! You'll have to see for yourself!"
    u @ wink "On my way!"

label lobby:

    scene bg lobby

    show u basic

    "You arrive at an office building."
    "You might recognize the logo or not."
    u "Hmm..."
    u "They told me to come to the coffee room."

    menu: 
        "Where do you go?"

        "Coffee room":
            jump coffeeRoom

        "Coffee room because I'm not dumb":
            jump coffeeRoom

        "Seriously why is this even a question? Coffee room!!":
            jump coffeeRoom

        "Home":
            "You give up and go home"
            jump end


label coffeeRoom:

    scene bg coffeeroom

    show u basic
    show c

    "You arrive at the coffee room"
    c "Help! Help!"
    u @ speak "What... happened here?"
    c "Someone didn't close the yogurt completely and when I shaked it..."
    u @ speak "Well... that sucks."
    c "You HAVE TO figure out who did this!"
    u @ wink "Don't worry! I'm an expert."
    menu:
        "Go to lobby":
            jump lobbyDetecting
        
        "Go to office":
            jump yogurt


label lobbyDetecting:

    scene bg lobby

    show u basic

    "You look around in the lobby"
    u speak "Looks like there's nobody here..."
    menu:
        "Oh man! What to do now?"

        "Go to office":
            jump yogurt

        "Give up and go home":
            "You decide you've had enough of this nonsense"
            "It's too hard!"
            jump end

label yogurt:

    scene bg office

    show u basic

    "You arrive at the office"
    menu:
        "What's next?"

        "Yell":
            u @ speak "WHO LEFT THE YOGURT OPEN??"
            "A hand arises from behind one desk"
            bbg "Me"
            show bg officechair1


        "Go talk to them one by one":
            show bg officechair1
            show bbg basic
            "You walk up to a person"
            u @ speak "Heyyy"
            bbg @ speak "Hi?"
            u @ speak "Look... when did you last use the coffee room?"
            bbg @ speak "Ten minutes ago"
            u @ speak "Oh cool cool..."

            menu:
                "What do you ask them?"

                "How's your day been going?":
                    bbg speak "My day? I arrived at the office"
                    bbg "Then I started doing my completely normal job that I definitely do"
                    bbg "Like I did yesterday"
                    bbg "And the day before yesterday"
                    bbg "And the day before the day before yesterday"
                    bbg "And the day before day before..."
                    show bbg basic
                    u @ speak "Yeah I get the point!"
                    bbg @ speak "Oh"
                    u @ speak "Have you seen everything... abnormal?"
                    bbg @ speak "Nope"
                    menu:
                        "Go up to next person":
                            jump gum
                        
                        "Did you... touch the yogurt?":
                            bbg @ speak "Yeah why?"

                "Did you happen to eat any yogurt?":
                    bbg @ speak "Now that I think of it..."
                    bbg @ speak "Might have"
                    bbg @ mad "But why would I tell you about it?"
                    menu:
                        "Why are you acting so suspicious?":
                            bbg @ mad "I'm not!"
                            u @ speak "Ummm yes you are."
                            bbg @ mad "No"
                            u @ speak "Yes"
                            bbg @ mad "No"
                            jump debate

                        "I'm just a chill guy!":
                            bbg @ speak "Oh! I didn't realize!"
                            u @ speak "Well... now you did!"
                            bbg @ speak "Lol but yeah I ate a bowl of mac and cheese with yogurt"

                        "I'm trying to solve a crime here":
                            show bbg wink
                            bbg "Well I haven't done any crimes ;)"
                            bbg "But you might want to check out that guy"
                            menu:
                                "Go talk to him":
                                    jump gum

                                "But did you eat yogurt?":
                                    bbg @ speak "Yeah wh..."
                                    bbg @ mad "Aww man, you caught me!"
    

    u @ speak "So you DID eat yogurt!"
    u @ speak "Did you happen to leave it open"
    show bbg speak
    bbg "Hmm..."
    bbg "Did I?"
    bbg "Come to think of it..."
    bbg @ wink "Yes! I did!"
    show bbg basic
    u @ speak "WHAT? Why would you commit such a crime?"
    bbg @ speak "It was an accident!"
    menu:
        "Do you believe him?"

        "Yes":
            g "AAAAH!"
            u @ speak "What's that?"
            u @ speak "Sorry, I've got to go!"
            bbg @ speak "Oh okay"
            jump gum

        "Yes, why wouldn't I? It happens to everyone!":
            g "AAAAH!"
            u @ speak "What's that?"
            u @ speak "Sorry, I've got to go!"
            bbg @ speak "Oh okay"
            jump gum

        "Yes, why is this even a question?":
            g "AAAAH!"
            u @ speak "What's that?"
            u @ speak "Sorry, I've got to go!"
            bbg @ speak "Oh okay"
            jump gum

        "No!":
            u @ speak "Yeah doubt that"
            bbg @ mad "Why are you so nosy?"
            u @ speak "Why are you so sus?"
            bbg @ mad "No I'm not!"
            u @ speak "That's what a sus person would say!"
            bbg @ mad "How do you know?"
            u @ speak "I have 10 000 hours in Among Us!"
            u @ speak "Now answer the question!"
            bbg @ mad "What do you want me to say?"
            bbg @ mad "That I did it to blind anyone in the room so that I could sneak into the Super Secret Secret Room (SSSR)?"
            u @ speak "Well... did you?"
            bbg @ speak "Well... maybe..."
            u @ speak "Hmm okay..."
            u @ speak "In this completely hypothetical situation that you DID sneak into the SSSR..."
            u @ speak "WHY?"
            show bbg speak
            bbg "Well, since this is completely hypothetical and has nothing to do with what actually happened"
            bbg "I did... would have done it... because in the SSSR... there are secrets."
            bbg "Dark secrets."
            bbg "And had they ever met daylight..."
            bbg "Would expose the truth!"
            bbg "Which is that the train company"
            bbg "Runs merely on coffee and donuts!"
            show bbg basic
            u @ speak "Wow!"
            u @ speak "That was... oddly specific"
            bbg @ speak "But remember that it's just hypothetical!"
            u @ speak "Yeah right..."
            u @ speak "Look I don't-"
            g "AAAAAH!!!"
            u @ speak "What's that?"
            "You turn around to look at the voice"
            hide bbg
            "And when you turn back to the yogurt man"
            "He's gone!"
            u @ speak "What? He was just here!"
            g "AAH AAH AAH! It's killing me! Somebody help!"
            u @ speak "Maybe I should go check that out..."
            jump gum


label debate:
    show bbg mad
    bbg "Nope"
    u @ speak "Yup"
    bbg "Nuh uh"
    u @ speak "Yuh uh"
    bbg "No"
    menu:
        "Yes":
            jump debate

        "Just give up":
            jump gum

label gum:

    scene bg officechair2

    show u basic
    show g scream

    "You walk up to the screaming person"
    g "AAAH HELP!"
    g "I think I touched it!"
    show g basic
    u @ speak "You... what?"
    g @ scream "AAH! AAH! AAH! Get it out!"
    u @ speak "Hey! Calm down! What happened?"
    g @ scream "Someone... Someone commited..."
    g @ scream "A CRIME!"
    u @ speak "Another crime?"
    show g scream
    g "What do you mean another? Anyways..."
    g "I was just sitting at my desk..."
    g "Doing work as usual"
    g "Kind of like how I did yesterday"
    g "And the day before yesterday"
    g "And the day before that"
    g "And the d-"
    show g basic
    u @ speak "YES! I get it."
    show g scream
    g "Oh... Sorry... It's just this place."
    g "I swear I would quit if I just could."
    g "The only reason to stay is the coffee."
    g "And maybe the pay too."
    show g basic
    u @ speak "Sure... And the crime?"
    g @ scream "Oh, yes! I was reaching for some papers when it happened!"
    u @ speak "When what happened?"
    g @ scream "I touched it!"
    g @ scream "A chewed gum!"
    u @ speak "And that's the crime?"
    g @ scream "Yes! You'll have to find the culprit!"
    menu:
        "Seems random. What do you do?"

        "Find them":
            u @ wink "Okay."
            g "Good luck! This office needs justice!"

        "Go home":
            "You decide that none of this matters enough."
            "You start to leave the office"
            jump slowWalker
    menu:
        "But where to start?"

        "Investigate the gum":
            "The gum seems fresh."
            "They must be near!"

        "Interview the victim":
            u @ speak "So... have you seen anyone near your desk?"
            g "Nope"
            u @ speak "Right... well... do you have any enemies here?"
            g "Nope.  I don't talk to people."
            u @ speak "Any idea who could have done this?"
            g "Aren't you supposed to be the detective?"
            menu:
                "Give up and go home":
                    u speak "Yeah right"
                    u "Well... if you don't care, I'll head home"
                    u "Bye"
                    "And so you head towards the exit."
                    jump slowWalker
                "Investigate the gum instead":
                    u @ speak "Well if you don't want to collaborate, I'll investigate the evidence!"
                    "You take a look at the gum."
                    "It's sticky and still warm."
    u @ speak "Ewww! It's fresh!"
    g @ scream "Exactly!"
    u speak "And it smells like strawberry..."
    u "Wait..."
    u "What do you have there?"
    show u basic
    g "Gum"
    u @ speak "What flavour?"
    g "Strawberry cheesecake"
    u @ speak "And... When did you last eat it?"
    g "Like 10 minutes ago"
    u "..."
    u @ speak "...Seriously?"
    g "What?"
    u @ speak "Where did you put it?"
    g "Idk.. probably under my... Oh"
    u @ speak "How do you even forget that?"
    g "It was an accident!"
    menu:
        "Well... I guess teenagers are... teenagers":
            g "I'm not a teenager! I'm 42!"
            u @ speak "Yeah right"
            "You decide you've had enough"
            "Time to finally go home"
            jump slowWalker

        "Whatever":
            "You decide you've had enough"
            "Time to finally go home"
            jump slowWalker

        "That's disgusting! Why would you stick it under the table?":
            g "Because it's... nothing"
            g "I just... didn't pay attention"
            g "I was watching cat videos"
            menu:
                "Honestly I'm not surprised.":
                    "You decide you've had enough"
                    "Time to finally go home"
                    jump slowWalker
                "Are you sure?":
                    g "What else would I be doing?"
                    menu:
                        "I smell crime!":
                            u @ speak "You... are lying!"
                        "Your work!":
                            "You decide you've had enough"
                            "Time to finally go home"
                            jump slowWalker
    g "Ugh fine!"
    g "I was just lying all along"
    u @ speak "So... what's the deal then?"
    g "The deal? I honestly don't remember. It included money."
    u @ speak "Who did you make the deal with?"
    g "I don't remember! I was scrolling TokTik!"
    u @ speak "And... Your job was..."
    g "Uhhh something to do with gum but can you fuckle off now?"
    u @ speak "After this converstation... I'd love to!"
    jump slowWalker


label slowWalker:

    scene bg hallway
    show u basic
    show sw back

    "Unfortunately someone else wants to leave"
    "And they don't seem to be in a hurry"
    "Why are these slow walkers everywhere?"
    u mad "Hey!"
    u "Don't you know that walking slowly is a crime against humanity?!"
    u "Or at least it should be..."
    show sw basic
    sw @ speak "Sorry!"
    sw @ speak "I just work here!"
    u "And how does that affect your walking speed?"
    sw @ speak "It's my... I've had a rough week, okay!"
    menu:
        "Me too! A rough week doesn't give you the right to walk at whatever speed you want!":
            show u basic
            sw @ speak "But it's my... forget it"
            u @ speak "I don't forget anything!"
            sw @ speak "I'm just a bit slow!"       

        "I see. Can I get past?":
            sw @ speak "Sure"
            u @ speak "Thanks"
            "Finally it's over!"
            "You walk home peacefully."
            jump end

    menu: 
        "Oh okay. Makes sense.":
            u @ speak "So... I guess that's it?"
            sw @ speak "You can go past me if you want."
            u @ speak "Thanks!"
            "Finally it's over!"
            "You walk home peacefully."
            jump end
        
        "Lies!":
            sw @ speak "What can I do?!"
            sw @ speak "I'm a bad liar!"
            u @ speak "No you're not! I'm just very good at detecting lies."
            sw @ happy "Aww thanks! How did you get so good at it?"
            u @ speak "It's kind of my job. So... Why are you walking so slow?"
    
    sw @ speak "Well it all started a couple of weeks ago..."

    scene bg shadyplace

    show sw basic

    sw "I was unemployed"
    sw "And needed money to buy new Pokemon cards for my collection."
    sw "Then I got a job offer."

    show bbg shadywink at right

    sbbg "Heyyyy!"
    sw @ speak "What do you want?"
    sbbg "What do YOU want?"
    sw @ speak "A job?"
    sbbg "Well don't worry, be happy now!"
    sbbg "I have a job for you!"
    sw @ speak "Yay! Now I can buy Charizard!"
    sbbg "What?"
    sw @ speak "Forget."

    scene bg lobby

    show sw basic
    show u basic

    sw @ speak "You see? Not up to me!"
    u @ speak "Not at all..."
    sw @ speak "And then he gave me the instructions"
    sw @ speak "I was shocked!"
    sw @ speak "But the stakes were too high..."
    u @ speak "So what did you do?"
    sw @ speak "I infiltrated myself into VR"
    sw @ speak "And then I cancelled their donut subscription!"
    u @ speak "Because then..."
    sw @ speak "They would have no more donuts!"
    u @ speak "But why?"
    sw @ speak "Haven't you heard?"
    u @ speak "Heard what?"
    sw @ speak "That the boss is trying to take down-"
    sw @ speak "Oh wait"
    sw @ speak "That's probably classified"
    u @ speak "Who is your boss? And why do you walk so slowly?"
    sw @ speak "I can't tell you! And I stubbed my toe when I first walked in here!"
    u @ speak "What?"
    sw @ speak "If I had actually gotten the job, they would have briefed me about it!"
    sw @ speak "Wait..."
    sw @ speak "Why didn't I just..?"
    u @ mad "Whatever! Tell me who your boss is!"
    sw @ speak "I can't! I've said too much!"
    "And then he sprints off, apparently forgetting about the pain in his toe."
    "This entire mess just got way deeper"
    "And going on might change your life forever."
    menu:
        "Do you want to continue?"

        "Yes":
            jump office2

        "I've had enough of this!":
            "You decide that this scandal is too much"
            "Time to forget about it and walk home feeling relieved that it's over."
            jump end

    
label office2:

    scene bg office

    "You walk back into the office"
    "Time to find out who's behind this!"
    menu:
        "Who do you suspect?"

        "My instincts lead towards Joe":
            jump final

        "I feel like it's the catboy":
            jump gumSuspect

        "My guts are telling me it's the one who called me here!":
            jump callerSuspect

label gumSuspect:
    scene black
    "What an interesting decision!"
    "But is it right?"
    "Only one way to find out..."
    scene bg officechair2
    show u basic
    show g basic

    u @ speak "You havce committed a crime!"
    g "Yeah didn't you already lecture me?"
    u @ speak "Oh right... but another crime!"
    g "You're SO off! The real boss just came here to get what he needed. And now... Nothing will stop him!"
    u @ speak "W-wh-what??"
    g "Game over, loser!"
    "You run out crying. This is too big of a hit for your pride."
    "You decide to just go home and cuddle with your blahaj"
    "As weeks pass, you'll be fine and leave this scandal in the past"
    jump end

label callerSuspect:
    
    scene black

    "So that's what your gut told you!"
    "But is it right?"
    "Only one way to find out..."

    scene bg coffeeroom
    show u basic
    show bbg sad

    "You run to the coffee room as fast as you can"
    "Ready to make the accusation."
    "But the caller has dissapeared."
    
    scene bg coffee
    show bbg hand


label final:
    
    scene black

    "Your instincts havce guided you to..."
    "\"Human by chance, Alpha by choice\"? Imteresting..."
    "But are you correct?"
    "Only one way to find out..."
    
    scene bg officechair1
    show u basic

    u "What? This is empty!"
    menu:
        "Where should you go?"

        "Catboy's desk":
            jump gumSuspect

        "Coffee room":
            jump callerSuspect

        "Give up and go home":
            scene black
            "You tried so hard"
            "And got so far"
            "But in the end"
            "It doesn't even matter"
            "The end"
            return