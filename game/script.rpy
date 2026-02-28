# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#who_color="#4c64ce"

define u = Character("You")
define p = Character("Phone")
define c = Character("Caller")
define bbg = Character("Random person")
define g = Character("Another random person")
define sw = Character("Slow walker")


# The game starts here.

label end:
    scene bg room

    "You find another job,"
    "And die happily of old age"
    "The end"

    return

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    u "Ugh! Why are there literally NO CASES???"
    u "I'm going to be jobless!"
    u "People don't make crimes like they used to!"
    u "What happened to society?"
    u "What happened to the criminals?"
    u "Why can't someone... like... commit a murder or something?"
    u "I'm sooooo bor..."
    p "RING RING RING"
    u "FINALLY!!"
    
    menu:
        "Will you answer?"

        "Answer phone":
            "You answer the phone"

        "Just watch it ring until they give up":
            "You just let the phone ring."
            "It rings."
            "And it rings."
            "And it rings."
            "And finally..."
            "It stops ringing"
            jump end

    c "I... I... I..."
    u "Go on! What happened? A robbery? Arson? Or perhaps even... murder?"
    c "No, nothing like that. It's worse. I... I can't explain it on the phone! You'll have to see for yourself!"
    u "On my way!"

label lobby:

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
    "You arrive at the coffee room"
    c "Help! Help!"
    u "What... happened here?"
    c "Someone didn't close the youghurt completely and when I shaked it..."
    u "Well... that sucks."
    c "You HAVE TO figure out who did this!"
    u "Don't worry! I'm an expert."
    menu:
        "Go to lobby":
            jump lobbyDetecting
        
        "Go to office":
            jump youghurt


label lobbyDetecting:
    "You look around in the lobby"
    u "Looks like there's nobody here..."
    menu:
        "Oh man! What to do now?"

        "Go to office":
            jump youghurt

        "Give up and go home":
            "You decide you've had enough of this nonsense"
            "It's too hard!"
            jump end

label youghurt:
    "You arrive at the office"
    menu:
        "What's next?"

        "Yell":
            u "WHO LEFT THE YOUGHURT OPEN??"
            "A hand arises from behind one desk"
            bbg "Me"

        "Go talk to them one by one":
            "You walk up to a person"
            u "Heyyy"
            bbg "Hi?"
            u "Look... when did you last use the coffee room?"
            bbg "Ten minutes ago"
            u "Oh cool cool..."

            menu:
                "What do you ask them?"

                "How's your day been going?":
                    bbg "My day? I arrived at the office"
                    bbg "Then I started doing my completely normal job that I definitely do"
                    bbg "Like I did yesterday"
                    bbg "And the day before yesterday"
                    bbg "And the day before the day before yesterday"
                    bbg "And the day before day before..."
                    u "Yeah I get the point!"
                    bbg "Oh"
                    u "Have you seen everything... abnormal?"
                    bbg "Nope"
                    menu:
                        "Go up to next person":
                            jump gum
                        
                        "Did you... touch the youghurt?":
                            bbg "Yeah why?"

                "Did you happen to eat any youghurt?":
                    bbg "Now that I think of it..."
                    bbg "Might have"
                    bbg "But why would I tell you about it?"
                    menu:
                        "Why are you acting so suspicious?":
                            bbg "I'm not!"
                            u "Ummm yes you are."
                            bbg "No"
                            u "Yes"
                            bbg "No"
                            jump debate

                        "I'm just a chill guy!":
                            bbg "Oh! I didn't realize!"
                            u "Well... now you did!"
                            bbg "Lol but yeah I ate a bowl of mac and cheese with youghurt"

                        "I'm trying to solve a crime here":
                            bbg "Well I haven't done any crimes ;)"
                            bbg "But you might want to check out that guy"
                            menu:
                                "Go talk to him":
                                    jump gum

                                "But did you eat youghurt?":
                                    bbg "Yeah wh..."
                                    bbg "Aww man, you caught me!"
    u "So you DID eat youghurt!"
    u "Did you happen to leave it open"
    bbg "Hmm..."
    bbg "Did I?"
    bbg "Come to think of it..."
    bbg "Yes! I did!"
    u "WHAT? Why would you commit such a crime?"
    bbg "It was an accident!"
    menu:
        "Do you believe him?"

        "Yes":
            g "AAAAH!"
            u "What's that?"
            u "Sorry, I've got to go!"
            bbg "Oh okay"
            jump gum

        "Yes, why wouldn't I? It happens to everyone!":
            g "AAAAH!"
            u "What's that?"
            u "Sorry, I've got to go!"
            bbg "Oh okay"
            jump gum

        "Yes, why is this even a question?":
            g "AAAAH!"
            u "What's that?"
            u "Sorry, I've got to go!"
            bbg "Oh okay"
            jump gum

        "No!":
            u "Yeah doubt that"
            bbg "Why are you so nosy?"
            u "Why are you so sus?"
            bbg "No I'm not!"
            u "That's what a sus person would say!"
            bbg "How do you know?"
            u "I have 10 000 hours in Among Us!"
            u "Now answer the question!"
            bbg "What do you want me to say?"
            bbg "That I did it to blind anyone in the room so that I could sneak into the Super Secret Secret Room (SSSR)?"
            u "Well... did you?"
            bbg "Well... maybe..."
            u "Hmm okay..."
            u "In this completely hypothetical situation that you DID sneak into the SSSR..."
            u "WHY?"
            bbg "Well, since this is completely hypothetical and has nothing to do with what actually happened"
            bbg "I did... would have done it... because in the SSSR... there are secrets."
            bbg "Dark secrets."
            bbg "And had they ever met daylight..."
            bbg "Would expose the truth!"
            bbg "Which is that the "
            u "Wow!"
            u "That was... oddly specific"
            bbg "But remember that it's just hypothetical!"
            u "Yeah right..."
            u "Look I don't"
            g "AAAAAH!!!"
            u "What's that?"
            "You turn around to look at the voice"
            "And when you turn back to the youghurt man"
            "He's gone!"
            u "What? He was just here!"
            g "AAH AAH AAH! It's killing me! Somebody help!"
            u "Maybe I should go check that out..."
            jump gum


label debate:
    bbg "Nope"
    u "Yup"
    bbg "Nuh uh"
    u "Yuh uh"
    bbg "No"
    menu:
        "Yes":
            jump debate

        "Just give up":
            jump gum

label gum:

    "You walk up to the screaming person"
    g "AAAH HELP!"
    g "I think I touched it!"
    u "You... what?"
    g "AAH! AAH! AAH! Get it out!"
    u "Hey! Calm down! What happened?"
    g "Someone... Someone commited..."
    g "A CRIME!"
    u "Another crime?"
    g "What do you mean another? Anyways..."
    g "I was just sitting at my desk..."
    g "Doing work as usual"
    g "Kind of like how I did yesterday"
    g "And the day before yesterday"
    g "And the day before that"
    g "And the d-"
    u "YES! I get it."
    g "Oh... Sorry... It's just this place."
    g "I swear I would quit if I just could."
    g "The only reason to stay is the coffee."
    g "And maybe the pay too."
    u "Sure... And the crime?"
    g "Oh, yes! I was reaching for some papers when it happened!"
    u "When what happened?"
    g "I touched it!"
    g "A chewed gum!"
    u "And that's the crime?"
    g "Yes! You'll have to find the culprit!"
    menu:
        "Seems random. What do you do?"

        "Find them":
            u "Okay."
            g "Good luck! This office needs justice!"

        "Go home":
            "You decide that none of this matters enough."
            "You start to leave the office"
            jump slowWalker



label slowWalker:
    "Unfortunately someone else wants to leave"
    "And they don't seem to be in a hurry"
    "Why are these slow walkers everywhere?"
    u "Hey!"
    u "Don't you know that walking slowly is a crime against humanity?!"
    u "Or at least it should be..."
    sw "Sorry!"
    sw "I just work here!"
    u "And how does that affect your walking speed?"
    sw "It's my... I've had a rough week, okay!"
    menu:
        "Me too! A rough week doesn't give you the right to walk at whatever speed you want!":
            sw "But it's my... forget it"
            u "I don't forget anything!"
            sw "I'm just a bit slow!"       

        "I see. Can I get past?":
            sw "Sure"
            u "Thanks"
            "Finally it's over!"
            "You walk home peacefully."
            jump end

    menu: 
        "Oh okay. Makes sense.":
            u "So... I guess that's it?"
            sw "You can go past me if you want."
            u "Thanks!"
            "Finally it's over!"
            "You walk home peacefully."
            jump end
        
        "Lies!":
            sw "What can I do?!"
            sw "I'm a bad liar!"
            u "No you're not! I'm just very good at detecting lies."
            sw "Aww thanks! How did you get so good at it?"
            u "It's kind of my job. So... Why are you walking so slow?"
    
    sw "Well it all started a couple of weeks ago..."
    sw "I was unemployed"
    sw "And needed money to buy new pokemopn cards to my collection."
    sw "Then I got a job offer."

    

    return