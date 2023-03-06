# Karate Kata Database with Django

## Project Description
The Kata Database notes all technique names and moveset in Shotokan Karate.
It displays each form's moveset with various searchable parameters.

The idea for this project came from my teacher at my local Karate dojo.
He wanted to make SQL-like queries to all the forms to find similarities and 
differences and I thought it would make a cool project. 

Project deployed on [Railway](https://railway.app/)

Access the demo of the project at <https://karatedb-django-production.up.railway.app/>

## Project Goal
My sensei want to run queries such as:

- How many blocks are done with the left arm in all forms?
- Are there more blocks or attacks in the Heian forms?
- Are there more right-handed moves for attacks in this form versus another form?
- How many left-hand strikes there are in all forms combined and how does that 
compare to number of right-hand strikes?
- How many attacks are in front-stance compared to blocks in back-stance?
- Which form has the most fast moves in a row and which has the most slow moves in a row?
- Number of techniques overlapping in one form compared to another form

The basic skeleton of this project is a table showing all techniques and 
parameters and a user login to limit who can create, update, and delete entries. 

## Resources used to make project
- [Django 4 by Example](https://djangobyexample.com/) by Antonio Melé
- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Railway Docs](https://docs.railway.app/)

## Credits
Initial help and planning of the project with Bob Belderbos through the 
[Pybites Developer Mindset Program](https://pybit.es/catalogue/the-pdm-program/).

Kata data provided by Jon sensei and other dojo members.
