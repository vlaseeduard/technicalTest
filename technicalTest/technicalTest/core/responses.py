# py
import json
#
from . import constants as const


class StandardResponse(object):
    def __init__(self, data=None, success=False, message=None, status_code=None):
        self.data = data
        self.success = success
        self.message = message
        self.is_unhandled_error = False
        self.unhandled_error_data = None

        if status_code is None and success is True:
            self.status_code = const.HTTP_STATUS_CODE_OK
        else:
            self.status_code = status_code

        if message is None and success is True:
            self.message = const.OK

    def __as_dict(self):
        return {
                    const.KEY_DATA:                 self.data,
                    const.KEY_SUCCESS:              self.success,
                    const.KEY_MESSAGE:              self.message,
                    const.KEY_IS_UNHANDLED_ERROR:   self.is_unhandled_error,
                    const.KEY_UNHANDLED_ERROR_DATA: self.unhandled_error_data,
                    const.KEY_STATUS_CODE:          self.status_code
                }

    def json(self):
        return self.__as_dict()

    def __repr__(self):
        return json.dumps(self.__as_dict())

    def __str__(self):
        return json.dumps(self.__as_dict())

    @property
    def data(self):
        return self._data

    @property
    def success(self):
        return self._success

    @property
    def message(self):
        return self._message

    @property
    def status_code(self):
        return self._status_code

    @data.setter
    def data(self, val):
        try:
            if val is not None and not isinstance(val, dict) and not isinstance(val, list):
                raise Exception(f'{const.ERROR_EXPECTED_DICT_LIST}{type(val)}')
            self._data = val
        except Exception as e:
            raise Exception(f'{const.ERROR_INVALID_VALUE}data: {str(e)}')

    @success.setter
    def success(self, val):
        try:
            if not isinstance(val, bool) or val not in [True, False]:
                raise Exception(f'{const.ERROR_EXPECTED_TRUE_FALSE}{type(val)}')
            self._success = val
        except Exception as e:
            raise Exception(f'{const.ERROR_INVALID_VALUE}success: {str(e)}')

    @message.setter
    def message(self, val):
        try:
            if val is not None and not isinstance(val, str):
                raise Exception(f'{const.ERROR_EXPECTED_STR}{type(val)}')
            self._message = val
        except Exception as e:
            raise Exception(f'{const.ERROR_INVALID_VALUE}message: {str(e)}')

    @status_code.setter
    def status_code(self, val):
        try:
            if val is not None and not isinstance(val, int):
                raise Exception(f'{const.ERROR_EXPECTED_INT}{type(val)}')
            self._status_code = val
        except Exception as e:
            raise Exception(f'{const.ERROR_INVALID_VALUE}status_code: {str(e)}')

    def set_unhandled_error(self, error_data):
        self.is_unhandled_error = True
        self.unhandled_error_data = error_data
        return self