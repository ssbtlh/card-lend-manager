CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  phone TEXT,
  hashed_password TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE card_master (
  id SERIAL PRIMARY KEY,
  external_id TEXT, -- opcional (p.ex. id da API Pokémon TCG)
  name TEXT NOT NULL,
  set_code TEXT,
  rarity TEXT,
  image_url TEXT
);

CREATE TABLE user_collections (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  card_id INTEGER REFERENCES card_master(id),
  quantity INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE loans (
  id SERIAL PRIMARY KEY,
  owner_id INTEGER REFERENCES users(id),
  borrower_id INTEGER REFERENCES users(id),
  card_id INTEGER REFERENCES card_master(id),
  quantity INTEGER NOT NULL,
  start_date DATE NOT NULL DEFAULT CURRENT_DATE,
  due_date DATE,
  returned_date DATE,
  status TEXT NOT NULL DEFAULT 'active', -- active, returned, overdue, cancelled
  notes TEXT
);
