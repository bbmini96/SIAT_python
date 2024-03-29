# 데코레이터 => 메소드를 장식하는데 쓰인다
# 형식: @
# 자동으로 해야하는 것이 있으면 데코레이터로 만들어 준다

def shopping_format(mode):
    
    def add_mode(func): 
        def execute():
            print(mode, '어서옵쇼')
            func()
            print(mode, '안녕히 가십쇼')
        return execute

    return add_mode



@shopping_format('순하게')
def shopping_item():
    # print('어서옵쇼')
    print('item 쇼핑')
    # print('안녕히 가십쇼')

@shopping_format('격하게')
def shopping_phone():
    # print('어서옵쇼')
    print('phone 쇼핑')
    # print('안녕히 가십쇼')

# 순하게    
shopping_item()
print('======')
# 격하게   
shopping_phone()   
































