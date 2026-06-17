# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-17T14:42:31Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `89b42ae23b5e65705ed3800afb4ebd64a321c088a705958047e1d1fa5db54959`
- PROD hash: `869b6e3fcb154896180e3b90aca07835cadcab442f84246ec5e6053f4d361a8a`

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
