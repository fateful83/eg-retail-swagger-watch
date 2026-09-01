# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-01T02:08:35Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9996aca953605bab9e3ef0a58f126558d736fe8ee0885a463f02a104e42b95d6`
- PROD hash: `ed58e90546bd279d3fd6b3033131dd3ffd335e1ce71d4774ff559e6b0bb0a0e8`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 1

## Only in TEST
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Only in PROD
- None

## Different in TEST and PROD
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
