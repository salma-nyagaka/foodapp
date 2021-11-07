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
        export DB_NAME="test4"
        export DB_USER="test4"
        export DB_HOST="localhost"
        export DB_PASSWORD="test4"
        export SECRET_KEY="#8-9*p&2kor^he5v2$tbm$q5x3+nh@q&^9zev2em5e$pr2=qf$"
        export DJANGO_SETTINGS_MODULE=survey.settings

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

 #### Endpoint
| REQUEST | DESCRIPTION  | URL  |
| :-----: | :-: | :-: |
| POST | User sign Up|  http://ec2-18-203-249-202.eu-west-1.compute.amazonaws.com/users/register?is_admin=is_admin |
| POST | User Sign In|  http://ec2-18-203-249-202.eu-west-1.compute.amazonaws.com/users/login |
| GET | Get all users|  http://ec2-18-203-249-202.eu-west-1.compute.amazonaws.com/users/details|
| GET | Get a single user|  http://ec2-18-203-249-202.eu-west-1.compute.amazonaws.com/users/details/{{user_id}} |
| DELETE | Delete a user|  http://ec2-18-203-249-202.eu-west-1.compute.amazonaws.com/users/details/{{user_id}} |
| POST | Create a menu|  http://ec2-18-203-249-202.eu-west-1.compute.amazonaws.com/menu/ |
| GET | Fetch all menu items |  http://ec2-18-203-249-202.eu-west-1.compute.amazonaws.com/menu/items |
| GET | GET a menu item|  http://ec2-18-203-249-202.eu-west-1.compute.amazonaws.com/menu/item/{{menu_id}} |
| PUT | Update a menu item | http://ec2-18-203-249-202.eu-west-1.compute.amazonaws.com/menu/item/{{menu_id}} |
| DELETE | Delete a menu item|  http://ec2-18-203-249-202.eu-west-1.compute.amazonaws.com/menu/item/{{menu_id}} |
| GET | Create an order|  http://ec2-18-203-249-202.eu-west-1.compute.amazonaws.com/order/ |
| GET | Fetch user's orders |  http://ec2-18-203-249-202.eu-west-1.compute.amazonaws.com/order/user |
| GET | Fetch all orders | http://ec2-18-203-249-202.eu-west-1.compute.amazonaws.com/order/all |
| DELETE | Delete a order|  http://ec2-18-203-249-202.eu-west-1.compute.amazonaws.com/surverymanager/question/{{question_id}} |
| POST | Answer a question | http://ec2-18-203-249-202.eu-west-1.compute.amazonaws.com/surverymanager/question/answer/ |
| GET | Get all answers for question|  http://ec2-18-203-249-202.eu-west-1.compute.amazonaws.com/surverymanager/question/answer/{{question_id}} |
