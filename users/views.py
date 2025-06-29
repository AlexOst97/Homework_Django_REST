from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny

from users.models import Payment, User
from users.serializers import PaymentSerializers, UserSerializers
from users.services import (create_checkout_session, create_price,
                            create_product)


# User
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [
        AllowAny,
    ]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


# Payment
class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        stripe_product_id = create_product(payment)
        price_id = create_price(payment, stripe_product_id)
        session_id, payment_link = create_checkout_session(price_id)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()


class PaymentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()


class PaymentDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["course", "lesson", "paid_course_or_lesson"]
    ordering_fields = ["payment_date"]


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()
