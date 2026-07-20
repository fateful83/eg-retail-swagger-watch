# TEST vs PROD drift detected: POS API

- Time: 2026-07-20T19:19:16Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `bb82d77943134acc63044a0c4650e1ca991877dca7733250938eba1cefae1334`
- PROD hash: `0e7c1cac988f11efa1a7b0129e74e4c8a9fdec78d8842532c11627f4501ea6f3`

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
