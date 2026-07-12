# DEV vs TEST drift detected: POS API

- Time: 2026-07-12T07:52:06Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `058ec8d7150b9052c78f650e6138922995a6ff49727d11b2c5e7be355e2afd69`
- TEST hash: `06d3de083cdb9dc8b5591a3897d3156cc25d4b9ed95d9432151f0b1ef6a514bd`

## Summary
- Only in DEV: 7
- Only in TEST: 0
- Present in both but different: 0

## Only in DEV
- POST /api/Order/queue/Basic
- POST /api/Order/queue/Complete
- POST /api/Order/queue/Delivery
- POST /api/Order/queue/ItemTransaction
- POST /api/Order/queue/OrderPayments
- POST /api/Order/queue/Payment
- POST /api/Order/queue/Sale

## Only in TEST
- None

## Different in DEV and TEST
- None
