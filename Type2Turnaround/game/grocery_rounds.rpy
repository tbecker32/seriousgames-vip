init python:
    # Define the rounds data structure
    grocery_rounds = [
        {
            "name": "Fresh Produce",
            "description": "Fresh produce aisle! What greens are going in your basket?",
            "items": [
                {"pos": (0.1, 0.5), "money": 3, "health": 3},
                {"pos": (0.25, 0.5), "money": 3, "health": 4},
                {"pos": (0.4, 0.5), "money": 3, "health": 3},
                {"pos": (0.55, 0.5), "money": 4, "health": 3},
                {"pos": (0.70, 0.5), "money": 3, "health": 3},
                {"pos": (0.15, 0.75), "money": 4, "health": 3},
                {"pos": (0.30, 0.75), "money": 3, "health": 4},
                {"pos": (0.45, 0.75), "money": 3, "health": 2},
                {"pos": (0.60, 0.75), "money": 3, "health": 2}
            ]
        },
        {
            "name": "Fruits",
            "description": "Next stop...Fruit Aisle! Choose fruits that suit your taste!",
            "items": [
                {"pos": (0.1, 0.5), "money": 3, "health": 3},
                {"pos": (0.25, 0.5), "money": 3, "health": 3},
                {"pos": (0.4, 0.5), "money": 1, "health": 2},
                {"pos": (0.55, 0.5), "money": 4, "health": 1},
                {"pos": (0.70, 0.5), "money": 1, "health": 2},
                {"pos": (0.15, 0.75), "money": 3, "health": 3},
                {"pos": (0.30, 0.75), "money": 3, "health": 3},
                {"pos": (0.45, 0.75), "money": 3, "health": 3},
                {"pos": (0.60, 0.75), "money": 3, "health": 3}
            ]
        },
        {
            "name": "Carbs",
            "description": "Don't Skip the Carbs...Pick wisely because your energy levels depend on it!",
            "items": [
                {"pos": (0.1, 0.5), "money": 2, "health": -1},
                {"pos": (0.25, 0.5), "money": 2.5, "health": 1},
                {"pos": (0.4, 0.5), "money": 3, "health": 2},
                {"pos": (0.55, 0.5), "money": 1.5, "health": 2},
                {"pos": (0.70, 0.5), "money": 1.5, "health": 1},
                {"pos": (0.15, 0.75), "money": 4, "health": 1},
                {"pos": (0.30, 0.75), "money": 5, "health": 1},
                {"pos": (0.45, 0.75), "money": 6, "health": 3},
                {"pos": (0.60, 0.75), "money": 6, "health": 4}
            ]
        },
        {
            "name": "Protein",
            "description": "You need protein for the gains!",
            "items": [
                {"pos": (0.1, 0.5), "money": -6, "health": 3},
                {"pos": (0.25, 0.5), "money": -6, "health": 4},
                {"pos": (0.4, 0.5), "money": -7, "health": 2},
                {"pos": (0.55, 0.5), "money": -4, "health": 2},
                {"pos": (0.70, 0.5), "money": -6, "health": 5},
                {"pos": (0.15, 0.75), "money": -8, "health": 4},
                {"pos": (0.30, 0.75), "money": -4, "health": 3},
                {"pos": (0.45, 0.75), "money": -4, "health": 3},
                {"pos": (0.60, 0.75), "money": -2, "health": 3}
            ]
        },
        {
            "name": "Treats",
            "description": "Almost done...only temptation aisle is left! Will you resist, or indulge? I mean, who says no to a treat?",
            "items": [
                {"pos": (0.1, 0.5), "money": 0, "health": 4},
                {"pos": (0.25, 0.5), "money": -2, "health": -2},
                {"pos": (0.4, 0.5), "money": -2, "health": -2},
                {"pos": (0.55, 0.5), "money": -6, "health": -3},
                {"pos": (0.70, 0.5), "money": -6, "health": -2},
                {"pos": (0.15, 0.75), "money": -3, "health": -2},
                {"pos": (0.30, 0.75), "money": -3, "health": -3},
                {"pos": (0.45, 0.75), "money": -3, "health": -3},
                {"pos": (0.60, 0.75), "money": -1, "health": -5}
            ]
        }
    ]

screen grocery_round(round_data):
    # Use a fixed container so we don't draw a framed panel over the scene
    fixed:
        for index, item in enumerate(round_data["items"]):
            imagebutton:
                idle "images/question.png"
                action ToggleVariable("food{}_selected".format(index + 1))
                xpos item["pos"][0]
                ypos item["pos"][1]
                at Transform(zoom=0.2 + 0.025 * globals()["food{}_selected".format(index + 1)])

label grocery_round(round_index):
    $ round_data = grocery_rounds[round_index]
    
    # Reset selections for this round
    $ food1_selected = food2_selected = food3_selected = food4_selected = food5_selected = food6_selected = food7_selected = food8_selected = food9_selected = False
    
    """
    [round_data["description"]]
    """
    
    show screen grocery_round(round_data)
    
    menu:
        "Whats Next??":
            hide screen grocery_round
            
            # Process selections
            python:
                for index, item in enumerate(round_data["items"]):
                    if globals()["food{}_selected".format(index + 1)]:
                        money -= item["money"]
                        health += item["health"]
    
    return