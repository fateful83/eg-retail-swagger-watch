# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-08T10:08:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5157221dcf366763d01211d3b66c711d44244d998db414b5498436b6f36ff376`
- PROD hash: `65c7c9eaaa74e1ecdc28f204be5d56bb621522237e79117d5523e86694fde712`

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
