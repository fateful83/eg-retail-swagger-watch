# TEST vs PROD drift detected: POS API

- Time: 2026-07-11T18:39:44Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d55fa3dd1663ce19623e75dd5e3f44ec168e67741d954f347ee0d75a8278ef54`
- PROD hash: `f4edff3d674c9f29b20a9e42916248887fd56801f28a563b468c4cd6899d4047`

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
