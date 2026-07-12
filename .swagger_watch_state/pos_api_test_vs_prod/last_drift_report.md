# TEST vs PROD drift detected: POS API

- Time: 2026-07-12T01:16:32Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a99e92bbd51a24a8610569f68f016483663e5e1cdb14db5f61d9f98457b6e0f1`
- PROD hash: `f2c75ba530dc479d6e2ee1feb37ed7b47ae9637a3d72f471ce7c1d2c18cdc94f`

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
