from django.core.exceptions import ValidationError
import re

def validate_name_format(value):
    if not re.match(r'^[A-Za-z]+ [A-Za-z]\. [A-Za-z]+$', value):
        raise ValidationError('Name must be in the format "First Middle Initial. Last"')
    
def validate_school_email(value):
    if not value.endswith('@school.com'):
        raise ValidationError('Email must be from school domain')
    
def validate_combination_format(value):
    if not re.match(r'^\d{2}-\d{2}-\d{2}$', value):
        raise ValidationError('Combination must be in the format "12-12-12"')