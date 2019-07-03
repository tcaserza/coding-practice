# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
#
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.


class order_log:
    def __init__(self):
        self.order_ids = []
    def record(self, order_id):
        self.order_ids.append(order_id)
    def get_last(self,i):
        return self.order_ids[len(self.order_ids) - i]


ol = order_log()
ol.record(1)
ol.record(5)
ol.record(6)
ol.record(10)
print ol.get_last(2)
