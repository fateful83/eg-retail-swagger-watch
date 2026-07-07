# TEST vs PROD drift detected: POS API

- Time: 2026-07-07T08:58:55Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8e3e35e08bdbdf6c8e5bcf191cf51a9d18a8a339d20dafdd04530a13a7ef85e1`
- PROD hash: `244c54afebdffb0df090af0bb90188d4e6092563db24c756b5620d6b00c28f25`

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
