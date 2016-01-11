class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # DP
        # states:
        #   sell: max profit at day i sell on day i
        #   buy : max profit at day i buy on day i
        #   cool: max profit at day i cooldown on day i
        if not prices or len(prices) < 2:
            return 0

        sell, buy, cool = 0, -prices[0], 0
        for price in prices[1:]:
            sell, buy, cool = max(buy + price, sell), max(cool - price, buy), max(sell, buy, cool)
        return max(sell, buy, cool)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # FSM
        # states:
        #         sell
        #        /   ^
        #       /     \
        #      c       s(+)
        #     /         \
        #    <           >
        # - cool - b(-) -> buy -|
        # |  |              |   |
        # -c-|              --c-|
        #
        if not prices or len(prices) < 2:
            return 0

        states = {'sell': 0, 'cooldown': 0, 'buy': -prices[0]}
        for price in prices[1:]:
            sell, cool, buy = states['sell'], states['cooldown'], states['buy']
            states['cooldown'] = max(sell, cool)
            states['buy'] = max(cool - price, buy)
            states['sell'] = buy + price
        return max(states.values())

if __name__ == '__main__':
    # buy, sell, cooldown, buy, sell
    print(Solution().maxProfit([1,2,3,0,2]))
