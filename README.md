# to-do-list
To-do List Project
### ucksylr's To-do Organizer Project(Capstone) Documentation

### Introduction
In daily life, lists usually use for keep someting temporarily. During to day, people sometimes forget little things while they have one's mind on other thing. Thanks to the lists, we keep these things temporarily. Lists may be a shopping list, a wedding preparation list, to-dos, requirements, aim and objectives, imagines etc.  But, we often do not have a notepad and pencil when they need. Also, usage of smart phones and computers raise dramatically. Therefore, if we adaptation these improvements in our daily life, it can be offer more comfortable life. Moreover, with the web applications, we can use application in all platforms. In addition, thanks to the responsive desing, we can use it in all device sizes. So, I decided to create a web application to keep our lists easily. We can organize lists, add item to lists and manage our lists. The To-do Organizer is created for organize manage your to-do list easily. Its not only ~a todo app~ but also an **organizer**!:punch: Here is the what you can do with it:

- Create and login a special account and manage lists into it
- Create and manage lists(Shopping List, Todos, etc.)
- Add, delete, mark, filter, order and track your items in list
- Track your deadlines 

### How to work 
The project uses django for backend and JS for frontend. Backend side has two extra models called Todo and TodoList. Also, project has 5 filter methods, 10 different pages, CSS and JS support and 10 different html templates. Now, we examine each folder:

to_do_organizer: main project folder auto created by django<br>
todo: subfolder created with startapp command to build main workflow<br>
todo/static: to keep js and css files <br>
todo/templates: to keep html templates<br>
todo/migrations: to keep database changes<br>

### Why this project

This project was designed to help people daily routines. It has a useful design. 
For example, adding new item in list is next to he list name and it is a popover item. 
Thus, while adding a lot of items in list, user does not need go and back from page to page. 



Thanks for Brian Yu and who helped to create this **great** course!

### INSTALL & RUN
Clone repository from your local computer

git clone https://github.com/ucksylr/to-do-list.git


Open file then right click/Git Bash Here(for Windows)

If you do not have Git, download here (https://git-scm.com/downloads)



Open file then right click/Terminal here(for Linux)


Type this command

code . (For Visual Studio Code)


Menu/Terminal/New Terminal or Ctrl+Shift+"


Type this command

python manage.py runserver

