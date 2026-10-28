# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-28T02:39:38Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `312eb4f999f69ef43d1e4a8d5e0d656222a479c30bc43c842fba046e1a95f249`
- PROD hash: `7acd96d1044080245b04376a9efd688a03410bdac9872363bf6bbcbfd77182c9`

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
