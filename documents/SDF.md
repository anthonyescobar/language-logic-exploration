# Language Logic Conversion Application
Anthony Escobar  
CMSI 402 - Spring 2018  
Loyola Marymount University

# Table of Contents
* [1.0 Project Status Sheets](#10-project-status-sheets)  
* [2.0 Preliminary Project Proposal](#20-preliminary-project-proposal)  
* [3.0 Project Proposal](#30-project-proposal)  
  * [3.1 Verbal Description](#31-verbal-description)  
  * [3.2 Justification](#32-justification)  
* [4.0 Software Development Plan](#40-software-development-plan)
  * [4.1 Plan Introduction](#41-plan-introduction)
    * [4.1.1 Project Deliverables](#411-project-deliverables)
  * [4.2 Project Resources](#42-project-resources)
    * [4.2.1 Hardware Resources](#421-hardware-resources)
    * [4.2.2 Software Resources](#422-software-resources)
  * [4.3 Project Organization](#43-project-organization)
  * [4.4 Project Schedule](#44-project-schedule)
    * [4.4.1 PERT / GANTT Chart](#441-pert--gantt-chart)
    * [4.4.2 Task / Resource Table](#442-task--resource-table)
* [5.0 Requirements Document](#50-requirements-document)  
  * [5.1 Introduction](#51-introduction)  
  * [5.2 Functional Requirements](#52-functional-requirements)  
    * [5.2.1 Graphical User Interface](#521-graphical-user-interface)  
    * [5.2.2 Command Line Interface](#522-command-line-interface)  
  * [5.3 Performance Requirements](#53-performance-requirements)  
    * [5.3.1 Symbolic Breakdown Detection Time](#531-symbolic-breakdown-detection-time)  
    * [5.3.2 Symbolic Breakdown Return Time](#532-symbolic-breakdown-return-time)  
  * [5.4 Enviroment Requirements](#54-enviroment-requirements)  
* [6.0 Software Design Description](#60-software-design-description)  


# 1.0 Project Status Sheets

# 2.0 Preliminary Project Proposal

The goal of the Language-Logic application is to create an application where, when given a sentence can identify prepositional phrases and breakdown its structure in order to output the symbolic logic of the statement. A project like this will allow me to exercise my understanding of language and logic and explore Natural Language Processing, a path that I am extremely interested in, in a structured context .

# 3.0 Project Proposal

## 3.1 Verbal Description

This project is an exploration into the compatibility between language and computation. Many individuals believe there to be an invisible barrier separating natural language from computers, however what is not understood is that computers are actually designed to understand us, we just have to speak its language. 

With the onset of AI upon us, computers are now being trained to understand humans, talk like humans, and even act like humans. Computers are already better than humans at computational power, however humans still reign supreme in reasoning. One way to bridge that gap is to study how language is used for arguments and adapt that language for a program to understand. Breaking sentences into symbolic logic could end up being like giving a computer a math problem, except instead of 2+2=? The computer could answer “with these symbols”: find the valid output, find the logical flaw, is this statement true. In this structured environment I plan on exploring the grammar of symbolic logic and how humans are taught to break down the statements in order to come up with the correct solution.

The application will be written in Python due to its access to large parsing libraries and applicability to a webpage or console input/output.

## 3.2 Justification

I have always had a bittersweet relationship with language: despite being in the most anti-literature major, I enjoy storytelling (can you believe that I ran a creative writing club in high school). Even though my vocabulary is absolute trash, I find words fascinating and worth studying. Maybe it is because I am algebraically driven, but I’ve always understood writing as a pseudo equation. Certain words tied together can draw out completely different meanings, even if the theme of the statements are the same. Due to this it is safe to assume that words have a defined value and adding certain values together can lead to a specific solution. This becomes most applicable in arguments where one party applies their verbal value against another party’s verbal strength. This is why we have lawyers, we hire individuals who are experts with words to defend our property and rights. Imagine if there existed a computer that could act as a judge: that took in the arguments of both lawyers, computed their argument value dexterity against one another, and gave judgement. Judgement could potentially become more consistent (or we would be putting our whole liberty into the hands of a really smart terminator bot). 

# 4.0 Software Development Plan
(Wk 9/11)

## 4.1 Plan Introduction
This Software Development Plan provides the details of the planned development for the Language-Logic Conversion Exploration which provides an application to convert a given string into symbolic logic.

The Language Logic Conversion Application is designed to be my own exploration into natural language processing and apply it to a context with clear fundamentals. In order for this project to be rendered complete, documentation must be fully and thuroughly completed. Documentation includes but is not limited to a: project proposal, requirements specification, software development plan, a presentation, and status reports. In addition to documentation, the application must also be completed to a standard specified and agreed to by myself and Prof B.J.

### 4.1.1 Project Deliverables
**Project Proposal:** A written declaration of project and its purpose. Inclludes a section for the verbal description of the project and a section for the justification of the project.  
**Requirements Specification:** Specifies *exactly* what is being built. Includes high and low level designs and descriptions of components of the project.
**Software Development Plan:** Describes the process that will be employed for completeion of the project. Includes information regarding when all components of a project (documentation and application) will be delivered.

D# |Deliverable | Due
:---:|:---:|:---:
D#01	| Project Proposal Document	| Wk 2
D#02	| Requirements Specification Document (Initial)	| Wk 5
D#03	| Software Development Plan Document (Initial) | Wk 9
D#04	| Software Development Plan Document (Updated) | Wk 11
D#05	| Requirements Specification Document (re-submit)	| Wk 13
D#06	| Preliminary Demonstration Presentations	| Wks 13 — 15
D#07	| FINAL Product Delivery & Project Presentation (Lessons Learned/History sections)	| Wk 16
D#08	| Oral Status Reports	Done in class as SCRUM | Most Weeks
D#09	| Written Status Reports or Quad Charts in SDF |	Wk 9/11/13/15

## 4.2 Project Resources

### 4.2.1 Hardware Resources
No extra hardware besides my computer is required to utilize this application.

### 4.2.2 Software Resources
1. Python 3.5+
2. Natural Language Toolkit (NLTK)
3. Numpy
4. git
5. Atom

## 4.3 Project Organization
This project employes 3 major components
1. **Sentence parsing and organization with NLTK:** Using NLTK to seperate and tag words in the given string. Then categorize the words into prepositional statements by looking for conditional indications.
2. **Conversion to sybolic logic:** fFrom the modified output from NLTK, symbolize the prepositional statemts and use their location within the conditional indicators to figure out what side of the clause it is on. Create symbolic statement from this linked list of prepositional statements.
3. **Output to a web user interface:** Create a simple web interface that an inexperienced user can use. May include error messages and hints for application use.

## 4.4 Project Schedule
This section provides schedule information for the the *Language Logic Exploration* project.  
TODO
### 4.4.1 PERT / GANTT Chart
TODO
### 4.4.2 Task / Resource Table
TODO

# 5.0 Requirements Document
(Wk 5/13)

## 5.1 Introduction
one-paragraph description of the system being designed, and should include a high-level UML diagram of the system components. It should conclude with a verbal outline description of the document, worded something like "The remainder of this document is structured as follows. Section 5.2 contains . . . . Section 5.3 contains . . ." and so on.

## 5.2 Functional Requirements
This application shall utilize two different ways for the user to interact with the application, a Graphical User Interface which can be accessed by a web browser, or a Command Line Interface which can be accessed with a shell application.
### 5.2.1 Graphical User Interface
The Graphical User Interface (GUI) for the application provides the user with a way to input text for the application to run its computations upon and return the result in a clear and organized manner for the user to view.
  1. The GUI shall provide a `textarea` for the user to input the conditional statements
  2. The GUI shall denote when a statement may be incomplete or syntatically incorrect
  3. The GUI shall provide the propositions and the output formatted cleanly and properly in an output space below the input area
### 5.2.2 Command Line Interface
The Command Line Interface (CLI) for the application provides the user with a way to input text for the application to run its computations upon and return the result in a console for the user to utilize with other scripts.
  1. The CLI shall take only one argument which will be the input statement for the application
  2. The CLI shall denote if there are errors with the statement given
  3. The CLI shall provide the propositions on lines below the program call followed by the symbolic logic on a different new line.

## 5.3 Performance Requirements
### 5.3.1 Symbolic Breakdown Detection Time
  * The application shall compute the symbolic breakdown of a given argument so long that there are proper conditional statements to be detected.
### 5.3.2 Symbolic Breakdown Return Time
  * The application shall return the argument into its symbolic breakdown in a reasonable amount of time.

## 5.4 Enviroment Requirements
 The following are the software requirements for this project:  

Category | Requirement
:---:|:---:
Language | Python 2.7 + Natural Language Toolkit (NLTK)
Shell (CLI) | Terminal
Web Browser (GUI) | Chrome (Recommended) / Firefox
  
There are no hardware requirements for this application

# 6.0 Software Design Description
(Wk 9/11)
