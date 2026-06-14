# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-14T08:57:14Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `be21bc9465ac5eb449ea32bef227bf0aa2e7631f9e61410fddeff389b4974109`
- PROD hash: `1256e8059e109e62a0f9b80f79f49af219ea2317a0659480222c9fc309935533`

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
