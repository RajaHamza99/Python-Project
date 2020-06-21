# Python-Project

## Contents

<ul>
  <li>Project Objective</li>
<li>App Overview</li>
<li>Database Structure</li>
<li>CI Pipeline</li>
<li>Trello Board</li>
<li>App design</li>
<li>Current Issues</li>
<li>Testing</li>
<li>Improvements</li>
</ul>

## Project Objective  
The project objective was as follows:  
"To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training."  

In order to meet this requirement, I create a basic application which allows a user to create, read, update and delete playlists.  

As well as meeting the basic CRUD functionality, the project required the following:
<ul>
  <li>Kanban board</li>
  <li>A relational database consisting of at least 2 tables, with a modelled relationship.</li>
  <li>Clear documentation from a design phase describing the architecture used as well as risk assessment.</li>
  <li>A functional CRUD application created in Python, following best practises.</li>
  <li>Test suites for the application, as well as automated tests for validation of the application.</li>
  <li>A functioning front-end website using Flask.</li>
  <li>Code integrated into a Version Control System to be built through a CI server and deployed to a cloud-based VM.</li>
  </ul>
  
## App Overview
To meet the CRUD functionality, I have created an application which allows the user to meet the criteria in the following ways:  
  
### Create
A user can create an account for themselves, as well as create any songs, and playlists.  
  
### Read
A user is able to view their created songs, as well as view any created playlists with their songs.  
  
### Update
A user is able to update their playlists, and change the songs within them. They are also able to update their account details.  

### Delete
A user is able to delete both their playlists and songs. They can also delete their account which will delete any playlists and songs created by them.

## Kanban Board - Trello  
![Diagram of project tracking trello board](https://theredshift.org/index.php/s/TdoZHyzGzGx35rl/download)  
A Kanban Board was used to keep track of my Project. A Trello board has been used to keep track of my progress. I initially created this with only the user stories, but developed on it to add testing as well as deployment objectives. The different labels specify the Minimum Viable Product (MVP) which allowed me to direct my focus. Other features are listed on here as "should have" - identifying future objectives I would like my application to have but have not yet been implemented. The listed User Stories are the basic functions the application should have to meet the CRUD specification, and the user's basic needs. 

## Database Structure (ERD)
### First ERD  
This diagram is the initial entity relationship diagram I created to show the planned structure of the database.
![Diagram that shows initial ERD](https://theredshift.org/index.php/s/8MenBfWEbLHOPwz/download)  

### Final ERD
However, I simplified the application and relationship. This was my final ERD displaying the actual relationship.  
![Diagram that shows final, implemented ERD](https://imgur.com/pfHP0W6.jpg)


## CI Pipeline  
Below is a diagram detailing the CI Pipeline with the services used to display how the project was created and executed. By using these systems, it vastly reduces time from development to deployment. After editing code, I can push my work to a GitHub repository. From this, a build trigger is executed on Jenkins via webhook, deploying the application to the VM on Google Cloud Platform. Jenkins automatically runs tests after every push to GitHub after which, if successful, deploys the application. The application is also created with debugger mode active, which allows for dynamic testing.  

The entire process after a commit is handled by Jenkins, which fully automates testing and deployment. After a commit to GitHub, webhooks are triggered which run the tests and then deploy the application. If any tests fail, Jenkins outlines where the errors occurred in the console output. This is extremely helpful as it allows you to see where your testing or code failed, and allows for much easier fixes.  

The application is run using Gunicorn, which assigns workers which divide the CPU resources of the VM. When a user connects to the server, a worker is assigned to that user allowing the application to run much faster.  
![Diagram showing CI Pipeline](https://theredshift.org/index.php/s/Soq5a6Wu2UyFtkC/download) 

## Application Front-End Design  
Here I have included some screenshots displaying the different pages of the application. Although the design is very simple, it is functional.

The user begins on the home page, where there are several options for different pages listed at the top. This is also where their created playlists would be listed.  

![Diagram showing CI Pipeline](https://theredshift.org/index.php/s/EQJfnc3KahB0Fc3/download) 

The register page allows a user to register an account to access the other features of the application.  

After registering, a user will be redirected to the login page where they can now log in.  

![Diagram showing CI Pipeline](https://theredshift.org/index.php/s/gMVwtG60nRrV1uq/download) 

After logging in, a user is redirected to the songs page, where they can create and delete songs. This is necessary as songs have to be created before being able to create a playlist.  

![Diagram showing songs page](https://theredshift.org/index.php/s/8eWl5F9nDFfWgMK/download)

After creating songs, a user can visit the playlists page. This will allow them to select their created songs from the dropdown box and select a title for their playlist. This will then create their playlist.  

![Diagram showing create playlist page](https://theredshift.org/index.php/s/HYpwcZCp9TFFtvF/download)

After creating a playlist, the user will be redirected to the home page. Here, they will be able to view their created playlists as well as the songs within them, and see options to update or delete their playlists.  

After clicking the update button, a user will be able to select different songs from within the dropdown box to change the contents of their playlist.  

![Diagram showing home page with playlists on it](https://theredshift.org/index.php/s/EQJfnc3KahB0Fc3/download)

From the home page, if a user clicks "delete playlist", their playlist will be deleted from the database.  

A user also has the option to delete their account. If they do this, all playlists created by them will also be deleted.  

## Testing  

Debugger mode was active throughout development to allow for dynamic testing.  

## First Unit Test Coverage  

Pytest was also used to run unit and integration tests. Unit tests are designed to test a function. If the test result returns the expected result, the test passes. Jenkins also provides information on which tests have passed and failed through the console output. 

My first unit test provided 50% coverage for my application. 
![Diagram of first unit test coverage](https://imgur.com/VTQeGX0.jpg)

To meet the 75% test coverage requirement, I used the command to view lines which hadn't been tested. This allowed me to focus further testing on areas that hadn't already been tested.

![Diagram showing lines covered by unit tests](https://imgur.com/kLG3HWN.jpg)

![Diagram that shows testing coverage](https://theredshift.org/index.php/s/RJhGiaW8TpKnQdJ/download)

## Risk Assessment

As part of the project brief, I carried out a risk assessment identifying the potential issues and risks associated with the project.  

![Diagram displaying risk assessment table]()
## Current Issues
Right now, there are some issues with the application. These are as follows:  
<ul>
  <li>A user cannot delete a song if that song exists in a playlist.</li>
  <li>When trying to log in, if the information is incorrect, it does not notify the user, but instead just reloads the page.</li>
  <li>To create a playlist, there have to be a minimum of 3 songs. This means a playlist can have a miniumum of 3 songs instead of having 2 empty fields.</li>
  <li>The home page displays all playlists, not just playlists belonging to that user. However, any user can delete all playlists, even if it doesn't belong to them.</li>
  <li>Deleting a user deletes their created playlists, but does not delete any songs they created.</li>
</ul>

## Improvements
Outside of fixing the current issues, I would like to make improvements to the application. These include:  
<ul>
  <li>Create a association table to have a many to many relationship between playlists and songs.</li>
  <li>Allow a user to tag other users to recommend a playlist to them.</li>
  <li>Re-design the application to be much more visually appealing.</li>
  <li>Include more information about songs, potentially recommending playlists with similar music to their own.</li>
  <li?Implement album art, and give the user to select an album cover to associate with their playlist.</li>
  
  
  jenkins test 13
