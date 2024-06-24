# Estuda Vagão
This is the repository of the Estuda Vagão website project.

## The Project

This repository is divided and organized into folders, which are:

- [Static](/static) which has all the project's static files such as javascript files, CSS, and images (separated into folders named by file type), within static they have other folders for better organization of the site and also some that are dependencies on libraries we use;

- [cmsm_PROJECT](/cmsm_PROJECT/) where the main Django files and their dependencies are located;

- [App](/app/) which also contains basic Django files and has the files [models](/app/models.py) that will be used for the database and the file [views](/app/views. py) which will be used to define the pages, together with the file [url](/cmsm_PROJECT/urls.py) define the routes.

- [Register](/register/) where the files used to log in, register, and update the profile of website users are located.

- [media](/media/) where the users' profile photo is stored.

- [Templates](/templates/) which has all the project's HTML templates;

- In addition to files that are not in folders but are crucial for the functioning of the site, such as [manage.py](/manage.py), the file that makes the site run, [dbatabase](/db.sqlite3/) of the application, where our SQL script is, and also the [requirements.txt](/requirements.Txt) where the application's dependencies are defined.
