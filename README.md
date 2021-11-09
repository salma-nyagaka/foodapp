[![Build Status](https://app.travis-ci.com/salma-nyagaka/foodapp.svg?branch=develop)](https://app.travis-ci.com/salma-nyagaka/foodapp)
[![Coverage Status](https://coveralls.io/repos/github/salma-nyagaka/foodapp/badge.svg?branch=develop)](https://coveralls.io/github/salma-nyagaka/foodapp?branch=develop)


## Food app
A Food Menu API.

### Description
A Django web application that allowes admin to create users and menus, food attendant to update order status and users to make orders

### Postman collection

    ```
    https://www.getpostman.com/collections/3a4ce9cdbada9b9b137a
    ```

### Development set up

-   Check that python 3 is installed:

    ```
    python --version
    >> Python 3.7.10
    ```

-   Check that PostgreSQL is installed and create the database:


-   Clone the foodapp repo and cd into it:

    ```
    git clone https://github.com/salma-nyagaka/foodapp
    ```

- Access the project

    ```
    cd foodapp/foodapi
    ```

- Install virtualenv

    ```
    pip install virtualenv
    ```

-   Create the virtual environment:

    ```
    virtualenv venv
    ```

-   Activate the virtual environment:

    ```
    source venv/bin/activate
    ```

-   Install dependencies:

    ```
    pip install -r requirements.txt 
    ```

-   Create a .env file and the following configurations

    ```
        export DB_NAME="DB_NAME"
        export DB_USER="DB_USER"
        export DB_HOST="localhost"
        export DB_PASSWORD="DB_PASSWORD"
        export SECRET_KEY="#8-9*p&2kor^he5v2$tbm$q5x3+nh@q&^9zev2em5e$pr2=qf$"
        export DJANGO_SETTINGS_MODULE=foodapi.settings

    ```

-   Get environment variables:

    ```
    source .env
    ```

-   Apply migrations:

    ```
    python manage.py migrate
    ```

-   Run the application with the command:

    ```
    python manage.py runserver 
    ```

-   Run the tests with the command:

    ```
    pytest
    ```
 #### Instructions 
 - Log in as an admin to add users, get all users, get a single user, create a menu, 
 update a menu item, get all users

   ```
    "email": "admin@gmail.com",
    "password": "admin123"
    ```
 - Log in as a food attendant to get all orders and update order status

    ```
    "email": "attendant@gmail.com",
    "password": "attendant123"
    ```

 - Log in as a normal user to view past orders

    ```
    "email": "user@gmail.com",
    "password": "user12345"
    ```
 

 #### Endpoints
| REQUEST | DESCRIPTION  | URL  |
| :-----: | :-: | :-: |
| POST | User sign Up|  https://sapplication.link/users/register?is_admin=is_admin |
| POST | User Sign In|  https://sapplication.link/users/login |
| GET | Get all users|  https://sapplication.link/users/details|
| GET | Get a single user|  https://sapplication.link/users/details/{{user_id}} |
| DELETE | Delete a user|  https://sapplication.link/users/details/{{user_id}} |
| POST | Create a menu|  https://sapplication.link/menu/ |
| GET | Fetch all menu items |  https://sapplication.link/menu/items |
| GET | GET a menu item|  https://sapplication.link/menu/item/{{menu_id}} |
| PUT | Update a menu item | https://sapplication.link/menu/item/{{menu_id}} |
| DELETE | Delete a menu item|  https://sapplication.link/menu/item/{{menu_id}} |
| GET | Create an order|  https://sapplication.link/order/ |
| GET | Fetch user's orders |  https://sapplication.link/order/user |
| GET | Fetch all orders | https://sapplication.link/order/all |
| DELETE | Delete a order|  https://sapplication.link/surverymanager/question/{{question_id}} |
| POST | Answer a question | https://sapplication.link/surverymanager/question/answer/ |
| GET | Get all answers for question|  https://sapplication.link/surverymanager/question/answer/{{question_id}} |
