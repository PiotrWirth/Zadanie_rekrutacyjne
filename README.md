# Images

To properly use this project you have to change the path for python in pyvenv.cfg to use the python virtual enviroment

This project uses two apps - 'accounts' and 'picture'. The project uses pillow imagekit package to upload pictures and create thumbnails.

One administrator account has been created with login credentials
login: test
password: test

3 user accounts have been created:
test1 - Basic
test2 - Premium
test3 - Enterprise

password to all three accounts is: superuser

Login is done via 'accounts/login'. Once logged in, we can add a photo from 'picture/upload'. 
Once the photo is uploaded, we are redirected to 'picture/tier' where, depending on the user's level, links to thumbnail photos are displayed. 
The list of all user's photos is located under 'accounts/' . Each user has access only to their own photos
