# DEV vs TEST drift detected: POS API

- Time: 2026-07-01T09:23:18Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `d291b5e2e94ca1a58dbf6a0793f9abb8e8ad3137c112b1dc61c525716a205506`
- TEST hash: `9bc99f1c7ffc24a7be40269c6a471c3c270da63e0966093a9bc81b447dd89554`

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
