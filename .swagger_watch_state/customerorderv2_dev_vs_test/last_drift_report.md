# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-04T09:37:09Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `d1073c60cbe9635ef33041004b0db3581d739fec037f80d9e508b0c30aa7c3df`
- TEST hash: `7703520984249e24490484e509fa3e2435f6d415459bcebb669d9d3e0ab168bc`

## Summary
- Only in DEV: 1
- Only in TEST: 0
- Present in both but different: 0

## Only in DEV
- PATCH /api/gateway/ServiceOrders/{orderNumber}/order-status

## Only in TEST
- None

## Different in DEV and TEST
- None
