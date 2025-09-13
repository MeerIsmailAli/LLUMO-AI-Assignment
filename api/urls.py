from django.urls import path
from . import views

urlpatterns = [
    path('employees/avg-salary/', views.avg_salary_by_department), # Specific first
    path('employees/search/', views.search_by_skill),              # Specific first
    path('employees/<str:employee_id>/', views.employee_detail),   # Catch-all last
    path('employees/', views.employees),                           # List/create last
]

