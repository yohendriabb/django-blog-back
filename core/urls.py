
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static 
from django.views.generic import TemplateView

urlpatterns = [
	path('api/blog/', include('blog.urls')),
	path('api/category/', include('category.urls')),
    path('admin/', admin.site.urls),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns += [re_path('^.*', TemplateView.as_view(template_name='index.html'))]

