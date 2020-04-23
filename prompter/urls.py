from django.urls import path
from . import views
from .views import (
    PrompterCreateView,
    PrompterListView,
    PrompterDraftListView,
    PrompterDetailView,
    PrompterUpdateView,
    PrompterDeleteView
)

urlpatterns = [
    path('blank/', views.Blank, name='blank'),
    path('screen/<int:pk>/', views.ScreenView, name='screen'),
    path('create/', PrompterCreateView.as_view(), name='promp-create'),
    path('list/', PrompterListView.as_view(), name='promp-list'),
    path('draft/', PrompterDraftListView.as_view(), name='promp-draft'),
    path('detail/<int:pk>/', PrompterDetailView.as_view(), name='promp-detail'),
    path('update/<int:pk>/', PrompterUpdateView.as_view(), name='promp-update'),
    path('delete/<int:pk>/', PrompterDeleteView.as_view(), name='promp-delete'),
]
