# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-09-23T10:20:08Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `510b5e0d841dc1344936020782bf5a936d4bd8ca794541297a66960ba60ce3ec`
- TEST hash: `3dcd501ceb736bd3db36272d69a0022e55be34e3fe64dfa906f33f20709d351e`

## Summary
- Only in DEV: 17
- Only in TEST: 0
- Present in both but different: 4

## Only in DEV
- DELETE /api/gateway/Orders/drafts/{orderNumber}
- GET /api/gateway/Orders
- GET /api/gateway/Orders/store/{storeNumber}
- GET /api/gateway/Orders/{orderNumber}
- GET /api/gateway/PickLists/store/{storeNumber}
- GET /api/gateway/PickLists/{pickListId}
- PATCH /api/gateway/Orders/drafts/{orderNumber}/submit
- PATCH /api/gateway/Orders/drafts/{orderNumber}/undoDelete
- PATCH /api/gateway/Orders/{orderNumber}/delivery
- PATCH /api/gateway/Orders/{orderNumber}/delivery/properties
- PATCH /api/gateway/Orders/{orderNumber}/fulfillments/{fulfillmentOrderId}/tracking
- PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}/properties
- PATCH /api/gateway/Orders/{orderNumber}/properties
- POST /api/gateway/Orders/{orderNumber}/copy
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
