import emoji
from django import forms


class CharacterValidator:
    def validate(self, password, user=None):
        if emoji.__version__.count(password):
            raise forms.ValidationError('Twoje hasło nie może zawierać emoji.')

    def get_help_text(self):
        return 'Twoje hasło nie może zawierać emoji.'