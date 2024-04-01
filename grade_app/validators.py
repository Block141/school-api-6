from django.core.exceptions import ValidationError

def validate_grade_limit(grade):
    if grade > 100 or grade < 1:
        raise ValidationError('Ensure this value is less than or equal to 100.0.')