-- Setup Database for Airbnb_clone_v2
-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create user and passwd if they do not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
        IDENTIFIED BY "hbnb_dev_pwd";
-- Grant all privileges on new db to new user
GRANT ALL ON hbnb_dev_db.*
        TO 'hbnb_dev'@'localhost';
-- Grant select privilege on performance_schema
GRANT SELECT ON performance_schema.*
        TO 'hbnb_dev'@'localhost'
