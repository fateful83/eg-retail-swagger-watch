# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-10-21T02:07:07Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `150e3eecf58fb48a4d437c698b7e551304ed5560d4962a6e33c328d7b83b1fa5`
- TEST hash: `5c0a68e44c16ba6983f033060fcc3b1c26ba1813405236ee1a98fe0224952b82`

## Summary
- Only in DEV: 25
- Only in TEST: 0
- Present in both but different: 7

## Only in DEV
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

## Only in TEST
- None

## Different in DEV and TEST
- DELETE /api/gateway/Orders/{orderNumber}/lines/{lineNo}
- PATCH /api/gateway/Orders/{orderNumber}/lines/deliver
- PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}
- PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}/deliver
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
- PUT /api/gateway/Orders
- PUT /api/gateway/Orders/{orderNumber}/lines
