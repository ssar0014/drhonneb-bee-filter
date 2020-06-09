# Dr.HoneeB - Bee Filter API

## **What is an API?**
-	An API is basically a set of rules which lets programs (client and server) communicate in order to get and send information in the form of requests
-	It stands for Application Programming Interface.
-	REST is an architectural style of APIs. The REST architecture allows APIs to be built in a specific way such that a user should be able to get a piece of data or resource, when linked to a specific URL.
-	REST – Representational State Transfer
-	APIs which obey REST architecture are called REST APIs or RESTful APIs.
-	REST APIs are designed to be compliant with HTTP. There are one or more endpoints created which are then exposed to the clients. The clients then communicate with the API using these endpoints via relevant HTTP methods.

-	We will mostly be using the GET and POST requests to upload photos from the app and getting results back

-	There are 2 ways to make HTTP requests with android:

o	`OKhttp` - https://square.github.io/okhttp/

o	`HttpURLConnection` https://developer.android.com/reference/java/net/HttpURLConnection.html

## What is Middleware?
* Middleware is computer software that provides services to software applications beyond those available from the operating system. It can be described as "software glue".

* Middleware makes it easier for software developers to implement communication and input/output, so they can focus on the specific purpose of their application. It gained popularity in the 1980s as a solution to the problem of how to link newer applications to older legacy systems, although the term had been in use since 1968.

* A middleware component can perform such functions as:

    1. Routing a request to different application objects based on the target URL, after changing the environment variables accordingly.
    2. Allowing multiple applications or frameworks to run side-by-side in the same process
    3. Load balancing and remote processing, by forwarding requests and responses over a network
    4. Performing content post-processing, such as applying XSLT stylesheets


## What is a Web Server Gateway Interface?

* The Web Server Gateway Interface (WSGI) is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language.
* WSGI was created as an implementation-agnostic interface between web servers and web applications or frameworks to promote common ground for portable web application development.
* The WSGI has two sides:
    1. *Server/gateway side* - This is often running full web server software such as Apache or Nginx, or is a lightweight application server that can communicate with a webserver, such as flup.
    2. *Application/framework side* - This is a Python callable, supplied by the Python program or framework.
Between the server and the application, there may be one or more WSGI middleware components, which implement both sides of the API, typically in Python code.

* WSGI does not specify how the Python interpreter should be started, nor how the application object should be loaded or configured, and different frameworks and webservers achieve this in different ways.

**We are using the Gunicorn framework as our WSGI HTTP server**

## What Web server should be used?
* To host our API, we are using Heroku.


## **Deep Learning with Fast.AI and PyTorch**
* To build the classifier, image data was downloaded from the COCO dataset.
* We have used the ImageNet style of having separate folders for training and testing data.
* The model is trained to identify bee images from other random images from the COCO dataset.
* All models in this repository are built on Fast.AI and PyTorch
* There is a Jupyter notebook file which contain all the pre-processing of data, and the build of the model. To run them, simply open up a Jupyter Notebook kernel and run all cells. 
* The model is output as an .pkl file, which is then called by the API.

## **API and hosting on Heroku**
* The API was built on Python Flask
* There is one route to the home`/` which loads in the image from S3, and the model .pkl file, runs the model, and returns the output as a JSON response.
* The API, and all models are hosted on Heroku, and are available at `https://drhoneeb-bee-filter.herokuapp.com/`
* The output of this is then used by the other classifier for bee health condition.

