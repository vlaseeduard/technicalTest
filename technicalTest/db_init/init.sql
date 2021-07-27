CREATE DATABASE technical_test_db;
CREATE USER technical_test_user WITH ENCRYPTED PASSWORD 'technical_test_pass';
GRANT ALL PRIVILEGES ON DATABASE technical_test_user to technical_test_user;