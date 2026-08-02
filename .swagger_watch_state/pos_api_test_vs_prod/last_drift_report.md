# TEST vs PROD drift detected: POS API

- Time: 2026-08-02T12:49:45Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `592d777dff311a467f2fd664248ecadb84a22588e085f95cec558946d5c0ff87`
- PROD hash: `c3a97c6fd9579d5f69567973da4020d816590b58eaddcc0fa6f0f9c31ed6ed64`

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
