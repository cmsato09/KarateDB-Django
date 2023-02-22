# Karate Database with Django

## Project Description
The Kata Database notes all technique names and moveset in Shotokan Karate.
It displays each form with various parameters and is searchable. 

## How to Run
### Run project locally
1. Clone repo
2. Run the following commands to populate Kata, Stance, and Technique tables
    - `python manage.py kata_importer`
    - `python manage.py stance_importer`
    - `python manage.py technique_importer`
3. Run the server with `python manage.py runserver`
## Resources used to make project

## Credits
Initial help with planning with Bob Belderbos through the Pybites Developer 
Mindset Program. 