# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-29T02:58:46Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e718cc310432e95274715fab456f47dd85c6024b0afdbc3da271989f523298a5`
- PROD hash: `f789af6320dc255ffe59b2776a94ac2b75bb59c04378f8af12e90b448d85a652`

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
