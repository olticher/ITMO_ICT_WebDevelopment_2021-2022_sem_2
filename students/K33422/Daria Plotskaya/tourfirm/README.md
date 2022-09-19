# requests examples:
## Lab 2

### manual filters:

- http://localhost:8000/api/tours_by_count/?count=50
- http://localhost:8000/api/tours_by_count_destination/?count=50&destination=France
- http://localhost:8000/api/reservations_by_count_approved/?count=3&approved=True

### automatic filters:

- http://localhost:8000/api/reviews_ordered/2
- http://localhost:8000/api/reservations_search_all/?search=1,Bulgaria
- http://localhost:8000/api/tours_price_range/?price_min=1000&price_max=1500

### pagination:
- http://localhost:8000/api/tours_price_range/?price_min=1000&price_max=5000

### file upload
- http://localhost:8000/api/upload_review_photo/
- http://localhost:8000/api/upload_review_photos/

### signals
- http://localhost:8000/api/create_tour/
- http://localhost:8000/api/tour/1/
- http://localhost:8000/api/tour/1/

## Lab 3
- ```python manage.py test tours.tests```
- ```python manage.py test tours.tests.<models | GET | POST | PATCH>```
