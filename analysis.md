# Products:

    - name
    - sku
    - brand * [name-img]
    - images *
    - subtitle
    - description
    - tags * package
    - price
    - flag [new-sale-features] dropdown
    - quantity
    - reviews * [name-img-rating-date-comment]
    - category * [name-img]

# Orders:

    - status [recieved-processing-shipped-delivered] dropdown
    - user
    - id
    - total item count
    - delivery time
    - order time
    - total
    - sub_total

# OrderDetails:

    - order_id
    - product_id
    - quantity
    - price
    - total

# User:

    - name
    - email
    - password
    - phone
    - address
    - city
    - state
    - zip
    - country
    - orders * [id-status-total-item_count-delivery_time-order_time]
    - reviews * [name-img-rating-date-comment]
