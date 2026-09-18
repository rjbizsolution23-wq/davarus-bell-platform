-- D1 Database Schema for Davarus Bell Brand OS & Lead CRM

CREATE TABLE IF NOT EXISTS leads (
    id TEXT PRIMARY KEY,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    lead_type TEXT NOT NULL, -- buyer, seller, relocation, investor, speaking
    timeline TEXT,
    budget_range TEXT,
    loan_type TEXT, -- FHA, VA, ITIN, Conventional, Cash
    preferred_cities TEXT,
    notes TEXT,
    source TEXT DEFAULT 'davarusbell.com',
    utm_source TEXT,
    utm_medium TEXT,
    utm_campaign TEXT,
    status TEXT DEFAULT 'NEW_LEAD',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS appointments (
    id TEXT PRIMARY KEY,
    lead_id TEXT NOT NULL,
    appointment_type TEXT NOT NULL,
    scheduled_time TIMESTAMP NOT NULL,
    status TEXT DEFAULT 'SCHEDULED',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(lead_id) REFERENCES leads(id)
);

CREATE TABLE IF NOT EXISTS crm_activity_log (
    id TEXT PRIMARY KEY,
    lead_id TEXT NOT NULL,
    action_type TEXT NOT NULL, -- SMS_SENT, EMAIL_SENT, STATUS_CHANGE, NOTE_ADDED
    details TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(lead_id) REFERENCES leads(id)
);

CREATE INDEX IF NOT EXISTS idx_leads_phone ON leads(phone);
CREATE INDEX IF NOT EXISTS idx_leads_email ON leads(email);
CREATE INDEX IF NOT EXISTS idx_leads_type ON leads(lead_type);
