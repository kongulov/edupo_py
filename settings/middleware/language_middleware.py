from django.utils.translation import activate
from django.utils import timezone

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Eğer kullanıcı oturum açmışsa dil tercihini uygula
        if request.user.is_authenticated:
            # Kullanıcının dil tercihini kontrol et
            if request.user.language:
                activate(request.user.language)
        else:
            # Eğer oturum açmamışsa, varsayılan dil tercihine bak
            activate(request.LANGUAGE_CODE)  # Oturum açmamış kullanıcılar için varsayılan dil
        response = self.get_response(request)
        return response
