
![image](https://user-images.githubusercontent.com/101609196/167264725-3c9e426e-0c39-4913-9821-2c7af233c0c9.png)
![image](https://user-images.githubusercontent.com/101609196/167264732-d254024c-690b-485c-a79f-eba0616757ef.png)
![image](https://user-images.githubusercontent.com/101609196/167264745-0967d6c0-7437-4416-b9cf-e3fdd4aaa416.png)

Below is the resulting page when the docker-compose project is running:
![image](https://user-images.githubusercontent.com/101609196/167264798-9511a6c0-1e8a-4fab-b41f-f7e68508b7df.png)

To run the project successfully, you need to create 2 files to be used as secret
1) root_secret.txt   <- use this to store the root password for your mysql instance
2) hw4_secret.txt    <- use this to store the hw4app user password for your mysql instance

Also, review docker-compose.yml file to change any configuration as you see fit.
To build the project, use the below command:
>docker-compose build

To start the project, use the below command:
>docker-compose up -d
