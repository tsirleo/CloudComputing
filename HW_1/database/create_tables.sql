CREATE TABLE IF NOT EXISTS authors (
    author_id VARCHAR(36) PRIMARY KEY NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    birthplace VARCHAR(255),
    birthdate DATE
);

CREATE TABLE IF NOT EXISTS books (
    book_id VARCHAR(36) PRIMARY KEY NOT NULL,
    title VARCHAR(255) NOT NULL,
    publication_date DATE,
    publishing_house VARCHAR(255),
    author_id VARCHAR(36) NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);