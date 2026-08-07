# Swagger/OpenAPI change detected: CustomerOrderV2 [DEV]

- Time: 2026-08-07T12:33:02Z
- Fetch completed at: 2026-08-07T12:33:01Z
- Fetch duration ms: 4748
- Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- Previous hash: `fe9b963e8c52a3bfde1a4e708e551b040b280b5471b6df81af5d8a85e82da010`
- Current hash: `0a8b0aeb3cb63bf35c18e5cbb5c4622c7ad6b81c170d566d3a4d2737bfedd694`

## Summary
- Status: breaking
- Added operations: 9
- Removed operations: 2
- Changed operations: 2
- Breaking removed operations: 2
- Breaking changed operations: 1
- Non-breaking changed operations: 1

## Added
- DELETE /api/gateway/Orders/drafts/{orderNumber}
- GET /api/gateway/Orders/store/{storeNumber}
- GET /api/gateway/Orders/{orderNumber}
- PATCH /api/gateway/Orders/drafts/{orderNumber}/submit
- PATCH /api/gateway/Orders/drafts/{orderNumber}/undoDelete
- PATCH /api/gateway/Orders/{orderNumber}/delivery/properties
- PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}/properties
- PATCH /api/gateway/Orders/{orderNumber}/properties
- PUT /api/gateway/Orders/drafts

## Removed
- GET /api/gateway/ServiceOrders/{storeNumber}
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Changed
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
- PUT /api/gateway/Orders

## Breaking classification
- Removed operations: 2
  - GET /api/gateway/ServiceOrders/{storeNumber}
  - PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

- Breaking changed operations: 1
  - POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment

- Non-breaking changed operations: 1
  - PUT /api/gateway/Orders
