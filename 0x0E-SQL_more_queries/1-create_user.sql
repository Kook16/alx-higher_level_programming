-- If the user user_0d_1 already exists, your script should not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' INDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILIGES ON *.* TO 'user_0d_1'@'localhost';
