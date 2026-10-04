# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-04T20:32:26Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5fa3d447c14f34c87b4359a8f07123f46d59b5d0d905eaddbfc575a683bf06ab`
- PROD hash: `48d376f1444c8302b7504f22740c7b0cbe180e985779f52155f9faf6697516b7`

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
