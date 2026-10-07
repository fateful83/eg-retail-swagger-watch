# Swagger/OpenAPI change detected: CustomerOrderV2 [DEV]

- Time: 2026-10-07T12:07:38Z
- Fetch completed at: 2026-10-07T12:07:38Z
- Fetch duration ms: 2066
- Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- Previous hash: `b70df9dfb63206829724abe0c6e6b0e79e6c05a090930a02cd45591bf3d29dc8`
- Current hash: `321eba7c8b52c15699aaaff0cd559f9cdd1d1f5a328e0069c4d0fedb26522b74`

## Summary
- Status: breaking
- Added operations: 2
- Removed operations: 0
- Changed operations: 4
- Breaking removed operations: 0
- Breaking changed operations: 4
- Non-breaking changed operations: 0

## Added
- GET /api/gateway/Orders/store/{storeNumber}/payable
- POST /api/gateway/Orders/{orderNumber}/payments

## Removed
- None

## Changed
- GET /api/gateway/Orders/store/{storeNumber}
- PATCH /api/gateway/Orders/{orderNumber}/lines/deliver
- PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}/deliver
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment

## Breaking classification
- Removed operations: 0
- None

- Breaking changed operations: 4
  - GET /api/gateway/Orders/store/{storeNumber}
  - PATCH /api/gateway/Orders/{orderNumber}/lines/deliver
  - PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}/deliver
  - POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment

- Non-breaking changed operations: 0
- None
