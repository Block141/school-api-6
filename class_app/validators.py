from django.core.exceptions import ValidationError
import re

def validate_subject_format(value):
    if not re.match(r'^[A-Za-z0-9\s]+$', value):
        raise ValidationError('Subject must be in title case format.')
    
def validate_professor_name(value):
    if not re.match(r'^Professor [A-Za-z\s]+$', value):
        raise ValidationError('Professor name must be in the format "Professor Adam".')
    
def clean(students):
    if not 1 <= len(students) <= 30:
        raise ValidationError('A student must be enrolled in between 1 and 7 classes.')