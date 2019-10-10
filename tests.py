from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from app import app
#Will be used to run tests for the project
sample_fabrict_id = ObjectId('5d55cffc4a3d4031f42827a3')
sample_fabric = {
    'name': 'Silk',
    'description': 'Shiny and soft',
    'price': 50,
    'source': 'Britex',
    'image_url': 'https://sc02.alicdn.com/kf/HTB1C.p.mb_I8KJjy1Xaq6zsxpXas/pure-silk-fabric-100-natural-silk-satin.jpg'
}
sample_form_data = {
    'name': sample_fabric['name'],
    'description': sample_fabric['description'],
    'price':sample_fabric['price'],
    'source':sample_fabric['source'],
    'image_url': sample_fabric['image_url'])
}

class FabricsTests(TestCase):
    """Flask tests."""
