import api from './api'

export const accountService = {
// Orders

getOrders() {
return api.get(
'/orders/'
)
},

getOrder(
orderNumber
) {
return api.get(
`/orders/${orderNumber}/`
)
},

// Addresses

getAddresses() {
return api.get(
'/orders/addresses/'
)
},

createAddress(
payload
) {
return api.post(
'/orders/addresses/',
payload
)
},

updateAddress(
id,
payload
) {
return api.patch(
`/orders/addresses/${id}/`,
payload
)
},

deleteAddress(id) {
return api.delete(
`/orders/addresses/${id}/`
)
},
}
