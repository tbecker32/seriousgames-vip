# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Buzz")
image pre_note = "images/note.png"
image note = "images/note.png"
image wallet = "images/wallet.png"
image metformin = "images/metformin.png"

define player = Character("[playerName]", color=(222, 34, 213, 255))
define doctor = Character("Doctor Cabrera", color=(17, 144, 255, 255))
define buzz = Character("Buzz", color=(190, 166, 9, 255))
define cousin = Character("Cousin", color=(235, 111, 10, 255))

define audio.titlemusic = "titlescreen.ogg"
define audio.party1 = "collegekids1.ogg"
define audio.partymusic = "partymusic.ogg"
define audio.rowdyparty = "rowdyparty.ogg"

define audio.addpoints = "addpoints.ogg"
define audio.addpoint = "addpoint.ogg"
define audio.nopoints = "nopoints.ogg"

# sound effect for phone notifications
define audio.ping = "ping.ogg"
# sound effect for each time money is spent
define audio.coin = "coindrop.ogg"
# sound effect for when energy goes down
define audio.energy = "energydown.ogg"
# when a1c changes
define audio.a1c_beep = "a1c_beep.ogg"

# sound effect for button clicking sound
define audio.click = "click.ogg"

# set to starting levels to display in hud
default current_a1c = "a1c_080"
default current_stress = "high_stress"
default current_energy = "low_energy"
default stress = 5
default health = 5
default energy = 5

define inventory_open = False


########### START INVENTORY DEMO
#
#    "Hi [playerName]! Here's a doctor's note."
#
#    $ inventory_items.append("doctor's note")
#
#    "Ooh, it has a lot of information. Have a look at it."
#
#    # hide screen inventory_display_toggle (this hides the inventory button on the top left)
#
#    "Oh no, you dropped your wallet! Here you go..."
#
#    $ inventory_items.append("wallet")
#
#    "Check out your wallet!"
#
#    $ inventory_items.remove("wallet")
#
#    "I'm taking away your wallet :)"

########### END INVENTORY DEMO


########### START GAME SCRIPT

image buzz normal = "images/normalbuzzsprite.png"
image buzz doctor = "images/doctorbuzz.png"
image buzz funny = "images/funnybuzz.png"
image buzz lab = "images/labbuzz.png"
image buzz cousin = "images/cousin_buzz.png"

define wallet_low = "images/wallet_low.png"
define wallet_midlow = "images/wallet_midlow.png"
define wallet_mid = "images/wallet_mid.png"
define wallet_high = "images/wallet_high.png"

image phone = "images/phone_talking.png"
image doctors_note = "images/doctors_note.png"
image prediabetes_screenshot = "images/prediabetes_info.png"
image prediabetes_note = "images/doctors-note-prediabetes.png"

image bg good_ending = "images/good_ending.png"
image bg okay_ending = "images/okay_ending.png"
image bg bad_ending = "images/bad_ending.png"
image bg black_background = "images/black_background.jpg"

image bg doctors_office = "images/doctors-office.jpg"
image bg apartment_bday = "images/apartment-bday.jpg"
image bg apartment_bedroom = "images/apartment-bedroom.jpg"
image bg bioinformatics_lab = "images/bioinformatics-lab.jpg"
image bg culc_photo = "images/culc-photo.jpg"
image bg crc_photo = "images/crc-photo.jpg"
image bg florida_photo = "images/florida.jpg"
image bg restaurant = "images/chilis_restaurant.jpg"

image chips = "images/chips.png"
image frozenfrenchfries = "images/frozenfrenchfries.png"
image soda = "images/soda.png"
image bcsoup = "images/bcsoup.png"
image beer = "images/beer.png"
image burgerfries = "images/burgerfries.png"
image chipsguac = "images/chipsguac.png"
image ctasalad = "images/ctasalad.png"
image salmonbroccoli = "images/salmonbroccoli.png"
image steakpotato = "images/steakpotato.png"
image doordash = "images/doordash.png"
image energydrink = "images/monster.png"
image panera = "images/panera.png"
image cfa = "images/cfa.png"
image burgerfriesshake = "images/burgerfriesshake.png"
image choccake = "images/choccake.png"
image cookies = "images/chocchipcookies.png"
image lavacake = "images/choclavacake.png"
image chocsb = "images/chocdippedsb.png"
image sorbet = "images/sorbet.png"
image icecreamcontainer = "images/icecream.png"
image grilledprotveg = "images/grilledPV.png"
image chipotle = "images/chipotle.png"
image treadmill = "images/treadmill.png"
image stairmaster = "images/stairmaster.png"
image weights = "images/weights.png"

image carbcountingstart = "images/carbcountingstart.png"
image symptomsstart = "images/symptomsstart.png"

### BEGINNING SCENARIO

label start:
    $ score = 0
    $ money = 0
    $ carbCount = 0
    $ went_grocery_shopping = False

    show bg crc_photo

    play music titlemusic loop

    $ playerName = renpy.input("What is your name?", length = 15)
    $ playerName = playerName.strip()
    if not playerName: 
        $ playerName = "Techie"

    show screen inventory_display_toggle

### PREDIABETES


label intro1:
    with Dissolve(.5)
    pause 0.5
    scene bg apartment_bday:
        zoom 1.6

    show screen pre_stress_display
    show screen pre_energy_display
    show screen pre_health_display
    """
    You're attending a family reunion. Chitchatting with everyone.
    """
    player "Yeah, it is nice to see everyone again. I haven't seen Annie since… the incident…"

    show buzz cousin
    cousin "Oh right… that… well I'm glad they were able to save her toe at least."
    player "Can't say the same for Regina…"
    cousin "Oh don't tell me you're on her side for this!"
    player "I'm not saying anything!! *Laughs* Give me a second here, I need to use the restroom."
    cousin "Again? This is like the third time since we started talking an hour ago."
    player "I must've drank a lot, chatting with the family gets me thirsty!"
    hide buzz cousin
    """
    As you head to the bathroom, you glance down at your cup which you haven't refilled since getting here… and you've only drank half of it…
    """
    """
    After returning from the bathroom, you rejoin your cousin. He’s looking at you kinda strange.
    """
    player "What's up?"
    show buzz cousin
    cousin "I’m just a little worried about you. You really have been peeing a lot and I feel like your skin around your neck is a little dark… "

    menu:
        "Oh come on, it’s not that big a deal. I already told you, I drank a lot. Come on, let’s ask Uncle Haru about what he thinks of Annie being here. ":
            hide buzz cousin
            jump intro2
        "What are you trying to say? Do you think there’s something actually wrong with me?":
            pass
    
    cousin "Not necessarily, it’s just that… well… when my mom was first diagnosed with diabetes, they asked her if she had had any symptoms prior."
    cousin "The doctor said that if she had come into the office earlier, they might have been able to work out a plan so she didn’t develop diabetes."

label loopingMenu:
    menu:
        "And the symptoms were...?":
            cousin "Frequent urination and darkness on your neck, arms, and groin. I remember my mom peeing all the time back then."
            jump loopingMenu
        "So you think I have diabetes...?":
            cousin "No! No, the doctors said those symptoms are typical of *pre-diabetes*. Diabetes is a lifelong condition, but pre-diabetes is still reversible!"
            jump loopingMenu
        "Huh… okay I will keep that in mind, thanks for telling me… wanna go ask Uncle Haru what he thinks of Annie being here?":
            cousin "That man is such a gossip... of course I do."
            jump intro2
            


label intro2:
    hide buzz cousin
    with Dissolve(.5)
    pause 0.5
    scene bg apartment_bedroom:
        zoom 1.3
    """
    You're back at home, and what your cousin said to you today has really stuck with you. You can’t help but google “Pre-Diabetes”, just to see what comes up.
    """
    show prediabetes_screenshot:
        ypos 0
        xpos 650
    pause 10.0
    """
    Source: Prediabetes - Symptoms and causes. (2024). Retrieved March 18, 2025, from Mayo Clinic website: https://www.mayoclinic.org/diseases-conditions/prediabetes/symptoms-causes/syc-20355278
    """
    player "Well… that does sound serious… And since it’s still reversible, maybe I still have a chance to fix it?"
    hide prediabetes_screenshot
    menu:
        "I’ll schedule an appointment with a physician for this week. They’ll be able to tell me more and give me an idea of how to proceed if I actually do have pre-diabetes.":
            jump doctors_office_pred
        "I feel like I know enough about pre-diabetes. And whether or not I have it, it’s always a good idea to be healthier so… I’ll just follow the advice from this website and work on healthier foods and more exercise.":
            jump level1week1

label doctors_office_pred:
    with Dissolve(.5)
    stop music fadeout 3.0
    pause 0.5
    scene bg doctors_office:
        zoom 0.4
    pause 1.0
    show buzz doctor:
        zoom 0.4
        yoffset 80
        xoffset 200
    doctor "Hello! My name is Dr. Cabrera, the endocrinologist on staff today. What brings you in today?"
    player "The other day, my cousin noticed I was peeing rather frequently and that I had some darkness on my neck and arms."
    player "He said that his mom, my mom’s sister, had similar symptoms before she was first diagnosed with diabetes. I know this is genetic, so I wanted to get myself checked out."
    doctor "That was a very smart decision. I have an idea of what this might be, but in order to make a diagnosis, I am going to order an A1C test for you."
    doctor "This will test the amount of sugar in your blood over the past month or so based on the status of the hemoglobin in your blood. Since this is being used to diagnose, I want to do a vein blood draw instead of a finger prick. Is that okay with you?"
    
    hide buzz doctor
    menu:
        "Yes, thank you.":
            jump diagnose
        "I’m a little nervous about a blood draw, but I think I’ll be okay":
            jump diagnose
        "No, I would much rather do a finger prick.":
            pass
    show buzz doctor:
        zoom 0.4
        yoffset 80
        xoffset 200
    doctor "Are you sure? We have very skilled nurses that can take your blood with little to no pain. We want to make sure this reading is as accurate as possible since we will be basing a diagnosis on it."
    hide buzz doctor

    menu:
        "Okay you're right... I will just have to look away.":
            pass
        "No, I would still prefer the finger prick if available.":
            pass

label diagnose:
    """
    Your blood was taken and tested. After waiting for the results, Dr. Cabrera comes back in.
    """
    show buzz doctor:
        zoom 0.4
        yoffset 80
        xoffset 200
    doctor "Your A1C levels are 6 percent. Though that may seem like a small number, that is actually slightly elevated, as the normal levels for healthy individuals are below 5.7 percent."
    player "So what does that mean?"
    doctor "It means you are pre-diabetic. Have you heard of pre-diabetes before?"

    menu:
        "Yeah, I spent a lot of time googling last night. I feel confident I know what that means.":
            jump intro3
        "I searched it up a little yesterday, but I’d rather hear it from an in-person specialist.":
            pass
        "I don’t think I understand what that is.":
            pass

    doctor "Prediabetes is a condition where your A1C levels have been elevated but not quite to the irreversible levels that marks Type II diabetes."
    doctor "At this stage, there is still work that can be done that can ensure you do not get Type II diabetes and thus do not need to be put on a medication regiment for the rest of your life."
    player "Rest of my life... wow... sounds like I need to get some work done."

label intro3:
    doctor "Would you like to hear more about the kind of lifestyle choices we believe you should take?"

    menu:
        "No, I think I understand.":
            jump intro4
        "Yes, please. The more help the better.":
            pass
    
    doctor "What does your current lifestyle consist of? What do you do for work? What are your hobbies? How's your diet?"
    player "I am in my final year of my PhD program at Georgia Tech for bioinformatics. I have a good group of friends in my program that I talk to and visit frequently. I don’t have too much time for hobbies outside of school, but I do like to read when I can."
    player "I thought my diet was pretty normal, but I guess since I have prediabetes it wasn’t that good. I do tend to eat out a lot, especially after a hell week."
    player "I definitely am a caffeine lover and am known to snack on sugary or salty things while waiting for results or while working on my thesis."
    
    doctor "There is definitely a way to be able to enjoy all those things while still managing your condition. The key is in moderation. Limiting those sugary snacks by having a full healthy breakfast and lunch and not bringing munchables to class can help."
    doctor "Adding more fruits and vegetables to your diet will also keep you full longer while keeping your blood sugar at a healthier level."
    doctor "Stress is something really important to consider with your disease. Stress can change all kinds of levels in your body, including A1C."
    doctor "It sounds like you have a pretty stressful program with little time for things you enjoy outside of it. It might be helpful to make time in your week to rest, reset, and do something that can bring your stress levels down."
    doctor "I would also recommend starting an exercise program. Maybe you can ask a trusted friend or family member to start it with you so you can have someone for accountability."
    menu:
        "Seems easy enough.":
            pass
        "Seems really complicated...":
            pass
    doctor "I know it may seem hard, but it is possible. And don't try and do it all at once! Making one small change every week is a great way to start."

label intro4:
    doctor "Here are a couple brochures that may help. There is lots of good information here about your new diagnosis, lifestyle changes, and even tips for taking your medication."
    player "Thank you so much!"
    hide buzz doctor
    play sound click
    scene bg doctors_office:
        zoom 0.4
            # gain access to doctor's note
    $ inventory_items.append("pre_note")
    show prediabetes_note
    pause 20.0
    show prediabetes_note:
        zoom 0.6
        xalign 0.5 
        yalign 0.5
    """
    This note can be accessed at any time from your inventory.
    """
    jump level1week1

label level1week1:
    with Dissolve(.5)
    pause 0.5
    scene bg culc_photo:
        zoom 1.3
    pause 1.0
    """
    You’ve been studying at the CULC since noon, and you stretch to relieve the tension in your joints as you look over at the clock.
    """
    player "It’s 5 already?? How’d that happen?"
    show buzz normal:
        zoom 0.4
    buzz "Time flies when you’re knee-deep in formulas."
    """
    Your stomach grumbles loudly.
    """
    buzz "And unfortunately, formulas are not very calorically dense. We should probably take a break and grab something to eat."
    player "But the exam is at 7 and I still don’t have last week’s topic down."
    buzz "Oh come on, we can still make it. If you lock in for another half hour, you can drive us to--"
    player "I left my car off campus today… I’m trying to add in some exercise to my routine and I figured walking around on campus would be the best way to get some extra steps in. It’d take me an hour to home and make food and come back, I’d have to leave right now."
    buzz "Well, there’s always Blue Donkey..."
    hide buzz normal
    menu:
        "I’ll just grab a quick snack (and maybe a Vanilla Buzz?) from Blonkey. I’ll have a much healthier dinner after the exam.":
            $ stress -= 1
            $ health -= 1
            $ health += 1
        "I’d better wrap it up here and go home. I have some leftovers from last night so maybe I can keep reviewing while I eat.":
            $ health += 1
            $ stress += 1
        "I’ll just order something from a Starship and have it delivered here. They have healthy-ish options and I’d get to continue studying here.":
            $ stress -= 1
    
    # $ energy -= 3
    # $ stress += 2
    # # from time passing

    with Dissolve(.5)
    pause 0.5
    scene bg apartment_bedroom:
        zoom 1.3
    pause 1.0
    """
    You feel yourself already starting to wake up but refuse to open your eyes just yet. You’re exhausted.
    """
    """
    You had a huge presentation this morning that you pretty much pulled an allnighter for, only for the group in front of you to go over their time and for your professor to push your presentation to next week. 
    """
    """
    You swear you just laid down for a nap, but maybe it’d be better to just go to sleep right now...
    """
    """
    *BEEP BEEP*
    """
    player "You groan. My alarm? Oh that's right, the gym..."
    menu:
        "You’re too stressed and too tired to go to the gym right now. But maybe you could take a walk outside instead for a bit.":
            $ stress -= 2
            $ health += 1
            """
            You go to bed early. You have a feeling tomorrow will be a good day since you’ll be so well-rested.
            """
            # because of early sleep:
            $ energy += 1
        "You slowly sit up and start putting on your gym shoes. Maybe the gym will help you relieve some stress… maybe you could tape up a picture of the other group on a punching bag, that would be a really good motivator.":
            $ stress -= 1
            $ health += 2
            """
            The gym was a really good stress reliever, you’re glad you went. You are extremely tired now though and are going to bed a bit later than you had planned, but you had a nap and you feel like your tiredness will have you sleeping like a rock tonight anyway.
            """
        "You just reset your alarm to an early morning wake up. You’re too exhausted to do much of anything right now, but you’ll feel better in the morning and can go for a good workout then.":
            $ energy += 1
            """
            You go to bed early. You have a feeling tomorrow will be a good day since you’ll be so well-rested.
            """
            # because of early sleep:
            $ energy += 1

label level1week2:
    with Dissolve(.5)
    pause 0.5
    scene bg apartment_bedroom:
        zoom 1.3
    pause 1.0
    """
    You just turned in all your assignments from last week and can finally relax. You are deciding what to do with your free time...until your friend Buzz hits you up.
    """
    show buzz funny:
        zoom 0.4
    buzz "Hey [playerName] let's go out tonight!! What do you say?"
    hide buzz funny
    menu:
        "Go out with Buzz and friends for a night out":
            $ stress -= 1
            $ energy -= 1
            jump level2

        "Take advantage of this free time to go to the gym, Buzz can spot you on weights. Cook a well-rounded meal for yourself if there's time.":
            with Dissolve(.5)
            pause 0.5
            scene bg crc_photo:
                zoom 1.3
            pause 1.0
            $ health += 1
            show buzz normal:
                zoom 0.4
            buzz "Sure, that sounds like a better idea anyways. What do you want to hit today?"
            show treadmill:
                zoom 0.6
                xpos 700
                ypos 650
            show stairmaster:
                zoom 0.6
                xpos 125
                ypos 575
            show weights:
                zoom 0.6
                xpos 1280
                ypos 530
            menu:
                "Do some moderate cardio on the treadmill for 30 minutes.":
                    # good choice!
                    hide stairmaster
                    hide weights
                    $ health += 1
                    $ stress -= 1
                "Do some rigorous cardio on the stairmaster for 30 minutes":
                    # great choice!!
                    hide treadmill
                    hide weights
                    $ health += 1
                    $ stress += 1
                "Lift weights with Buzz for a few reps":
                    # pretty good choice
                    hide stairmaster
                    hide treadmill
                    $ health += 1
                    $ stress += 1
                
            hide buzz normal
            
            """
            What a workout! You feel energized and ready to chow down on some food! What should you eat?
            """
            menu:
                "Go back home and cook a healthy meal (grilled protein with side of vegetables).":
                    with Dissolve(.5)
                    pause 0.5
                    scene bg apartment_bedroom:
                        zoom 1.3
                    pause 1.0
                    # great choice!
                    show grilledprotveg:
                        xpos 600
                        ypos 250
                    $ health += 2
                    pause 2.0
                "No, you deserve a treat for that workout...but maybe something healthier like a Chipotle bowl.":
                    # (pretty?) good choice
                    show chipotle:
                        xpos 600
                        ypos 250
                    $ health += 1
                "No, you deserve a treat for that workout...a burger with fries, and a milkshake to top it off.":
                    # bad choice
                    show burgerfriesshake:
                        xpos 600
                        ypos 250
                    $ health -= 1
                    $ stress -= 1

            # sleep early
            $ energy += 1
            jump level2
                
        "Watch some Netflix and go to bed...why go to the gym when you can sleep?":
            $ stress -= 1
            $ energy += 2
            """
            You let yourself unwind completely. The restful evening leaves you refreshed and full of energy for tomorrow.
            """
            jump level2

label level2:
    with Dissolve(.5)
    pause 0.5
    scene bg apartment_bedroom:
        zoom 1.3
    pause 1.0
    """
    Whew...after a long day of research and classes, it's time to figure out what to do with the rest of your afternoon.
    """
    # menu:
    #     "Stay in for the night and unwind, maybe catch up on your favorite show...": # we aren't allowing this
    #         $ energy += 1
    #         jump level2contpart1 # should this go to carb count game too?

    show buzz normal:
        zoom 0.4
    buzz "Let's go out for dinner! It'll be fun to catch up, we haven't hung out in a while!"
    $ stress -= 2
    with Dissolve(.5)
    pause 0.5
    scene bg restaurant:
        zoom 2.6
    pause 1.0
    """
    You're at dinner with your friends having a great time catching up, you begin to tell them about your prediabetes diagnosis.
    """ # maybe replace with back and forth dialogue later on

    buzz "That must be really hard to manage with school and stuff. We're about to order a few beers, can you still drink?"
    menu:
        "Oh absolutely.":
            # bad choice, carbs consumed and/or A1c rise
            $ carbCount += 13
            $ health -= 1
        "No, I shouldn't...":
            pass
    jump game_carbCount 

label game_carbCount:
    hide buzz normal
    # Not going to include a carb count meter because that takes away from the game which is guessing the carbs and keeping track
    show carbcountingstart:
        zoom 0.8
        xpos 0.3
        ypos 0.4
    """ 
    Time to order some food! You look at the menu and see that your options for an appetizer are:
    """
    hide carbcountingstart
    show chipsguac:
        zoom 0.6
        xpos 750
        ypos 600
    show bcsoup:
        zoom 0.6
        xpos 300
        ypos 600
    show ctasalad:
        zoom 0.6
        xpos 1250
        ypos 600
    menu:
        "Broccoli and Cheddar Soup":
            pass
        "Chips and Guacamole":
            pass
        "Cucumber, Tomato, and Avocado Salad":
            pass
    
    """ 
    WAIT!! You remember your doctor telling you about watching your carb intake...
    """
    """
    You recall your doctor said you should consume about 200 grams of carbs per-day, and if your math is right, then you have a remaining amount of around 45-60 grams of carbs for this.
    """
    menu:
        "Let's go with the Broccoli and Cheddar Soup.":
            hide chipsguac
            hide ctasalad
            show bcsoup:
                zoom 0.8
                xpos 700
                ypos 350
            """
            Very good for the soul!
            """
            $ carbCount += 15
        "Chips and guac for sure.":
            hide bcsoup
            hide ctasalad
            show chipsguac:
                zoom 0.8
                xpos 700
                ypos 350
            """
            Wow! Those chips and guac were so good, you must have ate at least half of the basket.
            """
            $ carbCount += 20
        "Let's keep it healthy with the salad.":
            hide chipsguac
            hide bcsoup
            show ctasalad:
                zoom 0.8
                xpos 700
                ypos 350
            """
            Very refreshing and nutritious!
            """
            $ carbCount += 10

    hide chipsguac
    hide bcsoup
    hide ctasalad


    """
    On to the main course! Looking at the menu, these 3 options look the most enticing to you....
    """
    show salmonbroccoli:
        zoom 0.6
        xpos 850
        ypos 600
    show burgerfries:
        zoom 0.6
        xpos 300
        ypos 600
    show steakpotato:
        zoom 0.6
        xpos 1250
        ypos 600
    menu:
        "Burger and Fries":
            hide salmonbroccoli
            hide steakpotato
            show burgerfries:
                zoom 0.8
                xpos 700
                ypos 350
            """
            Very yummy!
            """
            $ carbCount += 60
        "Salmon and Broccoli":
            hide burgerfries
            hide steakpotato
            show salmonbroccoli:
                zoom 0.8
                xpos 700
                ypos 350
            """
            So healthy!
            """
            $ carbCount += 10
            
        "Steak with a loaded baked potato":
            hide salmonbroccoli
            hide burgerfries
            show steakpotato:
                zoom 0.8
                xpos 700
                ypos 350
            """
            That hit the spot!
            """
            $ carbCount += 45
            
        "Actually, I think I am feeling pretty full already after that appetizer.. maybe I'll skip out for tonight":
            hide salmonbroccoli
            hide burgerfries
            hide steakpotato
            jump carbCount_result

    hide salmonbroccoli
    hide burgerfries
    hide steakpotato
    """
    Now time for dessert! What are you thinking for tonight?        
    """
    show lavacake:
        zoom 0.5
        xpos 300
        ypos 600
    show sorbet:
        zoom 0.7
        xpos 750
        ypos 600
    show chocsb:
        zoom 0.5
        xpos 1250
        ypos 660

    menu:
        "A chocolate lava cake? Hell yeah, don't mind if I do!":
            # hide sorbet
            # hide chocsb 
            # show lavacake:
            #     zoom 0.8
            #     xpos 700
            #     ypos 350
            $ carbCount += 66
        "A scoop of strawberry sorbet? Well, that sounds delightful!":
            # hide lavacake
            # hide chocsb 
            # show sorbet:
            #     zoom 0.8
            #     xpos 700
            #     ypos 350
            $ carbCount += 20
        "12 strawberries dipped in dark chocolate? The whole table could share these!":
            hide sorbet
            hide lavacake 
            show chocsb:
                zoom 0.8
                xpos 700
                ypos 350
            """
            You end up eating two.
            """
            $ carbCount += 13
        "I think I'll pass on dessert tonight.":
            $ carbCount += 0

    hide chocsb
    hide lavacake
    hide sorbet

label carbCount_result:
    """
    Let's assess the damage.
    """

    if (carbCount < 45):
        """
        Your meal selections were less than 45 carbs, which was the recommended minimum. Don't pass up on every carb choice, because you still need your energy!
        """
        """
        Do you want to try carb counting again?
        """
        menu:
            "Yeah, let's try that again":
                $ carbCount = 0
                jump game_carbCount
            "No, I get the point and will be more accurate with counting in the future":
                $ health -= 1
                $ energy -= 1
                pass

    elif (carbCount > 60):
        """
        Your meal selections totalled over 60 carbs, which was the recommended maximum. You need to learn to count carbohydrates better, or risk your prediabetes progressing into Type 2 Diabetes!
        """
        """
        Do you want to try carb counting again?
        """
        menu:
            "Yeah, let's try that again":
                $ carbCount = 0
                jump game_carbCount
            "No, I get the point and will be more accurate with counting in the future":
                $ health -= 1
                pass
    else:
        """
        You nailed it! Your meal selections landed you right in the recommended range. Keep it up!
        """
        $ energy += 1
        $ health += 2

label level2contpart1:
    with Dissolve(.5)
    pause 0.5
    scene bg bioinformatics_lab:
        zoom 1.3
    pause 1.0
    """
    You are deep into your research proposal and need to spend some extra hours in the lab to collect data. 
    You look at the time and realize how late its gotten.
    """
    player "Damn, I'm starving!"
    show energydrink:
        zoom 0.8
        xpos 500
        ypos 600
    show doordash:
        zoom 0.8
        xpos 900
        ypos 600
    menu:
        "I need to finish up this research...I guess a Monster will do.":
            hide doordash
            show energydrink:
                zoom 1.0
                xpos 800
                ypos 400
            """
            You drink an energy drink.
            """
            $ stress += 1
        "You still need to eat...but a late night like this calls for some DoorDash!":
            hide doordash
            hide energydrink
            jump foodchoice
    """
    A COUPLE HOURS LATER...
    You struggle to fall asleep later that night.
    """
    jump level2contpart2

label foodchoice:
    # TODO: ADD SOME SCENE CHANGE
    show doordash:
        zoom 1.0
        xpos 800
        ypos 400
    player "What do I feel like ordering? Should I focus on health or comfort food..."
    hide doordash
    show panera:
        zoom 0.6
        xpos 700
        ypos 650
    show cfa:
        zoom 0.6
        xpos 125
        ypos 575
    show burgerfriesshake:
        zoom 0.6
        xpos 1280
        ypos 530
    menu:
        "A side salad and grilled chicken nuggets from CFA.":
            hide panera
            hide burgerfriesshake
            show cfa:
                zoom 1.0
                xpos 600
                ypos 350
            """
            You feel very good about your food choices! You feel energized. 
            """
            $ health += 2
        "A soup and grilled cheese sandwich from Panera. ":
            hide cfa
            hide burgerfriesshake
            show panera:
                zoom 1.0
                xpos 600
                ypos 250
            """
            You feel good about your food choices! Maybe not the best option, but also not the worst. 
            """
            $ health += 1
            $ stress -= 1
        "A burger and large fries from McDonalds.":
            hide panera
            hide cfa
            show burgerfriesshake:
                zoom 1.0
                xpos 500
                ypos 200
            """
            Not the best choice...but at least it was a rewarding treat.
            """
            $ stress -= 2
            $ health -= 1

    hide burgerfriesshake
    hide cfa
    hide panera
    jump level2contpart2

label level2contpart2:
    """
    Are you still up for a workout?
    """
    menu:
        "Yes, but I'm not walking all the way to the gym.":
            $ health += 1
            jump level2contpart3
        "Yea, I think I'm gonna walk there too!":
            $ health += 1
            jump level2contpart4
        "No way, I'm going straight to bed.":
            with Dissolve(.5)
            pause 0.5
            scene bg apartment_bedroom:
                zoom 1.3
            pause 1.0
            """
            Later, you wish you did some exercise...it would have helped you fall asleep, especially after that energy drink.
            You are unable to sleep.
            """
            $ stress += 1
            jump level2contcheckpt

label level2contpart3:
    with Dissolve(.5)
    pause 0.5
    scene bg culc_photo:
        zoom 1.3
    pause 1.0
    player "What should I do to exercise today?"
    menu:
        "I'll do moderate cardio by walking outside of the trail around the lab for 30 minutes. ":
            $ stress -= 1
            $ health += 1
        "I'll do rigorous cardio by running outside the trail around the lab for 30 minutes. ":
            $ stress += 1
            $ health += 3
    """
    You end up going to bed earlier since you did not walk to the gym, but you did not get the extra exercise in.
    """
    $ stress -= 1
    $ energy += 1
    $ health += 1
    jump level2contcheckpt

label level2contpart4:
    with Dissolve(.5)
    pause 0.5
    scene bg crc_photo:
        zoom 1.3
    pause 1.0
    player "What should I do at the gym to exercise today?"
    show treadmill:
        zoom 0.6
        xpos 700
        ypos 650
    show stairmaster:
        zoom 0.6
        xpos 125
        ypos 575
    show weights:
        zoom 0.6
        xpos 1280
        ypos 530
    menu:
        "I'll do moderate cardio on treadmill for 30 minutes.":
            hide stairmaster
            hide weights
            $ stress -= 1
            $ health += 1
        "I'll do rigorous cardio on stairmaster for 30 minutes.":
            hide treadmill
            hide weights
            $ stress += 1
            $ health += 3
        "I'll lift weights for Buzz for a couple reps.":
            hide stairmaster
            hide treadmill
            $ stress += 1
            $ health += 2
    """
    You end up going to bed later since you walked to the gym, but you did get extra exercise in!
    """
    $ stress -= 1
    $ health += 1
    jump level2contcheckpt

label level2contcheckpt:
    # check player points
    if (energy >= 7 and health > 7 and stress <= 4):
        jump level3part1
    else:
        jump finalScenario # doing so bad that we fail them


label level3part1:
    with Dissolve(.5)
    pause 0.5
    scene bg apartment_bedroom:
        zoom 1.3
    pause 1.0
    """
    It's pay day! Which also means... sigh... budget setting day.
    """
    """
    You should probably plan out the month ahead so you can decide how you're willing to spend money!
    """
    """
    You frown at your calendar... looks pretty busy. And with Mother's Day and your best friend's birthday coming up, you'll need to put aside some money.
    """
    """
    You should probably stick to no more than... a hundred dollars this week? Yeah, you can handle that!
    """
    player "Damn, my stomach is really growling..."
    menu:
        "I could save some money by getting groceries...but I have a deadline to meet and I haven't meal planned yet, so I might spend too long at the shop.":
            $ health += 1
            $ went_grocery_shopping = True
            jump game_grocerydash
        "I'll eat out! Better to do it now at the beginning of the week with my full budget up. Plus, it'll save me time that I can use to get back to work soon.":
            # $ health += 0 # placeholder
            jump level3part2

label level3part2:
    """
    You call up Buzz to come out with you, knowing he's always down, but where should you recommend?
    """
    menu:
        "Hipster vegan restaurant in downtown! Great food choices (not so great prices)":
            $ health += 2
            $ money -= 30
        "Save the money and go to a campus fast food place (dining dollars aren't real money anyway), swearing to yourself you'll get a salad with chicken":
            $ health += 1
        "Let Buzz pick! (But you're sure he'll choose the same poke bowl place he picks every time, and you have mastered the bowl that gives you the right kind of calories)":
            $ health += 2
            $ money -= 15
    jump level3part3

label game_grocerydash: # TODO

label level3part3:
    """
    You're about to walk into the gym with a certain pep in your step. You've managed to keep up this good habit for about a month now and you're proud of yourself!
    You go to the gym membership app to check yourself in, when an alert pops up.
    """
    """
    Your Free Month Trial period ended yesterday! In order to continue to work out with us, you must sign up for one of our monthly plans!
    For the type of workouts you've been used to, we would recommend our $30 Gold Member plan! Sign up here.
    """
    """
    So maybe it's been exactly a month since you started working out here. You only have 2 hours before your meeting, so you kinda gotta make a decision right now. Hmm...
    """
    menu:
        "I'll just pay the 30$. Afterall, I'm already here and I've been doing such a good job this month so far, I don't want to go back on my progress.":
            $ money -= 30
            $ health += 2
        "I'll just head back to my apartment. There's a gym already included there, and though it's small and doesn't have all the equipment I've been using, it'll do for now.":
            $ health += 1
    jump level3part4

label level3part4:
    """
    After your shower, you only have 10 minutes before your meeting, but if you don't eat something right now, your stomach will be grumbling the whole time. 
    """
    """
    You pull open your fridge and peer inside.
    """
    if went_grocery_shopping:
        menu:
            "I'm so glad I got groceries yesterday! You grab some fruit from your dash at the grocery store and scroll through social media while you wait for the meeting to start.":
                $ health += 1
                $ stress -= 1
            "Dang, only have some leftovers from earlier this week. If I mix that rice with this sad looking chicken in a skillet... it might take me the full 10 minutes to prepare it, but I'm hungry enough to try.":
                $ health += 1
                $ stress += 1
            "You see the peanut butter in the back of the fridge. You're sure you have some saltine crackers in your pantry... at least it's protein right?":
                $ stress -= 1
    else:
        menu:
            "Dang, only have some leftovers from earlier this week. If I mix that rice with this sad looking chicken in a skillet... it might take me the full 10 minutes to prepare it, but I'm hungry enough to try.":
                $ health += 1
                $ stress += 1
            "You see the peanut butter in the back of the fridge. You're sure you have some saltine crackers in your pantry... at least it's protein right?":
                $ stress -= 1
    jump level3part5

label level3part5:
    with Dissolve(.5)
    pause 0.5
    scene bg culc_photo:
        zoom 1.3
    pause 1.0
    """
    Later, while not feeling so well, you run into your friend Buzz while studying hard in the CULC.
    """
    show buzz normal:
        zoom 0.4
    buzz "Dang, you look awful, you feeling okay?"
    player "*Achoo!* Excuse me! I think I'm starting to develop a bit of a head cold. Must be that weird cough going around the lab right now. *Cough cough cough!!*"
    player "I can't really afford to be sick right now though, I have a meeting to practice my thesis with my professor tomorrow and it took me forever to book that with her."
    buzz "Ugh that sucks... Hey I think the PharmaBox on the third floor just got restocked. Maybe they have some medicine in there that could help?"
    player "Oh yeah? I'll go check, thanks Buzz!"
    buzz "Good luck! I'm heading out, catch up with you later!"
    hide buzz normal
    """
    You head upstairs to the PharmaBox.
    """
    player "Let's see here, Pepto Bismal, ibuprofen, tampons... ah yes, cough supressant! Oh dang... that's kinda expensive..."
    menu:
        "The cough suppressant will get rid of the cough, plus it says it's drowsy so I may even fall asleep quicker! Surely that's worth the price tag.":
            $ money -= 15
            jump level3part6
        "What if instead I just get some OTC melatonin? It'll at least help me fall asleep, and maybe I'll dream the cough away.":
            $ money -= 5
            jump level3part6
        "You know what, Buzz definitely has some acetaminophen. I can ask him for some later tonight.":
            jump level3part7

label level3part6:
    """
    You're now back home...
    """
    """
    You take the meds with some warm milk and tuck yourself into bed. Though you've been feeling anxious all day because of your thesis practice tomorrow, you feel your mind finally slow down as you drift peacefully off to sleep.
    """
    $ energy += 1
    $ stress -= 1
    
    jump finalScenario

label level3part7:
    """
    You reach home and your phone rings... *ring ring*
    """
    buzz "Acetaminophen? Yeah, I have some but... I thought you said you had a cough?"
    player "Yeah I do... what's the problem?"
    buzz "This is a pain reliever?? The best it can do for you is reduce the fever that you don't have."
    player "Oh... well thanks anyway..."
    """
    So much for that... you toss and turn all night, unable to fall asleep because of your anxieties and your cough waking you up every time you're about to. Not very helpful the night before your thesis presentation.
    """
    $ energy -= 1

    jump finalScenario

label finalScenario:
    $ passPlayer = (energy >= 7 and health > 7 and stress <= 4) # whether jumped to at level 2 or level 3, should fail the player if they don't meet this
    with Dissolve(.5)
    pause 0.5
    scene bg apartment_bedroom:
        zoom 1.3
    pause 1.0
    """
    As you get ready to leave your apartment, you take one final look in the mirror...
    """
    if passPlayer:
        """
        Well you know what they say, look good, feel good!
        """
        with Dissolve(.5)
        pause 0.5
        scene bg bioinformatics_lab:
            zoom 1.3
        pause 1.0
        """
        As you step up onto the podium, you know all of your hard work is about to payoff...!
        """
        """
        Yay! Your presentation went fantastic. Congratulations, you just got awarded more funding!"
        """
        with Dissolve(.5)
        pause 0.5
        scene bg apartment_bday:
            zoom 1.6
        pause 1.0
        """
        Flash forward 6 months, you're back at another family reunion and you happen to run into one of your favorite cousins!
        """
        show cousin_buzz
        """
        While talking to your cousin, you get on the topic of your prediabetes journey, when they then make a few comments about their health that make you start to think...
        """
        """
        You try to tell your cousin about getting diagnosed about prediabetes, but they don't seem to fully understand what these signs they are experiencing mean.
        """
        jump finalScenarioMiniGame
    else:
        with Dissolve(.5)
        pause 0.5
        scene bg bioinformatics_lab:
            zoom 1.3
        pause 1.0
        """
        You notice everything is starting to look a little fuzzy... maybe you should look into getting a new prescription...
        """
        """
        As you step up onto the podium to begin, the room begins to start spinning... uh-oh!
        """
        with Dissolve(1)
        scene bg black_background:
            zoom 3.5
        pause 2.0
        """
        You pass out!
        """
        pause 1.0
        """
        You were unable to reverse your prediabetes diagnosis. Time to head to your doctor's appointment...
        END of PREDIABETES
        """
        pause 4.0
        """
        You have simulated a prediabetic patient, but were unsuccessful in reversing the condition, which may lead to Type II Diabetes.
        """
        """
        In our real game, you would now progress to living as a Type II Diabetic while in college. Would you like to keep playing (optional for testing), or return to the home screen?
        """
        
        menu:
            "Return to home screen, I just wanted to test the prediabetes game":
                return
            "Sure, I'll keep playing and learn about Type II Diabetes!":
                jump doctors_office1
        
        #jump doctors_office1

label finalScenarioMiniGame:
    show symptomsstart:
        zoom 0.8
        xpos 0.2
        ypos 0.4
    """
    Time for you to use what you've learned to help your cousin!
    """
    $ finalmini_points = 0
    """
    Choose the question that would most effectively assist you in helping your cousin.
    """
    menu:
        "Do you often experience your finger getting locked into a certain position?":
            $ finalmini_points += 2
            """
            Best choice! +2
            """
        "Do you feel faint more than normal?":
            $ finalmini_points += 1
            """
            Good choice. +1
            """
        "How much sugar do you eat?":
            $ finalmini_points += 0
            """
            Not a good choice. +0
            """
    
    """
    Choose the question that would most effectively assist you in helping your cousin.
    """
    menu:
        "Have you been feeling extra tired for no known reason?":
            $ finalmini_points += 1
            """
            Good choice. +1
            """
        "Have you been experiencing weight gain for no known reason?":
            $ finalmini_points += 2
            """
            Best choice! +2
            """
        "Do you sleep more than normal?":
            $ finalmini_points += 0
            """
            Not a good choice. +0
            """

    """
    Choose the question that would most effectively assist you in helping your cousin.
    """
    menu:
        "Do you know of anyone who has type 2 diabetes?":
            $ finalmini_points += 1
            """
            Good choice. +1
            """
        "Do you know what type 2 diabetes is?":
            $ finalmini_points += 0
            """
            Not a good choice. +0
            """
        "Do you remember if anyone in your side of the family ever had type 2 diabetes?":
            $ finalmini_points += 2
            """
            Best choice! +2
            """
    
    jump prediabetes_end

label prediabetes_end:
    with Dissolve(.5)
    pause 0.5
    scene bg doctors_office:
        zoom 0.4
    pause 1.0
    "Congratulations on reaching the end of Type 2 Turnaround! You have successfully reversed your prediabetes diagnosis!"
    $ inventory_items = []
    return

    

### TYPE 2 DIABETES

label doctors_office1:
    with Dissolve(.5)
    stop music fadeout 3.0
    pause 0.5
    scene bg doctors_office:
        zoom 0.4
    pause 1.0
    show buzz doctor: # replace with doctor buzz
        zoom 0.4
        yoffset 80
        xoffset 200

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    doctor "Hello [playerName], my name is Dr. Cabrera. What brings you in today?"
    player "I've been feeling very thirsty, no matter how much water I drink, but then I can't stop urinating, especially at night." 
    player "I also have been feeling some tingling in my hands and feet."
    doctor "Thank you for coming in. I have an idea of what this might be." 
    doctor "But just in case, I'm going to order an A1C test for you."
    doctor "Since this is being used to diagnose, I want to do a vein blood draw instead of a finger prick. Is that okay with you?" 
    
    menu:
        "Yes, thank you.":
            play sound click
            jump doctors_office3
        "I'm a little nervous about a blood draw, but I think I'll be okay!":
            play sound click
            jump doctors_office3
        "No, I would much rather do a finger prick.":
            play sound click
            jump doctors_office2

label doctors_office2:

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    doctor "Are you sure? We have very skilled nurses that can take your blood with little to no pain." 
    doctor "We want to make sure this reading is as accurate as possible since we will be basing a diagnosis on it."
    
    menu:
        "Okay, you're right... I will just have to look away.":
            play sound click
            jump doctors_office3
        "No, I would still prefer the finger prick if it's available.":
            play sound click
            jump doctors_office3

label doctors_office3:

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    """
    Your blood was taken and tested. After waiting for the results, Dr. Cabrera comes back in.
    """
    doctor "Your A1C levels are 8%%. Though that may seem low, that is actually quite elevated, as the normal levels for healthy individuals are below 5.7%%."
    player "So what does that mean?"
    doctor "It means you have Type II Diabetes. Have you heard of this before?"
    
    menu:
        "Yes, I'm well aware of it.":
            play sound click
            jump doctors_office5
        "I've heard of it before":
            play sound click
            jump doctors_office4
        "I don't think I understand what that is.":
            play sound click
            jump doctors_office4

label doctors_office4:

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    doctor "Diabetes mellitus is a group of diseases that affect the body's ability to regulate glucose, the brain and body's favorite form of sugar." 
    doctor "Glucose is very important for the body's systems, but too much of it in the blood can lead to many health risks."
    player "Okay..."
    doctor "Having Type II diabetes means that your pancreas cannot produce enough insulin, a hormone that usually tells your cells to take up sugar from the blood." 
    doctor "Without this, glucose continues to circulate and can disrupt the organ systems."
    
    menu:
        "So... is there a cure?":
            play sound click
            pass
        "What are you saying? Am I doomed?": 
            play sound click
            pass
    
    doctor "There is no cure for Type II diabetes. This is a chronic disease that will continue to impact you for the rest of your life." 
    doctor "However, that doesn't mean you cannot live a full life. With medication, exercise, and healthy eating, diabetes is a manageable disease."
    
    menu:
        "So what's the next step?":
            play sound click
            pass
        "What kind of medication should I start taking?":
            play sound click
            pass
        "How much exercise are we talking about here?":
            play sound click
            pass
    
    jump doctors_office5

label doctors_office5:

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    doctor "I will be writing you a prescription for Metformin, the most common medication for Type II diabetes." 
    doctor "This, taken with moderate exercise and some healthier food choices, will help you keep your blood sugar at a lower level."

    menu:
        "Got it. So... is that it?":
            play sound click
            jump doctors_office7
        "Why am I not taking insulin? I hear a lot of diabetics take it.":
            play sound click
            jump doctors_office6

label doctors_office6:

    show screen a1c_display
    show screen stress_display
    show screen energy_display


    doctor "Actually, insulin is only necessary for those with Type I Diabetes because their body does not produce any form of usable insulin." 
    doctor "Those with Type II Diabetes do have their own insulin, it's just being masked by the amount of glucose in the blood."
    doctor "Metformin will allow you to clear up some of that glucose and your own insulin will do the rest."
    player "I see."
    jump doctors_office7

label doctors_office7:
    doctor "Would you like for me to explain how to take metformin?"
    
    menu:
        "That's okay, it will be written on the bottle.":
            play sound click
            jump doctors_office9
        "Yes, please!":
            play sound click
            jump doctors_office8

label doctors_office8:
    show screen a1c_display
    show screen stress_display
    show screen energy_display

    doctor "We need to wean you on the medication, as it does have some possible side effects that are more drastic if you start at full dosage." 
    doctor "Thus, for the first two weeks, I want you to only take it after breakfast every day. "
    player "After breakfast for two weeks, got it."
    doctor "Then after that, take it after breakfast and after dinner for two weeks."
    player "Breakfast and dinner for another two weeks, understood."
    doctor "By the second month, you should be ready to have the full dosage, once after every meal, every day."
    player "Month 2, breakfast, lunch, and dinner... and metformin."
    doctor "All of this will be on your pill bottles. You can always refer back to them when you need."
    
    jump doctors_office9

label doctors_office9:
    show screen a1c_display
    show screen stress_display
    show screen energy_display

    doctor "Would you like to hear more about the kind of lifestyle choices we believe you should take?"
    
    menu:
        "No, I think I understand.":
            play sound click
            jump doctors_office11
        "Yes, please. The more help the better.":
            play sound click
            jump doctors_office10

label doctors_office10:
    show screen a1c_display
    show screen stress_display
    show screen energy_display


    doctor "What does your current lifestyle consist of? What do you do for work? What are your hobbies? How's your diet?"
    player "I am a researcher at a bioinformatics lab at Georgia Tech. I have a good group of friends in the lab space that I talk to and visit frequently." 
    player "I don't have too much time for hobbies outside of my job, but I do like to read when I can."
    player "I thought my diet was pretty normal, but I guess since I have diabetes it wasn't that good. I do tend to eat out a lot, especially after long days in the lab." 
    player "I definitely am a caffeine lover and am known to snack on sugary or salty things while waiting for results during work."
    doctor "There is definitely a way to be able to enjoy all those things while still managing your diabetes. The key is in moderation." 
    doctor "Limiting those sugary snacks by having a full healthy breakfast and lunch and not bringing munchables to work can help." 
    doctor "Adding more fruits and vegetables to your diet will also keep you full longer while keeping your blood sugar at a healthier level."
    doctor "Stress is something really important to consider with your disease. Stress can change all kinds of levels in your body, including A1C." 
    doctor "It sounds like you have a pretty stressful job with little time for things you enjoy outside of it." 
    doctor "It might be helpful to make time in your week to rest, reset, and do something that can bring your stress levels down."
    doctor "I would also recommend starting an exercise program. Maybe you can ask a trusted friend or family member to start it with you so you can have someone for accountability."
    
    menu:
        "Seems easy enough.":
            play sound click
            pass
        "Seems complicated.":
            play sound click
            pass
    
    doctor "I know it may seem hard, but it is possible. And don't try and do it all at once! Making one small change every week is a great way to start."

    jump doctors_office11

label doctors_office11:
    show screen a1c_display
    show screen stress_display
    show screen energy_display

    doctor "Here are a couple brochures that may help." 
    doctor "There is lots of good information here about your new diagnosis, lifestyle changes, and even tips for taking your medication."

    menu:
        "Thank you so much!":
            play sound click
            # gain access to doctor's note
            $ inventory_items.append("note")
            pass
        "I think everything you told me was enough. I don't need the brochures, but thank you for offering.":
            play sound click
            pass
    
    doctor "Of course. Please let me know if you have any questions. And don't forget to stop by your local pharmacy on the way home!"
    hide buzz
    jump week1_day1

label week1_day1:
    with Dissolve(.5)
    pause 0.5
    scene bg bioinformatics_lab:
        zoom 1.3
    pause 1

    $ inventory_items.append("metformin")
    $ inventory_items.append("wallet")

    $ current_a1c = "a1c_080"
    $ current_stress = "high_stress"
    $ current_energy = "low_energy"

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    """
    Week 1! You're talking to Buzz about all the work that is due at your lab. You feel super overwhelmed and stressed out by all these deadlines. 
    You are also getting advice from all of your peers after they hear about your diagnosis.
    """
    """
    ~Be sure to check your inventory! There might be something useful in there!~
    """
    show buzz lab:
        zoom 0.4
    buzz "Hey [playerName]! I missed you at the lab yesterday, we have a lot of reports coming up, what were you up to?"
    player "I actually was at a doctor's appointment and found out some news... I have type 2 diabetes." 
    player "I don't even know if I can think about that right now with all the work we have." 
    player "I've also been hearing a lot of conflicting information about what I should do and now I'm just confused."
    buzz "Yeah I don't know too much about type 2 diabetes, other than that my uncle has it and still eats candy sometimes." 
    buzz "I also heard that if you just exercise regularly you can eat what you want since that should balance each other out."    
    player "Really? Because if that's true, it would make it so much easier to manage, at least for this week. We have so much work to do..."
    buzz "I think you should still be okay! Besides, you can just start the upkeep after our deadlines this week." 
    buzz "It won't be that bad if you're off by a little, it'd be like you were diagnosed next week instead of yesterday."

    menu:
        "The doctor is the professional after all, I should probably just stick to the information he gave me. I'll start by doing something small this week, like having a green breakfast and making sure to take my metformin. I'll also not eat snacks like he recommended, though it'll be kind of hard... ":
            """
            You realize that listening to your doctor is what's most important, so you follow their instructions 
            and decide to take your medications, exercise regularly, and eat healthy.
            """
            $ score += 2
            play sound addpoints
            """
            Score +2: Great choice!
            """
        "I'm gonna listen to Buzz and not worry about my diabetes this week. As long as I do the medication regime correctly, I should be fine not completely changing my lifestyle this week. I'll use this week to plan out what exercise program and diet I can manage from now on.":
            """
            You decide that you are going to listen to your friend's advice regarding eating whatever you want 
            because you realize that you can exercise to balance out your eating habits.
            """
            play sound nopoints
            """
            Score +0: Not a great choice.
            """
        "I'm going to listen to my doctor and take my medication regularly, but I do love my sweets! If Buzz says his uncle is fine then I'll snack during lab like I usually do. It's a stress reliever, and he said that stress is not good for my condition either.":
            """
            You refer to your doctor's instructions and realize that you need to take your medication regularly, 
            but your friend whose uncle has diabetes tells you that it is okay to eat sweets every other day.
            """
            $ score += 1
            play sound addpoint
            """
            Score +1: Okay choice.
            """
    jump week1_day2

label week1_day2:
    with Dissolve(.5)
    pause 0.5
    scene bg apartment_bedroom:
        zoom 1.3
    pause 1.0
    # main character needs to make a breakfast choice when short on time
    # {p} will make it so that they have to click to see the rest

    $ current_a1c = "a1c_080"
    $ current_stress = "medium_stress"
    $ current_energy = "high_energy"

    show screen a1c_display
    show screen stress_display
    show screen energy_display
    
    """
    It's the start of a new day. You yawn and stretch, then look at your clock... {p}8 AM! Already?? 
    You have to clock in at 8:30 AM to let the undergrads into the lab. Time to zip through your morning routine!
    """
    menu:
        "Let's skip breakfast and the metformin today. I can last until lunch (probably) and take the metformin then!":
            $ score += 1
            play sound addpoint
            """
            Score +1: Okay choice.
            """
            jump week1_day2_2
        "Let me have a quick breakfast and take my metformin with me. I'll drink it with some water in the elevator.":
            $ score += 2
            play sound addpoints
            """
            Score +2: Great choice!
            """
            jump week1_day2_1
        "Let me grab a muffin on the way out! It's not that high in sugar because it's wholegrain, but it's so small that I won't need to take metformin. I'll take that at lunch!":
            play sound nopoints
            """
            Score +0: Not a great choice.
            """
            jump week1_day2_2

label week1_day2_1:
    with Dissolve(.5)
    pause 0.5
    scene bg bioinformatics_lab:
        zoom 1.3
    pause 1

    show screen a1c_display
    show screen stress_display
    show screen energy_display


    """
    You made it to the lab on time and your co-worker Buzz was already there waiting for you and had everything set up for class!
    """
    show buzz lab:
        zoom 0.4
    buzz "Hey, [playerName]! You ready for today!"
    player "Definitely!"
    hide buzz
    jump week1_day6

label week1_day2_2:
    with Dissolve(.5)
    pause 0.5
    scene bg bioinformatics_lab:
        zoom 1.3
    pause 1

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    """
    You barely made it there on time, but the good thing is, you're there! As your lab progresses you start to get a headache and have to sit down while teaching your class. 
    """
    show buzz lab:
        zoom 0.4
    buzz "Hey, [playerName]? Are you doing ok?"
    player "I just feel woozy... I'm not sure what's wrong..."
    buzz "Could it be something to do with your new diagnosis?"
    player "Oh. Maybe you're right... Maybe taking my medication was important after all."
    hide buzz
    jump week1_day6

label week1_day6:
    with Dissolve(.5)
    pause 0.5
    scene bg apartment_bday:
        zoom 1.6
    pause 1
     
    $ current_a1c = "a1c_080"
    $ current_stress = "low_stress"
    $ current_energy = "high_energy"

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    play music partymusic loop
    play voice party1 loop

    # main character needs to make a choice about their partying
    # jump good_management_month2a
    # jump bad_management_month2a
    """
    You just got invited to a party!
    """
    "It's the end of the week, and I want to let loose a little. I already took my metformin this morning, so I should be good to go!"

    show buzz normal:
        zoom 0.4
    buzz "Thanks for coming [playerName]!"
    player "Happy to be here!"
    buzz "Are you good to drink tonight? Or would that mess with your medication?"
    player "I googled it before coming. I should be fine to have a drink or two, especially since I'm on a low dose and I took it this morning."
    buzz "Bet! I figured worse case scenario, you could be the DD, but this is even better! Come on, let's take a shot!"

    """
    Later, at the party, you have already had a shot and are nursing a drink, when you run back into your friend Buzz.
    """
    show buzz funny:
        zoom 0.4
    buzz "Hey [playerName]! Come shotgun with me!"

    $ renpy.music.set_volume(0.5, delay=2.0)
    stop voice fadeout 2.0

    menu:
        "Of course, Buzz, let's go! I'm gonna also grab one of those apples and some peanuts from over there to fuel up for a late night!":
            play sound nopoints
            """
            Score +0: Not a great choice.
            """
            jump week1_day6_2
        "Sorry Buzz, I've got some work to get done tomorrow so I need to be at my best in the morning!":
            $ score += 2
            play sound addpoints
            """
            Score +2: Great choice!
            """
            jump week1_day6_1
        "No thank you! But I will definitely be getting some of the birthday cake over there with me!":
            $ score += 1
            play sound addpoint
            """
            Score +1: Okay choice.
            """
            jump week1_day6_1

label week1_day6_1:

    $ renpy.music.set_volume(1.0, delay=0.5)
    play voice rowdyparty

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    buzz "Suit yourself! But you gotta at least cheer me on!"
    player "Chug chug chug chug!"
    hide buzz

    stop voice
    stop music

    jump week1

label week1_day6_2:
    $ renpy.music.set_volume(1.0, delay=0.5)
    play voice rowdyparty

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    buzz "Chug chug chug chug!!"
    show buzz normal:
        zoom 0.4
    """
    An hour or so later, you start to feel woozy... woozier than normal when you're tipsy.
    """
    player "Hey Buzz? I'm going to call an Uber and head home. I don't feel very good..."
    buzz "Oh shoot, you look like my uncle looks when he's low on blood sugar... Here, at least have a little soda while you wait. It might help stabilize you."
    """
    By the time your Uber arrives 10 minutes later, you are starting to feel better. But it's still probably best that you go home...
    """
    hide buzz

    stop voice
    stop music

    jump week1

label week1:
    if score >= 5:
        jump good_management_month2
    else:
        jump bad_management_month2
    ### CHECK POINT REACHED! If score > 5, go to good management. Otherwise, go to bad management.

### GOOD MANAGEMENT SCENARIO

label good_management_month2:
    with Dissolve(.5)
    pause 0.5
    scene bg apartment_bedroom:
        zoom 1.3
    pause 1.0

    
    $ current_a1c = "a1c_065"
    $ current_stress = "high_stress"
    $ current_energy = "medium_energy"
    $ curr_wallet = "wallet_low"
    $ item_toggle["wallet"] = True

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    show phone:
        zoom 0.4
        xpos 450
        ypos 0
    """
    Your phone has new notifications:
    """
    """
    [playerName],
    I regret to inform you that the grant your lab applied for was not approved for this next cycle.
    """
    """
    Due to this, your salary, as well as the salaries of all those in your lab, may be affected. 
    In order to not lose out on the research your team has been doing, we will continue to allow the lab to run.
    """
    """
    Funding will be reduced, however; I would suggest that you find and apply to more grants so this issue can be remedied soon.
    """
    """
    In the meantime, I would be happy to write you letters of recommendation or act as a referral if you begin job searching again.
    Please email me back with any questions, comments, or concerns.
    Dr. Souperrvizer
    """

    """
    Another email!
    """

    """
    Hello [playerName]!!
    Your rent is due for Jaloma Midtown East 1204-B. To pay online, view details, or view terms and conditions, log into our website at tinyurl.com/abc123.
    """

    """
    To agree to the terms and confirm your payment of 1250 dollars + a 8 dollar convenience fee using your Visa, reply with your Last Name and Unit Number (e.g Smith 123-A).
    """

    hide phone

    player "Well... shoot... I've gotta come up with some plan for the next couple of weeks... This would have been hard enough to deal with without having to follow my doctor's orders...
    What should I do?"
    menu: 
        "Budget time to eat and sleep, but decide to skip the gym so you have time to find a part-time job.":
            $ score += 1
            play sound addpoint
            """
            Score +1: Okay choice.
            """
        "Budget time to eat, sleep, go to the gym... hmm... don't have much time to work part time but it's important to put my health first so ask Buzz to help you out.":
            $ score += 2
            play sound addpoints
            """
            Score +2: Great choice!
            """
        "Go to the gym at night and cut into your sleep time a little. You can have time to do everything if you go to bed later.":
            play sound nopoints
            """
            Score +0: Not a great choice.
            """
            jump good_management_month2b
    jump good_management_month2a
    
label good_management_month2a:
    with Dissolve(.5)
    pause 0.5
    scene bg bioinformatics_lab:
        zoom 1.3
    pause 1

    $ current_a1c = "a1c_065"
    $ current_stress = "high_stress"
    $ current_energy = "high_energy"
    $ curr_wallet = "wallet_midlow"

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    """Your phone rings again!"""
    show phone:
        zoom 0.4
        xpos 450
        ypos 0
    buzz "Hey [playerName]! I know you have been needing some extra money, so I referred you to this other research lab where you would focus on training undergrads that doesn't interfere with our other lab too much!"
    player "Wow thanks so much Buzz that's awesome!"
    buzz "It will mean that you will have to spend a lot more time in the lab so make sure you don't overwork yourself too much."
    """Buzz was correct, this new job on top of your old one is a lot to handle and you are falling behind on sleep! How do you deal with this imbalance?
    """
    menu:
        "Plan ahead of time to set up training for undergrads, so you are able to have more reasonable work hours but you do have to stay up late when you want to workout and prepare a nutritious meal for the next day.":
            $ score += 2
            play sound addpoints
            """
            Score +2: Great choice!
            """
            jump good_management_month22a
        "Due to the long and late days in the lab, you don't have much time to meal prep because you're going to the gym after work, so you snack a lot during day.":
            $ score += 1
            play sound addpoint
            """
            Score +1: Okay choice.
            """
            jump good_management_month22a
        "You decide taking metformin 3x a day is too much to remember so you take it when you can since you only recently had your dosage increased.":
            play sound nopoints
            """
            Score +0: Not a great choice.
            """
            jump good_management_month22b

label good_management_month22a:
    with Dissolve(.5)
    pause 0.5
    scene bg apartment_bedroom:
        zoom 1.3
    pause 1.0

    $ current_a1c = "a1c_065"
    $ current_stress = "high_stress"
    $ current_energy = "medium_energy"
    $ curr_wallet = "wallet_low"

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    play sound coin
    """
    You wake up one morning to see your puppy throwing up in your room!
    """
    """You rush them to the vet and thankfully they are able to be treated and are ok, but will need some medication to make sure they get fully better."""
    """
    The bill from the vet for your visit and puppy's medication is quite a fortune so your wallet is now suffering. How do you want to deal with your finances going forward?
    """
    menu:
        "After buying the medication, you make sure to also refill your metformin. You can adjust how much you eat out and figure out a new schedule to workout and take care of your pet at the same time.":
            $ score += 2
            play sound addpoints
            """
            Score +2: Great choice!
            """
            # wallet
        "You start working Saturdays at the lab to help financially recover, but this negatively impacts your stress and sleep levels. You get lazy with meal planning but still find some time to work out.":
            $ score += 1
            play sound addpoint
            """
            Score +1: Okay choice.
            """
            # wallet
        "I'm going to just wing it this month, sticking to my normalish routine. What's important is that I have my pet's meds squared away, the rest will fall into place.":
            play sound nopoints
            """
            Score +0: Not a great choice.
            """
    jump end_scene

label good_management_month2b:
    with Dissolve(.5)
    pause 0.5
    scene bg bioinformatics_lab:
        zoom 1.3
    pause 1

    $ current_a1c = "a1c_065"
    $ current_stress = "high_stress"
    $ current_energy = "low_energy"
    $ curr_wallet = "wallet_mid"

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    show phone:
        zoom 0.4
        xpos 450
        ypos 0

    buzz "Hey [playerName]! I know you have been needing some extra money, so I referred you to this other research lab where you would focus on training undergrads that doesn't interfere with our other lab too much!"
    player "Wow thanks so much Buzz that's awesome!"
    buzz "It will mean that you will have to spend a lot more time in the lab so make sure you don't overwork yourself too much."
    """Buzz was correct, this new job on top of your old one is a lot to handle and you are falling behind on sleep! How do you deal with this imbalance?
    """
    menu:
        "Plan ahead of time to set up training for undergrads, so you are able to have more reasonable work hours but you do have to stay up late when you want to workout and prepare a nutritious meal for the next day.":
            $ score += 2
            play sound addpoints
            """
            Score +2: Great choice!
            """
            jump good_management_month22a
        "Due to the long and late days in the lab, you don't have much time to meal prep because you're going to the gym after work, so you snack a lot during day.":
            $ score += 1
            play sound addpoint
            """
            Score +1: Okay choice.
            """
            jump good_management_month22a
        "You decide taking metformin 3x a day is too much to remember so you take it when you can since you only recently had your dosage increased.":
            play sound nopoints
            """
            Score +0: Not a great choice.
            """
            jump good_management_month22b

label good_management_month22b:
    with Dissolve(.5)
    pause 0.5
    scene bg apartment_bedroom:
        zoom 1.3
    pause 1.0

    $ current_a1c = "a1c_065"
    $ current_stress = "high_stress"
    $ current_energy = "medium_energy"
    $ curr_wallet = "wallet_low"

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    play sound coin
    """
    You wake up one morning to see your puppy throwing up in your room!
    """
    """You rush them to the vet and thankfully they are able to be treated and are ok, but will need some medication to make sure they get fully better."""
    """
    The bill from the vet for your visit and puppy's medication is quite a fortune so your wallet is now suffering. How do you want to deal with your finances going forward?
    """
    menu:
        "After buying the medication, you make sure to also refill your metformin. You can adjust how much you eat out and figure out a new schedule to workout and take care of your pet at the same time.":
            $ score += 2
            play sound addpoints
            """
            Score +2: Great choice!
            """
            # wallet
        "You start working Saturdays at the lab to help financially recover, but this negatively impacts your stress and sleep levels. You get lazy with meal planning but still find some time to work out.":
            $ score += 1
            play sound addpoint
            """
            Score +1: Okay choice.
            """
            # wallet
        "I'm going to just wing it this month, sticking to my normalish routine. What's important is that I have my pet's meds squared away, the rest will fall into place.":
            play sound nopoints
            """
            Score +0: Not a great choice.
            """
    jump end_scene

### BAD MANAGEMENT SCENARIO

label bad_management_month2:
    with Dissolve(.5)
    pause 0.5
    scene bg doctors_office:
        zoom 0.4
    pause 1.0
    show buzz doctor: # replace with doctor buzz
        zoom 0.4
        yoffset 80
        xoffset 200

    $ current_a1c = "a1c_095"
    $ current_stress = "medium_stress"
    $ current_energy = "medium_energy"

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    """
    You haven't been feeling your best and decide to get your blood drawn to evaluate your A1C levels a couple months post-diagnosis.
    """

    doctor "Unfortunately, your A1C levels have gone up. It is very important to get your health in check and to not let your type 2 diabetes worsen as this could lead to more chronic conditions or even death."
    doctor "You will have to take Metformin 3 times daily with food to ensure your blood glucose level is in a healthy range. It is also important to make lifestyle changes to help with this!"
    player "I just find it very difficult to make lifestyle changes. Every time I manage to get one thing in check, everything else falls behind."
    doctor "It is important to find a balance that works for you. It may seem hard at first, but small incremental changes will help you reach your goals."

    with Dissolve(.5)
    pause 0.5
    scene bg culc_photo:
        zoom 1.3
    pause 1.0
    show buzz normal:
        zoom 0.4
        xpos 100
        ypos 100

    """You're thinking about this when you run into Buzz. 
    """

    buzz "Hey [playerName]! Why so glum, chum?"
    player "Was just at the doctors. Seems my diabetes is even worse. He says I could die if I don't get it all together."
    buzz "But surely he doesn't expect you to just turn your entire life around, right?"
    buzz "Besides, we just got that grant in the lab; It's going to be all hands on deck for a while. How are you going to manage your A1C levels while also balancing your busy schedule?"
    player """
    1. I should focus on healthy meals and medicine...
    2. I should focus on healthy snacks and getting more active...
    3. Trying my old plan again but sticking to it this time will help!! Medicine, sleep, and good exercise!"""

    menu:
        "Even with my hectic work schedule, I will get my meal schedule to be consistent and I'll start taking my medication with each meal. I will also dedicate more time to meal prepping with less carbs, fats, and processed foods.":
            $ score += 2
            play sound addpoints
            """
            Score +2: Great choice!
            """
        "Whenever I'm able to snack throughout the day, I'll make sure to take the correct dosage. Also, it's hard to limit the amount of sitting I do at work due to the nature of the job, but I'll set a timer every hour to make sure I get up and be active.":
            $ score += 1
            play sound addpoint
            """
            Score +1: Okay choice.
            """
        "Sticking to my old plan will be good enough! I will take Metformin once a day consistently this time during lunch, I'll get my sleep schedule back on track, and start exercising 3 times a week.":
            play sound nopoints
            """
            Score +0: Not a great choice.
            """
            jump bad_management_month2b
    
    jump bad_management_month2a


label bad_management_month2a:
    with Dissolve(.5)
    pause 0.5
    scene bg bioinformatics_lab:
        zoom 1.3
    pause 1

    $ current_a1c = "a1c_095"
    $ current_stress = "high_stress"
    $ current_energy = "low_energy"

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    """
    Work at the lab has really been ramping up over the past few weeks.
    """
    show buzz lab:
        zoom 0.4
        xpos 450
        ypos 0

    buzz "Hey [playerName]! It's almost quittin' time and I feel like I haven't seen you move from that microscope all day."
    player "Yeah yeah... I'm almost done, should be able to clock out on time..."
    buzz "I was going to grab you a snack since you skipped lunch, but I wasn't sure what would go well with your new diet, so I decided not to."
    player "LUNCH! I completely forgot!! Dang, guess that's another metformin lost this week..."
    buzz "Yeah... about that... isn't that like your third time this week forgetting it?"
    player "Fourth actually... but who's counting!"
    buzz "Well I was doing a little bit of googling after we talked about your new prognosis and I really think YOU should be counting."
    buzz "It's okay to miss your metformin every now and then, but surely this much means it's not really helping your A1C levels. You've gotta change something."
    player "Okay... I'll set a reminder. Looks like I'm all done here. I'll see you tomorrow Buzz."

    hide buzz

    """The next day, around 12:00PM:
    """
    show phone:
        zoom 0.5
        ypos 0
        xpos 400
    """
    Your phone alarm rings. It's lunch time!
    """
    player "Shoot! I just started a round of sequencing. With this big of a data pull, it could take up to an hour, and my phone needs to be kept awake or it glitches out and I'd have to start all over."
    player "And of course, everyone else has already left for lunch. But I promised Buzz I'd do better with my metformin..."

    menu:
        "I'll go on my lunch break and take my mid-day metformin. I'll just have to stay longer after hours I suppose, cut into my bedtime a little.":
            $ score += 2
            play sound addpoints
            """
            Score +2: Great choice!
            """
        "I'll just take my metformin here in lab. I can eat more later and just grab a snack from the vending machine for now.":
            $ score += 1
            play sound addpoint
            """
            Score +1: Okay choice.
            """
        "I'll wait until I clock out and then eat a larger dinner to make up for not eating lunch. I can take both my metformins at the same time then, its the same dose and probably the same number of calories overall.":
            play sound nopoints
            """
            Score +0: Not a great choice.
            """
            jump bad_management_month22b

    jump bad_management_month22a

label bad_management_month22a:
    with Dissolve(.5)
    pause 0.5
    scene bg florida_photo:
        zoom 1.5
    pause 1

    $ current_a1c = "a1c_095"
    $ current_stress = "low_stress"
    $ current_energy = "medium_energy"

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    """
    Your vacation has finally arrived! You get a break from all your work in the lab and get to escape to a nice beach in Florida with your friends for the weekend. 
    """

    buzz "Hey [playerName], we have to plan what we are going to get up to this week! What are you thinking?"
    menu: 
        "I want to PARTY this weekend! I've been so stressed with the lab that I deserve to let loose for once, lets go hard all weekend and I can get back to my routine when I get home":
            play sound nopoints
            """
            Score +0: Not a great choice.
            """
        "We should go on a morning run together, definitely go to some fun bars and restaurants near the beach! Can you maybe try to keep me accountable on taking my metformin?":
            $ score += 2
            play sound addpoints
            """
            Score +2: Great choice!
            """
        "I'm exhausted so I definitely want to sleep in! We should play some pickleball and try a bunch of different restaurants. I have to remember to take my metformin though. But other than that I'm down for whatever, you can choose!":
            $ score += 1
            play sound addpoint
            """
            Score +1: Okay choice.
            """
    jump end_scene

label bad_management_month2b:
    with Dissolve(.5)
    pause 0.5
    scene bg bioinformatics_lab:
        zoom 1.3
    pause 1

    $ current_a1c = "a1c_095"
    $ current_stress = "high_stress"
    $ current_energy = "high_energy"

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    """
    Work at the lab has really been ramping up over the past few weeks.
    """
    buzz "Hey [playerName]! It's almost quittin' time and I feel like I haven't seen you move from that microscope all day."
    player "Yeah yeah... I'm almost done, should be able to clock out on time..."
    buzz "I was going to grab you a snack since you skipped lunch, but I wasn't sure what would go well with your new diet, so I decided not to."
    player "LUNCH! I completely forgot!! Dang, guess that's another metformin lost this week..."
    buzz "Yeah... about that... isn't that like your third time this week forgetting it?"
    player "Fourth actually... but who's counting!"
    buzz "Well I was doing a little bit of googling after we talked about your new prognosis and I really think YOU should be counting."
    buzz "It's okay to miss your metformin every now and then, but surely this much means its not really helping your A1C levels. You've gotta change something."
    player "Okay... I'll set a reminder. Looks like I'm all done here. I'll see you tomorrow Buzz."

    """The next day, around 12:00PM:
    """
    show phone:
        zoom 0.4
        xpos 450
        ypos 0
    """
    Your phone notification rings: It's lunch time!
    """

    player "Shoot! I just started a round of sequencing. With this big of a data pull, it could take up to an hour, and my phone needs to be kept awake or it glitches out and I'd have to start all over. And of course, everyone else has already left for lunch. But I promised Buzz I'd do better with my metformin..."
    menu:
        "I'll just take my metformin here in lab. I can eat more later and just grab a snack from the vending machine for now.":
            $ score += 1
            play sound addpoint
            """
            Score +1: Okay choice.
            """
        "I'll go on my lunch break and take my mid-day metformin. I'll just have to stay longer after hours I suppose, cut into my bedtime a little.":
            $ score += 2
            play sound addpoints
            """
            Score +2: Great choice!
            """
        "I'll wait until I clock out and then eat a larger dinner to make up for not eating lunch. I can take both my metformins at the same time then, its the same dose and probably the same number of calories overall.":
            play sound nopoints
            """
            Score +0: Not a great choice.
            """
            jump bad_management_month22b

    jump bad_management_month22b

label bad_management_month22b:
    with Dissolve(.5)
    pause 0.5
    scene bg florida_photo:
        zoom 1.5
    pause 1

    $ current_a1c = "a1c_095"
    $ current_stress = "high_stress"
    $ current_energy = "medium_energy"

    show screen a1c_display
    show screen stress_display
    show screen energy_display

    """
    Your vacation has finally arrived! You get a break from all your work in the lab and get to escape to a nice beach in Florida with your friends for the weekend. 
    """
    """*in the car on the way to your vacation*"""

    buzz "Hey [playerName], we have to plan what we are going to get up to this week! What are you thinking?"
    menu: 
        "I'm exhausted so I definitely want to sleep in! We should play some pickleball and try a bunch of different restaurants. I have to remember to take my metformin though. But other than that I'm down for whatever, you can choose!":
            $ score += 1
            play sound addpoint
            """
            Score +1: Okay choice.
            """
        "I want to PARTY this weekend! I've been so stressed with the lab that I deserve to let loose for once, lets go hard all weekend and I can get back to my routine when I get home.":
            play sound nopoints
            """
            Score +0: Not a great choice.
            """
        "We should go on a morning run together, definitely go to some fun bars and restaurants near the beach! Can you maybe try to keep me accountable on taking my metformin?":
            $ score += 2
            play sound addpoints
            """
            Score +2: Great choice!
            """
    jump end_scene

### ENDING SCENARIO

label end_scene:
    with Dissolve(.5)
    pause 0.5

    hide screen a1c_display
    hide screen stress_display  
    hide screen energy_display

    scene bg culc_photo:
        zoom 1.3

    ### display different text on the screen depending on end score
    if score > 10:
        scene bg good_ending
    elif score > 5:
        scene bg okay_ending
    else:
        scene bg bad_ending
    pause 1000
    return

########### END GAME SCRIPT


########### START INVENTORY IMPLEMENTATION

define gt_navy_blue_color = "#9F99"
define gt_gold_color = "#99F9"

screen inventory_display_toggle:
    zorder 92
    #modal True
    frame:
        background gt_navy_blue_color
        xalign 0.05
        yalign 0.1

        if (inventory_open):
            textbutton "Close Inventory":
                action [
                    ToggleVariable("inventory_open"),  
                    ToggleScreen("inventory_item") 
                ]
        else:
            textbutton "Inventory":
                action [
                    ToggleVariable("inventory_open"), 
                    ToggleScreen("inventory_item") 
                ]

    on "hide" action Hide("inventory_item")

default item_descriptions = {
    "wallet" : "It holds all your money", 
    "note" : "Has information from your last doctor's visit", 
    "metformin" : "Your medicine, don't forget to take it at the right time!",
    "pre_note": "Has information from your last doctor's visit regarding pre-diabetes."
    }

default item_img = {
    "wallet" : "images/wallet.png", 
    "note" : "images/note.png", 
    "metformin" : "images/metformin.png",
    "pre_note": "images/note.png"
    }

## decides if player can use it at the moment or not
default item_toggle = {
    "wallet" : False, 
    "note" : True, 
    "metformin" : True,
    "pre_note": True
    }

## tracks if user used the item when needed
default item_used = {
    "wallet" : False, 
    "note" : True, 
    "metformin" : False,
    "pre_note": False
}

default inventory_items = []

default item_description = ""

style inv_button is frame:
    xsize 200
    ysize 100

style inv_button_text:
    xalign 0.5
    yalign 0.5

default selected_item = None

style inv_button is frame:
    xsize 200
    ysize 100

screen doctor_note:
    modal True
    image "images/doctors_note.png": 
        xalign 0.5 
        yalign 0.5  
    textbutton "Close":
        action Hide("doctor_note")
        xalign 0.5
        yalign 0.9
        style "inv_button"

screen prediabetes_note:
    modal True
    image "images/doctors-note-prediabetes.png": 
        xalign 0.5 
        yalign 0.5
        zoom 0.65
    textbutton "Close":
        action Hide("prediabetes_note")
        xalign 0.5
        yalign 0.9
        style "inv_button"

screen metformin_info:
    modal True
    image "images/metformin_info.png": 
        xalign 0.5 
        yalign 0.5  
        zoom 0.6
    textbutton "Close":
        action Hide("metformin_info")
        xalign 0.5
        yalign 0.9
        style "inv_button"

screen wallet_info:
    modal True
    image curr_wallet: 
        xalign 0.5 
        yalign 0.5  
        zoom 0.4
    textbutton "Close":
        action Hide("wallet_info")
        xalign 0.5
        yalign 0.9
        style "inv_button"

screen inventory_item:
    modal True
    window:
        background "#AAA9"
        xsize 600
        ysize 150
        xalign 0.5
        yalign 0.1
        text item_description:
            xfill True
            yfill True

    window:
        background gt_gold_color
        xsize 1290
        ysize 600
        xalign 0.5
        yalign 0.7
        hbox:
            box_wrap True
            box_wrap_spacing 10
            spacing 10
            xoffset 20
            yoffset 20
            style_prefix "inv"
            for item in inventory_items:
                imagebutton:
                    # Define the image states: normal, hover, and pressed
                    idle item_img.get(item)
                    xsize 300
                    ysize 300
                    # The action to perform when clicked
                    action [
                        SetVariable("item_description", item_descriptions.get(item)),
                        SetVariable("selected_item", item)
                    ]
                    selected False

            # Use Button only shows when an item is selected
        textbutton "Use" style "inv_button":
            action [
                If(item_toggle.get(selected_item, False),  # Check if the item can be used
                    [
                        SetVariable(f"item_used[{selected_item}]", True),
                        If(selected_item == "note", Show("doctor_note")),
                        If(selected_item == "metformin", Show("metformin_info")),
                        If(selected_item == "wallet", Show("wallet_info")),
                        If(selected_item == "pre_note", Show("prediabetes_note") ),
                        Hide("inventory_item"),
                        SetVariable("inventory_open", False)
                    ],
                    SetVariable("item_description", "This item cannot be used right now.")  # Notify user if item can't be used
                ),
                SetVariable("selected_item", None),  # Clear selected item
            ]
            xalign 0.5
            yalign 0.8

    on "hide" action SetVariable("item_description", "")
    ########### END INVENTORY IMPLEMENTATION


########### START HUD IMPLEMENTATION ############
default a1c_img = {
        "a1c_080" : "images/a1c_080.png",
        "a1c_065" : "images/ac1_065.png",
        "a1c_095" : "images/a1c_095.png"
}
## Note that the image name for a1c_065 is ac1_065.png
# I didnt change it, but just be aware!
    
default stress_img = {
        "high_stress" : "images/stress_high.png",
        "medium_stress" : "images/stress_medium.png",
        "low_stress" : "images/stress_low.png"
}

default energy_img = {
        "high_energy" : "images/energy_high.png",
        "medium_energy" :  "images/energy_medium.png",
        "low_energy" : "images/energy_low.png"
}

default pre_stress_img = {
    -2: "images/Status Bars/Stress/Stress1.png",
    -1: "images/Status Bars/Stress/Stress1.png",
    0: "images/Status Bars/Stress/Stress1.png",
    1: "images/Status Bars/Stress/Stress1.png",
    2: "images/Status Bars/Stress/Stress2.png",
    3: "images/Status Bars/Stress/Stress3.png",
    4: "images/Status Bars/Stress/Stress4.png",
    5: "images/Status Bars/Stress/Stress5.png",
    6: "images/Status Bars/Stress/Stress6.png",
    7: "images/Status Bars/Stress/Stress7.png",
    8: "images/Status Bars/Stress/Stress8.png",
    9: "images/Status Bars/Stress/Stress9.png",
    10: "images/Status Bars/Stress/Stress10.png",
    11: "images/Status Bars/Stress/Stress10.png",
    12: "images/Status Bars/Stress/Stress10.png"
}

default pre_health_img = {
    1: "images/Status Bars/Health/Health1.png",
    2: "images/Status Bars/Health/Health2.png",
    3: "images/Status Bars/Health/Health3.png",
    4: "images/Status Bars/Health/Health4.png",
    5: "images/Status Bars/Health/Health5.png",
    6: "images/Status Bars/Health/Health6.png",
    7: "images/Status Bars/Health/Health7.png",
    8: "images/Status Bars/Health/Health8.png",
    9: "images/Status Bars/Health/Health9.png",
    10: "images/Status Bars/Health/Health10.png",
    11: "images/Status Bars/Health/Health10.png",
    12: "images/Status Bars/Health/Health10.png",
    13: "images/Status Bars/Health/Health10.png",
    14: "images/Status Bars/Health/Health10.png",
    15: "images/Status Bars/Health/Health10.png",
    16: "images/Status Bars/Health/Health10.png",
    17: "images/Status Bars/Health/Health10.png",
    18: "images/Status Bars/Health/Health10.png",
    19: "images/Status Bars/Health/Health10.png",
    20: "images/Status Bars/Health/Health10.png",
    21: "images/Status Bars/Health/Health10.png",
    22: "images/Status Bars/Health/Health10.png"
}

default pre_energy_img = {
    1: "images/Status Bars/Energy/Energy1.png",
    2: "images/Status Bars/Energy/Energy2.png",
    3: "images/Status Bars/Energy/Energy3.png",
    4: "images/Status Bars/Energy/Energy4.png",
    5: "images/Status Bars/Energy/Energy5.png",
    6: "images/Status Bars/Energy/Energy6.png",
    7: "images/Status Bars/Energy/Energy7.png",
    8: "images/Status Bars/Energy/Energy8.png",
    9: "images/Status Bars/Energy/Energy9.png",
    10: "images/Status Bars/Energy/Energy10.png",
    11: "images/Status Bars/Energy/Energy10.png",
    12: "images/Status Bars/Energy/Energy10.png",
    13: "images/Status Bars/Energy/Energy10.png"
}


screen pre_stress_display:
    zorder 92
    frame:
        xalign 0.99
        yalign 0.04
        add pre_stress_img[stress]:
            zoom 0.8

screen pre_energy_display:
    zorder 92
    frame:
        xalign 0.94
        yalign 0.04
        add pre_energy_img[energy]:
            zoom 0.8

screen pre_health_display:
    zorder 92
    frame:
        xalign 0.89
        yalign 0.04
        add pre_health_img[health]:
            zoom 0.8


screen a1c_display:
    zorder 92

    frame:
        # alignment for stress and energy to be side by side
        xalign 0.85 # far left
        yalign 0.08 # further up

        # alignment for stress and energy to be stacked vertically
        #xalign 0.9
        #yalign 0.08

        add a1c_img[current_a1c]:
            zoom 0.35
    
    # I was trying to get the sound to play when a1c levels changes
    # but i couldnt figure out the logic to get it to work
    # but if you can figure it out, it can save alot of time hardcoding
    #on "show":
        #action If(
            #current_a1c == "a1c_065",
            #true=Queue("sound", audio.a1c_beep),
            #false=NullAction()
        #)          

screen stress_display:
    zorder 92
    frame:
        # alignment for stress and energy to be side by side
        xalign 0.92
        yalign 0.1

        # alignment for stress and energy to be stacked vertically
        #xalign 0.97
        #yalign 0.6

        add stress_img[current_stress]:
            zoom 0.35

screen energy_display:
    zorder 92
    frame:
        xalign 0.97
        yalign 0.1
        add energy_img[current_energy] :
            zoom 0.34
            

    ########### END HUD IMPLEMENTATION #############
