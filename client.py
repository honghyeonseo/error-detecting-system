# 기준 무게를 설정합니다.
STANDARD_WEIGHT = 75.0  # 기준 무게 (예: 75kg)

# 상품 데이터 (상품명, 무게)
products = [
    {"name": "상품1", "weight": 74.0},
    {"name": "상품2", "weight": 77.0},
    {"name": "상품3", "weight": 75.0},
    {"name": "상품4", "weight": 80.0}
]

def identify_weight_variation(products, standard_weight, tolerance=2.0):
    """
    상품의 무게가 기준 무게와 다를 때 식별합니다.
    
    :param products: 상품 데이터 리스트
    :param standard_weight: 기준 무게
    :param tolerance: 허용 오차 범위 (기본값은 2kg)
    :return: 이상이 있는 상품 리스트
    """
    if tolerance < 0:
        raise ValueError("허용 오차 범위(tolerance)는 음수일 수 없습니다.")
    
    defective_products = []
    
    for product in products:
        # 상품의 무게가 올바른 형식인지 확인
        if not isinstance(product["weight"], (int, float)):
            raise ValueError(f"상품 '{product['name']}'의 무게는 숫자여야 합니다.")
        
        weight = product["weight"]
        difference = abs(weight - standard_weight)
        
        if difference > tolerance:
            product["difference"] = difference
            defective_products.append(product)
    
    return defective_products

# 무게 차이가 있는 상품을 식별합니다.
try:
    defective_products = identify_weight_variation(products, STANDARD_WEIGHT)

    # 결과 출력
    if defective_products:
        print("이상 있는 상품:")
        for product in defective_products:
            print(f"상품명: {product['name']}, 무게: {product['weight']}kg, 기준 무게와의 차이: {product['difference']}kg")
    else:
        print("이상 있는 상품이 없습니다.")
except ValueError as e:
    print(f"오류 발생: {e}")