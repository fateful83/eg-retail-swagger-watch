# Swagger/OpenAPI change detected: CustomerOrderV2 [TEST]

- Time: 2026-06-12T09:49:21Z
- Fetch completed at: 2026-06-12T09:49:21Z
- Fetch duration ms: 1096
- Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- Previous hash: `02c1f1720b9564dcb184182d4f45efc9469b9f913895dace77334d3a108302db`
- Current hash: `8c6e9e352a53591f332fd7e4b0fb004ed12743073b7adbc1e84237e0061ed67e`

## Summary
- Status: breaking
- Added operations: 1
- Removed operations: 0
- Changed operations: 1
- Breaking removed operations: 0
- Breaking changed operations: 1
- Non-breaking changed operations: 0

## Added
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Removed
- None

## Changed
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment

## Breaking classification
- Removed operations: 0
- None

- Breaking changed operations: 1
  - POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment

- Non-breaking changed operations: 0
- None
