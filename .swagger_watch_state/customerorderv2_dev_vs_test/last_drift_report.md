# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-09T01:45:56Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `5aee9bc289fed143dc5872b1bf2108134780820567e41f26caec30402410097c`
- TEST hash: `b89336dfb14c23c575fb915653b7a03205dd5c77ae5866852459ac50ef0b1b2a`

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
