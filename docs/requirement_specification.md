# Requirement specification

## Purpose (generic)
Turukuun Pliis is a 2D Papers Please -like game implemented in Python using pygame. 

The game should be enjoyable to play and offer replayability through random generation.

---
## Description
### Game description
The game takes place in the year 2020 when the border of Uusimaa was closed due to... events.

The user (player) will take on the role of an "immigration officer" at the now closed border.

They are tasked with making the decision of who to let cross and who should turn back. They will base this decision on current visa etc. requirements (displayed to the user at the beginning of each grueling day) and their own judgement.

Additionally, the player must make sure that they do not make mistakes when processing those who wish to cross. Doing so too much may result in... severe punishment.

### User charasteristics
The game is single-player and does not require implementation of other user roles.

We assume that the user is familiar with basic knowledge of how to operate a generic video game.

---
## Specific requirements
*TWWTC = Those Who Wish To Cross, APWTC = A Person Wishing To Cross*
### Gameplay
- [ ] There exists APWTC
    - [ ] APWTC has a name
    - [ ] APWTC has an age
    - [ ] APWTC has a height
    - [ ] APWTC has an origin city
    - [ ] APWTC has a SSID

- [ ] There exists requirements that TWWTC must meet
    - [ ] Visa requirement, visa document details must match (name, age, SSID, etc.)
    - [ ] Vaccination requirement, vaccination document details must match (name, age, SSID, etc.)
    - [ ] Origin city requirement
    - [ ] Target city requirement
    - [ ] Specific origin to target requirement

- [ ] The game state should be able to be saved at the start/end of a cycle
- [ ] The game state should be able to be loaded from a saved state

### Graphical requirements
- [ ] The game should present the user with a windowed splash screen upon startup
    - [ ] The start-up screen should have a "New Game" option that starts a new game
    - [ ] The start-up screen should have a "Load Game" option that loads an existing game
    - [ ] The start-up screen should have an "Options" option that displays the options menu
- [ ] The player should receive immediate or end-of-day feedback on their decisions
- [ ] The game should have an end-of-day briefing (EODB)
    - [ ] The EODB should state day number
    - [ ] The EODB should show statistics (total cases, # crossings, # correct decisions)
- [ ] The game should be able to be controlled with a mouse
- [ ] The game can have additional features controlled with a keyboard
- [ ] The game should be able to be paused (*mouse, keyboard*)

---
### Further development ideas
- [ ] Calendar to keep track of days passed
- [ ] News ticker
- [ ] Events based on day progression
- [ ] Randomized character generation
- [ ] Recurring characters