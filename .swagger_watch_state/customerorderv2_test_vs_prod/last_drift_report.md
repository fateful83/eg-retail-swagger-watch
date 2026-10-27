# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-27T16:54:46Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c23a4dee86c346457772ea415a7735de9eccb138cc4d5e27a60d6379a933bc03`
- PROD hash: `a59cdea63ddd1fc14db3b8292ea51654b95e5458b93c34aee8ba545cc76d1730`

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
