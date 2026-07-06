# DEV vs TEST drift detected: POS API

- Time: 2026-07-06T09:47:12Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `9ae6c2fe8eba1bde793fe1843048645e5b085ce14b9a0e671298796847df993a`
- TEST hash: `c75edb95cf9902c70c96f00d6a94f0ee0e044ff1ac49af57eb053751f3ebe285`

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
