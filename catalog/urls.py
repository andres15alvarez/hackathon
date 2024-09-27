from rest_framework.routers import SimpleRouter

from catalog.views import (
    FrequentQuestionViewSet,
    IllnessMedicineViewSet,
    IllnessViewSet,
    MedicineViewSet,
    SectorViewSet
)


router = SimpleRouter()
router.register("sector", SectorViewSet)
router.register("illness", IllnessViewSet)
router.register("medicine", MedicineViewSet)
router.register("illnessmedicine", IllnessMedicineViewSet)
router.register("faq", FrequentQuestionViewSet)

app_name = "catalog"
urlpatterns = router.urls
