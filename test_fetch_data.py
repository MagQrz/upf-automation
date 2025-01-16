from full_workflow import fetch_data

def test_fetch_data () :
    data = fetch_data()
    if data:
        print ("fetch_data is working")
    else:
        print ("fetch_data not working")

test_fetch_data()