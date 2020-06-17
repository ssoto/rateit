# DB setting up

# sudo su - postgres

CREATE DATABASE django_admin_db;
CREATE USER django_admin_user WITH PASSWORD 'django_admin_password';
ALTER ROLE django_admin_user SET client_encoding TO 'utf8';
GRANT ALL PRIVILEGES ON DATABASE django_admin_db TO django_admin_user;
