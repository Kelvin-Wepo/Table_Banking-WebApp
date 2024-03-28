from django.contrib.auth.tokens import PasswordResetTokenGenerator  
import six
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):  
        def _make_hash_value(self, member, timestamp):  
            return (  
                six.text_type(member.pk) + six.text_type(timestamp) +  
                six.text_type(member.is_active)  
            )
account_activation_token = AccountActivationTokenGenerator()