# DEV vs TEST drift detected: POS API

- Time: 2026-06-26T08:44:14Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `6db30bf2a94d1447b83ac541c6ffaa4278fb289dddecea1f59bbb9b3d498fdb2`
- TEST hash: `edf86fd316139ee67aab864633d879e76c1d8c5657952a87bcc7e7d9ca5ecce7`

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
