# TEST vs PROD drift detected: POS API

- Time: 2026-08-07T01:54:59Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f7868d3afd242e71a34c7210cc385207fe4b27993002d7488aacbb6f28d638fe`
- PROD hash: `ef09ffdc544f9b7f2e87e1679727842812005a15b80e06ed27f5c6b1a8718351`

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
