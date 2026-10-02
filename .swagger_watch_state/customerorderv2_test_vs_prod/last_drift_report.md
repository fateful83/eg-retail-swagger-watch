# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-02T02:39:07Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `175fd61885ccac18611897dc8fe5fb7f82be1d29158b993fb154649624f0bb12`
- PROD hash: `bbb088e5938725df53daebf860e80a3b2ddc2f89517967c871b512e13eb49a0e`

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
