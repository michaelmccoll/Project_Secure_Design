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

CREATE TABLE triage (
    id SERIAL PRIMARY KEY,
    project_id INT REFERENCES projects(id) ON DELETE CASCADE,
    iam VARCHAR(25),
    infrastructure VARCHAR(25),
    supplier VARCHAR(25),
    privacy VARCHAR(25),
    confidentiality VARCHAR(25),
    integrity VARCHAR(25),
    availability VARCHAR(25),
    continuity VARCHAR(25),
    date VARCHAR(25)
);

CREATE TABLE risks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    description VARCHAR(100),
    owner VARCHAR(50),
    triage_id INT REFERENCES triage(id) ON DELETE CASCADE
);

CREATE TABLE controls (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    description VARCHAR(100),
    owner VARCHAR(50),
    risk_id INT REFERENCES risks(id) ON DELETE CASCADE
);

CREATE TABLE control_reviews (
    id SERIAL PRIMARY KEY,
    design VARCHAR(25),
    operating VARCHAR(25),
    rating VARCHAR(25),
    date VARCHAR(25),
    control_id INT REFERENCES controls(id) ON DELETE CASCADE
);

CREATE TABLE risk_reviews (
    id SERIAL PRIMARY KEY,
    inherrent_likelihood VARCHAR(25),
    inherrent_impact VARCHAR(25),
    residual_likelihood VARCHAR(25),
    residual_impact VARCHAR(25),
    date VARCHAR(25),
    risk_id INT REFERENCES risks(id) ON DELETE CASCADE
);