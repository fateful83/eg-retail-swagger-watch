# TEST vs PROD drift detected: POS API

- Time: 2026-07-08T08:02:03Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `10cf61562bd07832b6a9f3f7957132d5b5be74654672355bb2037614fa30301e`
- PROD hash: `5169790fe38e3d6fabd27178d8bbe05623427cb09d0ef024eab6d09a9209ed5c`

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
