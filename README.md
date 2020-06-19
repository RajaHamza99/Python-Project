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
To meet the CRUD functionality, I have created an application which allows the user to meet the criteria.
  
### Create
A user can create an account for themselves, as well as create any songs, and playlists.  
  
### Read
A user is able to view their created songs, as well as view any created playlists with their songs.  
  
### Update
A user is able to update their playlists, and change the songs within them. They are also able to update their account details.  

### Delete
A user is able to delete both their playlists and songs. They can also delete their account which will delete any playlists and songs created by them.

## Database Structure (ERD)
### First ERD  
This diagram is the initial entity relationship diagram I created to show the planned structure of the database.
![Diagram that shows initial ERD](https://theredshift.org/index.php/s/8MenBfWEbLHOPwz/download)  

### Final ERD
However, I simplified the application and relationship. This was my final ERD displaying the actual relationship.  
![Diagram that shows final, implemented ERD](https://theredshift.org/index.php/s/i6nLITYi5fgYk7u/download)  





## Application Front-End Design  
Here I have included some screenshots displaying the different pages of the application. Although the design is very simple, it is functional.

## Current Issues
Right now, there are some issues with the application. These are as follows:  
<ul>
  <li>A user cannot delete a song if that song exists in a playlist.</li>
  <li>When trying to log in, if the information is incorrect, it does not notify the user, but instead just reloads the page.</li>
  <li>To create a playlist, there have to be a minimum of 3 songs. This means a playlist can have a miniumum of 3 songs instead of having 2 empty fields.</li>
</ul>

## Improvements
Outside of fixing the current issues, I would like to make improvements to the application. These include:  
<ul>
  <li>Create a association table to have a many to many relationship between playlists and songs.</li>
  <li>Allow a user to tag other users to recommend a playlist to them.</li>
  <li>Re-design the application to be much more visually appealing.</li>
  <li>Include more information about songs, potentially recommending playlists with similar music to their own.</li>
