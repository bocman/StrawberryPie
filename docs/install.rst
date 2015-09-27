@author 
Boštjan novak

# StrawberryPie - Server side of the home automation system

1. INSTALLATION PROCESS
     apt-get install apache2
     apt-get install mysql-server
     apt-get install libmysqlclient-dev

2. In root directory run this command to install packages
     sudo pip -r install requirements.txt

     # Run this to get into mysql terminal
     mysql -u -p<mysql_username> -p<mysql_password>

     # Then execute this mysql command
     "Create database project;"

     # Exit mysql terminal and run this command in terminal
     python manage.py syncdb

     # When it ask you to create superuser, follow the steps
     # and fill it with your informations


# CONGRATS YOU'RE DONE !