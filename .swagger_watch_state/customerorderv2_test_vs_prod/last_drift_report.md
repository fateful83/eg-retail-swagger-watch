# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-11-28T00:44:54Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6cac279b29480042a066b0fb3552bcde66e18dce5d6e62c184616c4f69d6c033`
- PROD hash: `2851cc6193410aa21c3ac0913997e9639ab49729afd830855654f542ef5ae563`

## Summary
- Only in TEST: 26
- Only in PROD: 0
- Present in both but different: 8

## Only in TEST
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
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus
- POST /api/gateway/Orders/{orderNumber}/copy
- POST /api/gateway/Orders/{orderNumber}/payments
- POST /api/gateway/PickLists/{pickListId}/lines/{pickListLineId}/pick
- POST /api/gateway/PickLists/{pickListId}/reject
- POST /api/gateway/PickLists/{pickListId}/start
- PUT /api/gateway/Orders/drafts

## Only in PROD
- None

## Different in TEST and PROD
- DELETE /api/gateway/Orders/{orderNumber}/lines/{lineNo}
- PATCH /api/gateway/Orders/{orderNumber}/lines/deliver
- PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}
- PATCH /api/gateway/Orders/{orderNumber}/lines/{lineNo}/deliver
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
- PUT /api/gateway/Orders
- PUT /api/gateway/Orders/{orderNumber}/lines
- PUT /api/gateway/Orders/{orderNumber}/lines/{lineNo}/discount
