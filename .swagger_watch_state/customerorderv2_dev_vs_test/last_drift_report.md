# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-08-07T12:33:02Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `0a8b0aeb3cb63bf35c18e5cbb5c4622c7ad6b81c170d566d3a4d2737bfedd694`
- TEST hash: `f7ccb3cdd4024664f807c108248bc934745de88ee9f5f3634f05ba0de5d7f8bc`

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
