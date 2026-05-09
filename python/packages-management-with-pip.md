Managing packages with pip
===========================
https://docs.python.org/3/tutorial/venv.html
- You can install, upgrade, and remove packages using pip. 
- By default pip will install packages from the Python Package Index, https://pypi.org/
- pip has a number of subcommands: “install”, “uninstall”, “freeze”, etc. 
- 
1. Check installed packages
$ python3 -m pip list
Package    Version
---------- -------
pip        22.0.2
setuptools 59.6.0

2. Install latest version of package :
(countries) amaseghe@black-panther:~/developer/python/flask/projects$ python3 -m pip install requests
** You can also install a specific version of a package by giving the package name followed by == and the version
(tutorial-env) $ python3 -m pip install requests==2.6.0

3. Upgrade existing packagesL
you can run python -m pip install --upgrade to upgrade the package to the latest version:
(tutorial-env) $ python3 -m pip install --upgrade requests

4. Remove packages
python3 -m pip uninstall

5. Details about the package
 $ python3 -m pip show idna
Name: idna
Version: 3.7
Summary: Internationalized Domain Names in Applications (IDNA)
Home-page: 
Author: 
Author-email: Kim Davies <kim+pypi@gumleaf.org>
License: 
Location: /home/amaseghe/developer/python/flask/projects/countries/lib/python3.10/site-packages
Requires: 
Required-by: requests
(countries)

6. What if you are working on a project to be shipped to other users and you want them to know what packages are
   required? You have a virtualenv that has certain python packages installed and you need to document them.
   - You write them all on requirements.txt . 
   - The requirements.txt can then be committed to version control and shipped as part of an application. 
   - Users can then install all the necessary packages with install -r :
     $ python3 -m pip install -r requirements.txt
   - You write the requirements.txt easily with $ python3 -m pip freeze
   - The output uses the format that python -m pip install expects.
    
   $ python3 -m pip freeze > requirements.txt
   $ cat requirements.txt 
     certifi==2024.6.2
     charset-normalizer==3.3.2
     idna==3.7
     requests==2.32.3
     urllib3==2.2.1
