<p>
  <img title="Meta" alt="Alt text" src="https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/http://coursera-university-assets.s3.amazonaws.com/dd/9d81501fcf46f7981257ec9f7f5a0a/Metalogo_transparent.png?auto=format%2Ccompress&dpr=1&w=&h=45">
  <h1>Back-end Developer Capstone</h1>    
</p>

This course covers building a capstone project using Django, specifically building a Django Rest API app for the Little Lemon restaurant.

The Capstone project enables you to demonstrate multiple skills from the Certificate by solving an authentic real-world problems. Each module includes a brief recap of, and links to, content that you have covered in previous courses in this program. 

This course will test your knowledge and understanding, and provide you with a platform to show off your new abilities in back-end development using Django. During this course, you will be guided through the process of building an app, combining all the skills and technologies you've learned throughout this program to solve the problem at hand.

### Running the server for the first time 
#### Clone the repository
```
user:~$ git clone https://github.com/gochuicod/LittleLemonBackend.git
```

#### Install dependencies
```
user:~$ cd LittleLemonBackend
user:~$ pipenv shell
user:~$ pipenv install
```

#### Setup the database
```
mysql -u root -p

mysql> create database restaurant;
mysql> create user 'admin'@'localhost' identified by 'admin@123!'
mysql> grant all on *.* to 'admin'@'localhost'
mysql> flush privileges
```

#### Create a superuser
```
user:~$ python manage.py createsuperuser
Username: admin
Email address: admin@littlelemon.com
Password: admin@123!
Password (again): admin@123!
```

#### Migrate then run the server
```
user:~$ cd littlelemon/
user:~$ python manage.py migrate
user:~$ python manage.py runserver
```

### Available URLs
#### For the API
```
localhost:8000/api/
localhost:8000/api/users/
localhost:8000/api/bookings/
localhost:8000/api/menu-items/
```

#### For user authentication
```
localhost:8000/auth/
localhost:8000/auth/token/login/
localhost:8000/auth/token/refresh/
localhost:8000/auth/token/blacklist/
```

#### For everything else
```
localhost:8000/admin/
localhost:8000/home/
```
