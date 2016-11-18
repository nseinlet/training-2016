import openerplib

class HelloWorld():
    def say_hello(self, connection):
        partner_model = connection.get_model('res.partner')
        
        partner_ids = partner_model.search([('name', 'ilike', 'fletcher')])
        partners = partner_model.read(partner_ids, ['name', 'parent_id'])
        for partner in partners:
            print partner
            res = "Hello %s" % partner['name']
            if partner['parent_id']:
                res = "%s from %s" % (res, partner['parent_id'][1])
            print res
            
            
    def update_using_csv(self, connection):
        product_model = connection.get_model('product.product')
        
        product_ids = product_model.search([('name', 'ilike', 'ipad')])
        
        columns = ['id', 'list_price']
        lines = []
        
        for prod in product_model.read(product_ids,['name', 'list_price']):
            print "%s : %s " % (prod.get('name'), prod.get('list_price'))
        print "========================================================="
            
        products = product_model.export_data(product_ids, ['id', 'name', 'list_price'])
        for product in products['datas']:
            lines.append([product[0], float(product[2])*1.1])
        print "+++++++++++++++++++++++++++++++++++++++++=="
        print lines
        print "+++++++++++++++++++++++++++++++++++++++++=="
        product_model.load(columns, lines)
        
        for prod in product_model.read(product_ids,['name', 'list_price']):
            print "%s : %s " % (prod.get('name'), prod.get('list_price'))
        print "========================================================="


if __name__ == '__main__':
    #Connect by xml-rpc
    connection = openerplib.get_connection(hostname="localhost", 
                                           port=8069, 
                                           database="10training", 
                                           login="admin", 
                                           password="admin", 
                                           protocol="jsonrpc",
                                           user_id=1)
                                           
    connection.check_login()
            
    imp = HelloWorld()
    imp.update_using_csv(connection)
    
