# TEST vs PROD drift detected: POS API

- Time: 2026-07-25T07:46:15Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e9f1ba76778a715bdb73e02ac4b149ebe8c38073f9fbece00462dbe5e628ac1f`
- PROD hash: `990887145cb0153f4fd22adad12c0b73e6c54ecef05a2b25cbd77760258e7637`

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
