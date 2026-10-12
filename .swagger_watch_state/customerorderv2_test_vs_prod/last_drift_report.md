# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-12T02:43:55Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e1bf3ef16a638d48e82c83ac046443077975d2c8abc34df5a571b5a106d99f68`
- PROD hash: `1a0b0cebdea4f9af43546f51d7db91318ea394e59ac6ff752bec3c889a92a153`

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
