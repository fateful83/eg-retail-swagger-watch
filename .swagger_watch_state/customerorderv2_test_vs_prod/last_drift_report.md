# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-02T16:52:08Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c3d83fcf552600aff6e46dcb66e189f2cdc4ff37d59a509e82bd5a4fd24e0a41`
- PROD hash: `36e1a52963d16c123de997a78147b21c9c5ac3f56a11bd41f1ea74e5f17951d4`

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
