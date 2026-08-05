# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-05T08:10:34Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6a2097e525499a5e3c40ff5752b5d66b7305a3b113044d012b7138ae3bc53baa`
- PROD hash: `dad1b56ec3528dc04a252d1e90e1e709c108ea401676908daaa71271257f0808`

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
