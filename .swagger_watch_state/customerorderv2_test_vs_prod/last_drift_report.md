# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-19T10:06:27Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `961b8addddb6ecdfd73ea4307d4124a382a32697cf52fe50886a19edca674c16`
- PROD hash: `cc24986f8e966b659d3e6e48642f419b91245ac13adf5d4cb8bcff8408eac4de`

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
