# About
This project is about making a roguelike game in Python/Pygame. Everyone is welcome who would like to work on this project! Information about how to collaborate is below.


# Story
Once there was a knight who was cursed by a foe named The Mighty Python. The knight has to go through various events to fight his way to the Mighty Python, defeat it, and then remove the curse.


# Commits
In order to have a maintainable, easily changeable project, we need to keep the commit log clean.
Use this guide whenever you write a commit message.

## Usage
Write commit messages in the following way:
[where] - [action] [what]:
- [where]: Player Model, Board Controller, View, etc.
- [action]: Add, Update, Fix, Rework, Refactor, Polish
- [what]: player, boss, board, menu, etc.


Examples: 
- Player Model - Add player
- Main Controller - Update menu handling
- View - Fix printing board
- Board Model - Rework board creation


# Model-View-Controller Design Pattern
We use the MVC Design Pattern for this project. It briefly looks like this:

1. The Model contains only the pure application data, it contains no logic describing how to present the data to a user.

2. The View presents the model’s data to the user. The view knows how to access the model’s data, but it does not know what this data means or what the user can do to manipulate it.

3. The Controller exists between the view and the model. It listens to events triggered by the view (or another external source) and executes the appropriate reaction to these events. In most cases, the reaction is to call a method on the model. Since the view and the model are connected through a notification mechanism, the result of this action is then automatically reflected in the view.

![alt text](README/mvc.png)


# Clean Code Principles
- Single Responsibility Functions
- Descriptive Variable names - Nouns
- Descriptive Function names - Verbs (except: main, menu, etc.)

