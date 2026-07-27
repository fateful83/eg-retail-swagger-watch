# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-27T01:24:32Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4096ed9aa23ad653000b190b05e47e82bcb398b7443d5ba11095c907a02c1f07`
- PROD hash: `61666fe924f913bcb773155949dc078f7343a48c9fbf19d5fed4f104dc446639`

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
