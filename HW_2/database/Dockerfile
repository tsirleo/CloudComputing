FROM mysql:8.3.0
LABEL authors="tsirleo"

ADD create_tables.sql /docker-entrypoint-initdb.d

EXPOSE 3306