# Bay Area Student Rentals
## Introduction
The project is an AirBnB for students in Bay Area. The difference is that the rental length is for the whole studying year (e.g. 2021-2022) instead of short-terms. It allows you to search for rentals, make inquiries and post your own properties. The platform allows any person to rent the whole property, private or shared rooms for students for 21-22 college year.

## Demo preview
![project demo gif](student.gif)

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
The app is designed on the basis of the requirements of the project. It uses Django, including four models, on the backend and Javascript on the frontend. The app is also designed to be mobile responsive.

### Models
* User: AbstractUser model
* Property: Property model
    * Foreign key to the User model
    * Title
    * Description
    * Price
    * City (based on choices field in the table)
    * Address
    * Kind of place (based on choices field in the table, e.g. entire place, private room or shared room)
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
    * Status (e.g. pending, accepted or declined)
    * phone number
    * message






