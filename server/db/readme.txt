# INSTAL AND INIT OF POSTGRESQL-9.5
# install postgresql
sudo apt-get install postgresql-9.5

# init postegres console
sudo -u postgres psql

	# next steps in postgress console

	# create new user with password in postgres console 
	create user username with password 'password';

	# create database 
	create database example_db;

	# check if it is created
	\l

	# grant rights to chosen youser
	grant all privileges on database example_db to username;

	# exit postgres console
	\q

# start a postgress base 
psql -h localhost example_db username