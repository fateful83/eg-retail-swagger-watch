# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-25T01:17:14Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6bd9fba74fbdb0c3f3f8dfbe6323663cc79f7c6489314c313451dd09c7c1fcfb`
- PROD hash: `04a2802ef4d6c4da14c9814516d89213bd171aea35fca0e48251dc5b706a97c1`

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
