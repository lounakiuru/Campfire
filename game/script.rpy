# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define u = Character("You")
define p = Character("Phone")
define c = Character("Caller")


# The game starts here.

label notAnswer:
    scene bg room

    "You just let the phone ring."
    "It rings."
    "And it rings."
    "And it rings."
    "And finally..."
    "It stops ringing"
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

        "Just let watch it ring until they give up":
            jump notAnswer

    c "I... I... I..."



    

    # This ends the game.

    return
