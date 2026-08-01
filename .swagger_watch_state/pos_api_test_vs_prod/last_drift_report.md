# TEST vs PROD drift detected: POS API

- Time: 2026-08-01T01:23:57Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `faa8bd6f012eead78d4c0046a97a79f2c2ea39c5ad310d322b28c1a91adcf9a1`
- PROD hash: `451d76b9443f91c52fc80ebb981fe6adffda961bd5a2d0a5e2f7495c83cfd4e0`

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
