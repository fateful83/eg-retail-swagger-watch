# TEST vs PROD drift detected: POS API

- Time: 2026-08-12T00:46:45Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `01faa20c96e751fe2dd3e7d3a056e124aad7afe79c4f4d47f9241cdfa321efc9`
- PROD hash: `28d21be4b340be36bd8ae8868c37ad2d2a41488adf728dd5054da3420ea1531e`

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
