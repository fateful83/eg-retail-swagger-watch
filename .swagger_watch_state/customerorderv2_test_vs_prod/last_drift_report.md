# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-17T14:29:42Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0b30cde38aed600e96e6eb502f650f32012e22a979f3a952a6868746f496a611`
- PROD hash: `6c0843e5077f3339f9e86b8c46be6234859918602c77d5388777ddec431bcdb9`

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
