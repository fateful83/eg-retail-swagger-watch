# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-13T18:42:48Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7504bb3ffb1cb7a121f91470219c8acd8add4472bce904dd2b6908264e41b258`
- PROD hash: `193b0959b7e0e6a91c19ba0697fcf62bebb90453b53945090b046829e622859c`

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
