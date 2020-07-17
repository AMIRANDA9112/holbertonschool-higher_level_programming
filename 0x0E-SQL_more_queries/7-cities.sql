-- Create database
-- Create table using primary key with not null condition and foreign key
CREATE DATABASE IF NOT exists hbtn_0d_usa;
CREATE TABLE IF NOT exists hbtn_0d_usa.cities (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id));
