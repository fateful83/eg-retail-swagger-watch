# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-22T10:42:50Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e0179bcb1f2f07b9dd69637266f1d77912956bf0e0e7133abe623c48e33c837a`
- PROD hash: `674e4bead0333e17339a4474152c45bde9d7cb835335591f23f00e572ad80c0b`

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
