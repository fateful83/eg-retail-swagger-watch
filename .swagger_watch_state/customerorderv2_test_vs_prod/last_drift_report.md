# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-29T08:12:22Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d2eff7fe0c8849077a0e0614128e7c3c15cf490718110add032e3cef0ee5bbfa`
- PROD hash: `eb3a140e80beb489688c996f5206534f08095b9208ebc5f01fe1cf877b5420cc`

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
