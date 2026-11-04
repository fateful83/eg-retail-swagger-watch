# Swagger/OpenAPI change detected: CustomerOrderV2 [TEST]

- Time: 2026-11-04T13:19:56Z
- Fetch completed at: 2026-11-04T13:19:55Z
- Fetch duration ms: 1586
- Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- Previous hash: `1b171e82518023868b66aac3e2a09899f108e00d4979160cc8c509f99bb65371`
- Current hash: `accf9b31419c75bcc15eaedeb01a97a62bd9e3cb9437df9cd457af1236447f82`

## Summary
- Status: breaking
- Added operations: 25
- Removed operations: 0
- Changed operations: 8
- Breaking removed operations: 0
- Breaking changed operations: 3
- Non-breaking changed operations: 5

## Added
- DELETE /api/gateway/Orders/drafts/{orderNumber}
- DELETE /api/gateway/Orders/{orderNumber}/lines/{lineNo}/discount
- GET /api/gateway/Orders
- GET /api/gateway/Orders/store/{storeNumber}
- GET /api/gateway/Orders/store/{storeNumber}/payable
- GET /api/gateway/Orders/{orderNumber}
- GET /api/gateway/PickLists/store/{storeNumber}
- GET /api/gateway/PickLists/{pickListId}
- PATCH /api/gateway/Orders/drafts/{orderNumber}/submit
- PATCH /api/gateway/Orders/drafts/{orderNumber}/undoDelete
- PATCH /api/gateway/Orders/{orderNumber}/cancel
- PATCH /api/gateway/Orders/{orderNumber}/delivery
- PATCH /api/gateway/Orders/{orderNumber}/delivery/properties
- PATCH /api/gateway/Orders/{orderNumber}/fulfillments/{fulfillmentOrderId}/collectionDeadline
- PATCH /api/gateway/Orders/{orderNumber}/fulfillments/{fulfillmentOrderId}/pack
- PATCH /api/gateway/Orders/{orderNumber}/fulfillments/{fulfillmentOrderId}/readyForCollection
- PATCH /api/gateway/Orders/{orderNumber}/fulfillments/{fulfillmentOrderId}/tracking
- PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}/properties
- PATCH /api/gateway/Orders/{orderNumber}/properties
- POST /api/gateway/Orders/{orderNumber}/copy
- POST /api/gateway/Orders/{orderNumber}/payments
- POST /api/gateway/PickLists/{pickListId}/lines/{pickListLineId}/pick
- POST /api/gateway/PickLists/{pickListId}/reject
- POST /api/gateway/PickLists/{pickListId}/start
- PUT /api/gateway/Orders/drafts

## Removed
- None

## Changed
- DELETE /api/gateway/Orders/{orderNumber}/lines/{lineNo}
- PATCH /api/gateway/Orders/{orderNumber}/lines/deliver
- PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}
- PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}/deliver
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
- PUT /api/gateway/Orders
- PUT /api/gateway/Orders/{orderNumber}/lines
- PUT /api/gateway/Orders/{orderNumber}/lines/{lineNo}/discount

## Breaking classification
- Removed operations: 0
- None

- Breaking changed operations: 3
  - PATCH /api/gateway/Orders/{orderNumber}/lines/deliver
  - PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}/deliver
  - POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment

- Non-breaking changed operations: 5
  - DELETE /api/gateway/Orders/{orderNumber}/lines/{lineNo}
  - PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}
  - PUT /api/gateway/Orders
  - PUT /api/gateway/Orders/{orderNumber}/lines
  - PUT /api/gateway/Orders/{orderNumber}/lines/{lineNo}/discount
