# 3rd party
import json
# Django
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_http_methods
# external
from technicalTest.core.responses import StandardResponse
# internal
from ..utils import staff_check
from ..service import CountriesWrapper

@login_required
@user_passes_test(staff_check)
@require_http_methods(["GET"])
def get_country_cities(request, country_name) -> JsonResponse:
    try:
        if country_name is None:
            raise Exception(f'Expected city_name, got None')

        if not isinstance(country_name, str):
            raise Exception(f'Expected string, got {type(country_name)}')

        return JsonResponse(StandardResponse(
            data={
                'cities': CountriesWrapper().get_country_cities(country_name=country_name)
            }, success=True, message='Cities loaded successfully').json())
    except Exception as err:
        # todo add logger
        return JsonResponse(StandardResponse(
            data={}, success=False, message='An error has occurred').json())