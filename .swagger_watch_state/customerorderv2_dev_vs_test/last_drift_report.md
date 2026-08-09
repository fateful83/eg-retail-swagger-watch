# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-08-09T06:33:07Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `493d148be20b7e9b665e8405132c9509e030bc0da04dc98c9aa44d6c87b571f0`
- TEST hash: `26e8896fe42d4fb9c88c3b9ac6876b218321411a9b171a238f10df3a904815ca`

## Summary
- Only in DEV: 9
- Only in TEST: 2
- Present in both but different: 2

## Only in DEV
- DELETE /api/gateway/Orders/drafts/{orderNumber}
- GET /api/gateway/Orders/store/{storeNumber}
- GET /api/gateway/Orders/{orderNumber}
- PATCH /api/gateway/Orders/drafts/{orderNumber}/submit
- PATCH /api/gateway/Orders/drafts/{orderNumber}/undoDelete
- PATCH /api/gateway/Orders/{orderNumber}/delivery/properties
- PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}/properties
- PATCH /api/gateway/Orders/{orderNumber}/properties
- PUT /api/gateway/Orders/drafts

## Only in TEST
- GET /api/gateway/ServiceOrders/{storeNumber}
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Different in DEV and TEST
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
- PUT /api/gateway/Orders
