# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-03T18:55:46Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `63d8d36b5a165eadc858ae47202a47e40fc8ab3d179cef3fe66af02a19b14fad`
- PROD hash: `93cb2f6b0debd551e5dc6e57d9e65bfa4f37ab0760824bcf8e8446882b8cbfc1`

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
