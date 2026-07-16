# TEST vs PROD drift detected: POS API

- Time: 2026-07-16T07:49:42Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `73d0a59ae1f4c4bdce08d0ec4f1cc9e179f6da7a35ad5d13bc5e63c3409405ab`
- PROD hash: `1bc1853dee8ec17d18502b84240b9ca9252ae3245b632befc31d37901336a77c`

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
