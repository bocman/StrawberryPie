----------------------------
|   @author Boštjan novak  |
----------------------------

-------------------------------------------------------------------------------
# StrawberryPie - Server side of the home automation system
-------------------------------------------------------------------------------

1. INSTALLATION PROCESS
     apt-get install apache2
     apt-get install mysql-server
     apt-get install libmysqlclient-dev

     # In root directory run this command to install packages
     sudo pip -r install requirements.txt

     # In root directory run this command to install all npm dependences
     npm install

-------------------------------------------------------------------------------

2.# In root directory run this command to install packages
     sudo pip -r install requirements.txt

  # Run this to get into mysql terminal
     mysql -u -p<mysql_username> -p<mysql_password>

  # Then execute this mysql command
     "Create database project;"

  # Exit mysql terminal and run this command in terminal
     python manage.py syncdb

  # When it ask you to create superuser, follow the steps
  # and fill it with your informations (you'll use it for login)

  # In root directory run
    bower install
-------------------------------------------------------------------------------

3. Open settings.py file (located in directory /project) 
   and set values for next variables

   DOMAIN_NAME - (Example http://malina.webhop.me, if you don't have domain, just set ip address)
   ALLOWED_HOSTS - Here type all the address which you use to access to application, type '*' if want
                   to allow all.
   DATABASES - Change configurations to your needings, like password, username, url ...
   EMAIL - Fill values for email variables, like host, password, username ... you can fill it with your gmail
           settings

-------------------------------------------------------------------------------
# CONGRATS YOU'RE DONE !