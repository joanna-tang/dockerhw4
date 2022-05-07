
![image](https://user-images.githubusercontent.com/101609196/167264725-3c9e426e-0c39-4913-9821-2c7af233c0c9.png)
![image](https://user-images.githubusercontent.com/101609196/167264732-d254024c-690b-485c-a79f-eba0616757ef.png)
![image](https://user-images.githubusercontent.com/101609196/167264745-0967d6c0-7437-4416-b9cf-e3fdd4aaa416.png)

Below is the resulting page when the docker-compose project is running:
![image](https://user-images.githubusercontent.com/101609196/167275028-345fcf7c-2782-4e31-a0be-4663669c52bf.png)


This project is developed using Visual Studio 2019, with python 3.10.4 and flask for the web tier.
Backend is using mysql and redis.
here's some setting I added for this project

![image](https://user-images.githubusercontent.com/101609196/167274927-31e222de-fb97-42ad-aa87-df130eeebad3.png)

![image](https://user-images.githubusercontent.com/101609196/167274932-475f0525-fe49-42f4-8ce1-39a949725177.png)


To run the project successfully, you need to first modify 2 files that are used by docker secret.
1) root_secret.txt   <- use this to store the root password for your mysql instance
2) hw4_secret.txt    <- use this to store the hw4app user password for your mysql instance

Docker secret uses docker swarn, so before running the project, secrets need to be set up first.  To set up docker secret, use the below command:
> docker swarn init

> docker secret create root_secret root_secret.txt

> docker secret create hw4_secret hw4_secret.txt

![image](https://user-images.githubusercontent.com/101609196/167275379-5c64c70b-4519-47a5-9ad1-027519e6e6ca.png)

Also, review docker-compose.yml file to change any configuration as you see fit.

To build the project, use the below command:
>docker-compose build

To start the project, use the below command:
>docker-compose up -d

When the project is up, they should look like this:
![image](https://user-images.githubusercontent.com/101609196/167275218-a5d9d0c6-b82d-4df8-be0c-149808295791.png)

Open browser to http://localhost:5000 and have fun!
