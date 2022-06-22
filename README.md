# proj0_2
Hello, this is the first project I worked to showcase what I have leart so far with Revature at the time I am writing this.

In order to run my project:
- Download the most recent version of python along with your chosen IDE
- Make sure you use the Python interpreter in the IDE
- Make sure you also have pip
- You can check if you have installed them properly by putiing in "python --version" and "pip --version" in the cmd
- You just need the proj0.py and the env files
- the env files contains the details for when you would like to create the Mysql table
- what env should contain:
HOST="Name of yout host"
USER="Your username"
PASSWORD="mysql passsword"
- Once you have a connection to the Mysql databse create these tables
- copy paste the CREATE TABLE's below in Mysql workbrench
CREATE TABLE users (
    user_ID int NOT NULL auto_increment,
    name varchar(255),
    username varchar(255),
    password varchar(255),
    role varchar(255),
    PRIMARY KEY (user_ID)
);

CREATE TABLE Address (
    address_ID int NOT NULL auto_increment,
    address_line varchar(255),
    city varchar(255),
    country varchar(255),
    zipcode varchar(255),
    user_ID int,
    PRIMARY KEY (address_ID),
    FOREIGN KEY (user_ID) REFERENCES users(user_ID)
);

CREATE TABLE bank_accounts(
    account_ID int NOT NULL auto_increment,
    balance int,
    user_ID int,
    PRIMARY KEY (account_ID),
    FOREIGN KEY (user_ID) REFERENCES users(user_ID)
);

-Make sure you have all these packages by doing "pip install 'package_name'"

asgiref==3.5.2

asttokens==2.0.5

backcall==0.2.0

certifi==2022.6.15

charset-normalizer==2.0.12

colorama==0.4.4

debugpy==1.6.0

decorator==5.1.1

entrypoints==0.4

executing==0.8.3

idna==3.3

ipykernel==6.13.1

ipython==8.4.0

jedi==0.18.1

jupyter-client==7.3.4

jupyter-core==4.10.0

matplotlib-inline==0.1.3

mysql-connector==2.2.9

mysql-connector-python==8.0.29

nest-asyncio==1.5.5

numpy==1.22.4

packaging==21.3

parso==0.8.3

pickleshare==0.7.5

prompt-toolkit==3.0.29

protobuf==4.21.1

psutil==5.9.1

pure-eval==0.2.2

Pygments==2.12.0

pyparsing==3.0.9

python-dateutil==2.8.2

python-dotenv==0.20.0

pytz==2022.1

pywin32==304

pyzmq==23.1.0

requests==2.28.0

six==1.16.0

sqlparse==0.4.2

stack-data==0.2.0

tornado==6.1

traitlets==5.2.2.post1

tzdata==2022.1

urllib3==1.26.9

wcwidth==0.2.5

-and then run the program in the IDE!!
