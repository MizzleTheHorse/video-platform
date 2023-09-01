# video-platform


Flexible Software Architectures via Microservices and Containerization

Bachelor Project SDU 2023

Description: 

TODO: add descr


how to run whole system: 

turn off all nginx and mysql services 

> sudo service mysql stop
> 
> sudo service nginx stop 

Build all docker containers before running compose (docker-compose file can't build from path)

> docker-compose up --scale frontend=3
