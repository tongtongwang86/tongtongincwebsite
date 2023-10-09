import requests
import re
import json
import os
from orderkey import *


def get_order_details(ordernumber, email):
    req_session = requests.get('https://secure.store.apple.com/shop/order/list')
    res_session = req_session.text

    cookie_values = [v.name + "=" + v.value for v in req_session.cookies]

    x_aos_stk_match = re.search(r'"x-aos-stk":"([\w\-]+)"', res_session)
    if not x_aos_stk_match:
        raise ValueError('Needed x-aos-stk token not found')
    
    post_url = (req_session.url.replace('/orders', '/orderx')) + '&_a=guestUserOrderLookUp&_m=signIn.orderLookUp'

    post_req = requests.post(post_url, headers={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': req_session.url,
        'x-aos-model-page': 'olssSignInPage',
        'x-aos-stk': x_aos_stk_match.group(1),
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': '; '.join(cookie_values)
    }, data={
        'signIn.orderLookUp.orderNumber': str(ordernumber),
        'signIn.orderLookUp.emailAddress': email
    })

    res_post_req = post_req.text

    if post_req.status_code != 200:
        raise ValueError(f'Got HTTP {post_req.status_code} from API.')

    try:
        post_res_data = json.loads(res_post_req)
    except json.JSONDecodeError:
        raise ValueError('Can\'t parse API response.')

    if post_res_data['head']['status'] != 302:
        raise ValueError('Fetching the data failed. Got unexpected response. Please try it later.')

    req = requests.get(post_res_data['head']['data']['url'])
    res = req.text

    raw_json = re.search(r'<script id="init_data" type="application\/json">[\s]+(.*)[\s]+<\/script>', res)
    if not raw_json:
        return None
    
    data = json.loads(raw_json.group(1))
    if 'orderDetail' not in data:
        print(data)
        raise ValueError('no orderDetail attribute')

    data['widgetURL'] = post_res_data['head']['data']['url']
    
    
    return data



order_data = get_order_details(ordernumber,email)


# Access the order date and current status
order_date = order_data['orderDetail']['orderHeader']['d']['orderPlacedDate']
deliveryDate = order_data['orderDetail']['orderItems']['orderItem-0000101']['orderItemDetails']['d']['deliveryDate']

current_status = order_data['orderDetail']['orderItems']['orderItem-0000101']['orderItemStatusTracker']['d']['currentStatus']


# Convert variables to dictionary
data = {
    "order_date": order_date,
    "current_status": current_status,
    "deliveryDate": deliveryDate
    
}

# Convert dictionary to JSON
json_data = json.dumps(data, indent=4)

# Specify the file path
#file_path = "ordertrack/orderstatusoutput.json"
file_path = os.path.join(os.path.dirname(__file__), "orderstatusoutput.json")

with open(file_path, 'w') as file:
    file.write(json_data)
