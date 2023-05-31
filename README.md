# video-platform

how to run whole system: 

turn off all nginx and mysql services 

> sudo service mysql stop
> sudo service nginx stop 

Build all docker containers

> docker-compose up --scale frontend=3
