mimikry

This is a work-in-progress project.

**Install Notes:**

clone repo from github, checkout devel branch, create a virtual env, link the project into this env, activate the environment, install required packages, create django database, start development server.

	$ virtualenv openDCM-env
	$ cd openDCM-env/
	$ ln -s <PATH TO YOUR GITHUB CLONE>/mimikry 
	$ pip install -r mimikry/requirements.txt 
	$ . bin/activate
	$ pip install -r mimikry/requirements.txt 
	$ cd mimikry
	$ python manage.py syncdb
 	$ python manage.py runserver

