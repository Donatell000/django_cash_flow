from django.urls import path

from cashflow.views.transaction import TransactionListCreateView, TransactionDetailView
from cashflow.views.status import StatusListCreateView, StatusDetailView
from cashflow.views.transaction_type import TransactionTypeListCreateView, TransactionTypeDetailView
from cashflow.views.category import CategoryListCreateView, CategoryDetailView
from cashflow.views.subcategory import SubcategoryListCreateView, SubcategoryDetailView


urlpatterns = [
    path("transactions/", TransactionListCreateView.as_view(), name="transaction-list"),
    path("transactions/<int:pk>/", TransactionDetailView.as_view(), name="transaction-detail"),

    path("statuses/", StatusListCreateView.as_view(), name="status-list"),
    path("statuses/<int:pk>/", StatusDetailView.as_view(), name="status-detail"),

    path("transaction-types/", TransactionTypeListCreateView.as_view(), name="transaction-type-list"),
    path("transaction-types/<int:pk>/", TransactionTypeDetailView.as_view(), name="transaction-type-detail"),

    path("categories/", CategoryListCreateView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),

    path("subcategories/", SubcategoryListCreateView.as_view(), name="subcategory-list"),
    path("subcategories/<int:pk>/", SubcategoryDetailView.as_view(), name="subcategory-detail"),
]
