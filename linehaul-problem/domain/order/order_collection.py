from domain.base import BaseCollection
from domain.order.order_data import OrderData


class OrderCollection(BaseCollection[OrderData]):

    DataClass = OrderData


