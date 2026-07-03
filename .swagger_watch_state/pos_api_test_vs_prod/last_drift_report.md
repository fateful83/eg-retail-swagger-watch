# TEST vs PROD drift detected: POS API

- Time: 2026-07-03T01:24:26Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b4c5a62d079a89ca3149784d3c015c9e495c189895b641edc22cbe1362931d4b`
- PROD hash: `ebfc355160ffb16181122f1fd88194f160d40b2b9ecf5b892f7684f1d1b17287`

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
