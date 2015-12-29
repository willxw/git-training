#encoding:utf-8
import httplib
import json
import urllib
 
#conn = httplib.HTTPConnection("10.117.193.109",8080)
conn = httplib.HTTPConnection("10.117.193.109",8081)
headers = {"Content-type":"application/json"}
param = ({
	"pid": "415180",
	"pc_id": "31940",
	"openid": "",
	"total_price": "0.01",
	"out_trade_no": "A20151216-1111",
	"order_sn": "A20151216-1111",
	"notify_url": "http://10.117.193.109:8080/core/pc/payment/sync_biz_order_status",
	"modules_code": "MicroShop",
	"good_name": "萌店在线消费",
	"order_data": [{
		"total_price": "0.01",
		"logic_order_sn": "41400056181",
		"order_type": "0",
		"shop_id": "10000001981",
		"shop_title": "店铺2015100000888",
		"pid": "667",
		"is_delivery": "1",
		"coupon_amount": "0.00",
		"coupon_remark": "",
		"coupon_original_id": ""
	}],
	"ex_data": {
		"coupon_amount": "0.00",
		"coupon_remark": "",
		"coupon_original_id": ""
	},
	"uid": "10000010393",
	"utype": "1",
	"trade_type": "APP",
	"goods_data": "A0001:10000001981#A0002:店铺2015100000888#B0002:02#B0003:蔡松#B0004:18321498272#B0005:天津 天津市 和平区 忽大忽小#D0001:1#D0002:#D0004:101.81.38.36#D0005:10000010393#D0006:2015\/11\/09#D0007:02#D0008:0.01#D0009:1"
})
print 'execute pay request...'
conn.request("POST" ,"/core/pc/payment/pay",json.JSONEncoder().encode(param), headers)

response = conn.getresponse()
data = response.read(200000)
print(data)
 
conn.close()

