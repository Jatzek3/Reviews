Work in progress

# Reviews

https://learn-python-programming.herokuapp.com/


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
