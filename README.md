
![image](https://user-images.githubusercontent.com/101609196/167264725-3c9e426e-0c39-4913-9821-2c7af233c0c9.png)
![image](https://user-images.githubusercontent.com/101609196/167264732-d254024c-690b-485c-a79f-eba0616757ef.png)
![image](https://user-images.githubusercontent.com/101609196/167264745-0967d6c0-7437-4416-b9cf-e3fdd4aaa416.png)

Below is the resulting page when the docker-compose project is running:
![image](https://user-images.githubusercontent.com/101609196/167264798-9511a6c0-1e8a-4fab-b41f-f7e68508b7df.png)

This project is developed using Visual Studio 2019, with python 3.10.4 and flask for the web tier.
Backend is using mysql and redis.

To run the project successfully, you need to modify 2 files that are used docker secret.
1) root_secret.txt   <- use this to store the root password for your mysql instance
2) hw4_secret.txt    <- use this to store the hw4app user password for your mysql instance

Docker secret uses docker swarn, so before running the project, secrets need to be set up first.  To set up docker secret, use the below command:
> docker swarn init
> docker secret create root_secret root_secret.txt
> docker secret create hw4_secret hw4_secret.txt

Also, review docker-compose.yml file to change any configuration as you see fit.

To build the project, use the below command:
>docker-compose build

To start the project, use the below command:
>docker-compose up -d

open browser to http://localhost:5000 and have fun!
