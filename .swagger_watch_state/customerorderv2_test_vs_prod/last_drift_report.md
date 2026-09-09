# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-09T20:05:27Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e394c2b1fca43184f788873de59508daf69a04fd6128a537d4d9c98740af10e8`
- PROD hash: `133bec209a228b4b5419e7204f4e6a5bc7413c04ee4bee2ccde924225f81fd0e`

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
