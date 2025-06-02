from django.core.exceptions import ValidationError


class YouTubeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url = "http://www.youtube.com"
        if value.get("video_link"):
            if url not in value.get("video_link"):
                raise ValidationError("Ссылки на сторонние ресурсы запрещены")
        return None
