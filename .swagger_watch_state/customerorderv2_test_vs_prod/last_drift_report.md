# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-13T12:59:58Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4a7fd4a2653409fe2404475ce5cdd5088defb4d8bd8a4e0bcf130b6e4ba9d2a3`
- PROD hash: `fe2bfb30edc316b05476e55d70b9a22d02616aef944b382092b6d62adbc0b532`

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
