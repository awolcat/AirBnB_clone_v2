-- Setup TEST Database for Airbnb_clone_v2
-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create user and passwd if they do not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
        IDENTIFIED BY "hbnb_test_pwd";
-- Grant all privileges on new db to new user
GRANT ALL ON hbnb_test_db.*
        TO 'hbnb_test'@'localhost';
-- Grant select privilege on performance_schema
GRANT SELECT ON performance_schema.*
        TO 'hbnb_test'@'localhost'
