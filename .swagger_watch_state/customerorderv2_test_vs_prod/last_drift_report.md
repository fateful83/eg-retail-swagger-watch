# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-16T20:09:22Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e4dedb20c390195a77217c868e3dd04108ed8a250896e2683bdc8fc033a33656`
- PROD hash: `9202121c4760405fe2c929490708a232b74c8872fe858d3992c08b55ec943dbb`

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
