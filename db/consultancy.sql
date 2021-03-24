DROP TABLE IF EXISTS assignments;
DROP TABLE IF EXISTS consultants;
DROP TABLE IF EXISTS clients;

CREATE TABLE consultants (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  role VARCHAR(255),
  summary TEXT,
  day_rate INT
);

CREATE TABLE clients (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  type_of_business VARCHAR(255),
  contact_details VARCHAR(255)
);

CREATE TABLE assignments (
  id SERIAL PRIMARY KEY,
  description TEXT,
  consultant_id INT REFERENCES consultants(id) ON DELETE CASCADE,
  client_id INT REFERENCES clients(id) ON DELETE CASCADE,
  days_required INT,
  start_date VARCHAR(255),
  end_date VARCHAR(255),
  total_cost INT
);