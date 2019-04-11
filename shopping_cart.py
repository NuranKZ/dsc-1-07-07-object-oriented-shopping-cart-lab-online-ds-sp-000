class ShoppingCart:
    # write your code here
    def __init__(self, employee_discount=None):
        self.employee_discount = employee_discount
        self.total = 0
        self.items = []
        self.items_count = 0
        self.prices = []
        self.total_withdiscount = 0
        
    def add_item(self, name, price, quantity=1):
        self.total += price*quantity
        self.items.append(name)
        self.items_count += quantity
        self._prices = [price]*quantity 
        self.prices.extend(self._prices)
        self.prices.sort()
        return self.total
        
        
    def mean_item_price(self):
        return self.total / self.items_count

    def median_item_price(self):
        if len(self.prices) %2 != 0:
            self.med = self.prices[int((len(self.prices)-1)/2)]
        else:
            self.med = (self.prices[int(len(self.prices)/2)]+self.prices[int(len(self.prices)/2-1)])/2
        return self.med

    def apply_discount(self):
        if self.employee_discount == None:
            return 'Sorry, there is no discount to apply to your cart :('
        else:
            self.total_withdiscount = self.total*(1-self.employee_discount/100)
            return self.total_withdiscount
        
        
        
    def void_last_item(self):
        if len(self.prices) == 0:
            return 'There are no items in your cart!'
        else:
            self.void_price = self.prices.pop()
            self.total -= self.void_price
            return self.total

    
    
    
    
    
    
    
    
    
    
    
    
    
    