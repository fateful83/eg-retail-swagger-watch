# TEST vs PROD drift detected: POS API

- Time: 2026-07-26T08:01:28Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c0d7d27767d8cf5a44e5f3df078cf715715f7102866b31401b3f7aa642faef4f`
- PROD hash: `6aea8358382d264c54de03ef6fc86e2b24419af32226130e6e4c8070e21bacf3`

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
