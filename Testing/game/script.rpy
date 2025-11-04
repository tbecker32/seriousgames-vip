# --- Image definitions ---
image bg spooky = "Spooky.jpg"
image fred = "fred.png"
image scoobyshaggy = "ScoobyShaggy.png"
image daphne = "Daphne.png"
image velma = "velma.png"

# --- Global selection variables ---
default fred_selected = False
default scooby_selected = False
default daphne_selected = False
default velma_selected = False

# --- Screen for multi-select ---
screen multi_select():

    # Fred
    imagebutton:
        idle "fred.png"
        action SetVariable("fred_selected", not fred_selected)
        xpos 0.225
        ypos 0.2
        at Transform(zoom=2.0 + 0.2 * fred_selected)

    # Scooby & Shaggy
    imagebutton:
        idle "ScoobyShaggy.png"
        action SetVariable("scooby_selected", not scooby_selected)
        xpos 0.4
        ypos 0.2
        at Transform(zoom=0.9 + 0.2 * scooby_selected)

    # Daphne
    imagebutton:
        idle "Daphne.png"
        action SetVariable("daphne_selected", not daphne_selected)
        xpos 0.6
        ypos 0.2
        at Transform(zoom=0.7 + 0.1 * daphne_selected)

    # Velma
    imagebutton:
        idle "Velma.png"
        action SetVariable("velma_selected", not velma_selected)
        xpos 0.8
        ypos 0.2
        at Transform(zoom=0.8 + 0.1 * velma_selected)


# --- Game start ---
label start:
    scene bg spooky
    show screen multi_select
    "Click on the Mystery Inc. gang to select them!"

    # Move to next scene
    hide screen multi_select
    jump next_scene


# --- Next scene showing only selected characters ---
label next_scene:
    scene bg spooky

    if fred_selected:
        show fred at Transform(zoom=2.0, xpos=0.225, ypos=0.2)
    if scooby_selected:
        show scoobyshaggy at Transform(zoom=0.9, xpos=0.4, ypos=0.2)
    if daphne_selected:
        show daphne at Transform(zoom=0.7, xpos=0.6, ypos=0.2)
    if velma_selected:
        show velma at Transform(zoom=0.8, xpos=0.8, ypos=0.2)

    "Here are the characters you selected!"
    return
