# Obsidian:CMS  

## Requirements:
* Python 2.7.x  
`tested with 2.7.2 and 2.7.3`  
if you are on windows you might have to adjust your PATH to point to the python executable
	
2. Django 1.3.1 or 1.4.x
	
	
##Using Obsidian:

1. edit settings.py
	* adjust STATIC_ROOT to point to the "static" directory inside your Obsidian installation
	* adjust STATICFILES_DIRS to point to the "tiny_mce" directory inside your Obsidian installation
	* adjust TEMPLATE_DIRS to point to the "template" directory within your Obsidian installation
	
2. run the server  
	* run "python manage.py runserver 0.0.0.0:80" from within your Obsidian directory  
    (if you're on linux you probably need to sudo this)	

3. navigate your browser to http://localhost/
4. done.
5. administration can be accessed via http://localhost/admin
	* use "admin" as username and password
    

######Please do not run this in a live environment!!!