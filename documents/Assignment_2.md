# Assignment #2

## 5.1: What's the difference between a component-based architecture and a service-oriented architecture?
A component based architecture treats the system as a colllection of losely coupled parts of a whole. Service-oriented is similar except the components are now self-contained programs.

## 5.2: Suppose you're building a phone application that lets you play tic-tac-toe against a simple computer opponent. It will display high scores stored on the phone, not in an external database. Which architectures would be most appropriate and why?
A rule-based architecture would work best for tic-tac-toe because the game is relatively simple with a clear goal and with minimal unpredictable situations. A monolithic system would also work best because the game is self-contained because it does not utilize an external database and the game runs on a singular device.

## 5.4: Repeat question 3 [after thinking about it; it repeats question 2 for a chess game] assuming the chess program lets two users play against each other over an Internet connection.
Chess pieces would be rule-based again because the game pieces all interact with one another within a set of rules that applies to every piece and specific movement rules to each piece. A client/server architecture would be implemented to hold the chess game over the internet.

## 5.6: What kind of database structure and maintenance should the ClassyDraw application use?
Since ClassyDraw is self-contained and exports its drawings to a file, no database is needed to save the drawings, therefore a monolithic approach makes the most sense.

## 5.8: Draw a state machine diagram to let a program read floating point numbers in scientific notation as in +37 or -12.3e+17 (which means -12.3 x 1017). Allow both E and e for the exponent symbol.

![google docs screenshot](https://github.com/anthonyescobar/language-logic-exploration/blob/master/documents/images/hw2_5-8.png)

## 6.1: Consider the ClassyDraw classes Line, Rectangle, Ellipse, Star, and Text. What properties do these classes all share? What properties do they not share? Are there any properties shared by some classes and not others? Where should the shared and nonshared properties be implemented?
The classes all share properties that are not specific to the object's shape such as foreground and background color, thickness, line style, etc, along with anchoring its origin (0,0) in the top left corner of the shape. The shapes that are complete will also have a fill property. All the non-shape data can in an umbrella class and shape specific calculations for shapes can be left to the specific classes.

## 6.2: Draw an inheritance diagram showing the properties you identified for Exercise 1. (Create parent classes as needed, and don't forget the Drawable class at the top.)

![google docs screenshot](https://github.com/anthonyescobar/language-logic-exploration/blob/master/documents/images/hw2_6-2.png)

## 6.3:
![google docs screenshot](https://github.com/anthonyescobar/language-logic-exploration/blob/master/documents/images/hw2_6-3.png)

## Problem 6.6: Suppose your company has many managerial types such as department manager, project manager, and division manager. You also have multiple levels of vice president, some of whom report to other manager types. How could you combine the Salaried, Manager, and VicePresident types you used in Exercise 3? Draw the new inheritance hierarchy.
![google docs screenshot](https://github.com/anthonyescobar/language-logic-exploration/blob/master/documents/images/hw2_6-6.png)
