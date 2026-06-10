# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-10T01:56:53Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `30a9fd38fa0fdbc3253bff0ebb62e418a6ae9cc448e3fcbd7fa0f67317596e49`
- TEST hash: `b6e6756f4258654b256813508e0c1ddcfeeaabf195a612912c5ed8dc912fb490`

## Summary
- Only in DEV: 1
- Only in TEST: 0
- Present in both but different: 1

## Only in DEV
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Only in TEST
- None

## Different in DEV and TEST
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
