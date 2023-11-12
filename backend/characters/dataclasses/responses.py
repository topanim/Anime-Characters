class Body:
    USER_ALREADY_EXISTS = {
        'error': 'Пользователь уже существует'
    }

    BAD_REQUEST = {
        'error': 'Неправильный запрос'
    }

    INVALID_FORM_BODY = {
        'error': 'Некорректное тело запроса'
    }

    AUTHORIZED_FALSE = {
        'authorized': False,
    }

    AUTHORIZED_TRUE = {
        'authorized': True,
    }

    CREATED = {
        'text': 'Успешно создано'
    }

    DELETED = {
        'text': 'Успешно удалено'
    }

    NOT_FOUND = {
        'text': 'Не найдено'
    }


class Status:
    CONFLICT = 409
    BAD_REQUEST = 400
    OK = 200
    CREATED = 201
    DELETED = 204
    INVALID = 422
    NOT_FOUND = 404
