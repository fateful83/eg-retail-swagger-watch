# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-04T19:50:32Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `9e2ac798d9a0509cbe82dabd8a90426e75297e47fa7638096d3eecac712c3b99`
- TEST hash: `3ce25bf0031844dfdc694b1b031e10d1fed70ab0d359f817f11b5bbf8ec94b9e`

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
