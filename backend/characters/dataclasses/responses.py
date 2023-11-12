

class Response:




class Body:
    USER_ALREADY_EXISTS = {
        'error': 'Пользователь уже существует'
    }

    BAD_REQUEST = {
        'error': 'Неправильный запрос'
    }

    AUTHORIZED_FALSE = {
        'authorized': False,
    }

    AUTHORIZED_TRUE = {
        'authorized': True,
    }




class Status:
    CONFLICT = 409
    BAD_REQUEST = 400
    OK = 200
    CREATED = 201

