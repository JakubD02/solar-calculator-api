from django.db import models

class CalculationHistory(models.Model):
    """Stores a single calculation request and their result"""
    input_data = models.JSONField()
    result_data = models.JSONField()