# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-12T02:03:56Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `34ab96d2cd4f6ab3e369cc087d608fc5bd99987780badfbc473ba452ae13bf6e`
- TEST hash: `02c1f1720b9564dcb184182d4f45efc9469b9f913895dace77334d3a108302db`

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
