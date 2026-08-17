# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-17T18:18:38Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6b6a6db921ea2bc869e5a9d3d55fcdd0593f09d0df0b9903afc51602a1102157`
- PROD hash: `c7b82e22808021a652333c2b645961eee63be079e369244eed01205f8c2736d3`

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
