# TEST vs PROD drift detected: POS API

- Time: 2026-06-27T18:58:12Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `66488837ca1945d68b1a1648d7c0a54c40a46b4a3a4e0d797a640aa03b37800e`
- PROD hash: `523b0c0c8fc8e379a5f6d891a1d75269d2ed1360aec9ff45c91d2b9e2eff33f9`

## Summary
- Only in TEST: 0
- Only in PROD: 7
- Present in both but different: 0

## Only in TEST
- None

## Only in PROD
- POST /api/Order/queue/Basic
- POST /api/Order/queue/Complete
- POST /api/Order/queue/Delivery
- POST /api/Order/queue/ItemTransaction
- POST /api/Order/queue/OrderPayments
- POST /api/Order/queue/Payment
- POST /api/Order/queue/Sale

## Different in TEST and PROD
- None
