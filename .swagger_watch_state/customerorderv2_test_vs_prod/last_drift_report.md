# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-08T22:32:00Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c27b89c3015c504f579fee4f16a546301f14ae2cd54e59f47bf0d2e8e6c5b125`
- PROD hash: `1fa65f3fcf19aa3c2cdcbaf81b7306ac24df2f682bc693c9d9346a880ec32ef7`

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
