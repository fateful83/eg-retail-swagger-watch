# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-08-12T00:46:37Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `7feae67247d01e039f10a4ce7afc0e9532b984d3726f1f80401aca2ba2431ce9`
- TEST hash: `ebd30ec759a6d79b476d684bcbf3c8399f3fa30c5b664d8d9c36c38c5acde7bc`

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
