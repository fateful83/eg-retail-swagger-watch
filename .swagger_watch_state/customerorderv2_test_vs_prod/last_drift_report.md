# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-30T17:02:33Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d3fdea0666f81b245bc4f5556eae4c9883fcc9af182225437b2dd231de3842d7`
- PROD hash: `9beed43f6f15dccac673f58978188f93b9810bd3a2aef6b263b81b3855e275b7`

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
