# Identity Reconciliation 

- Web API for identity reconciliation in customer database. Customer's often use mutiple accounts for placing orders on a single web service. The API detect's and maintain's customer data, and reconciles such profiles. 

## Tech Stack: 
- Python3
- Flask
- PostgreSQL
- Docker

# Build and run service:
- Build image: `docker compose build`
- create volume: `docker volume create identity_reconcil_psql`
- Local run: `docker compose --env-file local.env up`
- Prod run: `docker compose --env-file prod.env up`

# Environment variables
Define the following variables:
- `POSTGRES_HOST` (postgres)
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_PORT` (5432)
- `POSTGRES_DB` (customer_data)
- `PYTHONUNBUFFERED` ("")
