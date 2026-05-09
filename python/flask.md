
# Overview
https://www.tutorialspoint.com/flask/index.htm

- Web Application Framework simply Web Framework represents a collection of libraries and modules that enables a 
  web application developer to write applications without having to bother about low-level details such as protocols, 
  thread management etc.

- Web Server Gateway Interface(WSGI) : WSGI is a specification for a universal interface between the web server and the web applications.
  WSGI has been adopted as the standard for Python web application development.

- Werkzeug : A WSGI toolkit, which implements requests, response objects, and other utility functions. 
  This enables building a web framework on top of it. The Flask framework uses Werkzeug as one of its bases.



## Jinja2
- Jinja2 is a popular templating engine for Python. 
- A web templating system combines a template with a certain data source to render dynamic web pages.

## Flask
- Flask is a web application framework written in Python. 
- Armin Ronacher, who leads an international group of Python enthusiasts named Pocco, develops it. 
- Flask is based on Werkzeug WSGI toolkit and Jinja2 template engine. Both are Pocco projects.
- Flask is often referred to as a micro framework. It aims to keep the core of an application simple yet extensible. 
- Flask does not have built-in abstraction layer for database handling, nor does it have form a validation support. 
  Instead, Flask supports the extensions to add such functionality to the application.

- Install : $ pip3 install Flask

## Sample code
- Check hello.py or app.py
- Importing flask module in the project is mandatory. An object of Flask class is our WSGI application.

# decorator - route() method
- The route() function of the Flask class is a decorator.
- The route() decorator in Flask is used to bind URL to a function.
- The decorator tells the application which URL should call the associated function.

syntax : 
@app.route(rule, options)
def function_name():
   ! what function does.

Example :
@app.route('/')
def hello_world():
   return 'Hello World'

- The rule parameter represents URL binding with the function.
- The options is a list of parameters to be forwarded to the underlying Rule object.
- In the example, ‘/’ URL is bound with hello_world() function.
- Hence, when the home page of web server is opened in browser, the output of this function will be rendered.

# run() method
- The run() method of Flask class runs the application on the local development server.
- Once started, server starts listening to incoming requests & it is continous until stopped ( CTRL+C , or is there another way??)

  app.run(host, port, debug, options)
   - All parameters are optional.
   - host    : Hostname to listen on. Defaults to 127.0.0.1 (localhost). Set to ‘0.0.0.0’ to have server available externally
   - port    : Defaults to 5000
   - debug   : Defaults to false. If set to true, provides a debug information
   - options : To be forwarded to underlying Werkzeug server.

## debug mode
- A Flask application is started by calling the run() method. 
  However, while the application is under development, it will need to be restarted manually for each change in the code. 

- To avoid this inconvenience, enable debug support. The server will then reload itself if the code changes. 
  It will also provide a useful debugger to track the errors if any, in the application.
  
-The Debug mode is enabled by either :
 1) setting the debug property of the application object to True before running 
    app.debug = True
    app.run()

 2) passing the debug parameter to the run() method.
    app.run(debug = True)

- As you change the code, alerts will be coming up:

  $ python3 app-v2.py 
 * Serving Flask app 'app-v2'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 665-521-729
127.0.0.1 - - [17/Jun/2024 13:34:51] "GET /hello/Allan HTTP/1.1" 200 -
127.0.0.1 - - [17/Jun/2024 13:35:01] "GET /hello/Stevo HTTP/1.1" 200 -
127.0.0.1 - - [17/Jun/2024 13:35:11] "GET /hello/Shujaa HTTP/1.1" 200 -
127.0.0.1 - - [17/Jun/2024 13:35:20] "GET /hello/Albert HTTP/1.1" 200 -
 * Detected change in '/home/amaseghe/developer/python/flask/projects/app-v2.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 665-521-729
 * Detected change in '/home/amaseghe/developer/python/flask/projects/app-v2.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 665-521-729
 * Detected change in '/home/amaseghe/developer/python/flask/projects/app-v2.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 665-521-729
 

# firewall - host port
- You have to ensure the port you are using is allowed through the firewall.
- Clients requests through either web url or curl will routed to the chosen port.

- Check if firewall allows the ports through:
    $ sudo ufw status

- If UFW is active, the output will show a list of allowed ports and services. Check if port 5000 appears in the list: 
    $ sudo ufw status | grep 5000

- If port 5000 is not allowed, you can allow it with the following command: 
    $ sudo ufw allow 5000/tcp

- After allowing the port, reload the firewall to apply the changes:
    $ sudo ufw reload

- Check again within step 2 command.


# flask methods
https://www.tutorialspoint.com/flask/flask_http_methods.htm

- Http protocol is the foundation of data communication in world wide web. 
- Different methods of data retrieval from specified URL are defined in this protocol.

- Methods used :
1. GET    : Sends data in unencrypted form to the server. Most common method.
2. HEAD   : Same as GET, but without response body
3. POST   : Used to send data in HTML form to the server. Data received by POST method is not cached by server.
4. PUT    : Replaces all current representations of the target resource with the uploaded content.
5. DELETE : Removes all current representations of the target resource given by a URL

- By default, the Flask route responds to the GET requests. 
  However, this preference can be altered by providing methods argument to route() decorator.


# variable rules
https://www.tutorialspoint.com/flask/flask_variable_rules.htm

- what if i don't want to repeat many functions that get out an output that's common on the root?
What if I want to build a URL dynamically?

- It is possible to build a URL dynamically, by adding variable parts to the rule parameter. This variable part is marked as <variable-name>. 
- It is passed as a keyword argument to the function with which the rule is associated.
- Check app-v2.py that improves on app.py

Sample code 
------------

from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return "Hello %s!" %name 

if __name__ == '__main__':
   app.run(debug = True)

output
------
SERVER:
$ python3 app-v2.py 
 * Serving Flask app 'app-v2'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 665-521-729
127.0.0.1 - - [17/Jun/2024 13:34:51] "GET /hello/Allan HTTP/1.1" 200 -
127.0.0.1 - - [17/Jun/2024 13:35:01] "GET /hello/Stevo HTTP/1.1" 200 -
127.0.0.1 - - [17/Jun/2024 13:35:11] "GET /hello/Shujaa HTTP/1.1" 200 -
127.0.0.1 - - [17/Jun/2024 13:35:20] "GET /hello/Albert HTTP/1.1" 200 -
 * Detected change in '/home/amaseghe/developer/python/flask/projects/app-v2.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 665-521-729
 * Detected change in '/home/amaseghe/developer/python/flask/projects/app-v2.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 665-521-729
127.0.0.1 - - [17/Jun/2024 13:42:52] "GET /hello/Albert HTTP/1.1" 200 -
127.0.0.1 - - [17/Jun/2024 13:42:56] "GET /hello/Shujaa HTTP/1.1" 200 -
127.0.0.1 - - [17/Jun/2024 13:43:00] "GET /hello/Shujaa HTTP/1.1" 200 -
127.0.0.1 - - [17/Jun/2024 13:43:04] "GET /hello/Stevo HTTP/1.1" 200 -


CLIENT:
 $ curl http://localhost:5000/hello/Albert
Hello Albert!
 $ curl http://localhost:5000/hello/Shujaa
Hello Shujaa!
 $ curl http://localhost:5000/hello/Shujaa
Hello Shujaa!
 $ curl http://localhost:5000/hello/Stevo
Hello Stevo!

# Converters and Strings

In addition to the default string variable part, rules can be constructed using the following converters −

int   : accepts integer
float : Floating point value
path  : Accepts slashes used in directory separator character