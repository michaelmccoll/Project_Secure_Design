DROP TABLE IF EXISTS assignments;
DROP TABLE IF EXISTS consultants;
DROP TABLE IF EXISTS clients;

CREATE TABLE consultants (
  id SERIAL PRIMARY KEY,
  consultant_name VARCHAR(255),
  role VARCHAR(255),
  summary VARCHAR(255),
  day_rate INT
);

CREATE TABLE clients (
  id SERIAL PRIMARY KEY,
  client_name VARCHAR(255),
  type_of_business VARCHAR(255),
  consultants_hired VARCHAR(255)
);

CREATE TABLE assignments (
  id SERIAL PRIMARY KEY,
  consultant_id INT REFERENCES consultants(id) ON DELETE CASCADE,
  client_id INT REFERENCES clients(id) ON DELETE CASCADE,
  days_required INT
);