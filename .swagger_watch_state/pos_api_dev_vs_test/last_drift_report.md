# DEV vs TEST drift detected: POS API

- Time: 2026-07-12T01:16:32Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `fbaae9840127df72659d2b1453cd2f005e8550a49d4e6a895c63b7c6d8094b53`
- TEST hash: `a99e92bbd51a24a8610569f68f016483663e5e1cdb14db5f61d9f98457b6e0f1`

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
