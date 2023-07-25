# Step 1:
## Programming Language: Python

## Python's Web Framework: Django

## Database Used: MySQL

## Instructions To Set Up And Run The Application and Perform CRUD Operation on Web Page:
1. You need to install python application, django application, pymysql (as I have used "MySQL" database). #To install, write on terminal "pip install <app or module name>" and run.
2. Then, create a database in MySQL and also create a model in models.py, and run makemigrations, and migrate command.
3. You can view the web page as per the corresponding URLs.
4. You can go perform CRUD Operations on webpages like State, City and Branch.
5. You can also add data through django admin by creating a superuser.

## Necessary Instructions To Set Up And Run The Application and Perform CRUD Operation using RestAPI:
1. You need to install djangorestframework, serializers.
2. To check my API, I use 'Postman'.
3. My APIToken is f077604032c318af9f732210561245579fb17547
4. You can go to 'Postman' website to see all the details or perform CRUD operations and URLs are "http://127.0.0.1:8000/tech/state/, http://127.0.0.1:8000/tech/city/, http://127.0.0.1:8000/tech/branch/". There are a few more URLs which you can check in urls.py files.

# Step 2:
1. Created CRUD (Create, Edit, Delete, List in templates) Operations for the above database.

# Step 3:
Written Script in Javascript to handle Client-side validations.

# Step 4: A brief description of HTTP GET and POST methods.
## HTTP GET Method:
1.	GET is one of the most commonly used HTTP methods and is primarily used to request data from a specified resource on the web server.
2.	When a client (such as a web browser) sends a GET request, it sends the request parameters to the URL as query strings. 
3.	This method is commonly used for retrieving data, fetching resources, or performing read-only operations.

## HTTP POST Method:
1.	POST is used to submit data to be processed to a specified resource on the web server.
2.	When a client sends a POST request, the data is sent in the request body rather than in the URL, allowing for more data to be sent compared to GET requests.
3.	This method is mostly used for creating new resources, submitting data to be processed, updating existing resources, or performing write operations.

# Step 5: Explain Django framework MVT architecture briefly.
1.	Django is a Python’s web framework for building web applications and follows MVT(Models, Views and Templates) architecture which is a variant of MVC(Models, Views and Controllers) architecture.
2.	If we talk about a website, when an user click on a page, the request(HTTP Request) goes from browser to Django Server. There, the manage.py file searches for settings.py file which contains information of all the installed apps in the project, middleware used, database connections and path to the main URLs configured.
3.	Then the request goes to the urls.py file and check for the available resource in the URLs. Then the request goes to the views.py, from views.py to models.py, from models.py to template files and then returns to the browser as HTTP Response.
4.	The flow is:
HTTP_Request-->Django_Server-->URLs-->Views-->Models-->Templates-->HTTP_Response

## GitLab Profile: https://github.com/Suv-Mohanty