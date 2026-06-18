# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-18T09:59:57Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `037a3f59cb879135e029307fa28ab3d9fa9f0e56c883292f5718bba51016102e`
- PROD hash: `9469633b5968bebd4b51475fb155bf8ae94b4c6524dd12186eb2ee178f77b4b5`

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
