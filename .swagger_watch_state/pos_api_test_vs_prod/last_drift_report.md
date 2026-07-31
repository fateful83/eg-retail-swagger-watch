# TEST vs PROD drift detected: POS API

- Time: 2026-07-31T08:24:58Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `32e62e14e6ab8816813b2f0ceb318d0af00847e3bc2bf6cdaa0d53b05785d850`
- PROD hash: `e2a977928510a552d50648560aaad024283f46ca154f9a1debb1a35921cf0a2d`

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
