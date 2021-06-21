# A SitSpot in LA Zoo 
(MyNatureStories)    

[link to deployed website](https://sitspots.page/)

A collaboration with LA Zoo Botanical Garden to build a community blog-like platform. Introduce wildlife observation experience to the general public.  

- This website is designed to be mobile-friendly, so users can share their nature observation experience anywhere, whether they are at home or at the LA Zoo. 
- Django's built-in User class was modified to achieve role-based access control. An admin user-friendly interface was implemented for zoo mangagement to use.
- Profanity check validation feature and post flagging feature were added to ensure the family-friendliness of the site.

## Roadmap
- The models were designed to be future-proof. Future work include linking community shared Nature Stories(observaions) to iNaturalist API for scientific research contribution.
- Further implementation of the role-based access control: The zoo website manager have access to delete user accounts, posts, and comments. Other zoo workers (interns) can have access to review flagged posts or comments, while professional observationist (e.g. bird watchers) can add or modify the species tags.

## Installation
Create a virtual environment folder for Django projects, then use the package manager [pip](https://pip.pypa.io/en/stable/) to install django.
```bash
python -m virtualenv djangoEnv
call djangoEnv/Scripts/activate
pip install django
```
## Usage
Activate the Django environment
```bash
source djangoEnv/Scripts/activate
```
Make migrations and migrate for the database
```bash
cd ZooGarden
python manage.py makemigrations
python manage.py migrate
```
Run the server
```bash
python manage.py runserver
```

## Website Snapshots
- Home page  
<img src="https://github.com/jilllhung/MyNatureStories/blob/main/SnapShots/Screenshot%202021-06-20%20homepage.png?raw=true" width="600">

- Introduction page: (How to) Find Your SitSpot  
<img src="https://github.com/jilllhung/MyNatureStories/blob/main/SnapShots/Screenshot%202021-06-20%20find%20your%20nature%20sitspot.png?raw=true" width="600">

- Blog page: Share Your Nature Stories  
<img src="https://github.com/jilllhung/MyNatureStories/blob/main/SnapShots/Screenshot%202021-06-20%20share%20your%20nature%20stories%201.png?raw=true" width="600">

- Guide page: LA Zoo Bird Gardens  
<img src="https://github.com/jilllhung/MyNatureStories/blob/main/SnapShots/Screenshot%202021-06-20%20la%20zoo%20bird%20gardens%201.png?raw=true" width="600">
<img src="https://github.com/jilllhung/MyNatureStories/blob/main/SnapShots/Screenshot%202021-06-20%20la%20zoo%20bird%20gardens%202.png?raw=true" width="600">

## Phone SnapShots
- Home page
<img src="https://github.com/jilllhung/MyNatureStories/blob/main/SnapShots/PhoneScreenshot%202021-06-20%20home%20page.png?raw=true" width="250">

- Blog page: Share Your Nature Stories  
| <img src="https://github.com/jilllhung/MyNatureStories/blob/main/SnapShots/PhoneScreenshot%202021-06-20%20share%20your%20nature%20stories%201.png?raw=true" width="250">  | <img src="https://github.com/jilllhung/MyNatureStories/blob/main/SnapShots/PhoneScreenshot%202021-06-20%20share%20your%20nature%20stories%202.png?raw=true" width="250">  | <img src="https://github.com/jilllhung/MyNatureStories/blob/main/SnapShots/PhoneScreenshot%202021-06-20%20share%20your%20nature%20stories%203.png?raw=true" width="250"> |  

## Authors
[Hai Qi](https://github.com/0xhqli)  
[nick lantz](https://github.com/nicklantzATS)  
