# TEST vs PROD drift detected: POS API

- Time: 2026-07-24T19:06:58Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3f08c36798dbcfb16fc99d923520b0c458af5846e30e0b2c36fc287e9b04bf0f`
- PROD hash: `1b87372f4f2bce124273862cfa24aa85c35a6a24bc1aff1860d4f8a9c1bf2f00`

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
