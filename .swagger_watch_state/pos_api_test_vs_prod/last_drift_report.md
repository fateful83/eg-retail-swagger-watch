# TEST vs PROD drift detected: POS API

- Time: 2026-08-10T00:41:51Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0c77d0d877bd6a691c6a4e57c25b7773f27e5a32752b2425de291f7e7bd887bf`
- PROD hash: `5fb99c10ec8c773595eaf4bccfe4545925d3ce9e5a841d5a6e992e032042ff22`

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
