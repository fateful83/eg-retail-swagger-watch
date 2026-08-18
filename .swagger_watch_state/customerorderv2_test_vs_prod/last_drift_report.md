# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-18T12:17:34Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0baa9f8b878dca1e9a75e9ba253a9bed7309c1a2d2205ea8ec0f55632c6530ca`
- PROD hash: `c45371bf2b53216bd657970d84206739d461eb61d7ee0477363fc61297b3950c`

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
