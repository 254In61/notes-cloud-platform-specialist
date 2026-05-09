Steps for virtualenv setup
===========================
1. sudo apt install python3.10-venv          # install virtual environment

2. python3 -m venv countries                 # create a virtual environment. Creates a whole python env with supporting files.


3. source countries/bin/activate             # Activate the created virtual environment
!
** Activating the virtual environment will change your shell’s prompt to show what virtual environment you’re using, 
and modify the environment so that running python will get you that particular version and installation of Python. 
For example:

(countries) amaseghe@black-panther:~/developer/python/flask/projects$ python
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>

!
** happy coding!...
!
deactivate                                # deactivate a virtual environment


Candles
=======
- This is fun! Makes me feel like a real Pythonista!..ha ha
- Virtualenv create an environment. Yes, the environment is a directory, BUT you DO NOT cd in the directory to work on it!
  You instead activate the environment..And when done, you deactivate!
- You notice that, you always work from the directory that contains the projects.. You just activate the project name.