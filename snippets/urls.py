from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from rest_framework_simplejwt import views as jwt_views




urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/api/', views.snippet_list_api),
    path('snippets/api/<int:pk>/', views.snippet_detail_api),
    path('snippets/apilist/', views.SnippetList.as_view()),
    path('snippets/apidetail/<int:pk>/', views.SnippetDetail.as_view()),
    path('snippets/apilistmixin/', views.SnippetList_mixins.as_view()),
    path('snippets/apidetailmixin/<int:pk>/', views.SnippetDetail_mixins.as_view()),
    path('snippets/apilistgeneric/', views.SnippetList_generic.as_view()),
    path('snippets/apidetailgeneric/<int:pk>/', views.SnippetDetail_generic.as_view()),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)