# DEV vs TEST drift detected: POS API

- Time: 2026-07-03T01:24:26Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `791fcc627824cbe65cd74dde9730d6a1b6962bbddfea538dd9694c29b64add8c`
- TEST hash: `b4c5a62d079a89ca3149784d3c015c9e495c189895b641edc22cbe1362931d4b`

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
