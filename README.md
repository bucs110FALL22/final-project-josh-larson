:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Josh & Larson Project (title)
## CS 110 Final Project
### Fall, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

https://replit.com/join/pbdwjvgvsq-joshuajanason

<< [link to demo presentation slides](#) >>

### Team: Josh & Larson 
#### Joshua Janason & Richard Larson

***

## Project Description

<< Give an overview of your project >>

***    

## User Interface Design

- **Initial Concept**
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components. >>
    
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design

* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. 
         For each additional module you should include
         - url for the module documentation
         - a short description of the module >>
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* Classes
    * << You should have a list of each of your classes with a description. >>
Class Deck:
-x(int): the horizontal position of the deck
-y(int): the vertical position of the deck
-amount(int): the amount of cards in the deck (can be updated)
-card: the card that is selected at the time
-list: a list of all of the possible cards in the deck (52 cards in total)
-image: the image of the deck (just cards facing down)
-FUNCTION: shuffle: the deck is able to shuffle through the cards randomly to create a new order
-FUNCTION: deal: the deck is able to hand out a card to the player and the dealer (removes the card from the deck)

Class Card: 
-x(int): the horizontal position of the card (changes if it is dealt to either the player or the dealer)
-y(int): the vertical position of the card (changes if it is dealt to either the player or the dealer)
-value(int): the value of the card
-FUNCTION: move: the card is able to move in any direction at a certain speed

Class Player:
-name("str"): the player's name
-points("int"): the amount of points (in card value) that the player has
-cards("str"): the specific cards that the player has in hand
-result("str"): the result if the player wins or loses
-x(int): the horizontal position of the player
-y(int): the vertical position of the player


## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * << all of your python files should go here >>
* assets
    * << all of your media, i.e. images, font files, etc, should go here) >>
* etc
    * << This is a catch all folder for things that are not part of your project, but you want to keep with your project >>

***

## Tasks and Responsibilities 

   * Outline the team member roles and who was responsible for each class/method, both individual and collaborative.

## Testing

* << Describe your testing strategy for your project. >>

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
