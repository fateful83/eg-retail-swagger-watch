# DEV vs TEST drift detected: POS API

- Time: 2026-06-26T19:24:46Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `c426474a1d8430111fd507f003f7a9f91e44fc4cd5c7ff83cd1e39a535957909`
- TEST hash: `f96b5a3bdb78255c6aef9e6e056ee07ca5328864122da8b43050ac6d61f10894`

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
