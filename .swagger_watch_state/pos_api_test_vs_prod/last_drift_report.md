# TEST vs PROD drift detected: POS API

- Time: 2026-07-10T13:47:24Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8b7b145e5e8fc161d352d734c31df8e16b2c3a0ea5836b7dac5557d176102510`
- PROD hash: `fac12ee8789554ec3db3b3d8894c7e55ea03ee7cbbd463d26285b5f6e618020e`

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
