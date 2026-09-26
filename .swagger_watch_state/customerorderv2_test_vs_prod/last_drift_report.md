# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-26T02:06:04Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e38699e7ee13a967aecc69b57c9779a07faf38c790a058123c6987bd420b4681`
- PROD hash: `6c84cc40d70ab727e164e26450f2e15baa7907bbeab39ca56317f4cd9d976c15`

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
