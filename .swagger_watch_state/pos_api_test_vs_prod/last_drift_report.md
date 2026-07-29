# TEST vs PROD drift detected: POS API

- Time: 2026-07-29T08:12:39Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `200acbb80209eb7537f4b9bb08a77cff8814eaf6f60d0cf8e24e54713c0c65b3`
- PROD hash: `14037772ac9d022fe2bc8c8f4863d89d84679523a17953f4eec1fe3a7e701296`

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
