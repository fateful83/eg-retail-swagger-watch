# TEST vs PROD drift detected: POS API

- Time: 2026-07-23T01:20:44Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e9acabfb882527cbc577e6fdf879365076eb9c9476bdc2579577fd8c96a82cb5`
- PROD hash: `f54bc2cdab50b2bbce7bd1e4d4fab106dc516877dc829008e69149439dec5a2b`

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
