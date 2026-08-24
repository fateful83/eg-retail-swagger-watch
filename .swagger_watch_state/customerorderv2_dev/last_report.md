# Swagger/OpenAPI change detected: CustomerOrderV2 [DEV]

- Time: 2026-08-24T12:19:21Z
- Fetch completed at: 2026-08-24T12:19:20Z
- Fetch duration ms: 5848
- Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- Previous hash: `8ece2c13b00704b4e233c24bb8c42fc7bfab33b854436e63b9efc313fc3ff43c`
- Current hash: `15db6c0010a3ee3c829c807a364b517da2d8f3e17e99a31f7fa54378e4489936`

## Summary
- Status: breaking
- Added operations: 5
- Removed operations: 0
- Changed operations: 5
- Breaking removed operations: 0
- Breaking changed operations: 1
- Non-breaking changed operations: 4

## Added
- GET /api/gateway/PickLists/store/{storeNumber}
- GET /api/gateway/ServiceOrders/{storeNumber}
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus
- POST /api/gateway/PickLists/{pickListId}/lines/{pickListLineId}/pick
- POST /api/gateway/PickLists/{pickListId}/start

## Removed
- None

## Changed
- DELETE /api/gateway/Orders/{orderNumber}/lines/{lineNo}
- GET /api/gateway/Orders/store/{storeNumber}
- PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
- PUT /api/gateway/Orders/{orderNumber}/lines

## Breaking classification
- Removed operations: 0
- None

- Breaking changed operations: 1
  - POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment

- Non-breaking changed operations: 4
  - DELETE /api/gateway/Orders/{orderNumber}/lines/{lineNo}
  - GET /api/gateway/Orders/store/{storeNumber}
  - PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}
  - PUT /api/gateway/Orders/{orderNumber}/lines
