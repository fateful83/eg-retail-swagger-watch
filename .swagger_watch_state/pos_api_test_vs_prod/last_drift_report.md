# TEST vs PROD drift detected: POS API

- Time: 2026-08-11T12:33:46Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `01faa20c96e751fe2dd3e7d3a056e124aad7afe79c4f4d47f9241cdfa321efc9`
- PROD hash: `99d5393321591aba7085ca02f604f480d381639ffddbf6f17395b2cd66759c6a`

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
