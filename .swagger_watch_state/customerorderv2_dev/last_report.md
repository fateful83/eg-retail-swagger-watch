# Swagger/OpenAPI change detected: CustomerOrderV2 [DEV]

- Time: 2026-10-20T10:28:57Z
- Fetch completed at: 2026-10-20T10:28:56Z
- Fetch duration ms: 1602
- Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- Previous hash: `3376d5c63235020c1063ef4973ce298a4584d1966bfb0dae1e47588b8f398782`
- Current hash: `5dfcfb5296bd0e57a6f85b834032649cfde6d48d97d4933d1f59d1f7925b5587`

## Summary
- Status: non_breaking
- Added operations: 5
- Removed operations: 0
- Changed operations: 0
- Breaking removed operations: 0
- Breaking changed operations: 0
- Non-breaking changed operations: 0

## Added
- DELETE /api/gateway/Orders/{orderNumber}/lines/{lineNo}/discount
- PATCH /api/gateway/Orders/{orderNumber}/fulfillments/{fulfillmentOrderId}/collectionDeadline
- PATCH /api/gateway/Orders/{orderNumber}/fulfillments/{fulfillmentOrderId}/pack
- PATCH /api/gateway/Orders/{orderNumber}/fulfillments/{fulfillmentOrderId}/readyForCollection
- POST /api/gateway/PickLists/{pickListId}/reject

## Removed
- None

## Changed
- None

## Breaking classification
- Removed operations: 0
- None

- Breaking changed operations: 0
- None

- Non-breaking changed operations: 0
- None
