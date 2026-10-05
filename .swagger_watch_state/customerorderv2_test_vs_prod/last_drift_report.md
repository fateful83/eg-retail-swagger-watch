# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-05T02:29:35Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `70dd6e3481673cd52276b2a2b82ccd86d6df08a6ff8a3321dc204ee207237fca`
- PROD hash: `e50c2486b487c6e05333672b3dc1533a20fa7323539cf8f73794623fdc48a9ce`

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
