# Bay Area Student Rentals
## Introduction
The project is an AirBnB for students in Bay Area. The difference is that the rental length is for the whole studying year (e.g. 2021-2022) instead of short-terms. It allows you to search for rentals, make inquiries and post your own properties. The platform allows any person to rent the whole property, private or shared rooms for students for 21-22 college year.

## Demo preview
![project demo gif](student.gif)

## Video demo
<https://youtu.be/EsCZDF2oRe8>

## Getting started
To get started, you need to clone the repository.
```
$ git clone https://github.com/nameelza/web.git
$ cd finalproject
```

Install the dependencies.
```
$ pip install -r requirements.txt
```

Apply the migrations.
```
$ python manage.py makemigrations
$ python manage.py migrate
```

You can now run the server.
```
$ python manage.py runserver
```

## Features
#### As a student:
* Search for properties, based on location
* See the location, amenitites and other details of the property
* Make inquiries
* See the status of your inquiries
* Edit your profile information
#### As a landlord:
* Post your own properties
* Add amenities, security, and other features
* See the inquiries made by students
* Accept or decline inquiries
* Edit your profile information

## Technical details
The app is built on Django, using JavaScript and SQLite3. The database is stored in the local file system.

## Distinctiveness and Complexity
The app is designed on the basis of the requirements of the project. It uses Django, including four models, on the backend and Javascript on the frontend. The app is also designed to be mobile responsive, using css media queries.

### Django views functions
* `index`: get request renders the index page with the search form
* `list_results`: get request renders the list of properties
* `list_booked`: get request renders the list of only already booked properties
* `rental`: get request renders the rental page, including prefilled first name, last name and  email in the inquiry form, post request sends the inquiry to the landlord
* `profile`: get request renders the profile page, user inquiries and properties
* `create`: get request renders the create property form, post request adds the property to the database
* `login_view`: get request renders the login page, post request logs in the user
* `logout_view`: logout request logs out the user
* `register`: get request renders the register page, post request adds the user to the database
* `accept`: post request accepts the inquiry, changes the database status of the inquiry to accepted
* `decline`: post request declines the inquiry, changes the database status of the inquiry to declined
* `profile_edit`: post request edits the user profile information, including first name, last name, and email

### Django models
* User: AbstractUser model
* Property: Property model
    * Foreign key to the User model
    * Title
    * Description
    * Price
    * City (based on choices field in the table)
    * Address
    * Kind of place (based on choices field in the table, e.g. entire place, private room, or shared room)
    * Four image links
    * Availability (boolean value)
* Amenities: Amenities model
    * Foreign key to the Property model
    * wifi
    * kitchen
    * washer
    * bike
    * parking
    * cctv
    * access gate
    * wifi bill
    * water bill
    * electricity bill
    * gas bill
    * heating bill
* Booking: Booking model
    * Foreign key to the Property model
    * Foreign key to the User model
    * Status (e.g. pending, accepted, or declined)
    * phone number
    * message

### Django templates
* layout.html: the main template
* index.html: main page of the app
* create.html: form for creating the property listing
* login.html: login page
* register.html: register page
* profile.html: profile page of the user, including the list of properties, the list of inquiries, and the edit profile page
* rental.html: page of the rental and inquiry form
* results.html: list of the results of the search


