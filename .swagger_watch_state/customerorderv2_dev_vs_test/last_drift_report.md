# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-10-12T23:52:05Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `9c039cb38d3d83c641c19ae2df8a67359cf86f878ef28f96a1dac88dcdb234fc`
- TEST hash: `0de3e37ac4ef7ad2f6427d6dad5c7f7a73a5f91cbfacd4a140ac2e0c57b007b7`

## Summary
- Only in DEV: 20
- Only in TEST: 0
- Present in both but different: 7

## Only in DEV
- DELETE /api/gateway/Orders/drafts/{orderNumber}
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
- PATCH /api/gateway/Orders/{orderNumber}/fulfillments/{fulfillmentOrderId}/tracking
- PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}/properties
- PATCH /api/gateway/Orders/{orderNumber}/properties
- POST /api/gateway/Orders/{orderNumber}/copy
- POST /api/gateway/Orders/{orderNumber}/payments
- POST /api/gateway/PickLists/{pickListId}/lines/{pickListLineId}/pick
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
