__author__ = 'mstacy'
from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from obis.views import AcctaxViewSet, ComtaxViewSet, SyntaxViewSet,HightaxViewSet,FedStatusViewSet,StStatusViewSet
from obis.views import OkSwapViewSet, OccurrenceViewSet, SourceViewSet, InstitutionViewSet,CountyViewSet
from obis.views import CoTrsViewSet, IdentificationVerificationViewSet, RankChangeViewSet, SpatialRefSysViewSet
#from obis.views import VwSearchViewSet, VwSearchmvViewSet
#from obis.views import SearchViewSet


router = routers.SimpleRouter()
router.register('acctax', AcctaxViewSet)
router.register('comtax', ComtaxViewSet)
router.register('syntax', SyntaxViewSet)
router.register('hightax', HightaxViewSet)
router.register('fedstatus', FedStatusViewSet)
router.register('ststatus', StStatusViewSet)
router.register('okswap', OkSwapViewSet)
router.register('occurrence', OccurrenceViewSet)
router.register('source',SourceViewSet)
router.register('institution', InstitutionViewSet)
router.register('county', CountyViewSet)
router.register('cotrs', CoTrsViewSet)
router.register('identificationverification', IdentificationVerificationViewSet)
router.register('rankchange', RankChangeViewSet)
router.register('spatialrefsys', SpatialRefSysViewSet)

# View
#router.register('vwsearch', VwSearchViewSet)
#router.register('vwsearchmv', VwSearchmvViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'jsonp', 'xml', 'yaml'])
