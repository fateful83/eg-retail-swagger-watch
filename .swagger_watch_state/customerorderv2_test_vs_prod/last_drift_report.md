# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-21T01:47:30Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ddd321f14983e5c37f36d21d15c24cf22686d3490941c7c589b7efd9e735bc78`
- PROD hash: `fb6bcf08761820aa9896b9c92c51f9d1d79986d97b0d5e080cd5768023aad440`

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
