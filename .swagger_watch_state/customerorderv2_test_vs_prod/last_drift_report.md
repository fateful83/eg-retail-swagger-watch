# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-15T07:44:34Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `db6dcd6ed01e3e02265d730a88d2af4096491bfb3db58a2bf0c69d44be0e9afa`
- PROD hash: `4a47026a9acd47a092d78a7c017313a0179a50e51a5b41844fa1a0b16d6de373`

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
