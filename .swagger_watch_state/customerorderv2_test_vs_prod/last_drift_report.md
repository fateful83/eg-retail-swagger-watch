# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-25T08:42:32Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2415636551e9c19fc85516020f8506fd8ba4dd138210f9216674471cbf503156`
- PROD hash: `98bcedc239707e0589a52a88035d8bdcd9df291dea60a5f1a34e8d60e6688131`

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
