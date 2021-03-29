DROP TABLE IF EXISTS risk_assessments;
DROP TABLE IF EXISTS risks;
DROP TABLE IF EXISTS control_assessments;
DROP TABLE IF EXISTS controls;
DROP TABLE IF EXISTS triages;
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

CREATE TABLE traiges (
    id SERIAL PRIMARY KEY,
    project_id INT REFERENCES projects(id) ON DELETE CASCADE,
    question VARCHAR(100),
    category VARCHAR(25)
);

CREATE TABLE controls (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    description VARCHAR(100),
    category VARCHAR(25),
    owner VARCHAR(50)
);

CREATE TABLE control_assessments (
    id SERIAL PRIMARY KEY,
    control_id INT REFERENCES controls(id) ON DELETE CASCADE,
    design VARCHAR(25),
    operating VARCHAR(25),
    rating VARCHAR(25)
);

CREATE TABLE risks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    description VARCHAR(100),
    category VARCHAR(25),
    owner VARCHAR(50),
    control_id INT REFERENCES controls(id) ON DELETE CASCADE
);

CREATE TABLE risk_assessments (
    id SERIAL PRIMARY KEY,
    risk_id INT REFERENCES risks(id) ON DELETE CASCADE,
    inherrent_likelihood VARCHAR(25),
    inherrent_impact VARCHAR(25),
    residual_likelihood VARCHAR(25),
    residual_impact VARCHAR(25)
);


