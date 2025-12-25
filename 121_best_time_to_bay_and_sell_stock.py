class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
            
        min_price = prices[0]   # Инициализируем один раз
        max_profit = 0
        
        for i in range(1, len(prices)):  # Начинаем со 2‑го элемента
            price = prices[i]
            if price < min_price:
                min_price = price        # Сначала обновляем минимум
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit    # Потом считаем прибыль
                    
        return max_profit
# необходимо улучшить скорость выполнения