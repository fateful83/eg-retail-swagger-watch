# Swagger/OpenAPI change detected: CustomerOrderV2 [DEV]

- Time: 2026-09-22T10:24:51Z
- Fetch completed at: 2026-09-22T10:24:50Z
- Fetch duration ms: 1326
- Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- Previous hash: `908f04e704edeb89f9c6792d712b02b89ffc3b3b56df49f8558f6949f1a0b522`
- Current hash: `0837162883da6c7bd4302a9f49091c827ad83ea1ddf4f7340d0fe5fefcb1a9dd`

## Summary
- Status: non_breaking
- Added operations: 5
- Removed operations: 0
- Changed operations: 1
- Breaking removed operations: 0
- Breaking changed operations: 0
- Non-breaking changed operations: 1

## Added
- GET /api/gateway/Orders
- GET /api/gateway/PickLists/{pickListId}
- PATCH /api/gateway/Orders/{orderNumber}/delivery
- PATCH /api/gateway/Orders/{orderNumber}/fulfillments/{fulfillmentOrderId}/tracking
- POST /api/gateway/Orders/{orderNumber}/copy

## Removed
- None

## Changed
- GET /api/gateway/PickLists/store/{storeNumber}

## Breaking classification
- Removed operations: 0
- None

- Breaking changed operations: 0
- None

- Non-breaking changed operations: 1
  - GET /api/gateway/PickLists/store/{storeNumber}
