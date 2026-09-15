# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-15T01:58:08Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8667349ac5f90487cb8231fef7c5b514512cbf6eddf512bc3551c2a8ca83b371`
- PROD hash: `966163b0486662cf998b5af17059e064f97156f8e7a88f561841ace59558686f`

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
