from functools import total_ordering
from enum import Enum






class Side(Enum):
    BUY = 0
    SELL = 1


    
  
@total_ordering
class Order():
    def __init__(self, quantity, price, side):
        self.quantity = quantity
        self.price = price
        self.side = Side(side)
        self.priority = 0
        self.order_id=0

    def __eq__(self, other): # self == other
        return other and self.quantity == other.quantity and self.price == other.price

    def __lt__(self, other): # self < other
        return other and self.price < other.price    
    
    def __str__(self): # human-readable content
        return "%s @ %s" % (self.quantity, self.price)

    def __repr__(self): # unambiguous representation of the object
        return "Order(%s, %s)" % (self.quantity, self.price)

    def setOrder(self, value):
        self.order_id = value

    def getOrder(self):
        return self.order_id

    def setQuantity(self, value):
        self.quantity = value

    def getQuantity(self):
        return self.quantity

class Book(Order):

    def __init__(self,name):
        self.name = name
        self.buy_orders = []
        self.sell_orders = []
        self.count =0

    def tabular_print(self):
        dataframe_buy=pd.Dataframe(self.buy_orders,columns=["BUY"])
        dataframe_sell=pd.Dataframe(self.sell_orders,columns=["SELL"])
        final_dataframe=pd.concat([dataframe_buy,dataframe_sell],axis=1).fillna("        ")
        return(final_dataframe.to_markdown())
        
        
    def insert_order(self, quantity, price, side):
        order1=Order(quantity, price, side)
        self.count =self.count+1
        order1.setOrder(self.count)
        print("----------------------")
        if Side(side)== Side.BUY :
            self.buy_orders.append(order1)
            print("--- Insert BUY ", order1.__str__() , " id=" , order1.getOrder() , " on ", self.name ,"\n", "Book on ", self.name)
            
        elif Side(side)==Side.SELL:
            self.sell_orders.append(order1)
            print("--- Insert SELL ", order1.__str__() , " id=" , order1.getOrder() , " on ", self.name ,"\n", "Book on ", self.name)
    
        self.buy_orders=sorted(self.buy_orders,key=lambda Order:Order.price,reverse=True)
        self.sell_orders=sorted(self.sell_orders,key=lambda Order:Order.price,reverse=False)

  
        k=0
        answer=False
        answer1=False
        for k in range(10):
            answer=False
            answer1=False
            for i in range(len(self.buy_orders)):
                if len(self.sell_orders) != 0 and len(self.buy_orders) != 0 :   
                    if self.sell_orders[0].price == self.buy_orders[i].price or self.sell_orders[0].price < self.buy_orders[i].price:  
                        answer=True


            if answer==True and len(self.sell_orders) != 0 and len(self.buy_orders) != 0 :
                if self.sell_orders[0].quantity-self.buy_orders[0].quantity<0:
                    print("Execute", (self.sell_orders[0].getQuantity())," at ", self.buy_orders[0].price, "on" , self.name)
                    self.buy_orders[0].setQuantity(self.buy_orders[0].quantity-self.sell_orders[0].quantity)
                    del(self.sell_orders[0])
 
                    
                elif  self.sell_orders[0].quantity-self.buy_orders[0].quantity>0:
                    print("Execute", (self.buy_orders[0].getQuantity())," at ", self.buy_orders[0].price, "on" , self.name)
                    
                    self.sell_orders[0].setQuantity(self.sell_orders[0].quantity-self.buy_orders[0].quantity)
                    del(self.buy_orders[0])


            for i in range(len(self.sell_orders)):
                if len(self.sell_orders) != 0 and len(self.buy_orders) != 0 : 
                    if self.buy_orders[0].price == self.sell_orders[i].price or self.buy_orders[0].price > self.sell_orders[i].price:
                        answer1=True
    

            if answer1==True and len(self.buy_orders) != 0 and len(self.sell_orders) != 0 :
                if self.buy_orders[0].quantity-self.sell_orders[0].quantity<0:
                    print("Execute", (self.buy_orders[0].getQuantity())," at ", self.sell_orders[0].price, "on" , self.name)
                    self.sell_orders[0].setQuantity(self.sell_orders[0].quantity-self.buy_orders[0].quantity)
                    del(self.buy_orders[0])


                                
                elif  self.buy_orders[0].quantity-self.sell_orders[0].quantity>0:
                    print("Execute", (self.sell_orders[0].getQuantity())," at ", self.sell_orders[0].price, "on" , self.name)
                    
                    self.buy_orders[0].setQuantity(self.buy_orders[0].quantity-self.sell_orders[0].quantity)
                    del(self.sell_orders[0])
           



                
        for i in range(len(self.sell_orders)):
            print ("SELL ",self.sell_orders[i].__str__()," id=",self.sell_orders[i].getOrder())

        
        for j in range(len(self.buy_orders)):
            print ("BUY ",self.buy_orders[j].__str__(), "id=",self.buy_orders[j].getOrder())

