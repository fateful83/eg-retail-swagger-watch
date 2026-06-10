# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-10T20:01:58Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `93eeca294f61b63a12539cd29cc208e491a212450bfa67c0a6d282a2eed92a0f`
- TEST hash: `909e456ccda48afd7830763e6fd3105a5be6dd63e3d85008a8d941321df24492`

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
