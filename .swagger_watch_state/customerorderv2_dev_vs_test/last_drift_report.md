# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-08T15:19:22Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `474c7e0fe3a6a7cffab12ade18f1c97f1068796cb8c5a4d7e26f42a1c91aef47`
- TEST hash: `923d68bf04dbb5687878d310565bf543fa38703072c2fcf9eb1ea3155bb31c19`

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
