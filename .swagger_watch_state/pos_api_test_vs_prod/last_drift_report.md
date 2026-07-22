# TEST vs PROD drift detected: POS API

- Time: 2026-07-22T08:02:30Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7013a2b7a03b1ab374fdb44ac2bb05cfee1269338836eca54ea9ef890dc5cc70`
- PROD hash: `c30f23202ed32c0d2d460c96d7213fef1ef7e11676013631a42696ec6b7c099f`

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
