# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-30T13:19:00Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e1f108bdef705048441a110467f4cb6e45aa8cf563220c78e57cb3056380afbd`
- PROD hash: `6dd6cfc701a5fce4989ac5d7a3bae571f817072f97b62fc11340db0f8202ccb7`

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
