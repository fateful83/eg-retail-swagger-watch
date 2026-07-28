# TEST vs PROD drift detected: POS API

- Time: 2026-07-28T19:00:43Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7ddddf8c4cc50efec2a11b1203733dc65103ec6d5173d99acf2b7d77ca329590`
- PROD hash: `358a227c1fea4eeaf123ec504a7ea7b5c646bffc7b128e305cf680156cb3da85`

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
