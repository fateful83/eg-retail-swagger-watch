# TEST vs PROD drift detected: POS API

- Time: 2026-07-13T19:07:08Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8c1182a894364d81fe411a3ffda8abf28d52aa1806942837196dd1e0230e0c35`
- PROD hash: `47c8affb9a2ae7cbcef7084fb5a9b0b75087eff027861c2a2f2b44db948beaa9`

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
