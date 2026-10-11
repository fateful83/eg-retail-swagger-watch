# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-11T16:49:55Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `16dcec3f5fdec752b84d913dcec6039aa7269066a57d78edb521cddacf131d1f`
- PROD hash: `74433462ff7fe016f0b4b51ee45e9feeac31afcbc8c5c429e8d93dffa95bafc4`

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
