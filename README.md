Work in progress

# Reviews

This is the code for my website written in Django on my own. The code isnt transcribed from any source.

https://learn-python-programming.herokuapp.com/

In developing the backend i used the sources and knowledge from which i was learning, but it was only for chunks of code. I often seeked help on Stack Overflow which in many occasions proved to be very helpfull.

### Structure

Website consists of four main apps:
- Homepage
- Tutorials
- Exercises
- Books

Best practices
 - Added Test - Still not TDD but its a start.
 - Added Docstrings and Comments - For better comprehension

Devops stuff
- The site is deployed on heroku.
- Static files can be uploaded  (whitenoise module).
- It Uses a S3 AWS bucket for uploading the files(functionality not tested and not implemented in production)
- It uses PostrgreSQL as a Database since heroku offers it in default for free(django_storages module)


### Backend functionalities
Account managment
- Signup
- Log in and Log out
- Password reset
- New Model creation after logging in

Frontend linkage to backend
- Base.html
- Links for each app
- HTML Meta

Django view classes and costumization
- List View
- Detail View
- Create View
- Custom User

Testing
- SimpleTestCase
- TestCase
