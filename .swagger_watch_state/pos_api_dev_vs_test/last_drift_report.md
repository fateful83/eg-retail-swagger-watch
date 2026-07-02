# DEV vs TEST drift detected: POS API

- Time: 2026-07-02T08:37:08Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `2883224dbbc909be878cd199e29ceeb7928ebfe708f92dc223e6e3340e2534f5`
- TEST hash: `d7c2bb8c7b7c4ca49603e4ad6c7255e20305f87955f45acf539f8e77e666f2e8`

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
