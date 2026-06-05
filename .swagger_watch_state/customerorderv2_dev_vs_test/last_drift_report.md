# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-05T14:14:42Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `94e4c526ccdb70961412a17d037c4e4a01fd07e98b6d46b044082badaa4101e4`
- TEST hash: `5ec6f85f424cbfabf9e475154142d0888b4064160dd69b285f91d985faabb39b`

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
