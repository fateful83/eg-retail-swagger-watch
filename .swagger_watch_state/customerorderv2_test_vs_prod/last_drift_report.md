# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-04T01:12:29Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7dd6637e480b4e8833dcc448b44a1bb441931525fff07e45e20078b71a3176e6`
- PROD hash: `2375346b635ab7413639adc0adeb5ceac22e17d726a09f5f2abdbc83816e2ef9`

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
