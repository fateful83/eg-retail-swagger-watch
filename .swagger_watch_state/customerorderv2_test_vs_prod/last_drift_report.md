# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-25T01:53:06Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f8c414eaf7bb5f1fd515cb10695c6d040528de7e47dd879855040ac9497fb3f4`
- PROD hash: `880755cf83e465e1be57bbc2f0e37388740c6da9a647812a6e07db551fe0d50c`

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
