# Kite Stoploss Order Service

A minimal FastAPI service for initiating Kite Connect login and exchanging the Kite request token for an access token.

## Endpoints

- `GET /health` — health check
- `GET /auth` — returns the Kite login URL to start the login flow
- `GET /callback` — callback endpoint for Kite Connect to exchange the `request_token` for `access_token`

## Setup

1. `.env` is already included for testing. Update it with your Kite credentials.
2. Fill `KITE_API_KEY`, `KITE_API_SECRET`, and `KITE_REDIRECT_URL`
3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Run locally:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

## Render deployment

Create a `Procfile` with:

```text
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Use Render environment variables to set `KITE_API_KEY`, `KITE_API_SECRET`, `KITE_REDIRECT_URL`, and optionally `KITE_BASE_URL`.
