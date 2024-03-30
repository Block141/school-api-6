from django.core.exceptions import ValidationError
import re

def validate_subject_format(value):
    if not re.match(r'^[A-Za-z0-9\s]+$', value):
        raise ValidationError('Subject must only contain letters, numbers, and spaces.')
    
def validate_professor_name(value):
    if not re.match(r'^Professor [A-Za-z\s]+$', value):
        raise ValidationError('Professor name must start with "Professor" and only contain letters and spaces.')
    
def clean():
    pass