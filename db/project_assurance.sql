DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS risks;
DROP TABLE IF EXISTS controls;
DROP TABLE IF EXISTS triage;
DROP TABLE IF EXISTS risk_reviews;
DROP TABLE IF EXISTS control_reviews;
DROP TABLE IF EXISTS projects;

CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    sponsor VARCHAR(50),
    project_manager VARCHAR(50),
    start_date VARCHAR(25),
    end_date VARCHAR(25),
    status VARCHAR(25)
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category VARCHAR(25)
);

CREATE TABLE traige (
    id SERIAL PRIMARY KEY,
    question VARCHAR(100)
);

CREATE TABLE risks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    description VARCHAR(100),
    owner VARCHAR(50)
);

CREATE TABLE controls (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    description VARCHAR(100),
    owner VARCHAR(50)
);

CREATE TABLE control_reviews (
    id SERIAL PRIMARY KEY,
    design VARCHAR(25),
    operating VARCHAR(25),
    rating VARCHAR(25),
    control_review_date VARCHAR(25)
);

CREATE TABLE risk_reviews (
    id SERIAL PRIMARY KEY,
    inherrent_likelihood VARCHAR(25),
    inherrent_impact VARCHAR(25),
    residual_likelihood VARCHAR(25),
    residual_impact VARCHAR(25),
    risk_review_date VARCHAR(25)
);