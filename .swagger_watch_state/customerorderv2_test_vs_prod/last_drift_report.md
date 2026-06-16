# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-16T02:14:27Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `cb2d08e97b164e58bd66c85f832d070dd9457f8158c6075b8ebc153ababfb647`
- PROD hash: `1ca02d1e769ef02e3d8d122a19d1f9067ea3fcea2d001faf5d82fee61963c8e9`

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
