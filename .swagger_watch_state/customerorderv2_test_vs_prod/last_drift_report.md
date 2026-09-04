# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-04T19:56:35Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `49c633e803d9b1e32642529df00fe38a852fb073a22025a1e6db9d1cab91a4ff`
- PROD hash: `361d49bc8986234ba6787fca41916077d0caa4921f05f070a1153e12b125eeb4`

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
