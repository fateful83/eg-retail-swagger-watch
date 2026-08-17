# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-08-17T18:18:38Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `1da69c5b80c342821a04eac9fde27e48fc15874b38d3f4f0f8739159123a4b84`
- TEST hash: `6b6a6db921ea2bc869e5a9d3d55fcdd0593f09d0df0b9903afc51602a1102157`

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
