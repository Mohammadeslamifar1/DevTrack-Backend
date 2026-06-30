from projects.views import dashboard_stats

urlpatterns = [
    path("api/dashboard-stats/", dashboard_stats),
    path("api/", include(router.urls)),
]
