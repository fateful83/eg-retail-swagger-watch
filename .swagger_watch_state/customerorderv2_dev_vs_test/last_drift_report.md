# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-08-25T00:27:04Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `07ff703a0020d2e22a01c057f003cec406db9b45c2805c41b9035e9d61da61b1`
- TEST hash: `1e262cf1620a1985eab5c3998fb02f53e9a3b0d13912cd338bcb60e6e27a1596`

## Summary
- Only in DEV: 12
- Only in TEST: 0
- Present in both but different: 4

## Only in DEV
- DELETE /api/gateway/Orders/drafts/{orderNumber}
- GET /api/gateway/Orders/store/{storeNumber}
- GET /api/gateway/Orders/{orderNumber}
- GET /api/gateway/PickLists/store/{storeNumber}
- PATCH /api/gateway/Orders/drafts/{orderNumber}/submit
- PATCH /api/gateway/Orders/drafts/{orderNumber}/undoDelete
- PATCH /api/gateway/Orders/{orderNumber}/delivery/properties
- PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}/properties
- PATCH /api/gateway/Orders/{orderNumber}/properties
- POST /api/gateway/PickLists/{pickListId}/lines/{pickListLineId}/pick
- POST /api/gateway/PickLists/{pickListId}/start
- PUT /api/gateway/Orders/drafts

## Only in TEST
- None

## Different in DEV and TEST
- DELETE /api/gateway/Orders/{orderNumber}/lines/{lineNo}
- PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}
- PUT /api/gateway/Orders
- PUT /api/gateway/Orders/{orderNumber}/lines
