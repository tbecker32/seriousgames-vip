default hover_text = ""
init python:
    # renpy.show_screen("tooltip_hud")

    # Define the rounds data structure
    grocery_rounds = [
    {
        "name": "Fresh Produce",
        "description": "Fresh produce aisle! What greens are going in your basket?",
        "items": [
            {"pos": (0.1, 0.5), "image": "broccoli.png", "money": 3, "health": 3, "desc": "Crunchy, versatile, and vitamin-rich."},
            {"pos": (0.25, 0.5), "image": "kale.png", "money": 3, "health": 4, "desc": "Superfood? Kale yeah!"},
            {"pos": (0.4, 0.5), "image": "spinach.png", "money": 3, "health": 3, "desc": "Popeye knew something!"},
            {"pos": (0.55, 0.5), "image": "asparagus.png", "money": 4, "health": 3, "desc": "Fancy veggies, fancy health points."},
            {"pos": (0.70, 0.5), "image": "green_beans.png", "money": 3, "health": 3, "desc": "Classic sidekick for any meal."},
            {"pos": (0.15, 0.75), "image": "cauliflower.png", "money": 4, "health": 3, "desc": "Roast it, mash it, love it."},
            {"pos": (0.30, 0.75), "image": "carrot.png", "money": 3, "health": 4, "desc": "Brighten your plate and your vision."},
            {"pos": (0.45, 0.75), "image": "corn.png", "money": 3, "health": 2, "desc": "Sweet, tasty, and just a bit starchy."},
            {"pos": (0.60, 0.75), "image": "bell_pepper.png", "money": 3, "health": 2, "desc": "Colorful crunch with every bite."}
        ]
    },
    {
        "name": "Fruits",
        "description": "Next stop...Fruit Aisle! Choose fruits that suit your taste!",
        "items": [
            {"pos": (0.1, 0.5), "image": "apple.png", "money": 3, "health": 3, "desc": "An apple a day keeps the doctor away."},
            {"pos": (0.25, 0.5), "image": "grapes.png", "money": 3, "health": 3, "desc": "Nature’s bite-sized candy."},
            {"pos": (0.4, 0.5), "image": "banana.png", "money": 1, "health": 2, "desc": "Perfect energy snack!"},
            {"pos": (0.55, 0.5), "image": "mango.png", "money": 4, "health": 1, "desc": "Worth every penny of tropical sweetness."},
            {"pos": (0.70, 0.5), "image": "pineapple.png", "money": 1, "health": 2, "desc": "Juicy, sweet, and affordable too."},
            {"pos": (0.15, 0.75), "image": "peach.png", "money": 3, "health": 3, "desc": "Taste the sunshine in every bite."},
            {"pos": (0.30, 0.75), "image": "strawberry.png", "money": 3, "health": 3, "desc": "Delicious and antioxidant-rich."},
            {"pos": (0.45, 0.75), "image": "blueberry.png", "money": 3, "health": 3, "desc": "A tiny, tasty health boost."},
            {"pos": (0.60, 0.75), "image": "strawberry.png", "money": 3, "health": 3, "desc": "Perfectly tart and sweet."}
        ]
    },
    {
        "name": "Carbs",
        "description": "Don't Skip the Carbs...Pick wisely because your energy levels depend on it!",
        "items": [
            {"pos": (0.1, 0.5), "image": "white_bread.png", "money": 2, "health": -1, "desc": "Easy and affordable, but low on nutrients."},
            {"pos": (0.25, 0.5), "image": "wheat_bread.png", "money": 2.5, "health": 1, "desc": "Better than white bread, but moderation helps."},
            {"pos": (0.4, 0.5), "image": "whole_grain_bread.png", "money": 3, "health": 2, "desc": "Fiber-rich and heart-healthy!"},
            {"pos": (0.55, 0.5), "image": "whole_grain_pasta.png", "money": 1.5, "health": 2, "desc": "Pasta night with fewer carbs."},
            {"pos": (0.70, 0.5), "image": "protein_pasta.png", "money": 1.5, "health": 1, "desc": "Pasta with a protein punch."},
            {"pos": (0.15, 0.75), "image": "potatoes.png", "money": 4, "health": 1, "desc": "Versatile kitchen staple, hearty meal addition."},
            {"pos": (0.30, 0.75), "image": "white_rice.png", "money": 5, "health": 1, "desc": "Easy and quick, but watch those portions."},
            {"pos": (0.45, 0.75), "image": "brown_rice.png", "money": 6, "health": 3, "desc": "More fiber, more satisfaction."},
            {"pos": (0.60, 0.75), "image": "quinoa.png", "money": 6, "health": 4, "desc": "The trendy grain that lives up to the hype."}
        ]
    },
    {
        "name": "Protein",
        "description": "You need protein for the gains!",
        "items": [
            {"pos": (0.1, 0.5), "image": "chicken.png", "money": 6, "health": 3, "desc": "Lean protein, endless recipes."},
            {"pos": (0.25, 0.5), "image": "turkey.png", "money": 6, "health": 4, "desc": "Flavor beyond the holidays!"},
            {"pos": (0.4, 0.5), "image": "steak.png", "money": 7, "health": 2, "desc": "Indulge, but watch the portion."},
            {"pos": (0.55, 0.5), "image": "ground_beef.png", "money": 4, "health": 2, "desc": "Burgers tonight? Balance tomorrow."},
            {"pos": (0.70, 0.5), "image": "salmon.png", "money": 6, "health": 5, "desc": "Heart-healthy and tasty!"},
            {"pos": (0.15, 0.75), "image": "shrimp.png", "money": 8, "health": 4, "desc": "Light, lean, a bit pricey but yummy."},
            {"pos": (0.30, 0.75), "image": "tofu.png", "money": 4, "health": 3, "desc": "Plant-based power!"},
            {"pos": (0.45, 0.75), "image": "edamame.png", "money": 4, "health": 3, "desc": "Protein-packed snack, anyone?"},
            {"pos": (0.60, 0.75), "image": "kidney_beans.png", "money": 2, "health": 3, "desc": "Are you kidney me? Cheap, nutritious, and versatile."}
        ]
    },
    {
        "name": "Treats",
        "description": "Almost done...only temptation aisle is left! Will you resist, or indulge? I mean, who says no to a treat?",
        "items": [
            {"pos": (0.1, 0.5), "image": "picknothing.png", "money": 0, "health": 4, "desc": "I say no...Willpower pays off!"},
            {"pos": (0.25, 0.5), "image": "chips2.png", "money": 2, "health": -2, "desc": "Crunchy, but think twice."},
            {"pos": (0.4, 0.5), "image": "soda.png", "money": 2, "health": -2, "desc": "Refreshing? Maybe. Healthy? Nope."},
            {"pos": (0.55, 0.5), "image": "pizza.png", "money": 6, "health": -3, "desc": "Easy dinner, health trade-off. Mabye some veggie toppings??"},
            {"pos": (0.70, 0.5), "image": "fries.png", "money": 6, "health": -2, "desc": "Too good not to try, but convenience has a cost!"},
            {"pos": (0.15, 0.75), "image": "chocolate_cake.png", "money": 3, "health": -2, "desc": "Indulge today, but regret tomorrow?"},
            {"pos": (0.30, 0.75), "image": "cookies.png", "image": "cookies.png", "money": 3, "health": -3, "desc": "Feeling chippy today, but regret tomorrow?"},
            {"pos": (0.45, 0.75), "image": "ice_cream.png", "money": 3, "health": -3, "desc": "Cold comfort now, but regret tomorrow?"},
            {"pos": (0.60, 0.75), "image": "ramen2.png", "money": 1, "health": -5, "desc": "Very cheap, but convenience has a cost!"}
        ]
    }
]


screen tooltip_hud() zorder 65:
    timer 0.01 repeat True action SetScreenVariable("dummy", True)
    default dummy = False # weird dummy workaround to force screen updates

    if hover_text:
        $ mx, my = renpy.get_mouse_pos()
        frame:
            xpos mx + 20
            ypos my + 20
            anchor (0, 0)

            background Frame("#0008", 8, 8) 
            padding (10, 6)

            text hover_text:
                size 22
                color "#fff"
                outlines [(1, "#000")]


screen grocery_round(round_data):
    # Use a fixed container so we don't draw a framed panel over the scene
    python:
        renpy.show_screen("tooltip_hud")
    fixed:
        for index, item in enumerate(round_data["items"]):
            imagebutton:
                idle item["image"] #chooses which image
                action ToggleVariable("food{}_selected".format(index + 1))
                hovered SetVariable("hover_text",
                    "Cost: {money}, Health: {health}\n{desc}".format(
                        money=item["money"], health=item["health"], desc=item["desc"]
                    )
                )
                unhovered SetVariable("hover_text", "")
                xpos item["pos"][0]
                ypos item["pos"][1]
                at Transform(zoom=0.9 + 0.025 * globals()["food{}_selected".format(index + 1)])

label grocery_round(round_index):
    $ round_data = grocery_rounds[round_index]

    # Reset selections
    $ food1_selected = food2_selected = food3_selected = food4_selected = food5_selected = food6_selected = food7_selected = food8_selected = food9_selected = False

    """
    [round_data["description"]]
    """

    # Loop until player can afford their selection
    $ round_complete = False
    while not round_complete:
        show screen grocery_round(round_data)

        menu:
            "Whats Next??":
                $ total_cost = 0
                $ total_health = 0

                python:
                    for index, item in enumerate(round_data["items"]):
                        if globals()["food{}_selected".format(index + 1)]:
                            total_cost += item["money"]
                            total_health += item["health"]

                if money - total_cost < 0:
                    "You don't have enough money to buy that selection!"
                    # nothing else, loop will restart this round
                    hide screen grocery_round
                else:
                    $ money -= total_cost
                    $ ghealth += total_health
                    hide screen grocery_round
                    $ round_complete = True  # exit the loop

    return