from django.contrib import admin
from django.urls import path,include

admin.site.site_header="SalesMasterCRM"
admin.site.site_title="SalesMasterCRM"
admin.site.index_title="Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('management.urls'))
]
