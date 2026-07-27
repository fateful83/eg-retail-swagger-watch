# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-27T09:00:09Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `64aa8c947626c1f23a8254b8673bae2e18b010ed22a0c22c03a57f56a5815206`
- PROD hash: `eaeecb35e09744239ff5760ad647201a4f8a63a7e5e23026f2909f08f9e4ec1e`

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
