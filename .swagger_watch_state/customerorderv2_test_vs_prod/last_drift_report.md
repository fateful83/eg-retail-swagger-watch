# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-12T09:49:21Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8c6e9e352a53591f332fd7e4b0fb004ed12743073b7adbc1e84237e0061ed67e`
- PROD hash: `4b1bd93308a10f756eccd50b06e99240ef317c692ff1fb683fb5ad0391cfdd4c`

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
