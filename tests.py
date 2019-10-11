from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from app import app
#Will be used to run tests for the project
sample_fabric_id = ObjectId('5d55cffc4a3d4031f42827a3')
sample_fabric = {
    'name': 'Silk',
    'description': 'Shiny and soft',
    'price': '50', #For some reason it only likes strings and not integers
    'source': 'Britex',
    'image_url': 'https://sc02.alicdn.com/kf/HTB1C.p.mb_I8KJjy1Xaq6zsxpXas/pure-silk-fabric-100-natural-silk-satin.jpg'
}
sample_form_data = {
    'name': sample_fabric['name'],
    'description': sample_fabric['description'],
    'price':sample_fabric['price'],
    'source':sample_fabric['source'],
    'image':sample_fabric['image_url']
}

sample_shopping_cart_item = {
    'name': sample_fabric['name'],
    'description': sample_fabric['description'],
    'price':sample_fabric['price'],
    'source':sample_fabric['source'],
    'image':sample_fabric['image_url']

}

class FabricsTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_index(self):
        """Test the Fabrics homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Fabric', result.data)

# -------------------------------------------------------
    def test_new(self):
        """Test the new fabric creation page."""
        result = self.client.get('/fabrics/new')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'New Fabric', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_playlist(self, mock_find):
        """Test showing a single fabric."""
        mock_find.return_value = sample_fabric

        result = self.client.get(f'/fabrics/{sample_fabric_id}')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Silk', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_edit_playlist(self, mock_find):
        """Test editing a single fabric."""
        mock_find.return_value = sample_fabric

        result = self.client.get(f'/fabrics/{sample_fabric_id}/edit')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Silk', result.data)

    @mock.patch('pymongo.collection.Collection.insert_one')
    def test_submit_playlist(self, mock_insert):
        """Test submitting a new fabric."""
        result = self.client.post('/fabrics', data=sample_form_data)

        self.assertEqual(result.status, '302 FOUND')
        mock_insert.assert_called_with(sample_fabric)

    @mock.patch('pymongo.collection.Collection.update_one')
    def test_update_playlist(self, mock_update):
        result = self.client.post(f'/fabrics/{sample_fabric_id}', data=sample_form_data)

        self.assertEqual(result.status, '302 FOUND')
        mock_update.assert_called_with({'_id': sample_fabric_id}, {'$set': sample_fabric})

    @mock.patch('pymongo.collection.Collection.delete_one')
    def test_delete_fabric(self, mock_delete):
        form_data = {'_method': 'DELETE'}
        result = self.client.post(f'/fabrics/{sample_fabric_id}/delete', data=form_data)
        self.assertEqual(result.status, '302 FOUND')
        mock_delete.assert_called_with({'_id': sample_fabric_id})


#=========================================
    def test_shopping_cart(self):
        """Test the Fabrics shopping cart."""
        result = self.client.get('/shopping_cart')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Fabric', result.data)

    # def test_new_item(self):
    #     """Test adding to shopping cart."""
    #     result = self.client.get('/shopping_cart/<fabric_id>/add_item')
    #     self.assertEqual(result.status, '200 OK')



        # self.assertEqual(result.status, '302 FOUND')
        # mock_insert.assert_called_with(sample_fabric)




if __name__ == '__main__':
    unittest_main()
