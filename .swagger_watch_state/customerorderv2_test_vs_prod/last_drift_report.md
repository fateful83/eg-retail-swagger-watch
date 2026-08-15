# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-15T18:09:24Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a7103660ef79bb3d8871bcdccc1c71eab4c19771f9f9a82a70c1c4648ebd5ca7`
- PROD hash: `8433a7c68ca27381d0cba926ca96f3d0668c03cfd00028f81bb30126220c521b`

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
