# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-11T21:06:43Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `064f09f928c1c334d3ba7c9e6e45696a4427c64fc082a7b8765a0135b42528e9`
- PROD hash: `d7a5701c30f9487f33f68605b45423906a53866fa4a941c1f767b0eaacc89fa4`

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
