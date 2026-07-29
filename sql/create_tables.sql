DROP TABLE IF EXISTS jobs;

CREATE TABLE jobs (
    id BIGINT PRIMARY KEY,
    title TEXT NOT NULL,
    company_name TEXT,
    category TEXT,
    job_type TEXT,
    candidate_required_location TEXT,
    salary TEXT,
    publication_date TIMESTAMP,
    tags TEXT
);