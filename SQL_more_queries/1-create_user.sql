--creates the MySQL server user
CREATE USER 'user_0d_1'@'localhost' IF 'user_0d_1'@'localhost' NOT EXISTS IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
