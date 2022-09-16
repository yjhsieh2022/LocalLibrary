"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

# Use include() to add paths from the catalog application
from django.urls import include
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # forwards requests with the pattern catalog/ to the module catalog.urls
    # 通常url mapping的設定不會在locallibrary網站層次的urls.py做設定，而是會到較低階層的catalog應用程式層次做。
    # 將下列程式碼加入locallibrary\locallibrary\urls.py的最末端之後，就代表著：
    # catalog應用程式的url mapping的細節，將由他自己的locallibrary\catalog\urls.py來做設定
    # include() will split the URL string at the designated end character and sends the remaining substring
    # to the included URLconf module for further processing.
    path('catalog/', include('catalog.urls')),
    # 目前locallibrary網站下僅有一個應用程式catalog，因此要設定一進入網站，就進入catalog應用程式。
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
    # Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)