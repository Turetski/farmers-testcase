# Farms test project
1. initialize virtual env
``virtualenv -p python3 venv`` in project root directory
2. activate virtualenv
``source venv/bin/activate``
3. install dependencies
``pip install -r requirements.txt``
4. migrate
``./src/manage.py migrate``
5. create django superuser
``./src/manage.py createsuperuser``
6. import farms data from json
``./src/manage.py agvend_parser``
7. run server
``./src/manage.py runserver``
8. navigate with your browser http://127.0.0.1:8000  
/api/customers - list of customers with pagination  
/api/farms?customer=XXX - list of farms with pagination and possible filter by customer  
/admin - django admin page
