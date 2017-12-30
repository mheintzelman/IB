from ib.opt import Connection


def print_message_from_ib(msg):
    print(msg)

def main():
    conn = Connection.create(port=7496, clientId=177)  #Doesn't need to match TWS unless running multiple scripts
    conn.registerAll(print_message_from_ib)
    conn.connect()
    
    import time
    time.sleep(1) #Simply to give the program time to print messages sent from IB
    conn.disconnect()
    
if __name__ == "__main__": main()

#
#def make_contract(symbol, sec_type, exch, prim_exchange, curr):
#    Contract.m_symbol = symbol
#    Contract.m_secType = sec_type
#    Contract.m_exchange = exch
#    Contract.m_primaryExch = prim_exch
#    Contract.m_currency = curr
#    return Contract
#
#def make_order(action,quantity, price = None):
#    if price is not None:
#        order = Order()
#        order.m_orderType = 'LMT'
#        order.m_totalQuantity = quantity
#        order.m_action = action
#        order.m_lmtPrice = price
#        
#    else:
#        order = Order()
#        order.m_orderType = 'MKT'
#        order.m_totalQuantity = quantity
#        order.m_action = action
#
#    return order    
#    
#
#def main():
#    conn = Connection.create(port=7496, clientId=177)
#    conn.connect()
#    
#    oid = cid
#    cont = make_contract('TSLA', 'STK', 'SMART', 'SMART', 'USD')
#    offer = make_order('BUY', 1, 200)
#    conn.placeOrder(oid, cont, offer)
#    conn.disconnect()
#    x = raw_input('enter to resend')
#    cid += 1
#     
#     
     