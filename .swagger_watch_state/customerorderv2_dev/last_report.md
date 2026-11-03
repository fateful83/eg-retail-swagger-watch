# Swagger/OpenAPI change detected: CustomerOrderV2 [DEV]

- Time: 2026-11-03T13:03:57Z
- Fetch completed at: 2026-11-03T13:03:55Z
- Fetch duration ms: 1857
- Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- Previous hash: `7d41f57348e8a0b654d782d3af0348b7e62e00e589ee4dbdafd2cb4aab4c35eb`
- Current hash: `bf051ba5aa5d48fb6ca4fd4f3f7cf9e3c987a321c88c65e28b2d04f7a8e94742`

## Summary
- Status: non_breaking
- Added operations: 0
- Removed operations: 0
- Changed operations: 4
- Breaking removed operations: 0
- Breaking changed operations: 0
- Non-breaking changed operations: 4

## Added
- None

## Removed
- None

## Changed
- DELETE /api/gateway/Orders/{orderNumber}/lines/{lineNo}
- PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}
- PUT /api/gateway/Orders/{orderNumber}/lines
- PUT /api/gateway/Orders/{orderNumber}/lines/{lineNo}/discount

## Breaking classification
- Removed operations: 0
- None

- Breaking changed operations: 0
- None

- Non-breaking changed operations: 4
  - DELETE /api/gateway/Orders/{orderNumber}/lines/{lineNo}
  - PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}
  - PUT /api/gateway/Orders/{orderNumber}/lines
  - PUT /api/gateway/Orders/{orderNumber}/lines/{lineNo}/discount
