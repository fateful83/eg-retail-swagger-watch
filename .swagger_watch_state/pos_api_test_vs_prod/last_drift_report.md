# TEST vs PROD drift detected: POS API

- Time: 2026-07-21T01:14:37Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `bb82d77943134acc63044a0c4650e1ca991877dca7733250938eba1cefae1334`
- PROD hash: `e80ba41fbcf4ea7bccbdc6848dcf805fb51bd7776f742a6d5b55f777411c6c03`

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
