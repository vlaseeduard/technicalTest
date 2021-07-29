# Django
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_http_methods
# external
from technicalTest.core.responses import StandardResponse
# internal
from ..utils import staff_check
from ..service import WeatherWrapper


@login_required
@user_passes_test(staff_check)

def get_weather(request, city_name) -> JsonResponse:
    try:
        if city_name is None :
            raise Exception(f'Expected city_name, got None')

        if not isinstance(city_name, str):
            raise Exception(f'Expected string, got {type(city_name)}')

        return JsonResponse(StandardResponse(
            data={
                'weather': WeatherWrapper().get_city_weather(city_name=city_name)._asdict()
            }, success=True, message='Cities loaded successfully').json())
    except Exception as err:
        #todo add logger
        return JsonResponse(StandardResponse(
            data={}, success=False, message='An error has occurred').json())
