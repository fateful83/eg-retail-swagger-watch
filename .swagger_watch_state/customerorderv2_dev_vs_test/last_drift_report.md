# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-11T15:24:55Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `07bd37985e71b8519cfaacab09cf65c62c5867c755beba9b3e9fd561621c2da8`
- TEST hash: `af1b4290e15af851d0f7b0e619307fa156df4f59b35611d57e24580c0965e715`

## Summary
- Only in DEV: 1
- Only in TEST: 0
- Present in both but different: 1

## Only in DEV
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Only in TEST
- None

## Different in DEV and TEST
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
