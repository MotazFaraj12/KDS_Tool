from flask import Flask, jsonify
from faker import Faker
import random
import random

app = Flask(__name__)
faker = Faker()

@app.route('/api/data', methods=['GET'])
def get_data():
    List_of_data = []

    random_number = random.randint(1, 10)
    print(random_number)
    for i in range(random_number):
        data ={
            "branch": {
                "id": faker.uuid4(),
                "name": "Branch 01",
                "name_localized": "الفرع الأول",
                "type": 1,
                "latitude": faker.latitude(),
                "longitude": faker.longitude(),
                "phone": faker.phone_number(),
                "opening_from": "08:00",
                "opening_to": "00:00",
                "inventory_end_of_day_time": "03:00",
                "receipt_header": "Welcome",
                "receipt_footer": "Thank You",
                "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "deleted_at": None,
                "reference": "B06"
            },
            "promotion": {
                "id": faker.uuid4(),
                "name": "Weekend promotion",
                "name_localized": None,
                "type": 1,
                "from_date": faker.date(),
                "to_date": faker.date(),
                "from_time": 0,
                "to_time": 23,
                "is_sat": True,
                "is_sun": True,
                "is_mon": True,
                "is_tue": True,
                "is_wed": True,
                "is_thu": True,
                "is_fri": True,
                "is_active": True,
                "include_modifiers": True,
                "target_quantity": 2,
                "reward_type": 1,
                "reward_quantity": 3,
                "reward_amount": 3,
                "maximum_discount_amount": 30,
                "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "deleted_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "condition_type": None,
                "priority": None,
                "order_types": [
                1,
                2,
                3
                ]
            },
            "original_order": None,
            "table": {
                "section": {
                "id": faker.uuid4(),
                "name": "Section 1",
                "name_localized": None,
                "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "deleted_at": None
                },
                "id": faker.uuid4(),
                "name": "New Table 3",
                "status": 1,
                "seats": 1,
                "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "deleted_at": None
            },
            "creator": {
                "pin": "*****",
                "is_owner": True,
                "id": faker.uuid4(),
                "name": "Cashier",
                "number": None,
                "email": faker.email(),
                "phone": faker.phone_number(),
                "lang": "en",
                "display_localized_names": False,
                "email_verified": False,
                "last_console_login_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "deleted_at": None,
                "last_cashier_login_at": None
            },
            "closer": {
                "pin": "*****",
                "is_owner": True,
                "id": faker.uuid4(),
                "name": "Cashier",
                "number": None,
                "email": faker.email(),
                "phone": "0",
                "lang": "en",
                "display_localized_names": False,
                "email_verified": False,
                "last_console_login_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "deleted_at": None,
                "last_cashier_login_at": None
            },
            "driver": {
                "pin": "*****",
                "is_owner": True,
                "id": faker.uuid4(),
                "name": "Cashier",
                "number": None,
                "email": faker.email(),
                "phone": faker.phone_number(),
                "lang": "en",
                "display_localized_names": False,
                "email_verified": False,
                "last_console_login_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "deleted_at": None,
                "last_cashier_login_at": None
            },
            "customer": {
                "id": faker.uuid4(),
                "name": faker.name(),
                "dial_code": 966,
                "phone": faker.phone_number(),
                "email": faker.email(),
                "gender":  random.choice([0, 1]),
                "birth_date": faker.date_of_birth().strftime('%Y-%m-%d'),
                "is_blacklisted": False,
                "is_house_account_enabled": True,
                "house_account_limit": 1000,
                "is_loyalty_enabled": 1,
                "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "deleted_at": None,
                "last_order_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "order_count": random.randint(1, 100)
            },
            "customer_address": {
                "delivery_zone": {
                "id": faker.uuid4(),
                "name": "District Naz",
                "name_localized": None,
                "coordinates": [
                    float(faker.latitude()), 
                    float(faker.longitude()), 
                    float(faker.latitude()), 
                    float(faker.longitude()), 
                    float(faker.latitude())
                ],
                "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "deleted_at": None,
                "reference": None
                },
                "id": faker.uuid4(),
                "name": "Work",
                "description": "15688 Kohler Ceceliaville, RI 90603",
                "latitude": faker.latitude(),
                "longitude": faker.longitude(),
                "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "deleted_at": None
            },
            "discount": {
                "id": faker.uuid4(),
                "name": "Coupon Discount",
                "name_localized": None,
                "qualification": 2,
                "amount": 5,
                "minimum_product_price": None,
                "minimum_order_price": None,
                "maximum_amount": 25,
                "is_percentage": False,
                "is_taxable": True,
                "order_types": [
                1,
                2,
                3
                ],
                "reference": "disc-03",
                "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "deleted_at": None
            },
            "tags": [
                {
                "id": faker.uuid4(),
                "type": 4,
                "name": "Staff",
                "name_localized": None,
                "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "deleted_at": None,
                "pivot": {
                    "order_id": faker.uuid4(),
                    "tag_id": faker.uuid4()
                }
                }
            ],
            "coupon": {
                "id": faker.uuid4(),
                "name": "Weekend",
                "maximum_uses": 5,
                "is_active": True,
                "from_date": faker.date(),
                "to_date": faker.date(),
                "from_time": 0,
                "to_time": 0,
                "is_sat": True,
                "is_sun": True,
                "is_mon": True,
                "is_tue": True,
                "is_wed": True,
                "is_thu": True,
                "is_fri": True,
                "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "deleted_at": None
            },
            "gift_card": {
                "gift_card_product": {
                "id": faker.uuid4(),
                "name": "100 SAR Card",
                "name_localized": None,
                "sku": "sk-0030",
                "barcode": None,
                "pricing_method": 1,
                "price": 100,
                "is_active": True,
                "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "deleted_at": None
                },
                "id": faker.uuid4(),
                "amount": 100,
                "balance": 100,
                "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S')
            },
            "charges": [
                {
                "charge": {
                    "id": faker.uuid4(),
                    "name": "Service Charge",
                    "name_localized": None,
                    "type": 2,
                    "is_auto_applied": False,
                    "value": 10,
                    "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "deleted_at": None,
                    "order_types": [
                    1,
                    3,
                    2
                    ]
                },
                "taxes": [
                    {
                    "pivot": {
                        "amount": 0.4,
                        "rate": 5,
                        "tax_exclusive_discount_amount": None
                    },
                    "id": faker.uuid4(),
                    "name": "VAT",
                    "name_localized": None,
                    "rate": 5,
                    "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "deleted_at": None
                    }
                ],
                "amount": 8,
                "tax_exclusive_amount": 8
                }
            ],
            "payments": [
                {
                "user": {
                    "pin": "*****",
                    "is_owner": True,
                    "id": faker.uuid4(),
                    "name": "Cashier",
                    "number": None,
                    "email": faker.email(),
                    "phone": faker.phone_number(),
                    "lang": "en",
                    "display_localized_names": False,
                    "email_verified": False,
                    "last_console_login_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "deleted_at": None,
                    "last_cashier_login_at": None
                },
                "payment_method": {
                    "id": faker.uuid4(),
                    "name": "Cash",
                    "name_localized": None,
                    "type": 7,
                    "code": "Cash",
                    "auto_open_drawer": True,
                    "is_active": True,
                    "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "deleted_at": None
                },
                "amount": 24.15,
                "tendered": 25,
                "tips": 0,
                "business_date": faker.date_time().strftime('%Y-%m-%d'),
                "added_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "meta": None
                }
            ],
            "products": [
                {
                "product": {
                    "category": {
                    "id": faker.uuid4(),
                    "name": "Sandwiches",
                    "name_localized": None,
                    "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "deleted_at": None,
                    "reference": None
                    },
                    "id": faker.uuid4(),
                    "sku": "P002",
                    "barcode": "1561630164",
                    "name": "Tuna Sandwich",
                    "name_localized": None,
                    "description": "Desc",
                    "description_localized": None,
                    "image": "https://alwans-dev.s3.amazonaws.com/q5pk2aglz.jpg",
                    "is_active": True,
                    "is_stock_product": False,
                    "is_ready": True,
                    "pricing_method": 2,
                    "selling_method": 2,
                    "costing_method": 2,
                    "preparation_time": 6,
                    "price": 10,
                    "cost": None,
                    "calories": None,
                    "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "deleted_at": None
                },
                "promotion": None,
                "discount": {
                    "id": faker.uuid4(),
                    "name": "Sprint Discount",
                    "name_localized": None,
                    "qualification": 3,
                    "amount": 10,
                    "minimum_product_price": 10,
                    "minimum_order_price": 20,
                    "maximum_amount": 900,
                    "is_percentage": True,
                    "is_taxable": False,
                    "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "deleted_at": None,
                    "reference": None,
                    "order_types": [
                    1,
                    2
                    ]
                },
                "options": [
                    {
                    "modifier_option": {
                        "id": faker.uuid4(),
                        "name": "Cheese Slice",
                        "name_localized": None,
                        "sku": "M002",
                        "is_active": True,
                        "costing_method": 2,
                        "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "deleted_at": None,
                        "price": 4,
                        "cost": None,
                        "calories": None
                    },
                    "taxes": [
                        {
                        "pivot": {
                            "amount": 0.225,
                            "rate": 5,
                            "tax_exclusive_discount_amount": None
                        },
                        "id": faker.uuid4(),
                        "name": "VAT",
                        "name_localized": None,
                        "rate": 5,
                        "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "deleted_at": None
                        }
                    ],
                    "quantity": 2,
                    "partition": 1,
                    "unit_price": 3,
                    "total_price": 12,
                    "total_cost": 0.362,
                    "tax_exclusive_unit_price": 3,
                    "tax_exclusive_total_price": 12,
                    "added_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "tax_exclusive_discount_amount": 6
                    }
                ],
                "taxes": [
                    {
                    "pivot": {
                        "amount": 0.525,
                        "rate": 5,
                        "tax_exclusive_discount_amount": None
                    },
                    "id": faker.uuid4(),
                    "name": "VAT",
                    "name_localized": None,
                    "rate": 5,
                    "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "deleted_at": None
                    }
                ],
                "timed_events": [
                    {
                    "id": faker.uuid4(),
                    "name": "Always",
                    "name_localized": None,
                    "type": 1,
                    "value": 4,
                    "from_date": faker.date(),
                    "to_date": faker.date(),
                    "from_time": 0,
                    "to_time": 23,
                    "is_sat": True,
                    "is_sun": True,
                    "is_mon": True,
                    "is_tue": True,
                    "is_wed": True,
                    "is_thu": True,
                    "is_fri": True,
                    "is_active": True,
                    "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "deleted_at": None,
                    "priority": 7,
                    "order_types": [
                        3
                    ]
                    }
                ],
                "void_reason": None,
                "creator": {
                    "pin": "*****",
                    "is_owner": True,
                    "id": faker.uuid4(),
                    "name": "Cashier",
                    "number": None,
                    "email": faker.email(),
                    "phone": faker.phone_number(),
                    "lang": "en",
                    "display_localized_names": False,
                    "email_verified": False,
                    "last_console_login_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "deleted_at": None,
                    "last_cashier_login_at": None
                },
                "voider": None,
                "discount_type": 1,
                "quantity": 2,
                "unit_price": 14,
                "discount_amount": 20,
                "total_price": 20,
                "total_cost": 1.932,
                "tax_exclusive_discount_amount": 20,
                "tax_exclusive_unit_price": 14,
                "tax_exclusive_total_price": 20,
                "status": 4,
                "is_ingredients_wasted": 0,
                "is_ingredients_returned": 0,
                "delay_in_seconds": None,
                "kitchen_notes": "Some Product Kitchen Notes 72725",
                "added_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "closed_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "meta": None
                }
            ],
            "combos": [
                {
                "combo_size": {
                    "combo": {
                    "id": faker.uuid4(),
                    "sku": "sk-0014",
                    "barcode": None,
                    "name": "Lunch Combo",
                    "name_localized": None,
                    "description": None,
                    "description_localized": None,
                    "image": None,
                    "is_active": True,
                    "is_ready": True,
                    "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "deleted_at": None
                    },
                    "id": faker.uuid4(),
                    "name": "Small",
                    "name_localized": None,
                    "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "deleted_at": None
                },
                "products": [
                    {
                    "product": {
                        "category": {
                        "id": faker.uuid4(),
                        "name": "Sandwiches",
                        "name_localized": None,
                        "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "deleted_at": None,
                        "reference": None
                        },
                        "id": faker.uuid4(),
                        "sku": "P001",
                        "barcode": None,
                        "name": "Burger",
                        "name_localized": None,
                        "description": None,
                        "description_localized": None,
                        "image": "https://image.com/q5pk2aglz.jpg",
                        "is_active": True,
                        "is_stock_product": False,
                        "is_ready": True,
                        "pricing_method": 2,
                        "selling_method": 1,
                        "costing_method": 1,
                        "preparation_time": 0,
                        "price": None,
                        "cost": 4,
                        "calories": None,
                        "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "deleted_at": None
                    },
                    "promotion": None,
                    "discount": None,
                    "options": [
                        {
                        "modifier_option": {
                            "id": faker.uuid4(),
                            "name": "Sugar",
                            "name_localized": None,
                            "sku": "M001",
                            "is_active": True,
                            "costing_method": 2,
                            "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                            "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                            "deleted_at": None,
                            "price": 2,
                            "cost": None,
                            "calories": None
                        },
                        "taxes": [
                            {
                            "pivot": {
                                "amount": 0,
                                "rate": 5,
                                "tax_exclusive_discount_amount": None
                            },
                            "id": faker.uuid4(),
                            "name": "VAT",
                            "name_localized": None,
                            "rate": 5,
                            "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                            "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                            "deleted_at": None
                            }
                        ],
                        "quantity": 2,
                        "partition": 1,
                        "unit_price": 0,
                        "total_price": 0,
                        "total_cost": 0,
                        "tax_exclusive_unit_price": None,
                        "tax_exclusive_total_price": None,
                        "added_at": None,
                        "tax_exclusive_discount_amount": None
                        }
                    ],
                    "taxes": [
                        {
                        "pivot": {
                            "amount": 0,
                            "rate": 5,
                            "tax_exclusive_discount_amount": None
                        },
                        "id": faker.uuid4(),
                        "name": "VAT",
                        "name_localized": None,
                        "rate": 5,
                        "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "deleted_at": None
                        }
                    ],
                    "timed_events": [],
                    "void_reason": None,
                    "creator": None,
                    "voider": None,
                    "discount_type": None,
                    "quantity": 2,
                    "unit_price": 0,
                    "discount_amount": 0,
                    "total_price": 0,
                    "total_cost": 8,
                    "tax_exclusive_discount_amount": None,
                    "tax_exclusive_unit_price": None,
                    "tax_exclusive_total_price": None,
                    "status": 4,
                    "is_ingredients_wasted": 0,
                    "is_ingredients_returned": 0,
                    "delay_in_seconds": None,
                    "kitchen_notes": "well done",
                    "added_at": None,
                    "closed_at": None,
                    "meta": {
                        "external_additional_product_info": "some info"
                    },
                    "combo_option": {
                        "id": faker.uuid4(),
                        "combo_item_id": faker.uuid4(),
                        "name": "Burger",
                        "name_localized": None,
                        "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "deleted_at": None
                    },
                    "combo_size": {
                        "id": faker.uuid4(),
                        "combo_id": faker.uuid4(),
                        "name": "Small",
                        "name_localized": None,
                        "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "deleted_at": None
                    }
                    },
                    {
                    "product": {
                        "category": {
                        "id": faker.uuid4(),
                        "name": "Salad",
                        "name_localized": None,
                        "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "deleted_at": None,
                        "reference": None
                        },
                        "id": faker.uuid4(),
                        "sku": "P003",
                        "barcode": None,
                        "name": "Salad",
                        "name_localized": None,
                        "description": None,
                        "description_localized": None,
                        "image": "https://image.com/q5pk2aglz.jpg",
                        "is_active": True,
                        "is_stock_product": False,
                        "is_ready": True,
                        "pricing_method": 1,
                        "selling_method": 1,
                        "costing_method": 1,
                        "preparation_time": None,
                        "price": 8,
                        "cost": 2.2,
                        "calories": None,
                        "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "deleted_at": None
                    },
                    "promotion": None,
                    "discount": None,
                    "options": [
                        {
                        "modifier_option": {
                            "id": faker.uuid4(),
                            "name": "Cheese Slice",
                            "name_localized": None,
                            "sku": "M002",
                            "is_active": True,
                            "costing_method": 2,
                            "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                            "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                            "deleted_at": None,
                            "price": 4,
                            "cost": None,
                            "calories": None
                        },
                        "taxes": [
                            {
                            "pivot": {
                                "amount": 0,
                                "rate": 5,
                                "tax_exclusive_discount_amount": None
                            },
                            "id": faker.uuid4(),
                            "name": "VAT",
                            "name_localized": None,
                            "rate": 5,
                            "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                            "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                            "deleted_at": None
                            }
                        ],
                        "quantity": 2,
                        "partition": 1,
                        "unit_price": 0,
                        "total_price": 0,
                        "total_cost": 0.362,
                        "tax_exclusive_unit_price": None,
                        "tax_exclusive_total_price": None,
                        "added_at": None,
                        "tax_exclusive_discount_amount": None
                        }
                    ],
                    "taxes": [
                        {
                        "pivot": {
                            "amount": 0,
                            "rate": 5,
                            "tax_exclusive_discount_amount": None
                        },
                        "id": faker.uuid4(),
                        "name": "VAT",
                        "name_localized": None,
                        "rate": 5,
                        "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "deleted_at": None
                        }
                    ],
                    "timed_events": [],
                    "void_reason": None,
                    "creator": None,
                    "voider": None,
                    "discount_type": None,
                    "quantity": 2,
                    "unit_price": 0,
                    "discount_amount": 0,
                    "total_price": 0,
                    "total_cost": 4.4,
                    "tax_exclusive_discount_amount": None,
                    "tax_exclusive_unit_price": None,
                    "tax_exclusive_total_price": None,
                    "status": 4,
                    "is_ingredients_wasted": 0,
                    "is_ingredients_returned": 0,
                    "delay_in_seconds": None,
                    "kitchen_notes": "well done",
                    "added_at": None,
                    "closed_at": None,
                    "meta": {
                        "external_additional_product_info": "some info"
                    },
                    "combo_option": {
                        "id": faker.uuid4(),
                        "combo_item_id": faker.uuid4(),
                        "name": "Side Dish",
                        "name_localized": None,
                        "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "deleted_at": None
                    },
                    "combo_size": {
                        "id": faker.uuid4(),
                        "combo_id": faker.uuid4(),
                        "name": "Small",
                        "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "deleted_at": None
                    }
                    }
                ],
                "discount_type": None,
                "quantity": 2,
                "returned_quantity": 0,
                "discount_amount": 0
                }
            ],
            "id": faker.uuid4(),
            "promotion_id": faker.uuid4(),
            "discount_type": 1,
            "reference": "00292",
            "number": 1,
            "type": 3,
            "source": 1,
            "status": 4,
            "delivery_status": 2,
            "guests": 1,
            "kitchen_notes": "Some Kitchen Notes 73664",
            "customer_notes": "Some Customer Notes 83083",
            "business_date": faker.date_time().strftime('%Y-%m-%d'),
            "subtotal_price": 20,
            "discount_amount": 5,
            "rounding_amount": 0,
            "total_price": 24.15,
            "tax_exclusive_discount_amount": 5,
            "delay_in_seconds": None,
            "meta": {
                "foodics": {
                "device_id": faker.uuid4(),
                "kitchen_done_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "kitchen_received_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "decline_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                "joined_orders": [
                    faker.uuid4()
                ]
                }
            },
            "opened_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            "accepted_at": None,
            "due_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            "driver_assigned_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            "dispatched_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            "driver_collected_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            "delivered_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            "closed_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            "created_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": faker.date_time().strftime('%Y-%m-%d %H:%M:%S')
            }
        List_of_data.append(data)

    return jsonify(List_of_data)

if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.119' , port=5000)
