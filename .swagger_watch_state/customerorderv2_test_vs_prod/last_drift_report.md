# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-25T15:58:58Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ed40b4fd7b2f92caf755eea6739cce54359bcb4a5f383e9291cf22152fb36138`
- PROD hash: `d6673f7b13be595b03cee0cf1725243cd9aa29df44841dd803902d6c0f82b025`

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
