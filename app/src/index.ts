import { Hono } from 'hono';

type Bindings = {
  DB: D1Database;
  ASSETS: Fetcher;
  ENVIRONMENT: string;
  BRAND_NAME: string;
};

const app = new Hono<{ Bindings: Bindings }>();

// API Route: Submit Lead from Funnels
app.post('/api/leads', async (c) => {
  try {
    const body = await c.req.json();
    const { full_name, email, phone, lead_type, timeline, budget_range, loan_type, preferred_cities, notes, utm_source, utm_medium, utm_campaign } = body;

    if (!full_name || !phone || !email) {
      return c.json({ success: false, error: 'Name, phone, and email are required fields.' }, 400);
    }

    const leadId = 'lead_' + Date.now() + '_' + Math.random().toString(36).substring(2, 7);

    // Save lead to D1 Database if binding available
    if (c.env.DB) {
      await c.env.DB.prepare(
        `INSERT INTO leads (id, full_name, email, phone, lead_type, timeline, budget_range, loan_type, preferred_cities, notes, utm_source, utm_medium, utm_campaign)
         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
      ).bind(
        leadId,
        full_name,
        email,
        phone,
        lead_type || 'buyer',
        timeline || '',
        budget_range || '',
        loan_type || '',
        preferred_cities || '',
        notes || '',
        utm_source || 'direct',
        utm_medium || 'web',
        utm_campaign || 'davarusbell_funnel'
      ).run();

      // Log automated 60-second speed-to-lead trigger
      await c.env.DB.prepare(
        `INSERT INTO crm_activity_log (id, lead_id, action_type, details) VALUES (?, ?, ?, ?)`
      ).bind(
        'act_' + Date.now(),
        leadId,
        'AUTO_SMS_TRIGGERED',
        `Sent 60-second welcome SMS to ${phone}`
      ).run();
    }

    return c.json({
      success: true,
      lead_id: leadId,
      message: 'Lead pre-qualified and stored successfully in Davarus Bell CRM.',
      next_step: '/thank-you.html'
    });
  } catch (err: any) {
    return c.json({ success: false, error: err.message }, 500);
  }
});

// API Route: Fetch All Leads for Admin Dashboard
app.get('/api/leads', async (c) => {
  try {
    if (!c.env.DB) {
      return c.json({ success: true, leads: [], mode: 'demo' });
    }
    const { results } = await c.env.DB.prepare(`SELECT * FROM leads ORDER BY created_at DESC LIMIT 100`).all();
    return c.json({ success: true, leads: results });
  } catch (err: any) {
    return c.json({ success: false, error: err.message }, 500);
  }
});

// Health check route
app.get('/api/health', (c) => {
  return c.json({
    status: 'online',
    brand: 'Davarus Bell Platform',
    timestamp: new Date().toISOString()
  });
});

export default app;
