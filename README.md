# Identity Reconciliation 

## Web API for identity reconciliation in customer database

## Tech Stack: 
- Node JS
- Express JS

# PSQL commands:
```sql
- psql -U postgres
- \c customer_data
```

# Build and run service:
- create volume: `docker volume create iden_reco_volume`
- Build image: `docker compose build`
- Local run: `docker compose --env-file local.env up`
